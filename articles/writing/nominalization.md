---
id: cm:nominalization
type: AntiPattern
title: Nominalization
aliases: [hidden verbs, zombie nouns, buried verbs, smothered verbs, nominalisation]
domain: writing
summary: >-
  Turning the main action of a sentence into an abstract noun (decide becomes "make a decision",
  analyse becomes "conduct an analysis"), which adds words, hides who is doing what and makes
  business prose slower to read; the fix is to put the actor in the subject and the action in the verb.
level: introductory
evidenceStatus: mixed
broader: [cm:wordiness]
related: [cm:concise-writing, cm:plain-language, cm:active-voice, cm:passive-voice, cm:paramedic-method, cm:editing-for-clarity, cm:clarity, cm:register-and-tone]
requires: []
relations:
  - {predicate: undermines, object: cm:clarity, source: s3, confidence: medium}
  - {predicate: undermines, object: cm:concise-writing, source: s1, confidence: medium}
  - {predicate: introducedBy, object: cm:joseph-m-williams, source: s3, confidence: medium}
  - {predicate: demonstratedBy, object: cm:spyridakis-isakson-1998, source: s5, confidence: medium}
  - {predicate: challengedBy, object: cm:isakson-spyridakis-1995, source: s4, confidence: low}
  - {predicate: supportedBy, object: cm:billig-2008, source: s6, confidence: medium}
example:
  situation: An operations analyst emails the leadership team about a recurring invoice-processing delay and needs one director to act.
  before: "Following the completion of a review of invoice processing times, a determination was made that the implementation of the new approval workflow has resulted in a reduction in throughput. A recommendation for the reconsideration of the two-signature requirement is under preparation, pending confirmation of the availability of resources for the provision of training."
  after: "We reviewed invoice processing times and found that the new approval workflow has slowed throughput. We recommend dropping the second signature for invoices under $5,000. Dana, can you confirm by Friday that your team can run the training?"
  why: The original turns every action (review, determine, implement, reduce, recommend, confirm, provide) into a noun, so nobody is shown doing anything and the request has no owner; the rewrite names the actors, makes the actions verbs, and is about half as long.
selfCheck:
  - Can I point to who is doing the main action in each key sentence, and is that person or team the grammatical subject?
  - Have I written "make a decision", "conduct a review" or "provide an explanation" where "decide", "review" or "explain" would do?
  - Does any sentence string together several "the ... of" phrases or words ending in -tion, -ment or -ance?
  - Where I kept a noun form, is it because readers already treat it as a named concept, not because it sounds more formal?
