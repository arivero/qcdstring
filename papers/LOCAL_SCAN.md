# Local scan: what is already on disk

Scan date: 6 November 2026 (machine clock). Scope: every PDF and Markdown
file under the parent directory of this repository, excluding the
editor and agent caches (`.codex`, `.vscode-server`, `.openclaw`) and this
repository itself. The shelf survey must precede any download, so the
results feed `fetch.py` through `local_sources.tsv`.

## Method

1. 27,758 candidate files found; 23,983 scored after dropping tool caches.
2. Each PDF: first four pages through `pdftotext`. Each Markdown file:
   first 30 kB. Weighted counts of 30 patterns (Nambu-Goto 5, flux tube 4,
   dual resonance 5, Luscher 3, Hagedorn 3, Pomeron 3, string tension 3, Regge 2,
   and so on) plus a triple weight for matches in the file name.
3. 898 files scored 8 or higher. Deduplication by SHA-1 collapsed 151 PDF hits
   to 111 distinct documents. The `physres5lineage/physres6` tree is a full
   copy of `physres5`, and `source_fragments` holds page-range Markdown
   transcriptions of the same PDFs.
4. Manifest matching by arXiv id, tight title overlap on page one, and
   author-year file names, followed by a manual look at the title page of
   every match. Keyword-only title matching produced many false positives
   and was discarded; the verified results are in `local_sources.tsv`.

## Findings

**Almost nothing here covers the hadronic string.** Of the 148 entries
in the original manifests, two exist locally: Miyazawa 1966 and
Catto-Gursey 1985. Nothing on disk covers Nambu, Goto, GGRT, Brink-Nielsen,
Luscher, Arvis, the Polchinski-Strominger effective string, the
lattice flux-tube papers, or the Dubovsky-Flauger-Gorbenko worldsheet
papers. All of those come from `fetch.py`.

**Eight further local PDFs belong on the shelf** and were added to the
manifests with their local paths: Chew 1962, Witten 1997 (branes and QCD),
Dosch-de Teramond-Brodsky 2015 (meson-baryon supersymmetry),
Pando Zayas-Sonnenschein-Vaman 2004 (Regge trajectories from rotating
strings), Fradkin-Shenker 1979, and the three string tutorials below.

**Modern formal string theory, as tools for Phase 1** (critical dimension,
light-cone quantisation, conformal field theory for the Liouville direction):

| Item | Where | Notes |
|---|---|---|
| Tong, String Theory (218 p) | `physres5/references/pdfs/02_...` | Also 22 page-range Markdown transcriptions under `physres5/context/source_fragments/02_tong_string_theory_notes` |
| Polchinski, What is String Theory (154 p) | `.../04_...` | 16 transcriptions |
| Ginsparg, Applied CFT (90 p) | `.../03_...` | 9 transcriptions |
| Xi Yin, Foundations of String Theory (845 p, April 2026) | `physres5lineage/kkorchestra/sources/stringbook/string notes.pdf` | Full Markdown transcription (2.2 MB) beside it. The prologue has a section "Yang-Mills theory as a string theory" and chapter 1 is "The effective string and its quantization" (Nambu-Goto, effective string, Polyakov formalism, critical string). That makes it the first file to read for ideas 001, 002 and 012. About 60 mentions of the effective or long string and 77 of Liouville. Source TeX and figures in `texsource/`. |

**Hadronic supersymmetry and diquarks (idea 016):** Catto-Gursey 1985 and
1988, Brodsky-de Teramond 2008 and Dosch-de Teramond-Brodsky 2015, all in
`phys4/sources`. The Physics Forums bibliography
`phys6gpd/analysis/results/pf_thread_bibliography.md` indexes a decade of
discussion on exactly this theme under the title "The Wrong Turn of
String Theory".

**Dual-model open strings with fermionic ends (idea 008):**
`chatpublic/discussions/2026-10-11-quark-antiquark-open-string/sources.md`
is an annotated source list that names Schwarz 1971, Ramond 1971,
Bars-Hanson 1976, both Polchinski-Strassler papers and
Sonnenschein-Weissman 2014. Its derived claims are unrefereed. Three of
the cited papers were added to the manifests (Schwarz 1971, Bars-Hanson
1976, Polchinski-Strassler 2002); none of their PDFs is stored there.

**Pomeron and cross-section abstracts (idea 006).** The abstract store
`vixra2/abstracts` contains 26 arXiv entries that match a hadronic-string
pattern. Four concern Pomeron or total cross-section phenomenology and
were added to `memory-future.tsv` as medium-confidence rows. The rest are
cosmic strings and gravity papers.

**Scans without a text layer** (invisible to keyword scoring, found by
hand): `physres5lineage/dv2/references/classical-kk-1980s/` holds Duff 1986
(Supergravity, Kaluza-Klein and superstrings), Duff-Nilsson 1986
(four-dimensional string on K3) and Duff-Nilsson-Pope-Warner 1986
(heterotic string). They concern superstring compactification and are
outside the hadronic programme, so they are listed here without manifest rows.

## Judged irrelevant, left alone

* The arXiv cache `.arxiv-mcp-server/papers` (26 papers): Koide mass
  relations, Seiberg duality, flavour composites.
* `phys4/sources` beyond the items above: supersymmetry, composites,
  soft-breaking.
* `vixra` and `vixra2`: 39 viXra abstracts and three PDFs matched
  string-related terms, among them "Proof of quark confinement and
  baryon-antibaryon duality" (vixra 1208.0219) and "Hadron Masses from
  Topological Vortex" (ai.vixra 2601.0026). They have not been vetted and
  are not on the shelf.
* `physres5/references/pdfs` items 05 to 50: M-theory on G2 manifolds,
  Kaluza-Klein, Standard Model reviews, heterotic duality.
* The Wilson-Kogut file under `navstokgap/docs` is a reading note, not
  the paper; the paper is in the library manifest without a local copy.

## Caveats

* Keyword scoring reads four pages. A relevant paper that never says
  "string" in its first pages would score low. The title-page check on
  every match limits false positives but cannot recover misses.
* `chew-1962.pdf` carries Chew's title in its metadata while the page-one
  text layer reads as a different article. Open it before citing.
* Local paths in `local_sources.tsv` are relative to the directory above
  this repository.
* `fetch.py` links local PDFs into `pdf/` as symlinks and skips the
  network for them. `--no-local` ignores the table.
