---
id: cm:burying-the-lede
type: AntiPattern
title: Burying the lede
aliases: [burying the lead, buried lede, buried main point, burying the ask]
domain: writing
summary: >-
  Placing the most important point of a message - the decision, request, risk or news - after background,
  history or lesser details, so readers who skim or stop early miss it or misread what the message is about.
level: introductory
evidenceStatus: mixed
broader: [cm:message-structure]
related: [cm:bottom-line-up-front, cm:pyramid-principle, cm:wall-of-text, cm:email, cm:executive-briefing, cm:status-reporting, cm:delivering-bad-news, cm:information-overload]
requires: []
relations:
  - {predicate: demonstratedBy, object: cm:kieras-1980, source: s3, confidence: medium}
  - {predicate: supportedBy, object: cm:kieras-1979, source: s4, confidence: medium}
  - {predicate: challengedBy, object: cm:ameseder-devetak-skubic-2026, source: s5, confidence: medium}
  - {predicate: undermines, object: cm:clarity, source: s2, confidence: medium}
example:
  situation: An engineering manager emails a vice president after a vendor slip and needs a go/no-go decision on paying for weekend overtime by Wednesday noon.
  before: "Hi Sam, quick update on the payments integration. As you know we kicked off with the vendor in July and the first two milestones went well. Over the last few weeks we have been working through some API changes on their side, and the team has done a great job adapting. Last Thursday the vendor told us their sandbox will be down until the 18th. We looked at a few options, including stubbing the service, and think weekend overtime is the most realistic way to protect the launch date, which would cost about $9K. Let me know what you think."
  after: "Subject: Decision by Wed noon - approve $9K overtime to keep the 1 Dec launch?\n\nSam, I need a yes/no by Wednesday noon on about $9K of weekend overtime. Without it, the 1 December launch slips about two weeks.\n\nWhy: the vendor's sandbox is down until the 18th, which removes our last test window.\nOption we rejected: stubbing the service - faster to build, but it leaves the riskiest calls untested.\n\nBackground on the integration is below if useful."
  why: In the original the cost, the decision and the deadline arrive in the last two sentences and the deadline is never stated, so a reader skimming the opening reads it as a routine progress note; the rewrite states the decision, amount, deadline and consequence in the subject line and first sentence and moves the history to the end.
selfCheck:
  - If my reader stopped after the first two sentences, would they know what I need, by when, and why it matters?
  - Is anything in my opening paragraph there only because it happened first, rather than because the reader needs it first?
  - Does my subject line or first slide name the decision, risk or news itself, not just the topic?
  - If I am delivering bad news, have I stated it plainly before the explanation instead of after it?
sameAs: []
sources:
  - id: s1
    title: "Is it 'Bury the Lede' or 'Bury the Lead'?"
    publisher: Merriam-Webster, Words at Play
    url: https://www.merriam-webster.com/wordplay/bury-the-lede-versus-lead
    type: encyclopedia
    accessed: 2026-11-11
  - id: s2
    title: "Army Regulation 25-50: Preparing and Managing Correspondence"
    publisher: Headquarters, Department of the Army (10 October 2020), copy hosted by the Maine Bureau of Veterans' Services
    url: https://www.maine.gov/dvem/policies/documents/AR%2025-50%20(10%20October%202020).pdf
    type: government
    accessed: 2026-11-11
  - id: s3
    title: "Abstracting Main Ideas from Technical Prose: A Preliminary Study of Six Passages"
    publisher: David E. Kieras, Technical Report No. 5, Department of Psychology, University of Arizona, for the Office of Naval Research (1980) (DTIC)
    url: https://apps.dtic.mil/sti/pdfs/ADA089910.pdf
    type: primary
    accessed: 2026-11-11
  - id: s4
    title: "Initial Mention as a Cue to the Main Idea and the Main Item of a Technical Passage"
    publisher: David E. Kieras, Technical Report No. 3, Department of Psychology, University of Arizona, for the Office of Naval Research (1979) (DTIC)
    url: https://apps.dtic.mil/sti/pdfs/ADA073773.pdf
    type: primary
    accessed: 2026-11-11
  - id: s5
    title: "Incidental Learning From Science Journalism: The Effects of a Narrative Writing Style on the Comprehension and Situational Interest of Austrian Non-Experts in Health Sciences"
    publisher: Christian Ameseder, Iztok Devetak & Darija Skubic, Center for Educational Policy Studies Journal 16(3), 201-234 (2026), doi:10.26529/cepsj.1899
    url: https://www.cepsj.si/index.php/cepsj/article/view/1899
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s6
    title: "When Writing for Busy Readers, Less Is More"
    publisher: Todd Rogers & Jessica Lasky-Fink, Behavioral Scientist (11 September 2023)
    url: https://behavioralscientist.org/when-writing-for-busy-readers-less-is-more/
    type: practitioner-journal
    accessed: 2026-11-11
