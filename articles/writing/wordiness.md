---
id: cm:wordiness
type: AntiPattern
title: Wordiness
aliases: [verbosity, verbiage, padded prose, needless words]
domain: writing
summary: >-
  Using more words than the message needs, through redundant pairs, empty qualifiers, inflated phrases,
  hidden verbs and content the reader does not need, so readers spend more effort to find less meaning.
level: introductory
evidenceStatus: mixed
broader: [cm:written-communication]
related: [cm:concise-writing, cm:paramedic-method, cm:nominalization, cm:plain-language, cm:wall-of-text, cm:passive-voice, cm:editing-for-clarity, cm:cognitive-load, cm:curse-of-knowledge, cm:email]
requires: []
relations:
  - {predicate: undermines, object: cm:clarity, source: s2, confidence: high}
  - {predicate: undermines, object: cm:credibility, source: s5, confidence: medium}
  - {predicate: supportedBy, object: cm:oppenheimer-2006, source: s5, confidence: medium}
  - {predicate: supportedBy, object: cm:bassin-martin-1976, source: s4, confidence: medium}
  - {predicate: supportedBy, object: cm:writing-for-busy-readers, source: s3, confidence: medium}
example:
  situation: An operations analyst emails a department head to ask for sign-off on moving a weekly report from Monday to Tuesday.
  before: "Hi Lena, I just wanted to reach out at this point in time in order to touch base with regard to the weekly KPI report. Due to the fact that the data warehouse refresh basically doesn't actually complete until quite late on Sunday night, the team is of the opinion that it would be really beneficial to give consideration to the possibility of making a change to the delivery day so that the report would be sent out on Tuesday instead of Monday going forward. Please let me know your thoughts and feedback at your earliest convenience."
  after: "Hi Lena, can we move the weekly KPI report from Monday to Tuesday, starting next week? The warehouse refresh finishes late on Sunday, so Monday's report often uses incomplete data. A yes by Friday lets us switch next week."
  why: The rewrite cuts the word count by more than half by dropping filler openers, empty qualifiers (just, basically, actually, really, quite), inflated phrases (due to the fact that, at this point in time) and hidden verbs (give consideration to, making a change), and it adds the one thing the original lacked, a clear question with a deadline.
selfCheck:
  - Could I delete my first sentence without the reader losing anything?
  - Which qualifiers (just, really, very, basically, actually) can I cut without changing the meaning?
  - Have I turned a verb into a noun phrase, such as "make a decision" or "give consideration to," where a single verb would do?
  - Does every sentence give this reader something they need to understand or act?
sameAs: []
sources:
  - id: s1
    title: "Writing Concisely"
    publisher: The Writing Center, University of North Carolina at Chapel Hill
    url: https://writingcenter.unc.edu/handouts/conciseness-handout
    type: academic
    accessed: 2026-11-18
  - id: s2
    title: "Plain Language Guide Series: Short and simple"
    publisher: Digital.gov, U.S. General Services Administration
    url: https://digital.gov/guides/plain-language/principles/short-simple
    type: government
    accessed: 2026-11-18
  - id: s3
    title: "Write shorter messages"
    publisher: Todd Rogers & Jessica Lasky-Fink, Harvard Kennedy School Executive Education (December 2020)
    url: https://www.hks.harvard.edu/sites/default/files/HKSEE/HKSEE%20PDFs/Write%20shorter%20messages.pdf
    type: academic
    accessed: 2026-11-18
  - id: s4
    title: "Effect of Three Types of Redundancy Reduction on Comprehension, Reading Rate, and Reading Time of English Prose"
    publisher: Carolyn B. Bassin & Clessen J. Martin, Journal of Educational Psychology 68(5), 649-652 (1976) (ERIC record EJ150857)
    url: https://eric.ed.gov/?id=EJ150857
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s5
    title: "Consequences of erudite vernacular utilized irrespective of necessity: problems with using long words needlessly"
    publisher: Daniel M. Oppenheimer, Applied Cognitive Psychology 20(2) (2006), doi:10.1002/acp.1178 (DeepDyve record)
    url: https://deepdyve.com/lp/doc/lPYnpsUrVG
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s6
    title: "The secret of impressive writing? Keep it plain and simple"
    publisher: EurekAlert! news release on Oppenheimer's Princeton University study (31 October 2005)
    url: https://www.eurekalert.org/news-releases/808085
    type: news
    accessed: 2026-11-18
created: 2026-11-18
---

# Wordiness

Wordiness is using more words than a message needs. It shows up as redundant pairs ("each and every"), empty qualifiers ("really," "basically"), inflated phrases ("due to the fact that" for "because"), strings of prepositional phrases, and modifiers the main word already implies ("anticipate in advance").[^s1] It also includes whole sentences and paragraphs the reader does not need, not just extra words inside a sentence.[^s1][^s2] Wordiness is the problem; [concise writing](concise-writing.md) is the skill that fixes it.

## Origin

Writing teachers have warned against padding for a long time, and university writing centres now sort it into recognisable types. The University of North Carolina's Writing Center, drawing on Joseph Williams and Joseph Bizup's *Style* and Richard Lanham's *Revising Prose*, lists seven common sources: redundant pairs, unnecessary qualifiers, overused prepositional phrases, unnecessary modifiers, wordy phrases, negative constructions and the passive voice.[^s1] In U.S. government writing, the federal plain-language guidance calls wordy, dense construction one of the biggest problems, and it singles out legal doublets such as "cease and desist" and modifiers such as "very" and "totally."[^s2]

## Why it matters

