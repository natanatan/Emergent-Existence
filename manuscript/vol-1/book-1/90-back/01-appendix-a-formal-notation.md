# Appendix A. Formal Notation

This appendix is the book’s reference for its notation: how to read a formula (A.1), the book’s arrows (A.2), its notation conventions (A.3), the symbol table (A.4) and the core equations (A.5). Readers new to formal notation will find a full introduction in the companion volume, *Emergent Existence: A Companion to the Formalism*, which explains every kind of formula the book uses, with examples from these chapters, exercises and answers.

## A.1 How to Read the Formulas

Most formulas stand on a line of their own, opened by a small square, ▪. Each is a sentence written in compressed form and can be read aloud:

▪ a ≬ b ⇒ b ≬ a

Read aloud: “if a differs from b, then b differs from a.” Three habits help. Translate a formula into words before judging it. Notice what it does not claim; the book often uses notation to show how little has been asserted. And check the surrounding prose for the formula’s status, since a definition, a working hypothesis and established mathematics look alike on the page.

The notation is standard logic and mathematics: connectives and quantifiers, sets, relations and their properties, equivalence and order, maps and transformations, symmetry, and comparison without numbers. The companion volume explains each of these in turn. The one convention particular to this book is its use of arrows, set out next.

## A.2 Arrows: Three Symbols, Separate Jobs

Arrows do several jobs in this book, and the jobs sit close together: the argument distinguishes the order in which it earns its concepts, the succession produced by an update, and genuine direction, and it must not let one pass for another. Following the notation discipline of A.3, jobs that could be confused have different symbols.

▪ Difference ⇝ Distinction ⇝ Retained distinction ⇝ Information

The squiggle arrow, ⇝, marks a chain of stages in the argument. Read it as “is followed in the derivation by.” It never means cause, time or physical direction. The book earns each of those later, and a chain written before they are earned must not borrow them.

▪ Σₙ ↦ Lₙ ↦ Σₙ₊₁

The barred arrow, ↦, marks what an update, transformation or assignment does to a particular state or item. Read it as “is sent to” or “is succeeded by,” or, in a perturbation such as r₀₁ ↦ r′₀₁, “is replaced by.” It is the standard notation for what a map does to a single member. The succession it records is the order of the update, not physical time, which Time earns separately.

▪ CG<sub>s</sub> : 𝒞 → 𝒞 / ≈<sub>s</sub>

The plain arrow, →, has two established uses, each in its own syntax. With a name and a colon, it states a map from one set to another. Read as “tends to,” as in d<sub>eff</sub>(σ) → 3, it states a limit. The two uses never meet in one expression, so they may share a symbol, and neither asserts direction. When Orientation earns direction, it writes it as orientational dependency, ≺ₒ (7.2, 7.6), and introduces no directed arrow of its own. A coupling between a variation and its consequences, such as K<sub>ij</sub> : Δr<sub>i</sub> ↦ Δ𝒫(r<sub>j</sub>), uses the barred arrow.

Two further symbols are easily mistaken for arrows of motion and are not. The double arrow ⇒ is logical implication. The curved sign ≺ is dependency precedence (14.4).

## A.3 Conventions

Notation discipline. A symbol may carry established meanings in formally distinct syntactic domains where confusion is unlikely. Where two meanings can occur in the same conceptual or mathematical neighborhood, they must be separated explicitly.

The notation follows the author’s frozen notation table, and any change needs an entry here before it appears in a chapter.

Established physical symbols (c, G, S<sub>BH</sub>, l<sub>P</sub>) keep their standard meanings and take precedence over model symbols.

A chapter may not introduce a symbol without an Appendix A entry. Letters are chosen to stay clear of symbols already in use: in Formalism’s signature, for example, 𝒞 avoids closure notation, ℜ avoids the matrix R and the relational domain ℛ, and fraktur 𝔊 names the formal carrier.

Script and blackboard-bold letters (𝒞, 𝒟, ℛ, 𝒻, 𝔖, 𝕋) must be set in a face that stays distinct from the plain letters in print.

The Status column uses three labels. Defined term is stipulative. Working definition may be refined as chapters test it. A proposition label, such as Proposition 1B, means the entry depends on a claim that is not yet Retained.

## A.4 Symbol table

