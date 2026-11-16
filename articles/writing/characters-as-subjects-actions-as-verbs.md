---
id: cm:characters-as-subjects-actions-as-verbs
type: Technique
title: Make characters subjects and actions verbs
aliases: [characters as subjects, actions as verbs, characters and actions, Williams's principles of clarity, denominalizing, unburying verbs]
domain: writing
summary: >-
  Joseph M. Williams's sentence-revision technique: find the main characters and the actions they
  perform, then rewrite so each character is a grammatical subject and each important action is a
  verb, which removes hidden verbs and makes clear who does what.
level: introductory
evidenceStatus: mixed
broader: [cm:editing-for-clarity]
related: [cm:nominalization, cm:paramedic-method, cm:active-voice, cm:passive-voice, cm:plain-language, cm:concise-writing, cm:clarity, cm:wordiness]
requires: []
relations:
  - {predicate: addresses, object: cm:nominalization, source: s2, confidence: high}
  - {predicate: develops, object: cm:concise-writing, source: s3, confidence: medium}
  - {predicate: complements, object: cm:active-voice, source: s3, confidence: medium}
  - {predicate: introducedBy, object: cm:joseph-m-williams, source: s1, confidence: high}
  - {predicate: introducedIn, object: cm:style-lessons-in-clarity-and-grace, source: s1, confidence: high}
  - {predicate: supportedBy, object: cm:spyridakis-isakson-1998, source: s5, confidence: medium}
  - {predicate: challengedBy, object: cm:balling-2018, source: s6, confidence: medium}
steps:
  - Pick a sentence that feels hard to read, usually a long one in a key paragraph such as the opening, the recommendation or the request.
  - Read its first seven or eight words and check whether the subject is an abstract noun and the verb arrives late or is a weak verb such as is, has, make or conduct.
  - Name the main characters, the people, teams or systems who act, even if the sentence never mentions them.
  - Find the important actions, especially those hidden in nouns ending in -tion, -ment or -ance, and in phrases like "make a decision" or "conduct a review".
  - Rewrite with each character as the subject and each action as its verb, and keep the subject close to its verb.
  - Join the resulting clauses with words that state the logic, such as because, if, when or although.
  - Keep a noun form when it names a concept readers already know, or when it links back to the previous sentence.
example:
  situation: An IT service manager updates department heads after a payroll-system outage and needs finance to rerun a batch.
  before: "Following the identification of the root cause as a configuration error during the patch deployment, the restoration of service was achieved at 14:10. Re-execution of the payroll batch by the finance team is required prior to the cutoff for the processing of payments."
  after: "Our infrastructure team found that a configuration error in Tuesday's patch caused the outage, and we restored service at 14:10. Finance, please rerun the payroll batch before the 17:00 payment cutoff."
  why: The original makes identification, restoration and re-execution the subjects and shows no one acting, so finance could miss that the next step is theirs; the rewrite names who found, restored and must rerun, puts each action in a verb, and states the deadline.
selfCheck:
  - In my most important sentences, is the subject a person or team who acts, rather than an abstract noun?
  - Is the action the reader must notice expressed as a verb, not as a noun after "make", "conduct" or "provide"?
  - Can a reader tell within the first few words who is doing what?
  - Where I kept a noun form, does it name a familiar concept or link to the previous sentence, rather than just sound formal?
sameAs: []
sources:
  - id: s1
    title: "Style: Lessons in Clarity and Grace, 13th edition"
    publisher: Joseph M. Williams & Joseph Bizup, Pearson (2021); Part II "Clarity", lessons "Actions" and "Characters" (publisher page)
    url: https://www.pearson.com/en-ca/subject-catalog/p/style-lessons-in-clarity-and-grace/P200000002140/9780137536603
    type: primary
    accessed: 2026-11-16
  - id: s2
    title: "Grammar and Style: Actions & Characters"
    publisher: Karin Gosselink, Yale Center for Teaching and Learning (handout adapted from Williams & Bizup, Style - The Basics of Clarity and Grace, 5th ed., Lessons 2-3)
    url: https://yale-nus.edu.sg/academics/wp-content/uploads/sites/8/2021/12/Grammar-Style-Actions-Characters.pdf
    type: academic
    accessed: 2026-11-16
  - id: s3
    title: "Plain Language Guide Series: Writing"
    publisher: Digital.gov, U.S. General Services Administration
    url: https://digital.gov/guides/plain-language/writing
    type: government
    accessed: 2026-11-16
  - id: s4
    title: "The Science of Scientific Writing"
    publisher: George D. Gopen & Judith A. Swan, American Scientist (1990), Sigma Xi (reprint hosted by Columbia University course page)
    url: https://www.cs.columbia.edu/~djhsu/coms6998-f17/science-of-writing.pdf
    type: primary
    accessed: 2026-11-16
  - id: s5
    title: "Study of nominalizations and denominalizations in technical prose"
    publisher: J. H. Spyridakis & C. S. Isakson, Journal of Technical Writing and Communication 28(2), 163-188 (1998), doi:10.2190/01hd-mhu1-qnx9-r3ye (catalogue record)
    url: https://katalog.adlr.link/Record/ai-49-aHR0cDovL2R4LmRvaS5vcmcvMTAuMjE5MC8wMWhkLW1odTEtcW54OS1yM3ll
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s6
    title: "No Effect of Writing Advice on Reading Comprehension"
    publisher: Laura Winther Balling, Journal of Technical Writing and Communication 48(1), 104-122 (2018), doi:10.1177/0047281617696983 (accepted manuscript, Copenhagen Business School)
    url: https://research-api.cbs.dk/ws/files/57294517/laura_winther_balling_no_effect_acceptedmanuscript.pdf
    type: peer-reviewed
    accessed: 2026-11-16
created: 2026-11-16
---

# Make characters subjects and actions verbs

This is a sentence-level revision technique: identify the main characters in a sentence (the people, teams or agents who do things) and the actions they perform, then rewrite so the characters are grammatical subjects and the important actions are verbs.[^s2] It is the standard remedy for nominalization, the habit of burying actions in nouns such as *implementation* or *determination*.[^s2] At work it turns "a decision was made to proceed with the migration" into "the steering group decided to migrate", which is shorter and says who owns the outcome.[^s3]

## Origin

The technique comes from Joseph M. Williams, who taught writing at the University of Chicago and built his textbook *Style* around it; the current edition, co-written with Joseph Bizup, opens its section on clarity with lessons titled "Actions" and "Characters".[^s1] University writing centres teach it from that book, summarising it as two principles, make main characters subjects and make important actions verbs, with a supporting rule to avoid unnecessary nominalizations.[^s2] Gopen and Swan reached a similar conclusion in a 1990 *American Scientist* article on scientific prose: readers expect a clause's action to sit in its verb and expect the verb to follow the subject closely.[^s4] U.S. federal plain-language guidance gives the same advice in simpler terms: restore hidden verbs and put the actor first, so it is clear who should do what.[^s3]

## Why it matters

Workplace writing usually exists to get someone to act, and readers act on what they can see: who did something, who must do something next, and by when.[^s3] When actions are nouns and characters are missing, a sentence can be grammatical yet leave readers unable to tell what the players are doing to one another, which is how Gopen and Swan describe a dense research paragraph whose key actions never appear as verbs.[^s4] Revising characters and actions also tends to shorten sentences, because each hidden verb needs a helper verb and prepositions that disappear once the verb is restored.[^s3]

## How to apply it

1. **Diagnose.** Scan for sentences that take effort to read and look at their opening words: an abstract subject and a late or weak verb are the warning signs.[^s2]
2. **Analyse.** Ask who the main character is and what the main action is; the character may be implied rather than named, so supply it from context.[^s2]
3. **Rewrite.** Make that character the subject, make the action the verb, and keep subject and verb close together.[^s2][^s4]
4. **Prefer active constructions where the actor matters.** This pairs naturally with active voice, which also puts the actor in the subject position.[^s3]
5. **Test the result.** Read the revised sentence alone: a reader should be able to say who does what without the surrounding paragraph.[^s4]

## Common mistakes

- **Forcing a person into every sentence.** Some subjects are rightly concepts or systems; the aim is a clear agent, not always a human.[^s2]
- **Fixing the verb but not the subject.** Replacing "conduct an analysis" with "analyse" helps, but if the subject is still "it" or "there", the reader may not know who analysed.[^s3]
- **Stopping at one sentence.** A restored verb can create a new subject that does not connect to the next sentence; read the paragraph again for flow.[^s4][^s6]
- **Treating it as a mechanical ban on nouns.** Familiar concepts (*the merger*, *the budget review*) can stay as nouns when readers already know them.[^s2]

## Evidence and limits

The technique is well established in writing instruction, but direct tests are few and mixed.[^s1][^s2] In a 1998 *Journal of Technical Writing and Communication* study, rewriting nominalizations as verbs helped native English readers focus on the more important information in technical passages, while nominalized versions could work well for non-native readers.[^s5] Balling's 2018 eye-tracking study of 27 Danish students reading English as a second language found no reliable reading-time or comprehension benefit when problem constructions, mostly nominalizations, were replaced with recommended ones; sentence length mattered more.[^s6] She concluded that the advice is too simple on its own and that how a construction supports cohesion between sentences probably matters more.[^s6] Neither study measured workplace outcomes such as whether readers took the requested action. Treat the technique as a strong default for showing accountability and next steps, and test important messages on international readers rather than assuming the verb version is always easier.[^s5][^s6]

## Connections

This technique **addresses** nominalization (`cm:nominalization`), the anti-pattern it was designed to fix.[^s2] It **develops** concise writing (`cm:concise-writing`) because restoring hidden verbs removes helper verbs and prepositions,[^s3] and it **complements** active voice (`cm:active-voice`), since both put the actor in the subject.[^s3] It was **introduced by** Joseph M. Williams (`cm:joseph-m-williams`) **in** *Style: Lessons in Clarity and Grace* (`cm:style-lessons-in-clarity-and-grace`).[^s1] Its benefit for native readers is **supported by** Spyridakis and Isakson 1998 (`cm:spyridakis-isakson-1998`),[^s5] and it is **challenged by** Balling 2018 (`cm:balling-2018`), which found no reading benefit for second-language readers.[^s6] It sits under editing for clarity and is close kin to Lanham's paramedic method, which also asks "where is the action?", and to plain language, which teaches the same hidden-verb rule; it helps against wordiness and passive constructions that hide the actor.[^s3]

## Sources

[^s1]: Williams & Bizup, *Style: Lessons in Clarity and Grace*, 13th ed., Pearson (2021), publisher page. https://www.pearson.com/en-ca/subject-catalog/p/style-lessons-in-clarity-and-grace/P200000002140/9780137536603 (accessed 2026-11-16)
[^s2]: Gosselink, "Grammar and Style: Actions & Characters", Yale Center for Teaching and Learning, adapted from Williams & Bizup, *Style*. https://yale-nus.edu.sg/academics/wp-content/uploads/sites/8/2021/12/Grammar-Style-Actions-Characters.pdf (accessed 2026-11-16)
[^s3]: Digital.gov (GSA), "Plain Language Guide Series: Writing". https://digital.gov/guides/plain-language/writing (accessed 2026-11-16)
[^s4]: Gopen & Swan, "The Science of Scientific Writing", *American Scientist* (1990). https://www.cs.columbia.edu/~djhsu/coms6998-f17/science-of-writing.pdf (accessed 2026-11-16)
[^s5]: Spyridakis & Isakson, "Study of nominalizations and denominalizations in technical prose", *Journal of Technical Writing and Communication* 28(2) (1998). https://katalog.adlr.link/Record/ai-49-aHR0cDovL2R4LmRvaS5vcmcvMTAuMjE5MC8wMWhkLW1odTEtcW54OS1yM3ll (accessed 2026-11-16)
[^s6]: Balling, "No Effect of Writing Advice on Reading Comprehension", *Journal of Technical Writing and Communication* 48(1) (2018), accepted manuscript. https://research-api.cbs.dk/ws/files/57294517/laura_winther_balling_no_effect_acceptedmanuscript.pdf (accessed 2026-11-16)
