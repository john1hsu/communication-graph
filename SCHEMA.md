# Article schema

Each article is one **node**: `articles/<domain>/<slug>.md`, where the filename equals the id's slug and `<domain>` is a key in `topics/seeds.yaml`. Scaffold one with `python3 scripts/kg.py new <domain> <slug> <Type>`, which pre-fills the fields and sections its class needs.

```markdown
---
id: cm:bottom-line-up-front              # cm: + lowercase-hyphen slug; never changes
type: Technique                          # most specific class from ontology/ontology.ttl
title: Bottom line up front
aliases: [BLUF, answer first]
domain: writing                          # key in topics/seeds.yaml (becomes a SKOS ConceptScheme)
summary: >-                              # 1–2 sentence definition (skos:definition)
  Opening a message with the conclusion or request, then giving the supporting detail.
level: introductory                      # introductory | intermediate | advanced
evidenceStatus: practitioner             # see table below
broader: [cm:message-structure]          # skos:broader, 1–3; must stay acyclic
related: [cm:pyramid-principle]          # skos:related (symmetric)
requires: [cm:audience-analysis]         # learning prerequisites (transitive, acyclic) -> graph/learning-path.md
relations:                               # typed edges: EVERY one cites a source id below
  - {predicate: addresses, object: cm:burying-the-lede, source: s1, confidence: high}
  - {predicate: appliedIn, object: cm:email, source: s2}                       # confidence defaults to medium
  - {predicate: structures, object: cm:executive-summary, source: s1}
steps:                                   # Technique: >= 3 ordered steps -> schema:HowTo
  - Write the one sentence you most need the reader to remember or act on.
  - Put that sentence first, stating any request and deadline explicitly.
  - Add only the background the reader needs to act, most important first.
example:                                 # Technique, AntiPattern: required before/after rewrite
  situation: Asking a director to approve extra budget by email.
  before: "Hi Dana, as you know the project started in March and we have had several vendor issues..."
  after: "Dana, please approve $12K for extra testing by Friday so we can keep the June go-live. Details below."
  why: The decision, amount and deadline are visible in the first line, so a busy reader can act without scrolling.
selfCheck:                               # Skill, Technique, AntiPattern, Barrier: >= 2, each ends with "?"
  - Could the reader act on my first sentence alone?
  - Is my request or conclusion stated before any background?
sameAs: []                               # optional entity links: Wikidata QIDs or https IRIs (incl. sibling graphs) -> skos:exactMatch
sources:                                 # >= 3; >= 2 strong; >= 1 scholarly
  - id: s1
    title: "Federal Plain Language Guidelines"
    publisher: plainlanguage.gov (U.S. federal Plain Language Action and Information Network)
    url: https://www.plainlanguage.gov/guidelines/
    type: government
    accessed: 2026-11-02
created: 2026-11-02
modified: 2026-11-09                     # optional; set when an article is revised
---

# Bottom line up front

Prose with footnote citations after each claim.[^s1]

## Origin
## Why it matters
## How to apply it         (Technique)        ## Common mistakes   (Technique)
## What good looks like    (Skill, Disposition) ## How to practise it (Skill, Disposition)
## How to spot it          (Barrier, AntiPattern) ## How to fix it  (Barrier, AntiPattern)
## What works here         (Context, Channel, Genre) ## Pitfalls    (Context, Channel, Genre)
## Evidence                (Barrier, Phenomenon, Theory: key studies, effect sizes, replications)
## Connections             (always: explain each edge in prose, with citations)
## Sources                 (always)
[^s1]: PLAIN, "Federal Plain Language Guidelines". https://www.plainlanguage.gov/guidelines/ (accessed 2026-11-02)
```

Class-specific headings are enforced; `## Origin` and `## Why it matters` are expected for every article.

## Classes (`type`)

| Class | Use for |
|---|---|
| `Concept` | general ideas: audience, message, register, rapport |
| `Skill` | learnable capabilities: active listening, storytelling, concise writing, facilitation |
| `Technique` | concrete methods with steps: SBI feedback, BLUF, paraphrasing, labeling, calibrated questions |
| `Framework` | structuring models: SCQA, Johari window, Thomas-Kilmann, nonviolent communication, ladder of inference |
| `Principle` | guiding norms: know your audience, plain language, Grice's maxims |
| `Disposition` | traits behind good communication: empathy, assertiveness, curiosity, candor |
| `Barrier` | obstacles: curse of knowledge, illusion of transparency, defensiveness, information overload |
| `AntiPattern` | bad habits: burying the lede, wall of text, interrupting, filler words, death by PowerPoint |
| `Context` | recurring situations: executive briefing, one-on-one, job interview, difficult conversation |
| `Channel` | media: email, chat, video call, phone, slide deck, in person |
| `Genre` | formats: executive summary, status report, elevator pitch, decision memo, apology |
| `Theory` | academic theories: media richness, politeness theory, elaboration likelihood model |
| `Phenomenon` | observed patterns: psychological safety, mirroring, primacy effect, high-/low-context cultures |
| `Field` | disciplines: rhetoric, pragmatics, organizational communication, negotiation research |
| `Person`, `Organization`, `Work`, `Study`, `Event` | people, institutions, landmark books/guides, landmark studies, milestones |

Disjointness is declared (problems — `Barrier`, `AntiPattern` — vs. remedies — `Skill`, `Technique`, `Principle`, `Disposition`; `Context` vs. `Channel` vs. `Genre`; concepts vs. people, works and studies). The reasoner types unwritten nodes from edge ranges; two edges that imply incompatible types fail the build.

