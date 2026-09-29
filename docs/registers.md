# Registers

The fields below follow [`claims-model.md`](claims-model.md).

## Claim Register (`registers/claims/`)

One file per claim.

| Field | Meaning |
| --- | --- |
| `id` | Permanent ID, `EE-C-nnnn` |
| `kind` | Proposition, definition, criterion, test, ledger, representation, rule |
| `use` | Constitutive, representational or diagnostic (Methodology, pp. 24–25) |
| `composition` | Element codes the claim rests on, generated from `requires` |
| `requires` | Constitutive dependencies. The earned-order check runs on these |
| `forward_refs` | Foreshadowing of concepts earned later. Exempt from the earned-order check |
| `checked_against` | Diagnostic references. Exempt from the earned-order check |
| `represents_with` | Representational references. Exempt from the earned-order check |
| `supersedes`, `superseded_by` | Links between claims that replace one another |
| `aliases` | Earlier or informal names that resolve to this claim |
| `versions` | Wording and formal statement of each version, with the date and the edition that first printed it |
| `appearances` | Each place an edition prints the claim: edition, label, chapter, section, version |
| `status_history` | Dated events: status, date, edition, reason. The current status is the latest event |
| `history` | Dated events for carried-forward dependencies and corrections |

## Elements (`registers/elements/`)

The Linking Lexicon's concepts, each with a two-letter code: label, symbols, kind (foundation, stage or term), the stage it belongs to, the chapter that introduces it, status, and its links to other elements.

## Editions (`registers/editions/`)

One record per released edition of a book: `id` (for example `book-1/beta`), `volume`, `book`, `released` and `source_commit`. A released edition's record is frozen.

## Hypothesis Register (`registers/hypotheses/`)

Appendix C as data: hypothesis, status history, reason, what would resolve it, where it is revisited, whether a Companion run could settle it, and its appearances.

## Ledgers (`registers/ledgers/`)

For each chapter: what it inherits, what it earns and what it withholds, with the chapter a withheld item is deferred to, or a note that it lies beyond the series or is open. The Origin Inheritance Ledger in the book is generated from this data.

## Views built from the registers

Manuscript order, derivation order, dependency graph, element table, status history, edition history, concept family, chapter placement.