created: 2026-11-11
---

# Burying the lede

Burying the lede means putting the most important point of a message - the decision you need, the risk you have found, the news the reader must act on - somewhere after the background, the history or the minor details. The phrase comes from newsrooms, where the lede is a story's opening and burying it means hiding the most important information beneath lesser material.[^s1] At work it shows up as status emails that open with what the team has been doing, briefings that reach the recommendation on the last slide, and bad-news messages that make the reader wade through context before learning what went wrong.[^s2][^s6]

## Origin

The idiom is journalism jargon. Merriam-Webster traces the spelling *lede* to the 1970s, when newsrooms used it to keep the opening of a story distinct from *lead*, the metal strips that spaced lines of type; the dictionary added *lede* in 2008, and *bury the lead* is still seen in print.[^s1] Workplace writing standards turned the newsroom lesson into a rule. The US Army's correspondence regulation names putting the main point at the beginning (bottom line up front) as one of the two essential requirements of Army writing, and tells writers of memorandums to state the purpose and then the recommendation, conclusion or most important information straight away.[^s2]

## Why it matters

Readers use the opening of a text to decide what the whole thing is about. In reading experiments sponsored by the US Office of Naval Research, David Kieras found that people treated the first-mentioned idea as the topic of a passage, and when two topics were present they more often judged the first-mentioned one to be the main one.[^s3][^s4] A buried point therefore does double damage: it is reached late, and the reader has already filed the message under the wrong heading by the time it arrives.[^s4] Busy readers also stop early. Todd Rogers and Jessica Lasky-Fink describe readers triaging messages by length and quitting partway through, so a request placed near the end can be missed entirely; in their 2023 field study of 7,002 school board members, a 49-word request drew a 4.8% response rate against 2.7% for a 127-word version that delayed the ask.[^s6] Because the reader cannot grasp the point in one quick read, which is the Army standard's test of clear writing, burying the lede undermines clarity.[^s2]

## How to spot it

- The first sentence describes what you did, when the project started, or how you feel, rather than what the reader must know or do.[^s2]
- The request, deadline, number or recommendation appears only in the last paragraph, or not at all as an explicit sentence.[^s6]
- A colleague who reads only the subject line and first two sentences summarises the message differently from what you meant.[^s3][^s4]
- Replies ask the question the message was meant to answer, or treat an urgent message as routine.[^s6]
- The structure follows the order events happened in rather than their importance to the reader.[^s2]

## How to fix it

- **Write the point first, then the message.** Before drafting, write the one sentence the reader must take away; make it the opening.[^s2]
- **State the ask completely.** Put the decision or action, the owner and the deadline in that first sentence, not just the topic.[^s2][^s6]
- **Promote the point into the subject line or slide title**, because readers triage on what they see before opening.[^s6]
- **Move the history down.** Keep background below the main point, and cut whatever the reader does not need in order to act.[^s2][^s6]
- **Test it cold.** Ask someone unfamiliar to read only the first lines and tell you the point; unfamiliar readers are the ones who most need it stated explicitly.[^s3]
- **For bad news, lead with the news itself**, then the cause and the plan; the main-point-first rule does not change because the point is unwelcome, and a neutral opening invites the reader to file it as routine.[^s2][^s4]

