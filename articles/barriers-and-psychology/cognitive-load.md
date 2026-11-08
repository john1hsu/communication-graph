---
id: cm:cognitive-load
type: Theory
title: Cognitive load theory
aliases: [cognitive load, CLT, working memory load, Sweller's cognitive load theory]
domain: barriers-and-psychology
summary: >-
  John Sweller's theory that new information must pass through a small, short-lived working
  memory, so a message is understood best when its design removes avoidable mental effort
  (extraneous load) and leaves room for the genuine complexity of the content (intrinsic load).
level: intermediate
evidenceStatus: mixed
broader: [cm:cognitive-psychology]
related: [cm:information-overload, cm:assertion-evidence-slides, cm:presentation, cm:plain-language, cm:curse-of-knowledge, cm:bottom-line-up-front, cm:gestures, cm:eye-contact, cm:elaboration-likelihood-model, cm:readability-formulas]
requires: []
relations:
  - {predicate: introducedBy, object: cm:john-sweller, source: s2, confidence: high}
  - {predicate: studiedIn, object: cm:educational-psychology, source: s1, confidence: high}
  - {predicate: supportedBy, object: cm:ginns-2006, source: s3, confidence: medium}
  - {predicate: challengedBy, object: cm:de-jong-2010, source: s2, confidence: high}
  - {predicate: complements, object: cm:plain-language, source: s5, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Cognitive Architecture and Instructional Design: 20 Years Later"
    publisher: Sweller, J., van Merriënboer, J. J. G. & Paas, F., Educational Psychology Review 31(2), 261-292, 2019, doi:10.1007/s10648-019-09465-5 (open-access copy via CORE)
    url: https://core.ac.uk/download/237588613.pdf
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s2
    title: "Cognitive load theory, educational research, and instructional design: some food for thought"
    publisher: de Jong, T., Instructional Science 38, 105-134, 2010, doi:10.1007/s11251-009-9110-0 (University of Twente repository)
    url: https://ris.utwente.nl/ws/files/6597420/Jong10cognitive.pdf
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s3
    title: "Spatial Continuity Effect vs. Spatial Contiguity Failure: Revising the Effects of Spatial Proximity Between Related and Unrelated Representations"
    publisher: Beege, M., Wirzberger, M., Nebel, S., Schneider, S., Schmidt, N. & Rey, G. D., Frontiers in Education 4:86, 2019
    url: https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2019.00086/pdf
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s4
    title: "Seeking a science of instruction"
    publisher: Mayer, R. E., Instructional Science 38, 143-145, 2010, doi:10.1007/s11251-009-9113-x (Springer)
    url: https://link.springer.com/article/10.1007/s11251-009-9113-x
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s5
    title: "Writing for user interfaces"
    publisher: GOV.UK Service Manual (UK Government Digital Service)
    url: https://gov.uk/service-manual/design/writing-for-user-interfaces
    type: government
    accessed: 2026-11-08
created: 2026-11-08
---

# Cognitive load theory

Cognitive load theory explains why a message can be accurate and still fail to land. Anything new a listener or reader takes in must first be handled by working memory, which holds only a few items and only for a short time; once knowledge is stored in long-term memory, those limits largely stop applying.[^s1] The theory splits the effort a message demands into two parts. **Intrinsic load** comes from how many elements of the content must be understood together, and it depends on what the audience already knows. **Extraneous load** comes from how the content is presented, and it is the part a communicator controls.[^s1]

## Origin

Educational psychologist John Sweller and colleagues developed the theory in the late 1980s and early 1990s, starting from studies of why solving practice problems was a surprisingly poor way to learn.[^s2] Sweller, van Merriënboer and Paas reviewed two decades of the work in 2019 and revised one idea: "germane" load is no longer treated as a third, separate load but as working memory redirected toward the content that matters.[^s1] The theory grew up in instruction research, but its findings map directly onto briefings, slides, documentation and onboarding at work.[^s1][^s2]

## Why it matters

Most communication failures that people blame on the audience's attention are design failures in this model. The research names several recurring ways a message adds extraneous load:[^s1]

- **Split attention:** the reader has to hold one source in mind while hunting for another, such as a chart on one slide and its explanation on the next.[^s1]
- **Redundancy:** the same self-contained information is repeated in another form, such as a presenter reading out text that is already on screen.[^s1]
- **Transient information:** spoken explanations and animations vanish as they go, so long spoken lists overload listeners faster than the same list in writing.[^s1]
- **Expertise reversal:** support that helps novices, such as step-by-step detail, can slow down and even hinder experts who already know it.[^s1]

The UK Government Digital Service builds the same aim into its writing guidance, telling teams to minimise cognitive load by writing clearly and using their users' own words.[^s5]

A workplace example. A product manager briefs executives on a delayed launch with a dense slide of six bullet points, a separate appendix chart and a spoken walk-through of each bullet. Listeners must read, listen and flip to the chart at once. Rewritten with cognitive load in mind, the slide states the conclusion as a headline ("Launch moves to 14 March; two vendor fixes remain"), puts the one chart that proves it on the same slide with labels on the lines, and the manager talks about the chart rather than reading the text. The content is identical; the effort to absorb it is not.[^s1][^s3]

### Applying it

Cut anything the audience does not need to act on. Put related words and visuals together. Do not read slides aloud. Break long spoken explanations into short segments and leave key numbers in writing. Adjust detail to the audience's expertise rather than giving everyone the novice version.[^s1][^s3]

## Evidence

The effects behind the theory have substantial support. A 2006 meta-analysis by Paul Ginns found that integrating related text and visuals improved learning with a large average effect (d = 0.85), but the benefit was clear for complex material and small and non-significant for simple material.[^s3] That boundary matters for workplace messages: careful layout pays off most when the content is genuinely hard.[^s3]

The theory itself is more disputed. In a widely cited 2010 critique, Ton de Jong argued that the three load types are hard to tell apart, that cognitive load is usually measured with a single self-rating item that studies interpret inconsistently, and that outcomes can be explained after the fact by relabelling a load as helpful or harmful, which makes the theory hard to falsify.[^s2] He also noted that many experiments use short, system-paced lessons with students, whereas real readers can pause, reread and take notes, so overload may occur less often outside the laboratory.[^s2] Richard Mayer replied that such failures are better read as boundary conditions that sharpen the theory.[^s4] Even supportive studies show the nuance: a 2019 pair of experiments found that a fully separated text-and-picture layout did not do worse than integrated versions, and the authors questioned the validity of their own load questionnaire.[^s3]

The fair summary is mixed: the practical design effects are well supported for complex, unfamiliar material, while the theory's account of why they work, and how to measure load, remains contested.[^s2][^s3][^s4]

## Connections

The theory was introduced by John Sweller and is studied in educational psychology, within the broader field of cognitive psychology.[^s1][^s2] It is supported by Ginns's 2006 meta-analysis of the contiguity (split-attention) effect and challenged by de Jong's 2010 critique of its concepts and measures.[^s2][^s3] It complements plain language: plain-language rules are one practical way to remove extraneous load, as the GOV.UK guidance makes explicit.[^s5] It is related to information overload, which describes the organisational state of too many messages while cognitive load describes the limit inside each reader, and to the curse of knowledge: because intrinsic load depends on prior knowledge, experts who forget what their audience lacks underestimate how hard their own content is.[^s1] Assertion-evidence slides, gestures, gaze and presentation design all draw on it to justify their advice, and it is related to bottom line up front, readability formulas and the elaboration likelihood model, which links persuasion to the audience's ability to process a message.[^s1][^s3]

## Sources

[^s1]: Sweller, van Merriënboer & Paas, "Cognitive Architecture and Instructional Design: 20 Years Later", Educational Psychology Review 2019. https://core.ac.uk/download/237588613.pdf (accessed 2026-11-08)
[^s2]: de Jong, "Cognitive load theory, educational research, and instructional design: some food for thought", Instructional Science 2010. https://ris.utwente.nl/ws/files/6597420/Jong10cognitive.pdf (accessed 2026-11-08)
[^s3]: Beege et al., "Spatial Continuity Effect vs. Spatial Contiguity Failure", Frontiers in Education 2019. https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2019.00086/pdf (accessed 2026-11-08)
[^s4]: Mayer, "Seeking a science of instruction", Instructional Science 2010. https://link.springer.com/article/10.1007/s11251-009-9113-x (accessed 2026-11-08)
[^s5]: GOV.UK Service Manual, "Writing for user interfaces". https://gov.uk/service-manual/design/writing-for-user-interfaces (accessed 2026-11-08)
