# Registers

> Draft. Field names will be fixed once the claim notation is final.

## Claim Register (`registers/claims/`)

| Field | Meaning |
| --- | --- |
| `claim_id` | Permanent ID, `EE-C-nnnn` |
| `label` | Printed label, if any. Mutable |
| `kind` | Proposition, definition, criterion, test, ledger, representation, rule … |
| `use` | Constitutive, representational or diagnostic (Methodology, pp. 24–25) |
| `current_volume`, `current_book`, `current_chapter`, `current_section` | Where the claim appears now. The full location is generated from these, never stored |
| `introduced_in_edition` | Edition that first registered the claim |
| `requires` | Claims it depends on constitutively. The earned-order check runs on these |
| `checked_against` | Diagnostic or representational references. Exempt from the earned-order check |
| `supersedes`, `superseded_by` | Links between claims that replace one another |
| `aliases` | Earlier or informal names that resolve to this claim |
| `status_history` | Dated events: status, edition or date, reason. The current status is the latest event |
| `versions` | Wording and formalization of each version, with the date it was introduced and the edition it first appeared in |

## Editions (`registers/editions/`)

One record per released edition of a book: `id` (for example `book-1/beta`), `volume`, `book`, `released` and `source_commit`. A released edition's record is frozen.

## Hypothesis Register (`registers/hypotheses/`)

Appendix C as data: hypothesis, status history, reason, what would resolve it, where it is revisited, and whether a Companion run could settle it.

## Ledgers (`registers/ledgers/`)

For each chapter: what it inherits, what it earns and what it withholds, with the chapter a withheld item is deferred to, or a note that it lies beyond the series or is open. The Origin Inheritance Ledger in the book is generated from this data.

## Views built from the registers

Manuscript order, derivation order, dependency graph, status history, edition history, concept family, chapter placement.
