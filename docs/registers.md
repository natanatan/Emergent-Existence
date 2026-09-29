# Registers

The fields below follow [`claims-model.md`](claims-model.md).

## Claim Register (`registers/claims/`)

One file per claim.

| Field | Meaning |
| --- | --- |
| `id` | Permanent ID, `EE-C-nnnn` |
| `kind` | Proposition, definition, criterion, test, ledger, representation, rule |
| `use` | Constitutive, representational or diagnostic (Methodology, pp. 24–25) |
| `dependencies` | Constitutive premises only: the claims that must hold for this claim to hold. The earned-order check runs on these |
| `relations` | Every other typed link: derives_from, supersedes, refines, equivalent_to, contrasts_with, generalizes, specializes, foreshadows, diagnoses, tests, represents |
| `composition` | Element codes the claim rests on, derived from its current dependencies |
| `aliases` | Earlier or informal names that resolve to this claim |
| `versions` | Wording and formal statement of each version, with the date and the edition that first printed it |
| `appearances` | Each place an edition prints the claim: edition, role (derivation, foreshadowing or restatement), chapter, section, version; a derivation adds its label (locator) and type word, the others the label they cite |
| `status_history` | Dated events: status, date, edition, reason. The current status is the latest event |
| `history` | Dated events for dependency corrections and lineage substitutions, and any resulting change to the composition |

## Elements (`registers/elements/`)

The Linking Lexicon's concepts, each with a two-letter code: label, symbols, kind (foundation, stage or term), the conceptual stage it belongs to, the chapter where that stage is currently developed, status, and its links to other elements. Stage is conceptual and chapter is editorial: codes never change when either is revised.

## Editions (`registers/editions/`)

One record per released edition of a book: `id` (for example `book-1/beta`), `volume`, `book`, `released` and `source_commit`. A released edition's record is frozen.

## Hypothesis Register (`registers/hypotheses/`)

Appendix C as data: hypothesis, status history, reason, what would resolve it, where it is revisited, whether a Companion run could settle it, and its appearances.

## Ledgers (`registers/ledgers/`)

For each chapter: what it inherits, what it earns and what it withholds, with the chapter a withheld item is deferred to, or a note that it lies beyond the series or is open. The Origin Inheritance Ledger in the book is generated from this data.

## Views built from the registers

Manuscript order, derivation order, dependency graph, element table, status history, edition history, concept family, chapter placement.
