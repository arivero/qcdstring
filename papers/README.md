# papers

Two manifests and a fetcher.

* `library-1974.tsv`: papers that exist as of November 1974. This is the
  shelf. Each line has a key, year, authors, title, journal, DOI where
  known, and one line on why it is on the shelf.
* `memory-future.tsv`: papers that do not exist yet. They are listed so
  that the results they contain can be rederived, and so that a reader
  in 2026 can download them. Each line also carries an arXiv identifier
  where one exists and a confidence flag on the identifier.
* `local_sources.tsv` and `LOCAL_SCAN.md`: what the 2026 disk already holds, found by a scan of the parent directory. `fetch.py` links those PDFs first and downloads the rest.
* `fetch.py`: resolves every entry through the INSPIRE API (by DOI,
  arXiv id, or title), writes `resolved.tsv`, and downloads whatever is
  freely available (arXiv, or a scanned preprint hosted on INSPIRE) into
  `pdf/`. Pre-1991 journal articles usually sit behind a publisher wall;
  the script prints the DOI link for those. Run with `--dry-run` first.

        python3 papers/fetch.py --dry-run
        python3 papers/fetch.py                 # everything
        python3 papers/fetch.py --future        # only the memory list
        python3 papers/fetch.py --key Wilson1974
        python3 papers/fetch.py --no-local      # ignore local_sources.tsv

Identifiers in the manifests were written from memory. The DOIs of APS
and Progress of Theoretical Physics articles follow a fixed pattern
and are reliable; Elsevier DOIs of the 1970s and arXiv numbers are
reliable in most cases and the fetcher checks each against INSPIRE's
title before trusting it. A mismatch is reported, never silently used.

`pdf/` and `resolved.tsv` are ignored by git.
