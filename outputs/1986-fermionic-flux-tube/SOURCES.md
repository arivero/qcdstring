# Source record for QCDS-86/1

Machine retrieval date: 13 November 2026. Scientific cutoff: 30 November 1986.

`sources.tsv` records all 31 external numbered references, their exact DOIs,
INSPIRE records, publication years and reading coverage. Their identifiers and
titles were checked against INSPIRE metadata in this run. References 1-5 are
the repository's five earlier papers; the review uses their final text and,
for 1984, its response and stored summary. Their raw analyses were not rerun.

## What was read

- The revised abstracts and conclusions of the earlier five papers, with the
  1984 response, selected derivations, mode-count discussion and stored results.
- The original CHSW1985 PDF, printed pp. 46-47 (introduction and compactification
  premises), extracted with `pdftotext -layout`. The downloaded original has
  29 pages and its PDF identity was checked with `pdfinfo`. The beginning of
  printed p. 48 was also displayed; it was not a full-page reading.
- The existing `papers/md/CattoGursey1985.md` machine transcript, printed
  pp. 201-202, for its distinction between hadronic and fundamental
  supersymmetry. Its OCR is imperfect; no delicate equation was imported.
- Publisher abstracts / INSPIRE-hosted publisher abstracts for selected historical
  claims, with metadata verified for the remaining references. This includes the explicit
  finite-flavour warning in Dashen-Ma-Rajaraman (1975), the nonsupersymmetric
  tachyon-free examples (1986), and Fu-Nielsen's layer construction (1984).
  `sources.tsv` distinguishes metadata-only entries.

No claim is made that all originals were read. The Bessel, gap-equation,
cutoff, representation and matching calculations are displayed as derivations
in this paper. The formal small-epsilon formula is derived from canonical
scaling and the four-dimensional one-loop coefficient; it is not presented
as a quotation of an unread equation in Peskin (1980).

## Originals and companions

CHSW1985:

- Title: *Vacuum configurations for superstrings*.
- Authors: P. Candelas, G. T. Horowitz, A. Strominger, E. Witten.
- Published edition: Nuclear Physics B 258 (1985), 46-74.
- DOI: https://doi.org/10.1016/0550-3213(85)90602-9
- Public source: https://ooguri.caltech.edu/documents/31340/Candelas_Horowitz_Strominger_Witten.pdf
- Local original: `../../papers/pdf/CHSW1985.pdf` (ignored by the repository).
- Local digest: `../../papers/md/CHSW1985.md` (same repository convention,
  ignored). This is a selected-reading digest, not a full transcription.
- Rights: the original states copyright North-Holland Publishing Company;
  the downloaded original is not redistributed in the publication commit.
- Relevant passage: pp. 46-47 specify candidate supersymmetric compactifications
  and the SU(3)-holonomy condition. The application to a confining flux tube
  and the need to gap its internal fluctuations are our questions, not a
  conclusion established by those pages.
- Visual equation verification / full proof review: not performed or claimed;
  no detailed equation from these pages is used in our calculation.

## Access gaps and stopped routes

The APS harvest endpoint returned HTTP 401 for Gross-Neveu (1974),
Dashen-Ma-Rajaraman (1975), GHMR (1985), BCN (1986), Affleck (1986), and
Isgur-Paton (1985). No downloaded original was claimed for those requests.
The Nightingale-hosted BCN PDF was discoverable, but retrieval from both
`phys.uri.edu` and `www.phys.uri.edu` failed certificate validation. TLS
verification was not disabled. Publisher/INSPIRE abstracts and metadata were
sufficient for the bounded historical claims made here; the finite-size
formulas are separately derived.

The CHSW published PDF was available from Caltech. No access-control bypass,
paid retrieval, or external correspondence was used.

## Era boundary and new proposals

No later paper enters the numbered scientific bibliography. The package's
retrospective appendix labels memory-guided questions separately. The user's
reported 2026 Lean development was not searched, verified, or used. The
user-suggested dimensional-selection argument is developed through period
power counting and matching, with a distinct 1984 precedent (Fu-Nielsen) and
explicit unproved premises. It is not claimed as an established theorem or
an exhaustive novelty finding.

## Added during the author review: the compact-coordinate countertest

Coleman1975, *Quantum sine-Gordon equation as the massive Thirring model*,
Physical Review D 11 (1975), 2088-2097; DOI 10.1103/PhysRevD.11.2088.
A public scan was downloaded from
https://users.physik.fu-berlin.de/~kamecke/ps/coleman.pdf to
`../../papers/pdf/Coleman1975.pdf`; `pdfinfo` reports ten pages. The scan has no
usable text layer: `pdftotext` returned only page breaks. The first page
(printed p. 2088) was rendered and read visually, including equations (1.1)-(1.3)
and the distinction between the classical fluctuation mass and the quantum
problem. The remaining nine pages were not read or OCR-transcribed. A
same-stem selected-reading digest is in `../../papers/md/Coleman1975.md`.
The published source remains under publisher copyright and is not included
in this commit. The Gaussian-shell scaling calculation in Section 8.4 is
our derivation; it does not claim a review of the full equivalence proof.