| **Symbol** | **Meaning** | **Note** |
| --- | --- | --- |
| Ω | Origin: the minimally resolved reference condition | Origin |
| 𝔇 | Primitive difference: the dyad ⟨a, b; ≬⟩, taken as one structure | Difference |
| ≬ | The primitive difference relation, symmetric and irreflexive | Difference |
| 𝒞\_𝔇 | The minimal configuration carrier {a, b}: Difference’s poles promoted to configurations once admissible succession is introduced | Distinction |
| 𝒰<sub>min</sub> | The minimal admissible transition relation {(a, b), (b, a)}, with no primitive self-transition | Distinction |
| J\_𝒰 | The reciprocal map induced by 𝒰<sub>min</sub>; J\_𝒰² = id, so identity arises from composition | Distinction |
| 𝔗<sub>test</sub> | Diagnostic transformation family used to test retention, declared in the metalanguage and not an internal update law | Boundary |
| Pres<sub>W</sub> | Preservation predicate: the images of a and b under a transformation remain non-equivalent as resolved by frame W; kept distinct from Return’s Ret(A<sub>F</sub>; ·) | Boundary |
| ⇝ | Derivational sequence: “is followed in the derivation by”; never cause, time or direction | All chapters; A.2 |
| ↦ | Update, transformation or assignment applied to a particular state or item: “is sent to”, “is succeeded by”, “is replaced by” | A.2 |
| → | Map (with a name and colon) or limit (“tends to”); never direction, which Orientation writes with ≺ₒ | A.2 |
| r<sub>ij</sub>, r<sub>ab</sub> | Retained distinction between i and j (r<sub>ab</sub> at the minimal dyad); symmetric until Orientation | Boundary to Relation |
| R = \[r<sub>ij</sub>\] | The retained relations r<sub>ij</sub> arranged as a pairwise array | Relation |
| ℛ | Relational set {q<sub>i</sub>, R<sub>ij</sub>} | Relation |
| Π<sub>F</sub> | Projection: a resolution map from a richer relational substrate to effective geometry, possibly many-to-one | Geometry |
| CG\[·\] | Coarse-graining operator | Space to Gravity |
| 𝔖 | Substrate state, reserved for Book II | Book II (Gravity) |
| d<sub>ij</sub> | Correlation-based emergent distance | Distance |
| d<sub>O</sub>(A,B) | Ontological distance: raised in Orientation as an open question, not constructed in Book I | Orientation |
| I | Information | Boundary |
| ι<sub>i</sub>, μ<sub>i</sub>, ρ<sub>i</sub>, σ<sub>i</sub>, α<sub>i</sub>, n<sub>i</sub> | Information capacity, memory depth, recursive depth, self-model, agency, accessible degrees of freedom | Vol II |
| 𝒞<sub>i</sub>, Ξ | Consciousness of entity i, and the function that combines the six quantities above | Vol II |
| 𝒻<sub>i</sub>, W<sub>i</sub> | Reference frame and its weighting operator | Boundary; Vol II |
| Φ | Substrate field, with ⟨Φ⟩ the vacuum value and Φ<sub>eff</sub> the effective field | Gravity to Quantum Gravity |
| Z<sub>a</sub> | Complex amplitude of oriented distinction, A<sub>a</sub> e^(iθ\_a) | Orientation |
| φ, F<sub>n</sub> | Golden ratio; Fibonacci numbers | Scale |
| f<sub>k</sub>, Θ | Layer map and network parameters | Vol II |
| 𝒰 | Admissible transition relation on configurations, the second foundational commitment; a subscript names what it updates | Distinction to Closure, 8, 16 |
| a\*, E<sub>req</sub> | Optimal intervention; required evidence | Vol III |
| 𝒫 | Possibility function: the set of relational states reachable from a configuration; 𝒫(r<sub>ij</sub> / ℛ) is the same set for a relation embedded in a domain | Boundary (4.10); Relation |
| 𝒜 | Aggregation, by convention only: 𝒜\_∃, 𝒜\_∀ abbreviate ∃ and ∀ over a shared membership predicate; not a primitive | Boundary (proposed); Relation (5.12) |
| M<sub>ℛ</sub>(r) | Membership predicate: r participates in the organization ℛ exactly when 𝒫(r given ℛ) ≠ 𝒫(r) | Relation (5.12) |
| ~#, ↪, ↔ | Equinumerosity, injection and bijection between organizations; \[A\]<sub>~#</sub> is a magnitude class. All available before numerals | Scale |
| mag(X), Cmp(X, Y) | Earned finite cardinal magnitude, and the comparative relation between two organizations. Lettered to stay clear of the marker vector m (3.6) and of Γ, which Book II reserves | Scale |
| λ\*, ⊔, ≈<sub>s</sub>, CG<sub>s</sub> | A stable scale factor as a fixed point of the ratio map; disjoint composition, implying no spatial separation; scale-relative equivalence and its coarse-graining operator | Scale |
| 𝔊, 𝒞, ℜ | The formal core and its parts: admissible configurations 𝒞 (clear of ℭ<sub>F</sub> and C<sub>ij</sub>) and the relation family ℜ (clear of ℛ and the matrix R) | Formalism |
| 𝒰\[Σ\], 𝒰̄, T̄ | The successor set of a configuration; the quotient transition relation; a transformation acting on identity classes. 𝒰 is a relation, and determinism is the case where every configuration has exactly one admissible successor | Formalism (Distinction to Return notation) |
| ~<sub>W</sub>, ≈<sub>𝒰</sub> | Frame equivalence, where a resolving frame cannot separate two configurations, and behavioral equivalence, where they support matching patterns of admissible transition. Neither is interchangeable with ~<sub>F</sub> | Boundary (4.5, 4.15); Formalism |
| Ind<sub>R</sub> = (V<sub>R</sub>, 𝒥<sub>R</sub>) | Candidate independence system over relational modes, offered as a possible pre-metric formalization of d<sub>R</sub>. Lettered to avoid 𝓘 (information) and I (the identity triple of 4.8) | Formalism (5.14) |
| Ret(A<sub>F</sub>; ·), Dom<sub>F</sub> | Return predicate for the organizational anchor A<sub>F</sub>, and the identity domain of the closed identity O<sub>F</sub>. Ret(A<sub>F</sub>; ·) takes a configuration (8.3) or an orientation structure (7.8, 8.16) | Return (named Orientation) |
| χ | Internal condition of a realization that is not constitutive of the identity criterion F; two realizations may satisfy the same F while differing in χ | Return |
| K<sub>ij</sub> | Constraint relation: how admissible variation in r<sub>i</sub> constrains that for<sub>j</sub>, K<sub>ij</sub> : Δr<sub>i</sub> ↦ Δ𝒫(r<sub>j</sub>) | Orientation |
| ≺ₒ | Orientational dependency: A ≺ₒ Σ₁ ≺ₒ … ≺ₒ Σ<sub>k</sub>. Not temporal precedence and not necessarily transitive or acyclic | Orientation |
| 𝔒, Ret(A<sub>F</sub>; 𝔒) | An orientation structure (fraktur O, clear of O<sub>F</sub> and O⁽ⁿ⁾), and whether a recursive organization under it returns to the identity class of anchor A | Orientation |
| W⁽ᴸ⁾, Res<sub>W₀</sub> | The resolving map of a frame at organizational level L, in the sense of 4.5 and not a length scale; Res<sub>W₀</sub>(Ω) = ∅ states that no distinction is resolvable in the framework’s initial frame | Orientation (Origin, Origin.5) |
| d<sub>O</sub> | Number of independent orientational modes; weaker than vector-space dimension, and its relation to d<sub>R</sub> and d<sub>P</sub> is open | Orientation |
| Closed<sub>F</sub>(ℛ) | Closure predicate: ℛ satisfies the structural closure test relative to F; a predicate, not an operator | Closure |
| 𝒮<sub>F</sub>(ℛ) | Set of configurations of ℛ satisfying the constraints constitutive of F; realizability requires 𝒮<sub>F</sub>(ℛ) ≠ ∅ (script S, to stay clear of S<sub>0</sub> and S<sub>1</sub>) | Closure |
| ℭ<sub>F</sub> | Class of configurations satisfying the structural closure conditions for F (fraktur C, to stay clear of 𝒞<sub>i</sub>, C<sub>ij</sub> and CG) | Closure |
| V<sub>F</sub> | Set of admissible variations that preserve F; a useful closure needs V<sub>F</sub> ≠ ∅ | Closure |
| F<sub>dyn</sub>, F<sub>obs</sub> | Invariant actually preserved by the dynamics, and a frame’s inferred criterion for it; F<sub>obs</sub> need not equal F<sub>dyn</sub> | Closure |
| λ<sub>i</sub>, λ<sub>W</sub>(O) | Relational profile of a state-position, or of an object as resolved by a frame W | Relation |
| 𝔗 | Class of admissible transformations for a structural invariant (fraktur, to stay clear of T<sub>ijkl</sub> and 𝕋²) | Relation |
| d<sub>R</sub> | Relational rank, d<sub>R</sub> := rank(Ind<sub>R</sub>), available once a suitable finite independence structure is earned; Geometry evaluates it on the stable independent modes of a geometric regime | Formalism (9.22); Geometry |
| d<sub>P</sub> | Dimension of whatever space a system’s components occupy; named in Book I only as a Book II quantity. d<sub>R</sub> ≠ d<sub>P</sub> in general; any comparison is withheld until both are earned | Relation (named); Distance |
| κ | Diffusion coefficient | Distance |
| ε, h, Δ | Curvature ratio l\_\*/L<sub>curvature</sub>; derivative step; finite difference | Distinction, Quantum Gravity |
| Closed<sub>F</sub>(ℛ) | Closure predicate for domain ℛ with respect to invariant F; true or false, not an operator | Closure |
| ℭ<sub>F</sub> | Class of configurations satisfying the structural closure conditions for F | Closure |
| V<sub>F</sub> | Admissible variations that preserve F | Closure |
| F<sub>dyn</sub>, F<sub>obs</sub> | The invariant preserved by the dynamics, and an observer’s criterion inferred from a resolving map W<sub>O</sub>; in general F<sub>obs</sub> ≠ F<sub>dyn</sub> | Closure |
| O<sub>F</sub>^(n), A<sub>F</sub>^(n) | A closed identity and its organizational anchor at organizational level n; the superscript is level, not scale or time | Closure; A.5 |
| 𝔐<sub>S</sub> | Internal model a system forms of its own state, reserved for Volume II | Vol II |
| A<sub>H</sub>, S<sub>BH</sub> | Horizon area; Bekenstein-Hawking entropy | Black Holes |
| d<sub>u</sub>(A,B) | The least magnitude of admissible relational mediation between two loci under the declared standard u; not a spatial length | Distance |
| u | The reusable relational standard against which chain magnitudes are compared; lettered to stay clear of the coarse-graining standard s of Scale | Distance |
| κ, K(A,B) | An admissible relational chain, and the set of such chains joining two loci; the minimum is taken over K(A,B), which must be non-empty and finite | Distance |
| L<sub>u</sub>(κ) | The magnitude of a chain: the comparative burden of the mediation it contains, additive only where composition is earned | Distance |
| 𝔏, 𝔏<sub>α</sub> | The layered relational substrate, and one metric-relational layer within it; distinct from the formal core 𝔊 of Formalism | Geometry |
| K<sub>α</sub>, K<sub>αβ</sub> | The constraints internal to a layer, and those coupling two layers; an extension of the constraint relation K<sub>ij</sub> of Orientation | Geometry |
| Π<sub>F</sub>, I<sub>F</sub> | The resolution map of a frame and the interaction it induces on the substrate; measurement is written O<sub>F</sub> = Π<sub>F</sub>(I<sub>F</sub>(𝔏)) | Geometry |
| d<sub>probe</sub> | Effective dimension in the operational sense: the fewest independent parameters preserving the declared invariants across probes; whether it always agrees with d<sub>R</sub> is open | Geometry |
| M(ε) | Covering number: the fewest neighborhoods N<sub>ε</sub> needed to cover a domain at scale ε | Geometry (12.19) |
| d<sub>B</sub> | Box-counting dimension, read from how M(ε) grows as ε shrinks; for a finite domain, the slope over a declared window | Geometry (12.19) |
| d<sub>sim</sub> | Self-similarity dimension, log N / log(1/r), for a set made of N copies of itself scaled by r | Geometry (12.19) |
| d<sub>H</sub> | Hausdorff dimension, the critical exponent of covers by sets of any size; defined on any metric domain | Geometry (12.19) |
| d<sub>T</sub> | Topological (covering) dimension, an integer fixed by the overlap of refined covers | Geometry (12.19) |
| d<sub>s</sub> | Spectral dimension, read from how the return probability p<sub>m</sub>(A) of a walk falls with its length m | Geometry (12.19) |
| p<sub>m</sub>(A) | Probability that a walk started at A stands at A again after m steps; m counts steps, not time | Geometry (12.19) |
| ε<sub>min</sub>, ε<sub>max</sub> | Lower and upper cutoffs of a scaling window | Geometry (12.19) |
| σ | The scale regime index, distinct from the magnitude standard u of Distance | Geometry |
| ℓ<sub>r</sub>, ℓ<sub>F</sub> | The resolution scale of the underlying organization and of the frame examining it; effective smoothness requires ℓ<sub>r</sub> much smaller than ℓ<sub>F</sub> | Geometry |
| Geo | An effective geometric organization: the coordinated structure on which localization is defined | Space |
| λ<sub>Geo</sub>(A), Loc(A) | The localization profile of A within Geo, and its localization class under the equivalence preserving that profile | Space |
| Adm(A,B \| ·) | The admissible relational couplings between two loci under a given geometric organization; the rule through which spatial locality would hide if it were assumed | Space |
| Sp, Sp<sub>F</sub> | A physically consequential spatial organization, and its resolution by a frame | Space |
| ≺ | Retained-dependency precedence: the later state contains consequences whose removal would change it or its admissibility; not yet physical succession | Time |
| ≺⁺ | Reachability through one or more ≺ links | Time (14.5) |
| ≈≺ | Mutual dependency: eᵢ ≈≺ eⱼ when each is reachable from the other; its classes collect dependency cycles | Time (14.5) |
| ≺ₜ | Temporal precedence between mutual-dependency classes; a strict partial order by construction | Time (14.5) |
| 𝒯 = (𝓔/≈≺, ≺ₜ, Rec, Cyc) | The candidate temporal object: resolvable events taken up to mutual dependency, temporal precedence between the resulting classes, the retained records by which precedence is recoverable, and an optional family of recurrent comparison processes | Time |
| Rec, Cyc | The record family and the recurrence family of 𝒯; lettered to stay clear of Formalism’s relation set ℜ and configuration set 𝒞 | Time |
| N<sub>C</sub>(eₐ,eᵦ) | The count of retained update steps along a chain: a structural quantity, and not yet a duration | Time |
| τ<sub>K</sub>(A,B) | The temporal measure supplied by a candidate clock K, as cycle count times the unit assigned to one cycle | Time |

