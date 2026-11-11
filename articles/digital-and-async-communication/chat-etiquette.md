---
id: cm:chat-etiquette
type: Technique
title: Chat etiquette
aliases: [workplace chat etiquette, Slack etiquette, Teams chat etiquette, instant messaging etiquette]
domain: digital-and-async-communication
summary: >-
  A small set of shared habits for workplace chat tools such as Slack or Teams - complete
  self-contained messages, threads, sparing use of group alerts, honest status, and explicit
  response expectations - that keep chat fast without turning it into a stream of interruptions.
level: introductory
evidenceStatus: practitioner
broader: [cm:team-communication-norms, cm:digital-communication]
related: [cm:setting-reply-time-expectations, cm:asynchronous-communication, cm:channel-selection, cm:emoji-and-tone-in-text, cm:scheduled-inbox-checks, cm:information-overload, cm:bottom-line-up-front]
requires: []
relations:
  - {predicate: appliedIn, object: cm:instant-messaging, source: s1, confidence: high}
  - {predicate: addresses, object: cm:information-overload, source: s1, confidence: medium}
  - {predicate: addresses, object: cm:workplace-telepressure, source: s2, confidence: medium}
  - {predicate: complements, object: cm:setting-reply-time-expectations, source: s5, confidence: medium}
steps:
  - Put the whole request in one message - who it is for, what you need, the context or link, and by when - instead of sending "hi" and waiting for a reply.
  - Choose the place deliberately - a team or project channel for work others may need to find later, a direct message only for genuinely private or one-person matters.
  - Reply in the thread of the original post so the discussion stays together and the main channel stays readable.
  - Mention a named person only when you need that person, and reserve channel-wide alerts such as @channel or @here for urgent items the team has agreed qualify.
  - Keep your status honest - set away, focus or out-of-office, and set notification hours - and respect other people's status rather than pinging through it.
  - Say how soon you need an answer, and state plainly that nobody is expected to reply outside their working hours.
  - Move to a call when a thread passes a few back-and-forths without agreement or the topic turns sensitive, then post the outcome back in the thread.
example:
  situation: A product manager needs the data engineer's estimate for a dashboard change before Thursday's planning meeting.
  before: "Direct message at 4:55pm: 'Hey, you around?' - then nothing until the engineer replies 'yes?' twenty minutes later."
  after: "In #dashboards thread: @Priya - could you estimate the effort to add region filters to the sales dashboard (spec linked)? A rough range is fine. Needed by Wed noon for Thursday planning; no need to look tonight."
  why: The rewrite carries the whole request, the link, the deadline and an explicit no-rush note in one interruption, posts it where teammates can see the answer later, and mentions only the person who must act.
selfCheck:
  - Could the recipient act on this message without asking me a single follow-up question?
  - Does this belong in a shared channel or thread rather than a direct message?
  - Am I about to alert more people than actually need to see this right now?
  - Have I said when I need a reply, and that it can wait if it can?