sameAs: []
sources:
  - id: s1
    title: "Plain Language Guide Series: Writing (Avoid hidden verbs)"
    publisher: Digital.gov, U.S. General Services Administration (successor to plainlanguage.gov's Federal Plain Language Guidelines)
    url: https://digital.gov/guides/plain-language/writing
    type: government
    accessed: 2026-11-16
  - id: s2
    title: "Sentence Clarity: Nominalizations and Subject Position"
    publisher: Purdue Online Writing Lab, Purdue University
    url: https://owl.purdue.edu/owl/multilingual/multilingual_students/nominalizations_and_subject_position.html
    type: academic
    accessed: 2026-11-16
  - id: s3
    title: "Grammar and Style: Actions & Characters"
    publisher: Karin Gosselink, Yale Center for Teaching and Learning (handout adapted from Joseph M. Williams & Joseph Bizup, Style - The Basics of Clarity and Grace, 5th ed., Lessons 2-3)
    url: https://yale-nus.edu.sg/academics/wp-content/uploads/sites/8/2021/12/Grammar-Style-Actions-Characters.pdf
    type: academic
    accessed: 2026-11-16
  - id: s4
    title: "Nominalizations: effect on recall and comprehension"
    publisher: C. S. Isakson & J. H. Spyridakis, Proceedings of IPCC '95, IEEE International Professional Communication Conference, 203-206 (1995), doi:10.1109/IPCC.1995.554908 (catalogue record)
    url: https://manuscript.isc.ac/Inventory/49/1580763.htm
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s5
    title: "Study of nominalizations and denominalizations in technical prose"
    publisher: J. H. Spyridakis & C. S. Isakson, Journal of Technical Writing and Communication 28(2), 163-188 (1998), doi:10.2190/01hd-mhu1-qnx9-r3ye (catalogue record)
    url: https://katalog.adlr.link/Record/ai-49-aHR0cDovL2R4LmRvaS5vcmcvMTAuMjE5MC8wMWhkLW1odTEtcW54OS1yM3ll
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s6
    title: "The language of critical discourse analysis: the case of nominalization"
    publisher: Michael Billig, Discourse & Society 19(6), 783-800 (2008), doi:10.1177/0957926508095894 (Loughborough University Institutional Repository)
    url: https://dspace.lboro.ac.uk/dspace-jspui/handle/2134/13361
    type: peer-reviewed
    accessed: 2026-11-16
created: 2026-11-16
---

# Nominalization

A nominalization is a noun built from a verb or adjective: *decision* from decide, *implementation* from implement, *difficulty* from difficult.[^s2] The words themselves are ordinary. The anti-pattern is using them to carry the main action of a sentence, so that "we analysed the data" becomes "we conducted an analysis of the data". Federal plain-language guidance calls these hidden verbs: the noun usually needs a second, weak verb such as *make*, *conduct*, *achieve* or *take* to do the work the original verb did.[^s1] In workplace writing, chains of them produce sentences in which things happen but no one does them.[^s3]

## Origin

Grammarians have long described nominalization, but the modern advice against overusing it comes from the plain-language movement and from writing teachers. Joseph M. Williams built his widely taught approach to clear prose around two principles: make the main characters the subjects of sentences, and express their important actions as verbs, not as nouns derived from verbs.[^s3] U.S. federal plain-language guidance gives the same rule to government writers, with examples such as rewriting "we are responsible for management of the program" as "we manage the program".[^s1] Law-school, engineering and university writing centres repeat it, and Purdue's Online Writing Lab teaches it as a sentence-clarity basic.[^s2]

## Why it matters

A sentence is easiest to follow when a clear subject comes early and is followed quickly by its verb; nominalizations push the real verb later and add words to hold the noun in place.[^s2] They also remove the actor. "A determination was made" does not say who decided, which matters at work because accountability, ownership and next steps depend on knowing who acts.[^s3] The plain-language guidance adds that hidden verbs travel with other wordy habits: uncovering one usually lets you cut a passive construction and a padded phrase as well.[^s1] Billig makes a related point about academic writing: turning actions into things lets writers sidestep saying who did what, and simpler prose that names human agents is clearer.[^s6]

## How to spot it

- Look for nouns ending in -tion, -sion, -ment, -ance, -ity or -ness that name an action someone takes.[^s1][^s2]
- Look for weak verb plus noun pairs: *make a decision*, *conduct a review*, *provide an explanation*, *achieve a reduction*, *reach an agreement*.[^s1]
- Look for chains of "the ... of" phrases, such as "the implementation of the approval of the request".[^s1]
- Ask who the character is and what they do; if neither appears as subject and verb, the action is probably buried.[^s3]

## How to fix it

- **Find the actor and the action.** For each long or vague sentence, name who does the main thing and what they do.[^s3]
- **Make the actor the subject and the action the verb.** For example, *the reduction of costs was achieved by the regional teams* becomes *the regional teams cut costs*.[^s3]
- **Delete the helper verb.** Replace *conduct an analysis* with *analyse* and *make a recommendation* with *recommend*.[^s1]
- **Keep the useful ones.** Leave a noun form when readers already treat it as a named concept (*the budget review*, *the merger*) or when you are making a general point about an idea rather than about who acts; just avoid stacking several in one sentence.[^s2]
- **Check for global readers.** For teams working in a second language, test the revised version on a colleague rather than assuming the verb form is always easier (see Evidence).[^s5]

## Evidence

The advice is widely taught but has had little direct testing, and the results are mixed. In a 1995 IEEE conference study, Isakson and Spyridakis gave readers nominalized or denominalized versions of technical passages: nominalizations central to a passage's main point affected recall, but comprehension scores did not differ between versions.[^s4] Their fuller 1998 study in the *Journal of Technical Writing and Communication* found that verb-based text helped native English speakers focus on the more important information, while the nominalized versions could work quite well for non-native readers.[^s5] These are small laboratory studies of technical prose, not of workplace outcomes such as response rates or decisions. Billig's critique is argument, not experiment, though it supports the clarity and agency concerns.[^s6] Treat "use verbs, not hidden verbs" as a strong default for native-speaker readers and a reason to check, rather than assume, for international ones.[^s4][^s5]

## Connections

Nominalization is a common form of **wordiness** (`cm:wordiness`) and **undermines clarity** (`cm:clarity`), because it hides who acts,[^s3] and **concise writing** (`cm:concise-writing`), because each hidden verb needs a helper verb and extra phrases.[^s1] Its modern framing as a style fault is **introduced by** Joseph M. Williams (`cm:joseph-m-williams`), whose characters-as-subjects, actions-as-verbs rule is the standard remedy.[^s3] The recall benefit of revising it is **demonstrated by** Spyridakis and Isakson 1998 (`cm:spyridakis-isakson-1998`),[^s5] while their 1995 study (`cm:isakson-spyridakis-1995`) **challenges** the assumption that it harms comprehension.[^s4] Billig 2008 (`cm:billig-2008`) **supports** the agency argument.[^s6] It often appears alongside the **passive voice** and is fixed by **active voice**, **plain language**, **editing for clarity** and the **paramedic method**; overusing it can also make the **register and tone** of a message feel stiff and bureaucratic.[^s1][^s3]

## Sources

[^s1]: Digital.gov (GSA), "Plain Language Guide Series: Writing", section "Avoid hidden verbs". https://digital.gov/guides/plain-language/writing (accessed 2026-11-16)
[^s2]: Purdue Online Writing Lab, "Sentence Clarity: Nominalizations and Subject Position", Purdue University. https://owl.purdue.edu/owl/multilingual/multilingual_students/nominalizations_and_subject_position.html (accessed 2026-11-16)
[^s3]: Gosselink, "Grammar and Style: Actions & Characters", Yale Center for Teaching and Learning, adapted from Williams & Bizup, *Style*. https://yale-nus.edu.sg/academics/wp-content/uploads/sites/8/2021/12/Grammar-Style-Actions-Characters.pdf (accessed 2026-11-16)
[^s4]: Isakson & Spyridakis, "Nominalizations: effect on recall and comprehension", IPCC '95 Proceedings, IEEE (1995). https://manuscript.isc.ac/Inventory/49/1580763.htm (accessed 2026-11-16)
[^s5]: Spyridakis & Isakson, "Study of nominalizations and denominalizations in technical prose", *Journal of Technical Writing and Communication* 28(2) (1998). https://katalog.adlr.link/Record/ai-49-aHR0cDovL2R4LmRvaS5vcmcvMTAuMjE5MC8wMWhkLW1odTEtcW54OS1yM3ll (accessed 2026-11-16)
[^s6]: Billig, "The language of critical discourse analysis: the case of nominalization", *Discourse & Society* 19(6) (2008). https://dspace.lboro.ac.uk/dspace-jspui/handle/2134/13361 (accessed 2026-11-16)
