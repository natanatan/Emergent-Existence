# Emergent Existence: Shared Style Sheet

*A shared working reference for Sol and Claude, drafted by Claude from decisions made with Natan through 30 September 2026 and revised with Sol's additions. Natan's decisions override anything here. This file is the canonical copy for every Claude session working in this repository; Sol receives it pasted.*

Rules marked **[T]** also affect typesetting: the build process recognizes them automatically, so departures show up as formatting errors, not just style lapses.

## 1. Roles and handoffs

- **Sol drafts; Claude reviews, edits, typesets and draws the figures; Natan decides.** Claude does not draft chapter arguments.
- **Send a change note with every block:** which sections changed, what changed, and why. This stops either of us overwriting the other's edits unknowingly.
- **Draft from the latest source.** Claude's edits land in the build source after each round; a block drafted from an older file will reintroduce text that was already cut.
- **[T] Keep editorial notes out of the chapter text.** Put them in a separate "Notes for the editor" file. Notes left in the text ("Editorial note for the next revision", "Not for print", author queries, pilot notes) have printed in the draft at least a dozen times.

## 2. Architecture

- **Title:** *Emergent Existence*, Volume I: Existence, Book I: Foundations of Physical Reality. Chapters 1 to 14, Origin through Time; Book II begins with physical spacetime.
- **Two foundational commitments so far:** Difference (Chapter 2) and admissible transformation 𝒰 (introduced in Distinction, Chapter 3). Origin is the starting point, not a commitment.
- **Ω** is the minimally resolved reference condition: not a pole, anchor, place, moment or cause. The first endogenous organizational reference role is earned in Closure, as the organizational anchor A_F.
- **Ω withholds, it does not specify.** Nothing below the initial frame's resolution is asserted or excluded: absolute nothing, perfect uniformity and unresolved variation all remain admissible. Don't write Ω as having, or lacking, sub-threshold structure, and don't give it set membership (1.7).
- **Do not index Ω as a recursively reproduced origin.** Higher-order originhood is written O_F^(n) / A_F^(n), never Ω_n. Closure re-instantiates the *role* of origin; it does not reproduce Ω.
- **"Before" is derivational, not temporal,** unless Time has earned it.
- **The chapter order is one reading order.** Dependencies are established within each chapter, not implied by sequence.
- **Stage sequence is not dependency.** A chapter or concept appearing earlier in the reading order does not by itself license a *requires* or *derives* claim. Dependency must be structure the claim actually needs; where a term is introduced is metadata, not a premise.
- **Dependency is not causation.** Say *dependency* unless causal structure has been earned (Time 14.19).
- **Role notation does not add an entity.** A_F, clockhood, reference, localization and similar role terms name functions of already-earned organizations, unless the text explicitly introduces a new entity.
- **A formal resource is not automatically an ontological dependency.** Later chapters may require a specific structure first made explicit in Formalism, such as Ind_R, d_R, quotient dynamics or a declared map, without making Formalism itself an ontological stage.

## 2a. Readability and testability are kept apart

- **The book carries readability; the register and the Computational Companion carry testability.** The prose states the argument cleanly. A claim's epistemic kind is carried by the prose and its epistemic mark; its standing, dependencies, derivation location and evidence live in the registers; tests of it live in the Companion.
- **Don't distribute testability through ordinary running prose.** Status, diagnostic burden and failure conditions belong in their designated audit sections, the registers and the Companion, not repeated throughout the argument. No status words, no repeated cautions that a step is provisional or not yet ruled out. The book presents a method and one proposed derivation; readers judge each step on their own foundations. A limit is stated once, in its designated place (§4), and only when a careful reader would otherwise be misled.
- **The epistemic marks stay** (●, —, ○, ◌, ▷, ▪, ◇). They classify the kind of claim, not its standing.
- **Claim tags link the two layers.** Each claim's derivation or statement carries an invisible tag in the source, `<!-- EE-C-nnnn derivation -->` or `<!-- EE-C-nnnn statement -->`, placed immediately before the line where it begins. Tags never print. Keep them with their claim when editing, and never add or remove one without the register changing too; the build checks that every tag matches the register and every register entry has its tag.
- **A tag identifies the claim occurrence, not its printed position.** Moving a claim does not change its EE-C-nnnn; only the appearance metadata (section, label) changes.
- **Consequences.** A voice edit cannot break a test, and a test result never forces a caveat into the prose. When a test changes a claim's standing, the register changes; the text changes only if the argument itself changes.

## 3. Chapter structure

- **Claim line:** leads with what emerges. One sentence of about 25 to 35 words, then a sentence of conditions if needed. Don't open with a negation.
- **[T] Chapter discipline:** begin the paragraph with the words "Chapter discipline." Give a short inheritance sentence and the chapter's burden. List exclusions only when a reader might actually assume them; the Origin Inheritance Ledger records the rest.
- **[T] Audit sections use these exact titles:** "Objections and Replies", "What Would Count Against the Claim", "Precursors and Departures", "Ontological Defensibility Pulse: [Chapter]", "Candidate Diagnostics and Failure Tests". The sage audit-layer styling is applied by matching these titles.
- **The Pulse in physical chapters (Book II onward)** answers two further fields after the standing ones (Natan, 5 October 2026; first used in 20.26). **Experimental discrimination:** for each empirical claim the chapter leans on, what was controlled, what distribution was observed, with what uncertainty, against which models; which accounts the result actually discriminated; and what new arrangement would make this account's prediction differ from its competitors'. **Resolution discipline:** a distinction obtained through one kind of coupling is not promoted to a property of the substrate unless it persists across very different couplings. The full eight questions are in Natan's evidence note (`Experimental_Evidence_and_Ontological_Underdetermination.md`); the per-source answers live in the sources register (`docs/sources.md`, "Evidence"), not in the prose.
- **[T] Objections:** each begins "Objection N:" followed by a one-sentence objection, and every reply begins "Reply:" (a colon, not a full stop), whether inline or as its own paragraph.
- **[T] End matter, in order:** "Implications and Handoff" (the last numbered section), then "Questions Opened by This Framework", then "Selected References Cited in [Chapter]".
- **Precursors:** at the chapter's end, not its opening. The book-wide statement that the ingredients are not new is made once, in 2.19; later chapters give only their own precursors.

