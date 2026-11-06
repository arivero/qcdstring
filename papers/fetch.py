#!/usr/bin/env python3
"""Resolve and download the papers listed in the two manifests.

Reads library-1974.tsv and memory-future.tsv, resolves each entry through
the INSPIRE REST API (by arXiv id, then DOI, then title), records what it
found in resolved.tsv, and downloads a PDF when one is freely available:
arXiv for post-1991 papers, or a scanned preprint that INSPIRE hosts.
Journal-only entries get their DOI link printed instead.

Standard library only. Be polite to INSPIRE: one request per second.
"""
import argparse
import csv
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
PDF_DIR = os.path.join(HERE, "pdf")
RESOLVED = os.path.join(HERE, "resolved.tsv")
INSPIRE = "https://inspirehep.net/api/literature"
UA = "qcdstring-fetch/0.1 (research manifest resolver)"
FIELDS = "titles,arxiv_eprints,dois,documents,control_number,publication_info"


def http_get(url, binary=False, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = r.read()
    return data if binary else data.decode("utf-8", "replace")


def inspire_query(q):
    url = INSPIRE + "?" + urllib.parse.urlencode({"q": q, "size": 1, "fields": FIELDS})
    try:
        hits = json.loads(http_get(url)).get("hits", {}).get("hits", [])
    except Exception as e:  # network or JSON trouble; report, continue
        print(f"    inspire error: {e}", file=sys.stderr)
        return None
    return hits[0]["metadata"] if hits else None


STOP = set("a an the of on in for and to from its with by at is are vs versus".split())


def words(s):
    return {w for w in re.sub(r"[^a-z0-9]+", " ", s.lower()).split() if w not in STOP}


def title_matches(a, b):
    """Loose match: at least 60% of the shorter title's content words occur in the other."""
    wa, wb = words(a), words(b)
    if not wa or not wb:
        return False
    return len(wa & wb) / min(len(wa), len(wb)) >= 0.6


def resolve(row):
    """Return dict with recid, arxiv, doi, pdf_url, matched(bool), how, note."""
    out = {"recid": "", "arxiv": row.get("arxiv", ""), "doi": row.get("doi", ""),
           "pdf_url": "", "matched": False, "how": "", "note": ""}
    queries = []
    if row.get("arxiv"):
        queries.append(("arxiv", f"arxiv:{row['arxiv']}"))
    if row.get("doi"):
        queries.append(("doi", f"doi:{row['doi']}"))
    queries.append(("title", 't:"%s"' % row["title"].replace('"', "")))
    for how, q in queries:
        md = inspire_query(q)
        time.sleep(1.0)
        if not md:
            continue
        found_title = md.get("titles", [{}])[0].get("title", "")
        if not title_matches(found_title, row["title"]):
            print(f"    {how} lookup returned a different title: {found_title!r}")
            if how in ("arxiv", "doi"):
                out[how] = ""          # manifest identifier is wrong; drop it
                out["note"] += f"manifest {how} wrong; "
            continue
        out["recid"] = str(md.get("control_number", ""))
        out["how"] = how
        out["matched"] = True
        eps = md.get("arxiv_eprints") or []
        if eps:
            out["arxiv"] = eps[0].get("value", "")
        dois = md.get("dois") or []
        if dois:
            inspire_doi = dois[0].get("value", "")
            if out["doi"] and inspire_doi and out["doi"].lower() != inspire_doi.lower():
                out["note"] += f"manifest doi {out['doi']} differs from inspire {inspire_doi}; "
            out["doi"] = inspire_doi or out["doi"]
        if out["arxiv"]:
            out["pdf_url"] = f"https://arxiv.org/pdf/{out['arxiv']}"
        else:
            for d in md.get("documents") or []:
                if d.get("url"):
                    out["pdf_url"] = d["url"]
                    break
        return out
    return out


def read_manifest(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true", help="resolve only, download nothing")
    ap.add_argument("--library", action="store_true", help="only library-1974.tsv")
    ap.add_argument("--future", action="store_true", help="only memory-future.tsv")
    ap.add_argument("--key", action="append", default=[], help="only these keys (repeatable)")
    ap.add_argument("--no-resolve", action="store_true", help="skip INSPIRE; use manifest ids as given")
    args = ap.parse_args()

    rows = []
    if not args.future:
        rows += [dict(r, manifest="library-1974") for r in read_manifest(os.path.join(HERE, "library-1974.tsv"))]
    if not args.library:
        rows += [dict(r, manifest="memory-future") for r in read_manifest(os.path.join(HERE, "memory-future.tsv"))]
    if args.key:
        rows = [r for r in rows if r["key"] in args.key]
    os.makedirs(PDF_DIR, exist_ok=True)

    results = []
    n_pdf = 0
    for r in rows:
        key = r["key"]
        target = os.path.join(PDF_DIR, key + ".pdf")
        print(f"[{r['manifest']}] {key}: {r['title'][:70]}")
        if args.no_resolve:
            res = {"recid": "", "arxiv": r.get("arxiv", ""), "doi": r.get("doi", ""),
                   "pdf_url": f"https://arxiv.org/pdf/{r['arxiv']}" if r.get("arxiv") else "",
                   "matched": bool(r.get("arxiv") or r.get("doi")), "how": "manifest", "note": ""}
        else:
            res = resolve(r)
        line = f"    inspire={res['recid'] or '-'} via={res['how'] or '-'} arxiv={res['arxiv'] or '-'} doi={res['doi'] or '-'}"
        print(line)
        if res.get("note"):
            print(f"    NOTE: {res['note']}")
        if res["pdf_url"]:
            if os.path.exists(target):
                print(f"    have {os.path.relpath(target, HERE)}")
                n_pdf += 1
            elif args.dry_run:
                print(f"    would fetch {res['pdf_url']}")
            else:
                try:
                    data = http_get(res["pdf_url"], binary=True, timeout=120)
                    if data[:4] == b"%PDF":
                        with open(target, "wb") as f:
                            f.write(data)
                        print(f"    saved {os.path.relpath(target, HERE)} ({len(data)//1024} kB)")
                        n_pdf += 1
                    else:
                        print("    response was not a PDF; skipped")
                except Exception as e:
                    print(f"    download failed: {e}")
                time.sleep(1.0)
        elif res["doi"]:
            print(f"    no free copy known; see https://doi.org/{res['doi']}")
        else:
            print("    no identifier resolved; search INSPIRE by hand")
        results.append({"key": key, "manifest": r["manifest"], **{k: res[k] for k in ("recid", "arxiv", "doi", "pdf_url", "how", "note")},
                        "pdf": os.path.relpath(target, HERE) if os.path.exists(target) else ""})

    with open(RESOLVED, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(results[0].keys()) if results else ["key"], delimiter="\t")
        w.writeheader()
        w.writerows(results)
    print(f"\n{len(results)} entries processed, {n_pdf} PDFs present, written {os.path.relpath(RESOLVED, HERE)}")


if __name__ == "__main__":
    main()
