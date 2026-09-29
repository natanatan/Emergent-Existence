# Claim IDs

Agreed 29 September 2026.

**Claim IDs are permanent and order-independent. They identify propositions, not where those propositions currently appear in the manuscript.**

| Kind | Format | Example |
| --- | --- | --- |
| Claim | `EE-C-nnnn` | `EE-C-0137` |
| Claim version | `EE-C-nnnn@vN` | `EE-C-0137@v3` |
| Hypothesis | `EE-H-nnnn` | `EE-H-0012` (legacy `H-12` kept as an alias) |

- An ID never encodes chapter, section, volume, edition, status or kind. All of these are metadata in the register.
- IDs are assigned in order of registration and never reused. Book I claims are registered first, in manuscript order.
- **New version or new claim?** Same assertion and same dependencies: a new version (`@vN`). A change in what the claim asserts, what it depends on, or what it licenses later: a new ID, linked with `supersedes` / `superseded_by`.
- A superseded claim keeps its ID and history. Nothing is silently rewritten.
- A claim may list `aliases`: earlier or informal names that should resolve to it.

## Editions

An edition is one release of one book's manuscript, for example `book-1/beta` or `book-1/ed1`. Each edition has a record in `registers/editions/` with its book, volume, release date and the source commit it was cut from.

- **Editions freeze.** Once released, an edition's record is never edited. Corrections go into the next edition.
- **Versions point to editions.** Each claim version records the date it was introduced and the edition it first appeared in, so a citation of an older edition stays traceable to the wording it printed.

## Printed labels

Still open, with the editor:

- Label types. One proposal: Proposition, Definition, Criterion and Test, with ledger entries written `№ n.m`, numbered by chapter where the claim is formally derived.
- Whether a label shows the claim's use, or the type word carries it.
- Whether the STRONG / OPEN / PROVISIONAL verdict markers stay in the prose. One proposal is to drop them, since status lives in the register.

The printed label (for example "Proposition 1A") is stored as the claim's `label` field. Its style is being settled with the editor. Whatever style is chosen, every labelled statement in print must map to exactly one claim ID.
