---
id: cm:active-voice
type: Technique
title: Active voice
aliases: [use the active voice, actor-first sentences, who-does-what sentences]
domain: writing
summary: >-
  Writing sentences so the person or organisation doing the action is the grammatical subject
  ("The team will send the report"), rather than the thing acted on ("The report will be sent"),
  so readers can see who does what.
level: introductory
evidenceStatus: mixed
broader: [cm:clarity]
related: [cm:plain-language, cm:bottom-line-up-front, cm:effective-writing-for-army-leaders, cm:concise-writing]
requires: []
relations:
  - {predicate: partOf, object: cm:plain-language, source: s1, confidence: high}
  - {predicate: addresses, object: cm:unclear-ownership, source: s1, confidence: high}
  - {predicate: contrastsWith, object: cm:passive-voice, source: s2, confidence: high}
  - {predicate: supportedBy, object: cm:paolazzi-et-al-2019, source: s4, confidence: medium}
  - {predicate: explainedBy, object: cm:good-enough-processing, source: s5, confidence: medium}
  - {predicate: challengedBy, object: cm:fear-and-loathing-of-the-english-passive, source: s3, confidence: high}
steps:
  - Find each sentence that has a form of "to be" plus a past participle (was sent, will be reviewed, has been approved).
  - Ask who does the action; if the sentence does not say, decide who should, and name them.
  - Rewrite with that actor as the subject and a strong verb right after it ("Finance will review the budget").
  - Address the reader as "you" when they are the one who must act.
  - Keep a passive only when the actor is unknown, unimportant or obvious, or when the thing acted on is what the paragraph is about.
example:
  situation: A project manager tells a client team what happens before go-live.
  before: "The test results will be reviewed and any outstanding issues must be resolved before the release can be approved."
  after: "Our QA lead will review the test results by Tuesday. Your team needs to fix any open issues by Thursday, and then I will approve the release."
  why: The original names no one, so each side can assume the other owns the work; the rewrite assigns every action to a person and a date.
selfCheck:
  - Can the reader tell, sentence by sentence, who is responsible for each action?
  - Where I kept a passive, is the actor unknown, unimportant or obvious, or am I hiding who decided?
  - Did I mislabel any sentence as passive just because it uses "was" or describes the past?
