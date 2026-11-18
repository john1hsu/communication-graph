---
id: cm:conversational-repair
type: Technique
title: Conversational repair
aliases: [repair initiation, other-initiated repair, repair in conversation, clarification requests]
domain: questioning-and-conversation
summary: >-
  Fixing a mishearing or misunderstanding in live talk at the moment it shows up: the listener
  signals the trouble, ideally as specifically as possible ("Who?", "You mean Thursday?") rather
  than with a bare "Sorry, what?", and the speaker clarifies on the next turn, so the exchange
  stays on track at little cost.
level: intermediate
evidenceStatus: mixed
broader: [cm:questioning, cm:checking-understanding]
related: [cm:conversational-turn-taking, cm:common-ground, cm:paraphrasing, cm:closed-loop-communication, cm:teach-back, cm:backchannel-responses, cm:face-to-face-conversation, cm:phone-call, cm:video-call-communication, cm:illusion-of-transparency, cm:pragmatics]
requires: []
relations:
  - {predicate: appliedIn, object: cm:synchronous-communication, source: s1, confidence: high}
  - {predicate: appliedIn, object: cm:face-to-face-conversation, source: s1, confidence: high}
  - {predicate: introducedIn, object: cm:schegloff-jefferson-sacks-1977, source: s4, confidence: high}
  - {predicate: demonstratedBy, object: cm:dingemanse-et-al-2015, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: cm:healey-et-al-2018, source: s3, confidence: medium}
  - {predicate: studiedIn, object: cm:conversation-analysis, source: s2, confidence: high}
steps:
  - Notice the moment you are unsure what was said or meant, and flag it on your very next turn instead of nodding along.
  - Point at the exact trouble spot - repeat the part you caught and ask about the rest ("The vendor said what about the contract?").
  - When you have a guess, offer it for confirmation ("You mean the 14th, before the client demo?") so the speaker only has to say yes or correct one detail.
  - Keep a bare "Sorry, what?" for when you truly missed everything, such as noise, overlap or a frozen video feed.
  - If the first clarification did not land, ask again more specifically rather than repeating the same general request.
  - As the speaker, answer the repair briefly and fix only the part that was asked about, then carry on.
example:
  situation: A weekly project call on video; the engineering lead gives a release update while the line is slightly choppy.
  before: "Lead: 'We should have the patch out by the fourteenth, pending QA.' Account manager (unsure, but nods): 'Great, thanks.' She later tells the client the patch is guaranteed for the 14th."
  after: "Lead: 'We should have the patch out by the fourteenth, pending QA.' Account manager: 'The fourteenth - and pending QA, so it could slip past the client demo on the fifteenth?' Lead: 'Right, it could slip by a day or two. Tell them the 16th to be safe.'"
  why: The account manager named the exact piece she was unsure of and offered her reading, so the lead could correct one detail in a single turn instead of re-explaining the whole update, and the misunderstanding never reached the client.
selfCheck:
  - Did I let anything pass in that conversation that I was not sure I had heard or understood correctly?
  - When I asked for clarification, did I point to the specific word or detail, or did I make the other person repeat everything?
  - Did I offer my best guess so they could just confirm or correct it?
  - When someone asked me to clarify, did I fix just the part they asked about, without getting defensive or starting over?
sameAs: []
sources:
  - id: s1
    title: "Universal Principles in the Repair of Communication Problems"
    publisher: Dingemanse, M., Roberts, S. G., Baranova, J., Blythe, J., Drew, P., Floyd, S., Gisladottir, R. S., Kendrick, K. H., Levinson, S. C., Manrique, E., Rossi, G. & Enfield, N. J., PLoS ONE 10(9), e0136100, 2015 (PubMed Central)
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC4573759
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s2
    title: "Repair: The Interface Between Interaction and Cognition"
    publisher: Albert, S. & de Ruiter, J. P., Topics in Cognitive Science 10(2), 279-313, 2018 (Loughborough University repository)
    url: https://dspace.lboro.ac.uk/2134/37528
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s3
    title: "Running Repairs: Coordinating Meaning in Dialogue"
    publisher: Healey, P. G. T., Mills, G. J., Eshghi, A. & Howes, C., Topics in Cognitive Science 10(2), 367-388, 2018 (PhilArchive record)
    url: https://dc2.philarchive.org/rec/HEARRC
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s4
    title: "The Preference for Self-Correction in the Organization of Repair in Conversation"
    publisher: Schegloff, E. A., Jefferson, G. & Sacks, H., Language 53(2), 361-382, 1977 (record in the Schegloff Media Archive, International Society for Conversation Analysis)
    url: https://www.conversationanalysis.org/schegloff-media-archive/preference-for-self-correction-in-repair-in-conversation-1977/
    type: primary
    accessed: 2026-11-18
created: 2026-11-18
---

# Conversational repair

Conversational repair is the set of moves people use to deal with trouble in speaking, hearing or understanding while a conversation is still going on.[^s2][^s4] The form that matters most for a listener is other-initiated repair: you signal that something did not land, and the speaker fixes it on the next turn.[^s1] Done well, it is quick and almost invisible; done badly, or not at all, a small mishearing turns into a wrong decision, a missed deadline or a message passed on to a client in garbled form.

## Origin

