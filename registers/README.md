# Registers

The source of truth for claims, hypotheses and what each chapter earns. See [`docs/registers.md`](../docs/registers.md) for the fields and [`docs/claim-ids.md`](../docs/claim-ids.md) for the ID rules.

| Folder | Register |
| --- | --- |
| `claims/` | Claim Register, `EE-C-nnnn` |
| `hypotheses/` | Hypothesis Register (Appendix C), `EE-H-nnnn` |
| `ledgers/` | Inherits, earns and withholds, per chapter |
| `elements/` | The element table: Linking Lexicon concepts with two-letter codes |
| `editions/` | One record per edition of a book, frozen at release |
| `sources/` | Sources: papers, datasets, proofs and Companion runs that claims rely on, with their grade and currency. See [`docs/sources.md`](../docs/sources.md) |

Imported from Book I Beta on 29 September 2026. Each claim's `import` block records how it was extracted; appearance roles are left for the author to assign. Book II claims are registered chapter by chapter as drafts arrive, starting with Chapter 20 on 5 October 2026 (edition `book-2/beta`).
