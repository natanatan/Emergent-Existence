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
- IDs are assigned when a proposition first enters the canonical register, not when it is first published, and are never reused. The number carries no meaning about position, importance or dependency.
- **New version or new claim?** Better wording or notation for the same assertion: a new version (`@vN`). A materially different assertion or inferential basis: a new ID that supersedes the old one. Correcting an omitted dependency, or repointing one to its designated successor, keeps the ID (see [`claims-model.md`](claims-model.md)).
- A superseded claim keeps its ID and history. Nothing is silently rewritten.
- A claim may list `aliases`: earlier or informal names that resolve to it.

## Labels

A printed label belongs to the claim's **derivation appearance**: the one place in an edition where the claim is formally derived. The label is a locator (for example `4.2`, printed perhaps as "Definition 4.2"), unique within an edition, and reset in each new edition. The type word is presentation, not identity. Foreshadowing and restatement appearances carry no label; they cite the derivation's label. A claim printed twice in one edition has two labels that point to the same ID.