## 4. Stating limits

- **State each limit once, in its designated place:** the "What … Does Not Earn" or handoff section, the Pulse, or the Register.
- **Elsewhere, keep a negation only if it prevents a live misreading at that point.** The test: complete the sentence *"Without this, a careful reader might reasonably infer that…"* If the completion is implausible, cut it.
- **The same test governs an analogy's limit.** State it only when the misleading feature could plausibly carry over into the claim.
- **Once a limitation is established in its designated place, don't repeat it** unless the local passage creates a new plausible misreading.
- **Say "not evidence for the ontology" once, in the Methodology.** Don't repeat it chapter by chapter.
- **Cut "X rather than Y"** where Y was never plausible.
- **Parsimony limits commitments, not conclusions.** Never argue that a structure does not exist because the framework does not yet require it; record it as open (Questions Opened, or the Register). A sparse foundation does not imply a sparse world: layered structure is to be derived, not denied.
- **Strength of evidence for an effect is not strength of evidence for its interpretation** (Natan, 5 October 2026). An experiment establishes a conditional distribution under stated conditions, with an uncertainty and a significance against a stated null model; it does not establish the picture attached to the model that fits it. Write what was observed in observation language, and give "path", "photon arrival", "virtual particle", "collapse" or "the vacuum is a structured state" as one theory's reading unless an experiment discriminated it. Preserve the empirical invariants; reopen the mechanism wherever experiment has not discriminated it. The full standard is Natan's evidence note (`Experimental_Evidence_and_Ontological_Underdetermination.md`); the Book II Methodology states it once.

## 5. Prose

- **No drafting history in the text:** "earlier drafts", "the revised chapter", "this revision", "the old architecture".
- **No "EE".** Write "the framework" or "this book".
- **American spelling:** favor, neighbor, behavior.
- **One quotation per source,** and under fifteen words; paraphrase otherwise.

## 6. Notation

- **Arrows (Appendix A.2):** ⇝ for derivational progression; ↦ for a map, coupling or update of a particular item; → only for a map between sets or a limit; ⇒ for implication. **Arrow glyphs do not themselves assert ontological direction:** direction is carried by earned relational structure, especially ≺ₒ.
- **Orders:** ≺ is retained-dependency precedence (Boundary); ≺ₒ is oriented dependency (Orientation); ≺ₜ is temporal precedence between classes (Time).
- **Keep resolving and identity notation separate.** W, Res_W and ~_W concern frame-relative resolvability; F, ~_F, O_F and A_F concern identity and organizational reference. Never use F for a resolving frame: a frame-resolved relational profile is λ_W(O), and local frames are W_A, W_B.
- **Settled symbols:** d_R for relational rank (not d_rank); Ret(A_F; ·) for return; O_F, A_F, Dom_F.
- **[T] Write subscripts with an underscore:** A_F, O_F, Σ_a, K_ij, d_R, and braces for longer ones, such as ~_{F′}. Subscripts written in Word formatting are often lost in conversion; more than 150 have had to be restored by hand.
- **Every new symbol needs an Appendix A entry,** chosen to stay clear of symbols already in use (A.3).

## 7. Figures

- **Claude draws them.** Describe the idea, or the analogy, and where it should go.
- **Captions state the point, not what the picture shows.** Description belongs in alt text.
- **Text stays at full strength;** only de-emphasized parts of the drawing are faded.
- **Numbers must be exact:** anything with a stated distance, count or proportion is drawn to scale.
- **Acknowledge known precedents** for an analogy, with a verified reference (as with Calvino's arch).

## 8. Register and references

- **Never rewrite a historical claim silently.** Once an edition is released, a changed claim is marked Superseded, keeps its original wording, and gets a new entry. Until then (the Beta stays open until it goes to a peer reviewer), wording is edited in place.
- **Check that new Register IDs are unused** (H-133 was assigned twice).
- **Claims and hypotheses are separate namespaces.** `EE-C-nnnn` identifies claims; `EE-H-nnnn` identifies hypotheses, with the legacy `H-n` kept as an alias of its EE-H entry. Never reuse a number across namespaces or alias an H entry to an EE-C claim.
- **References:** verified, alphabetical within each chapter, with at most a one-clause annotation.

## 9. Lexicon and dependency graph

- **Node metadata records where a term is introduced;** it does not establish dependency.
- ***requires*** means the target cannot be formulated or earned in the current framework without the source. ***derives*** means the target is actually obtained from the displayed prerequisites; use it sparingly.
- **Forward references must not become backward dependencies.** Mark them as forward references.
- **Role re-instantiation is not identity:** A_F may re-instantiate originhood without becoming Ω.
- **Not every edge is a dependency.** In the claim register, dependencies are constitutive premises; other links are relations (derives_from, supersedes, refines, equivalent_to, contrasts_with, generalizes, specializes, foreshadows, diagnoses, tests, represents). Only constitutive dependencies contribute to a claim's composition. The Lexicon's *requires* and *derives* are element-graph terms and are not interchangeable with claim relations.
- **Don't duplicate transitive dependencies** unless the direct edge carries explanatory weight.
- **Planned later-volume nodes are marked Planned,** and must not make Book I claims appear to depend on undeveloped future structure.