The concept comes from conversation analysis. In a 1977 paper in *Language*, Emanuel Schegloff, Gail Jefferson and Harvey Sacks described an organised system for handling recurrent problems of speaking, hearing and understanding, and showed a strong skew in recorded talk towards speakers repairing their own trouble rather than having others correct them.[^s4] They argued that this preference for self-repair is built into how conversation is organised.[^s4] Later researchers treated repair as the point where interaction and cognition meet: it is the visible evidence of how people build and keep mutual understanding, and a natural meeting ground for linguists, psychologists and cognitive scientists.[^s2]

## Why it matters

Repair is not a sign that a conversation is failing; it is a routine part of how talk works. In a 2015 *PLoS ONE* study, Dingemanse and eleven colleagues analysed about 48.5 hours of informal conversation in 12 languages from 8 language families and found 2,053 other-initiated repairs, roughly one every 1.4 minutes.[^s1] Three formats covered about 92% of cases: an open request ("Huh?"), a restricted request that targets one part ("Who?") and a restricted offer that proposes a reading for confirmation ("She had a boy?").[^s1] People tended to choose the most specific format they could, and a full repair sequence took on average about as long as the single turn it fixed, so repair is cheap when it is precise.[^s1]

Repair also does more than patch errors. In chat-based experiments, Healey and colleagues swapped participants' feedback for weaker acknowledgements or vaguer trouble signals and found that people quickly changed how they referred to things; the authors argue that shared meaning is coordinated through these small running repairs rather than through explicit agreement.[^s3]

## How to apply it

The cross-language evidence points to a simple rule: make your repair as specific as your understanding allows.[^s1] Repeat the part you did hear and question the part you did not, or offer your best guess so the speaker can confirm or correct one detail. That puts less work on the speaker and keeps the conversation moving.[^s1] Save the open "Sorry, what?" for when you missed everything, which the study found is typical of noise, overlapping talk or a distracted listener, and if a first attempt does not resolve the problem, become more specific rather than asking the same thing again.[^s1]

Raise the trouble on your next turn. Other-initiated repair works as a two-turn sequence - the listener flags the problem right after the trouble, and the speaker fixes it in the following turn - which is what keeps it so cheap.[^s1] As a speaker, welcome the signal and repair only what was asked about, then return to your point.[^s1][^s4]

This is a synchronous-channel technique: it depends on the other person being present to answer at once, whether face to face, by phone or on a video call.[^s1] In email or chat threads the same move costs a round trip, so there it is better to anticipate trouble when writing.

## Common mistakes

- **Nodding along.** Repair is how conversation maintains mutual understanding; skipping it to avoid seeming slow leaves the trouble in place to surface later.[^s2]
- **Defaulting to "What?"** A bare open request makes the speaker repeat everything; a targeted question or a candidate reading costs both people less.[^s1]
- **Correcting instead of asking.** The organisation of talk favours letting speakers fix their own trouble, so a prompt that invites self-repair usually goes down better than a flat correction.[^s4]
- **Repeating the same vague request.** When one attempt fails, narrow it down.[^s1]

## Evidence and limits

The descriptive evidence is strong: repair appears at similar rates and in similar formats across unrelated languages, including a sign language.[^s1] But the data come from informal talk among family and friends, and the authors call for study of other settings, so the workplace advice here is an extrapolation rather than a tested intervention.[^s1] Healey and colleagues' experiments used text chat in a laboratory task.[^s3] The evidence status is therefore mixed: the phenomenon is robust, while its value as a trained workplace habit is plausible but largely untested.

## Connections

Conversational repair is **applied in** synchronous communication (`cm:synchronous-communication`) and face-to-face conversation (`cm:face-to-face-conversation`), where the speaker can fix trouble on the very next turn.[^s1] It was **introduced in** Schegloff, Jefferson and Sacks's 1977 paper (`cm:schegloff-jefferson-sacks-1977`).[^s4] It is **demonstrated by** the cross-linguistic study of Dingemanse and colleagues (`cm:dingemanse-et-al-2015`), which documented its frequency, formats and low cost,[^s1] and by Healey and colleagues' experiments (`cm:healey-et-al-2018`) showing that running repairs shape how people coordinate meaning.[^s3] It is **studied in** conversation analysis (`cm:conversation-analysis`).[^s2] It sits under checking understanding (`cm:checking-understanding`), the broader habit of testing rather than assuming that a message landed, and is related to conversational turn-taking, common ground, paraphrasing and closed-loop communication.

## Sources

[^s1]: Dingemanse, M., Roberts, S. G., Baranova, J., et al. (2015). "Universal Principles in the Repair of Communication Problems". *PLoS ONE* 10(9), e0136100. https://pmc.ncbi.nlm.nih.gov/articles/PMC4573759 (accessed 2026-11-18)
[^s2]: Albert, S. & de Ruiter, J. P. (2018). "Repair: The Interface Between Interaction and Cognition". *Topics in Cognitive Science* 10(2), 279-313. https://dspace.lboro.ac.uk/2134/37528 (accessed 2026-11-18)
[^s3]: Healey, P. G. T., Mills, G. J., Eshghi, A. & Howes, C. (2018). "Running Repairs: Coordinating Meaning in Dialogue". *Topics in Cognitive Science* 10(2), 367-388. https://dc2.philarchive.org/rec/HEARRC (accessed 2026-11-18)
[^s4]: Schegloff, E. A., Jefferson, G. & Sacks, H. (1977). "The Preference for Self-Correction in the Organization of Repair in Conversation". *Language* 53(2), 361-382. https://www.conversationanalysis.org/schegloff-media-archive/preference-for-self-correction-in-repair-in-conversation-1977/ (accessed 2026-11-18)