sameAs: []
sources:
  - id: s1
    title: "Slack communication and notification best practices"
    publisher: U.S. General Services Administration, Technology Transformation Services Handbook
    url: https://handbook.tts.gsa.gov/tools/slack/notifications-general-communication
    type: government
    accessed: 2026-11-11
  - id: s2
    title: "Please respond ASAP: workplace telepressure and employee recovery"
    publisher: Barber, L. K. & Santuzzi, A. M., Journal of Occupational Health Psychology 20(2), 172-189, 2015 (PubMed record)
    url: https://pubmed.ncbi.nlm.nih.gov/25365629/
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s3
    title: "The Cost of Interrupted Work: More Speed and Stress"
    publisher: Mark, G., Gudith, D. & Klocke, U., Proceedings of CHI 2008, ACM (author's copy)
    url: https://interruptions.net/literature/Mark-CHI08.pdf
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s4
    title: "Instant messaging interruptions, stress and work performance"
    publisher: Hurbean, L., Wong, L. H. M., Ou, C. X. J., Davison, R. M. & Dospinescu, O., Information Technology & People 38(1), 249-278, 2025 (City University of Hong Kong record)
    url: https://scholars.cityu.edu.hk/en/publications/instant-messaging-interruptions-stress-and-work-performance/
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s5
    title: "The Blurring Boundaries Between Synchronicity and Asynchronicity: New Communicative Situations in Work-Related Instant Messaging"
    publisher: Darics, E., Aston University (author's copy, Aston Publications Explorer)
    url: https://publications.aston.ac.uk/id/eprint/25623/1/New_communicative_situations_in_work_related_Instant_Messaging.pdf
    type: primary
    accessed: 2026-11-11
created: 2026-11-11
---

# Chat etiquette

Chat etiquette is the set of habits a team agrees on for using workplace messaging tools such as Slack, Microsoft Teams or Google Chat: where to post, how to write a message someone can act on, when to alert people, how to show and respect availability, and how quickly replies are expected.[^s1] Chat sits between a phone call and email - fast enough to feel like conversation, persistent enough to be read hours later - so without shared norms each person improvises, and the same message can read as a quick question to the sender and an interruption to the receiver.[^s5]

## Origin

Chat etiquette has no single author; it grew out of practitioner and IT guidance as instant messaging spread into offices in the 2000s and team-chat platforms replaced much internal email in the 2010s.[^s1] A linguistic study by Erika Darics of a global consultancy's virtual team, analysing about 1,200 work chat conversations, found that norms for availability, reply timing, and openings and closings were not yet settled: some people tolerated an hour's silence while others sent repeated greetings within minutes, and status indicators were often ignored or wrong.[^s5] Public-sector teams now write the norms down; the U.S. General Services Administration's technology handbook, for example, sets out guidance on threads, mentions, channel-wide alerts, status and off-hours replies.[^s1]

## Why it matters

Each chat notification is a small interruption. In a controlled experiment, Gloria Mark and colleagues found that people interrupted every few minutes while answering email finished faster but reported significantly more stress, frustration, time pressure and effort - they compensated by working harder, at a cost.[^s3] A 2025 survey of 416 professionals found that instant messaging's net effect on performance was not negative, but that the complexity and interruptions it brings fully explained its link to technology overload, which suggests the tool itself is not the problem so much as how it is used.[^s4] Habits around reply speed also matter for wellbeing: Barber and Santuzzi defined workplace telepressure as the preoccupation with and urge to respond quickly to work messages, found it was moderately associated with perceived response expectations, and showed it predicted burnout, poorer sleep and absenteeism beyond general job demands.[^s2]

## How to apply it

Write the complete message first. A bare greeting forces the recipient to stop, reply and wait while you type the real question; one message with the request, context, link and deadline lets them handle it once, when they choose. Darics observed that colleagues often used chat as a "sticky note" board, leaving requests for later action, which works only when the note is self-contained.[^s5]

Then post in the right place. Team or project channels make answers findable later; replying in threads keeps a discussion together and quiets the main channel, and channel-wide alerts should be rare and governed by an agreed team rule.[^s1] Use status and notification schedules to show when you are unavailable, and make it explicit that nobody is expected to answer outside working hours - the GSA handbook states this directly.[^s1] Because perceived response expectations feed telepressure, saying "no rush" or giving a real deadline is part of etiquette, not an extra.[^s2]

## Common mistakes

- **The naked "hello".** Sending a greeting and waiting creates two interruptions instead of one and leaves the receiver guessing about urgency.[^s5]
- **Alerting everyone.** Overusing channel-wide alerts turns every member's notifications into noise; agree when they apply and use pinned posts or email for non-urgent updates.[^s1]
- **Private by default.** Solving team problems in direct messages hides the answer from the next person who needs it.[^s1]
- **Treating presence as permission.** A green dot does not mean someone is free; Darics found people apologising for being unavailable while showing as online.[^s5]
- **Expecting instant replies.** Implicit pressure to answer fast is the mechanism behind telepressure, so state your real deadline.[^s2]

## Evidence and limits

Specific chat rules are practitioner advice rather than tested interventions, so this article is rated `practitioner`. The supporting findings are indirect: interruption costs come from a 48-person lab study with mostly student participants,[^s3] the overload result from a single cross-sectional survey,[^s4] and the telepressure findings from scale-development studies that measured associations rather than the effect of changing team norms.[^s2] Norms also vary with hierarchy, familiarity and urgency, so a team should agree its own conventions rather than import someone else's list wholesale.[^s5]

## Connections

Chat etiquette is applied in instant messaging, the channel whose quasi-synchronous rhythm creates the ambiguity these habits resolve.[^s1] It addresses information overload by reducing needless alerts and scattered conversations,[^s1] and it addresses workplace telepressure by making response expectations explicit instead of implied.[^s2] It complements setting reply-time expectations: Darics's finding that tolerated reply delays varied widely between colleagues is exactly the gap that stating a reply-by time closes.[^s5] It sits under team communication norms and draws on channel selection, bottom line up front, and emoji and tone in text for the content of each message.[^s1]

## Sources

[^s1]: U.S. General Services Administration, "Slack communication and notification best practices", TTS Handbook. https://handbook.tts.gsa.gov/tools/slack/notifications-general-communication (accessed 2026-11-11)
[^s2]: Barber, L. K. & Santuzzi, A. M. (2015), "Please respond ASAP: workplace telepressure and employee recovery", Journal of Occupational Health Psychology 20(2), 172-189. https://pubmed.ncbi.nlm.nih.gov/25365629/ (accessed 2026-11-11)
[^s3]: Mark, G., Gudith, D. & Klocke, U. (2008), "The Cost of Interrupted Work: More Speed and Stress", CHI 2008. https://interruptions.net/literature/Mark-CHI08.pdf (accessed 2026-11-11)
[^s4]: Hurbean, L. et al. (2025), "Instant messaging interruptions, stress and work performance", Information Technology & People 38(1), 249-278. https://scholars.cityu.edu.hk/en/publications/instant-messaging-interruptions-stress-and-work-performance/ (accessed 2026-11-11)
[^s5]: Darics, E., "The Blurring Boundaries Between Synchronicity and Asynchronicity: New Communicative Situations in Work-Related Instant Messaging", Aston University. https://publications.aston.ac.uk/id/eprint/25623/1/New_communicative_situations_in_work_related_Instant_Messaging.pdf (accessed 2026-11-11)