## Predicates (`relations[].predicate`)

| Predicate | Meaning | Constraint | Inferred inverse |
|---|---|---|---|
| `partOf` | component of | transitive | `hasPart` |
| `requires`* | learning prerequisite | transitive, acyclic | `prerequisiteOf` |
| `instanceOf` | variant of | | `hasInstance` |
| `contrastsWith`, `confusedWith`, `alternativeTo`, `complements` | comparisons | symmetric | itself |
| `develops` | practice that builds a skill | Technique/Framework/Principle → Skill/Disposition | `developedBy` |
| `addresses` | fixes a problem | Technique/Framework/Principle/Skill/Disposition → Barrier/AntiPattern | `addressedBy` |
| `structures` | gives structure to a format | Technique/Framework/Principle → Genre | `structuredBy` |
| `appliedIn` | used in a situation, channel or format | → Context/Channel/Genre | `benefitsFrom` |
| `causes` | leads to | | `causedBy` |
| `undermines` | damages (trust, clarity, rapport…) | Barrier/AntiPattern → | `underminedBy` |
| `explainedBy` | mechanism or theory behind | | `explains` |
| `demonstratedBy` | shown by a landmark study | → Study | `demonstrates` |
| `supportedBy`, `challengedBy` | evidence for / critique, failed replication, myth-busting | | `supports`, `challenges` |
| `introducedBy` | named or popularised by | → Person | `introduced` |
| `introducedIn` | introduced in | → Work | `introduces` |
| `authoredBy` | author of a work | Work → Person | `authored` |
| `influencedBy` | intellectual influence | | `influenced` |
| `studiedIn` | studied in a discipline | → Field | |

\* `requires` is written as its own list, not under `relations`. Never write inverses yourself; the reasoner materialises them in `graph/inferred.nt`. If you need a new predicate or class, add it to `ontology/ontology.ttl` with a label, any domain/range, and its inverse/characteristics in the same commit.

## Evidence status

| value | meaning | rule |
|---|---|---|
| `robust` | empirical finding that has replicated well | needs a peer-reviewed or primary study |
| `mixed` | real but smaller, moderated or context-dependent effects | needs a peer-reviewed or primary study |
| `contested` | active dispute, or advice widely repeated beyond its evidence (e.g. the "7-38-55" rule) | needs a study + a `challengedBy` relation |
| `failed-replication` | large replications failed to reproduce the original effect (e.g. power posing's hormonal claims) | needs a study + a `challengedBy` relation |
| `practitioner` | expert or practitioner consensus with little formal testing | not allowed for `Theory` |
| `theoretical` | an academic model or theory, judged by explanatory use | |
| `historical` | mainly of historical interest (people, works, events) | |

## Source types

| type | strong | scholarly | examples |
|---|---|---|---|
| `peer-reviewed` | yes | yes | *J. Applied Psychology*, *Communication Monographs*, *Administrative Science Quarterly*, *Negotiation Journal* (DOI page) |
| `primary` | yes | yes | the original study, book or guide (publisher page, author's copy) |
| `textbook` | yes | yes | academic communication, rhetoric, negotiation and OB textbooks |
| `academic` | yes | yes | Harvard Program on Negotiation, Stanford GSB Insights, HBS Working Knowledge, Purdue OWL, university writing centres |
| `government` | yes | yes | plainlanguage.gov, Federal Plain Language Guidelines, GOV.UK style guide, OPM, CDC CERC |
| `intergovernmental` | yes | yes | OECD, UN, WHO communication guidance |
| `scholarly-encyclopedia` | yes | yes | Stanford / Internet Encyclopedia of Philosophy (rhetoric, speech acts, pragmatics) |
| `practitioner-journal` | yes | no | *Harvard Business Review*, *MIT Sloan Management Review* |
| `institutional` | yes | no | Center for Creative Leadership, Toastmasters International, SHRM, IABC |
| `encyclopedia` | yes | no | Britannica |
| `preprint`, `news`, `community` | no | no | context only, never the sole support for a claim |

**Banned:** Wikipedia (and mirrors), wikiHow, Quora, Fandom, content farms, SEO listicles and AI-generated pages.

## Enforcement summary (`scripts/kg.py check`)

1. **Structure:** required fields, enums, id/filename/folder agreement, known domain, dates.
2. **Citations:** ≥ 3 sources, ≥ 2 strong, ≥ 1 scholarly, empirical claims backed by a study, https only, no banned or duplicate URLs, every source cited, every substantive paragraph cited, every typed edge cites a source.
3. **Practice rules:** class-specific sections; ≥ 3 steps for techniques; before/after rewrites for techniques and anti-patterns (before ≠ after, with a reason); ≥ 2 self-check questions for skills, techniques, anti-patterns and barriers; `challengedBy` for disputed advice.
4. **Graph rules:** ≥ 3 edges and ≥ 1 typed relation per node, domain/range on written targets, no cycles in `broader` / `requires` / `partOf`.
5. **Uniqueness:** no shared ids, titles or aliases; no near-identical titles; no copied text (5-gram shingles); no same-topic rewrite (TF-IDF cosine ≥ 0.80; ≥ 0.60 warns).
6. **Reasoning:** OWL 2 RL closure; any node inferred into two disjoint classes fails.
7. **SHACL:** `ontology/shapes.ttl` over the exported RDF with RDFS inference.
