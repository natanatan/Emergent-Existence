# Claim IDs

Agreed 29 September 2026. The full model is in [`claims-model.md`](claims-model.md).

**Claim IDs are permanent and order-independent. They identify propositions, not where those propositions currently appear in the manuscript.**

| Kind | Format | Example |
| --- | --- | --- |
| Claim | `EE-C-nnnn` | `EE-C-0137` |
| Claim version | `EE-C-nnnn@vN` | `EE-C-0137@v3` |
| Hypothesis | `EE-H-nnnn` | `EE-H-0012` (legacy `H-12` kept as an alias) |
| Element | two letters | `Rd` (retained distinction) |
| Edition | `book-n/name` | `book-1/beta` |

- An ID never encodes chapter, section, volume, edition, status, kind or label.
- IDs are assigned in order of registration and never reused. The number carries no meaning about position, importance or dependency.
- **New version or new claim?** Same assertion and same dependencies: a new version (`@vN`). A change in what the claim asserts or depends on: a new ID, linked with `supersedes` / `superseded_by`.
- A superseded claim keeps its ID and history. Nothing is silently rewritten.
- A claim may list `aliases`: earlier or informal names that resolve to it.

## Labels

A printed label belongs to an **appearance**: one place where one edition prints the claim. Labels are positional (for example `Ch4.2`), unique within an edition, and reset in each new edition. A claim printed twice in one edition has two labels that point to the same ID.
