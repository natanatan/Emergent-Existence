# Claims model

Final design, 29 September 2026. This is the reference for every register, check and export in this repository. The editor's version of it is the *Claims Design Spec*.

## Five things kept separate

| Concept | Example | Identifies | Changes when |
| --- | --- | --- | --- |
| **Claim** | `EE-C-0137` | One proposition: what is asserted, and what that assertion depends on | Never. A different assertion is a different claim |
| **Version** | `EE-C-0137@v3` | One wording or formalization of that proposition | The wording or notation improves without changing the assertion |
| **Edition** | `book-1/beta` | One release of one book's manuscript | A new release is cut. Released editions are frozen |
| **Appearance** | Beta, `Ch4.2` | One place where one edition prints one version of the claim, and its label there | Per edition |
| **Element** | `Rd` (retained distinction) | One concept from the Linking Lexicon | The lexicon is revised |

## Claims

- **IDs are permanent, neutral and order-independent.** `EE-C-nnnn`, assigned in order of registration and never reused. The number records when a claim was registered and carries no meaning about position, importance or dependency.
- **An ID never encodes** chapter, section, volume, edition, status, kind or label.
- **Dependencies belong to the assertion.** They cannot change under one ID. Rewording or re-notating a claim is a new version and leaves its dependencies alone.
- **A changed assertion is a new claim.** The new ID `supersedes` the old one, and the old claim keeps its ID, history and dependencies, so citations of earlier editions still resolve.

### When a dependency is superseded (carried forward)

If `EE-C-0024` is superseded by `EE-C-0301`, a claim that requires `0024` keeps its own ID and its `requires` entry moves to `0301`. This is recorded as a dated event in its history. It is allowed only when the dependent claim still asserts the same thing and the successor plays the same role. If the dependent claim's assertion must change, it becomes a new claim as usual.

Until someone reviews it, the build lists every claim that still requires a superseded claim.

### When a hidden dependency is found (correction)

A dependency that was always needed but never declared is a correction, not a new claim. It is added to the same ID with a dated event, for example "dependency on EE-C-0026 found in v3, now declared". The build flags every correction for review.

## Versions

- A version holds the claim's wording and formal statement, the date it was introduced and the edition that first printed it.
- Earlier versions are never edited or deleted. An appearance in an old edition keeps pointing to the version it printed.

## Editions

- One record per release of one book: `id`, `volume`, `book`, `released`, `source_commit`.
- A released edition is frozen. Corrections go into the next edition.

## Appearances and labels

- **A label is positional.** It gives the order in which a claim appears in that edition, including its chapter, for example `Ch4.2`.
- **Numbering resets in each edition.** The same claim can be `Ch4.2` in the Beta and `Ch5.1` in the first edition.
- **Each appearance gets its own label.** If an edition prints the same claim twice, for example restated in a later chapter, each appearance has its own label and both point to the same claim ID.
- **A label is unique within one edition.** Different editions may reuse a label for different claims.
- Appearances are stored on the claim record:

```yaml
appearances:
  - { edition: book-1/beta, label: "Ch4.2", chapter: 4, section: "4.9",  version: v2 }
  - { edition: book-1/beta, label: "Ch9.6", chapter: 9, section: "9.10", version: v2 }   # restated in Formalism
  - { edition: book-1/ed1,  label: "Ch5.1", chapter: 5, section: "5.2",  version: v3 }
```

The printed label style (for example whether `Ch4.2` is set as "Definition 4.2") is a typographic decision. It does not affect the model.

## Uses of a concept

The Methodology separates constitutive, representational and diagnostic use. A claim records each reference by its use:

| Field | Use | Earned-order check |
| --- | --- | --- |
| `requires` | **Constitutive.** The claim needs it to hold | **Error** if it is earned in a later chapter |
| `forward_refs` | **Foreshadowing.** Points ahead to where it will be earned | Pass |
| `checked_against` | **Diagnostic.** A later framework used to check a result | Pass |
| `represents_with` | **Representational.** Richer notation for a structure already earned (Formal Admissibility Rule) | Pass |
| none | **Untyped.** A later concept appears and no use is declared | **Review flag**, not an error |

Order in the book alone never fails a claim.

## Elements and composition

- **Elements are the concepts of the Linking Lexicon,** each with a two-letter code, like a periodic table. The chapter stages are its rows. The three foundations sit at the top: Origin (Ω), primitive Difference (𝔇) and admissible transformation (𝒰).
- **A claim's `composition` lists the elements it rests on constitutively,** for example `Rd·Ps`. It is generated from the claim's `requires` and is therefore fixed for as long as the ID exists.
- Foreshadowed, diagnostic and representational references never enter the composition.
- The element table lives in `registers/elements/` and is shown in [`elements.md`](elements.md). The Linking Lexicon page is a view of it.

## Status

- Status lives only in the register, as dated `status_history` events. The current status is the latest event. The prose never prints it.
- Statuses are the Hypothesis Register's eight: Retained, Provisional, Derived, Open, Deferred, Rejected, Speculative, Superseded.

## Hypotheses

Hypotheses follow the same model. `EE-H-nnnn` is the identity, and the legacy `H-n` is kept as an alias. Their places in an edition are appearances.

## Complete claim record

```yaml
id: EE-C-0031
kind: criterion          # proposition | definition | criterion | test | ledger | representation | rule
use: constitutive        # constitutive | representational | diagnostic
composition: Rd·Ps       # generated from requires
requires: [EE-C-0024, EE-C-0025]
forward_refs: []
checked_against: []
represents_with: []
supersedes: []
superseded_by: []
aliases: []
versions:
  v1: { text: "𝒫(Σ, r_ab) ≠ 𝒫(Σ, ∅)", introduced: 2026-09-29, edition: book-1/beta }
appearances:
  - { edition: book-1/beta, label: "Ch4.9", chapter: 4, section: "4.17", version: v1 }
status_history:
  - { status: Provisional, date: 2026-09-29, edition: book-1/beta, reason: "Registered from Book I Beta" }
history:                 # carried-forward dependencies and corrections
  []
```

## Still open

- Which edition's order seeds the first ID numbers: the Beta, or the first edition when it freezes.
- The printed label style.
- Whether the STRONG / OPEN / PROVISIONAL verdict markers stay in the prose, given that status lives in the register.