## Evidence

The research behind the advice is real but narrower than the folklore. Kieras's studies were small laboratory experiments on short technical passages, published as technical reports rather than journal articles.[^s3][^s4] They show that a stated main idea at the start sharpened readers' summaries and, for unfamiliar topics, cut reading time substantially (for one passage, about 52 seconds versus 81 seconds without an explicit main idea), but for familiar topics readers inferred the main idea anyway, and in one experiment moving a theme sentence from the middle to the front did not change reading time.[^s3][^s4] Nor is front-loading always best for learning: a 2026 experiment with 461 adult readers of health journalism found that narrative articles produced higher comprehension and interest than inverted-pyramid versions, although interest in the narrative dipped after its first paragraph, a sign that low-interest readers may quit before the payoff.[^s5] The practical reading is that leading with the point matters most when readers are busy, unfamiliar with the topic or need to act, which describes most workplace messages; for explanatory writing meant to be read in full, a story-first structure can work if the reader knows why to keep going.[^s3][^s5][^s6]

## Connections

Burying the lede is a failure of **message structure** (`cm:message-structure`), the anti-pattern that **bottom line up front** and the **pyramid principle** are designed to fix.[^s2] It is **demonstrated by** Kieras 1980 (`cm:kieras-1980`), where an explicit opening main idea shaped readers' summaries and sped reading of unfamiliar text,[^s3] and **supported by** Kieras 1979 (`cm:kieras-1979`), which showed readers take the first-mentioned topic as the main one.[^s4] Ameseder, Devetak and Skubic 2026 (`cm:ameseder-devetak-skubic-2026`) **challenge** the idea that front-loaded structure always aids understanding, since narrative articles beat the inverted pyramid on comprehension.[^s5] It **undermines clarity** (`cm:clarity`) because the point cannot be grasped in one quick read.[^s2] It often travels with a **wall of text** and adds to **information overload**, and it is most costly in **email**, **executive briefings**, **status reporting** and **delivering bad news**.[^s2][^s6]

## Sources

[^s1]: Merriam-Webster, "Is it 'Bury the Lede' or 'Bury the Lead'?", Words at Play. https://www.merriam-webster.com/wordplay/bury-the-lede-versus-lead (accessed 2026-11-11)
[^s2]: Department of the Army, "Army Regulation 25-50: Preparing and Managing Correspondence" (2020), paras 1-38 and 2-4. https://www.maine.gov/dvem/policies/documents/AR%2025-50%20(10%20October%202020).pdf (accessed 2026-11-11)
[^s3]: Kieras, D. E. (1980). "Abstracting Main Ideas from Technical Prose: A Preliminary Study of Six Passages". Technical Report No. 5, University of Arizona. https://apps.dtic.mil/sti/pdfs/ADA089910.pdf (accessed 2026-11-11)
[^s4]: Kieras, D. E. (1979). "Initial Mention as a Cue to the Main Idea and the Main Item of a Technical Passage". Technical Report No. 3, University of Arizona. https://apps.dtic.mil/sti/pdfs/ADA073773.pdf (accessed 2026-11-11)
[^s5]: Ameseder, C., Devetak, I., & Skubic, D. (2026). "Incidental Learning From Science Journalism". *CEPS Journal* 16(3), 201-234. https://www.cepsj.si/index.php/cepsj/article/view/1899 (accessed 2026-11-11)
[^s6]: Rogers, T., & Lasky-Fink, J. (2023). "When Writing for Busy Readers, Less Is More". *Behavioral Scientist*. https://behavioralscientist.org/when-writing-for-busy-readers-less-is-more/ (accessed 2026-11-11)