sameAs: []
sources:
  - id: s1
    title: "Writing (Plain Language Guide Series): Use active voice"
    publisher: Digital.gov (U.S. General Services Administration)
    url: https://digital.gov/guides/plain-language/writing
    type: government
    accessed: 2026-11-03
  - id: s2
    title: "Choosing Active and Passive Voice"
    publisher: Purdue Online Writing Lab (Purdue University)
    url: https://owl.purdue.edu/owl/general_writing/academic_writing/active_and_passive_voice/choosing_passive_voice.html
    type: academic
    accessed: 2026-11-03
  - id: s3
    title: "Fear and Loathing of the English Passive"
    publisher: Geoffrey K. Pullum, University of Edinburgh (author's web version of an article in Language and Communication)
    url: https://pullum.ppls.ed.ac.uk/passive_loathing.html
    type: primary
    accessed: 2026-11-03
  - id: s4
    title: "Passives are not hard to interpret but hard to remember: evidence from online and offline studies"
    publisher: Paolazzi, Grillo, Alexiadou & Santi, Language, Cognition and Neuroscience, 2019 (White Rose repository record)
    url: https://eprints.whiterose.ac.uk/145484
    type: peer-reviewed
    accessed: 2026-11-03
  - id: s5
    title: "Good-Enough Representations in Language Comprehension"
    publisher: Ferreira, Bailey & Ferraro, Current Directions in Psychological Science 11(1), 2002 (APS abstract page)
    url: https://www.psychologicalscience.org/journals/current-directions/1467-8721.00158/
    type: peer-reviewed
    accessed: 2026-11-03
created: 2026-11-03
---

# Active voice

Active voice means building a sentence so that whoever performs the action is the subject: "We proposed new regulations" rather than "New regulations were proposed."[^s1] U.S. federal plain-language guidance recommends it because it makes clear who should do what, and calls passive sentences that hide the responsible party one of the biggest problems in government writing.[^s1] The Purdue Online Writing Lab gives the same default, saying active voice helps create clear, direct sentences, while still listing cases where a passive is the better choice.[^s2]

## Origin

Grammarians of the 19th century described the passive without judging it; according to linguist Geoffrey Pullum, blanket advice to avoid it took hold in early 20th-century style manuals, most famously William Strunk's rule to use the active voice.[^s3] Government plain-language programmes later made active voice a core habit of official writing, telling writers to prefer "You must do it" over "It must be done."[^s1]

## Why it matters

At work, most writing exists to get something done, and a passive sentence can describe a task without assigning it. "The contract must be signed by Friday" leaves the reader to guess whether they, legal or the vendor will sign; "You must sign the contract by Friday" does not.[^s1] Purdue's writing lab makes the same point from the reader's side: putting the doer first produces clear, direct sentences, and the passive is best saved for when the doer genuinely does not matter.[^s2] In client, project and policy writing, where missed ownership turns into missed deadlines, that visibility of who acts is the main payoff.[^s1]

## How to apply it

1. Scan the draft for a form of "to be" (is, was, were, will be, has been) followed by a past participle, usually ending in "-ed"; that pairing is the usual marker of a passive.[^s1]
2. For each one, ask who performs the action. If the sentence does not say, decide who should and name them.[^s1]
3. Put that actor first and the verb right after it, and use "you" when the reader is the one who must act.[^s1]
4. Keep the passive when the actor is unknown, unimportant or obvious, when the thing acted on is the topic of the paragraph, or when your field expects it, as in many scientific methods sections.[^s2]

**Example.** A project manager writes to a client: "The test results will be reviewed and any outstanding issues must be resolved before the release can be approved." Rewritten: "Our QA lead will review the test results by Tuesday. Your team needs to fix any open issues by Thursday, and then I will approve the release." The first version names no one, so each side can assume the other owns the work; the second assigns each action to a person, which is the gap federal guidance says passive voice creates.[^s1]

## Common mistakes

- **Confusing passive with past tense.** "The team shipped the fix" is past tense and fully active; tense and voice are separate questions.[^s1]
- **Flagging anything with "was."** Pullum documents style critics labelling sentences such as "a struggle ensued" or "five girls have died" as passive when they are not, so a mechanical word search over-corrects.[^s3]
- **Forcing an actor in.** When the doer is unknown or irrelevant ("The server was restarted overnight"), inventing one adds words without adding clarity.[^s2]
- **Using the passive to dodge accountability.** "Mistakes were made" is the opposite failure: the actor is known and matters, and the reader notices it is missing.[^s1][^s2]

## Evidence

Comprehension research supports part of the advice. Ferreira and colleagues review evidence that readers often build shallow, "good-enough" interpretations and misread who did what to whom in passive sentences, sometimes keeping the wrong reading even after reanalysing the sentence.[^s5] A 2019 set of experiments by Paolazzi and colleagues complicates that picture: across four self-paced reading studies, passives were read faster than matched actives, but readers answered questions about who did what less accurately after passives, a difficulty the authors locate in remembering the sentence rather than parsing it.[^s4] These are laboratory studies of single sentences, not tests of workplace documents.[^s4][^s5]

The style claims go further than that evidence. Pullum argues that charges that passives are always weak, dull or evasive are unsupported, notes that admired writers including Orwell and E. B. White use passives freely, and recommends teaching writers to recognise passives and choose them deliberately rather than banning them.[^s3] The status here is therefore `mixed`: naming the actor reliably helps when responsibility or "who did what" matters, but a blanket rule against the passive is not supported.[^s3][^s4]

## Connections

- **Part of plain language:** federal plain-language guidance lists active voice among its core writing practices.[^s1]
- **Addresses unclear ownership:** the guidance's main argument is that passive sentences hide who is responsible for each task.[^s1]
- **Contrasts with passive voice,** which Purdue OWL treats as a legitimate choice when the receiver of the action deserves the focus.[^s2]
- **Supported by** Paolazzi et al. (2019), whose readers were less accurate on who-did-what questions after passives, and **explained by** good-enough processing, the account Ferreira and colleagues give of such misreadings.[^s4][^s5]
- **Challenged by** Pullum's "Fear and Loathing of the English Passive", which argues the anti-passive rule is overstated and often misapplied.[^s3]
- **Related:** active voice sits beside the other plain-language writing habits, such as shorter words, short sections and addressing the reader as "you".[^s1] It also pairs with answer-first structure (bottom line up front) and concise writing, and *Effective Writing for Army Leaders* treats it as a core staff-writing habit (see those articles for their sources).

## Sources

[^s1]: Digital.gov (U.S. GSA). "Writing", Plain Language Guide Series (section on active voice). https://digital.gov/guides/plain-language/writing (accessed 2026-11-03)
[^s2]: Purdue Online Writing Lab. "Choosing Active and Passive Voice". Purdue University. https://owl.purdue.edu/owl/general_writing/academic_writing/active_and_passive_voice/choosing_passive_voice.html (accessed 2026-11-03)
[^s3]: Pullum, G. K. "Fear and Loathing of the English Passive". *Language and Communication* (author's web version, University of Edinburgh). https://pullum.ppls.ed.ac.uk/passive_loathing.html (accessed 2026-11-03)
[^s4]: Paolazzi, C., Grillo, N., Alexiadou, A. & Santi, A. (2019). "Passives are not hard to interpret but hard to remember: evidence from online and offline studies". *Language, Cognition and Neuroscience*. https://eprints.whiterose.ac.uk/145484 (accessed 2026-11-03)
[^s5]: Ferreira, F., Bailey, K. G. D. & Ferraro, V. (2002). "Good-Enough Representations in Language Comprehension". *Current Directions in Psychological Science* 11(1). https://www.psychologicalscience.org/journals/current-directions/1467-8721.00158/ (accessed 2026-11-03)