Extra words cost the reader time and attention and give them nothing back. In a field experiment by Todd Rogers and Jessica Lasky-Fink, 7,002 school district leaders received a survey request as either a 127-word email or a 49-word version with five middle sentences removed. The short email got 4.8% of recipients to click, against 2.7% for the long one. Yet 67% of 148 people asked beforehand predicted the longer email would do better.[^s3] Writers, in other words, tend to overestimate how much padding helps.

Wordiness can also hurt how readers see the writer. Across five experiments, Daniel Oppenheimer at Princeton found that readers rated the authors of needlessly complex texts as less intelligent than the authors of simpler versions of the same content. He traced the effect to processing fluency: text that is harder to read lowers how readers judge it.[^s5][^s6] The finding applies to words used needlessly, not to technical terms the content requires.[^s6]

## How to spot it

Read a draft once for each of these signs:

- **Pairs and repeats:** two words where one would do ("full and complete"), or the same idea restated with a synonym.[^s1][^s2]
- **Empty qualifiers:** "just," "really," "very," "quite," "basically," "actually," "totally."[^s1][^s2]
- **Inflated phrases:** "in order to," "at this point in time," "in the event that," "with regard to."[^s1]
- **Hidden verbs and prepositional chains:** "give consideration to the possibility of making a change," where one verb would do ("consider changing"). See [nominalization](nominalization.md).[^s1]
- **Throat-clearing openers and unneeded background:** a first sentence that announces you are writing, or context the reader already has. Plain-language guidance says to leave out anything the audience does not need and to have someone outside the subject check the draft from the reader's side.[^s2]

## How to fix it

1. Write the point and the request first. Then ask of each sentence whether this reader needs it to understand or act, and cut what fails.[^s2][^s3]
2. Delete empty qualifiers and redundant modifiers. Keep one word from each redundant pair.[^s1][^s2]
3. Swap inflated phrases for single words ("because," "if," "to," "about").[^s1]
4. Turn hidden verbs back into verbs, and put the actor first instead of using the passive voice ("the team approved" rather than "approval was given by the team").[^s1]
5. Rewrite negatives as positives where you can.[^s1]
6. For a fuller line edit, run the [paramedic method](paramedic-method.md), drawn from Richard Lanham's *Revising Prose*, one of the sources behind the UNC handout.[^s1]

**Pitfalls:** Do not cut so hard that you lose the reason, the deadline or the politeness the relationship needs. Rogers and Lasky-Fink's rewrites stayed polite and kept every request.[^s3] Do not swap clear technical terms for vaguer everyday ones just to save words.[^s6]

## Evidence

The evidence for cutting needless words is fairly consistent, but most of it comes from single studies, not meta-analyses. Rogers and Lasky-Fink's email experiment is a large field test, but it measured one outcome (clicking a survey link) with one audience.[^s3] An older laboratory study by Bassin and Martin cut a 2,217-word news article by 10%, 30% or 50% using three ways of removing redundancy. At the 10% and 30% levels, comprehension was the same whichever method was used, which suggests readers can lose a good share of redundant words without losing understanding.[^s4] Oppenheimer's five experiments used student raters and tested inflated vocabulary and fonts rather than padding as such, and we found no large multi-lab replication of them. They show a real fluency effect, but how far it reaches workplace email is untested.[^s5] For these reasons this node is rated *mixed*: the direction is well supported, but effect sizes depend on the audience, the channel and how the text is cut.

## Connections

- **Undermines clarity:** federal plain-language guidance counts wordy, dense writing among the biggest barriers to clear government writing.[^s2]
- **Undermines credibility:** needlessly complex wording lowered readers' judgments of the author's intelligence in Oppenheimer's experiments.[^s5]
- **Supported by Oppenheimer (2006),** the study behind the fluency explanation.[^s5]
- **Supported by Bassin and Martin (1976),** which found that removing a moderate share of redundant words left comprehension intact.[^s4]
- **Supported by *Writing for Busy Readers*:** Rogers and Lasky-Fink's research programme found that shorter messages got more responses.[^s3]
- **Related:** [concise writing](concise-writing.md) and the [paramedic method](paramedic-method.md) fix it. [Nominalization](nominalization.md) and the [passive voice](passive-voice.md) are common causes of it, as the UNC handout's categories show.[^s1] A [wall of text](wall-of-text.md) often shows up alongside it.

## Sources

[^s1]: The Writing Center, University of North Carolina at Chapel Hill. "Writing Concisely". https://writingcenter.unc.edu/handouts/conciseness-handout (accessed 2026-11-18)
[^s2]: Digital.gov (U.S. GSA). "Plain Language Guide Series: Short and simple". https://digital.gov/guides/plain-language/principles/short-simple (accessed 2026-11-18)
[^s3]: Rogers, T. & Lasky-Fink, J. (2020). "Write shorter messages". Harvard Kennedy School Executive Education. https://www.hks.harvard.edu/sites/default/files/HKSEE/HKSEE%20PDFs/Write%20shorter%20messages.pdf (accessed 2026-11-18)
[^s4]: Bassin, C. B. & Martin, C. J. (1976). "Effect of Three Types of Redundancy Reduction on Comprehension, Reading Rate, and Reading Time of English Prose". *Journal of Educational Psychology* 68(5), 649–652. https://eric.ed.gov/?id=EJ150857 (accessed 2026-11-18)
[^s5]: Oppenheimer, D. M. (2006). "Consequences of erudite vernacular utilized irrespective of necessity: problems with using long words needlessly". *Applied Cognitive Psychology* 20(2). doi:10.1002/acp.1178. https://deepdyve.com/lp/doc/lPYnpsUrVG (accessed 2026-11-18)
[^s6]: EurekAlert! (2005). "The secret of impressive writing? Keep it plain and simple" (news release on Oppenheimer's study, Princeton University). https://www.eurekalert.org/news-releases/808085 (accessed 2026-11-18)