## A.5 Core equations

Each equation is tagged by type, following the standing rule that established mathematics, model mathematics and conceptual notation stay distinct.

Recursive cycle (conceptual)

▪ ℛ⁽ⁿ⁾ ⇝ O<sub>F</sub>⁽ⁿ⁺¹⁾ ≡ A<sub>F</sub>⁽ⁿ⁺¹⁾ ⇝ ℛ⁽ⁿ⁺¹⁾

Read this only when ℛ⁽ⁿ⁾ satisfies the relevant closure and higher-order addressability conditions. The sequence is derivational and organizational, not temporal. Ω is not recursively copied forward; higher-order originhood is earned by closure (6.12, 6.13).

Fibonacci recurrence and golden ratio (established mathematics)

▪ Fₙ₊₁ = Fₙ + Fₙ₋₁, φ = (1 + √5) / 2

Consciousness vector (conceptual, Volume II)

▪ 𝒞<sub>i</sub> = Ξ(ι<sub>i</sub>, μ<sub>i</sub>, ρ<sub>i</sub>, σ<sub>i</sub>, α<sub>i</sub>, n<sub>i</sub>)

Bekenstein-Hawking entropy (established physics)

▪ S<sub>BH</sub> = k<sub>B</sub> A<sub>H</sub> / (4 ℓ<sub>P</sub>²)

Intervention rule (normative model, Volume III)

▪ a\* = argmax<sub>a</sub> \[ Benefit(a) − StructuralCost(a) − OtherHarm(a) − Uncertainty(a) \]

Evidence rule (normative model, Volume III)

▪ E<sub>req</sub> ∝ Depth × Irreversibility × Reach
