---
id: cm:synchronous-communication
type: Channel
title: Synchronous communication
aliases: [sync communication, real-time communication, live communication]
domain: digital-and-async-communication
summary: >-
  Communication in which everyone involved is attending at the same time and can respond at once -
  in-person conversation, phone and video calls, live meetings - so meaning can be negotiated
  turn by turn; it is best spent on converging on ambiguous decisions, resolving disagreement and
  building relationships, and is wasted on one-way information that a written message could carry.
level: introductory
evidenceStatus: mixed
broader: [cm:organizational-communication, cm:interpersonal-communication]
related: [cm:asynchronous-communication, cm:channel-selection, cm:workplace-meetings, cm:face-to-face-conversation, cm:phone-call, cm:video-call-communication, cm:instant-messaging, cm:meeting-agendas, cm:meeting-recaps, cm:media-richness-theory, cm:common-ground, cm:zoom-fatigue]
requires: []
relations:
  - {predicate: explainedBy, object: cm:media-synchronicity-theory, source: s1, confidence: high}
  - {predicate: contrastsWith, object: cm:asynchronous-communication, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: cm:burgoon-chen-twitchell-2010, source: s2, confidence: medium}
  - {predicate: demonstratedBy, object: cm:rogelberg-leach-burnfield-2006, source: s3, confidence: medium}
selfCheck:
  - Does this exchange need us to converge on a shared meaning or decision, or could a written message simply convey it?
  - Has a thread gone back and forth so long that a short live conversation would settle it faster?
  - Did everyone get the goal and any pre-read before we met, so live time goes on discussion rather than briefing?
  - Who will write down the decision and owners afterwards, and by when?
sameAs: []
sources:
  - id: s1
    title: "Media, tasks, and communication processes: A theory of media synchronicity"
    publisher: Dennis, A. R., Fuller, R. M. & Valacich, J. S., MIS Quarterly 32(3), 575-600, 2008 (University of Arizona research portal record)
    url: https://experts.arizona.edu/en/publications/media-tasks-and-communication-processes-a-theory-of-media-synchro/
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s2
    title: "Deception and its Detection Under Synchronous and Asynchronous Computer-Mediated Communication"
    publisher: Burgoon, J. K., Chen, F. & Twitchell, D. P., Group Decision and Negotiation 19(4), 345-366, 2010 (Springer)
    url: https://link.springer.com/doi/10.1007/s10726-009-9168-8
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s3
    title: "\"Not Another Meeting!\" Are Meeting Time Demands Related to Employee Well-Being?"
    publisher: Rogelberg, S. G., Leach, D. J., Warr, P. B. & Burnfield, J. L., Journal of Applied Psychology 91(1), 83-96, 2006 (author copy hosted by interruptions.net)
    url: https://www.interruptions.net/literature/Rogelberg-JAP06-2006-00819-008.pdf
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s4
    title: "Sync vs. Async Culture"
    publisher: GitLab Handbook (GitLab Inc.)
    url: https://handbook.gitlab.com/handbook/communication/sync-vs-async-culture/
    type: institutional
    accessed: 2026-11-18
created: 2026-11-18
---

# Synchronous communication

Synchronous communication is any exchange in which the people involved are attending at the same moment and can reply immediately: a hallway conversation, a phone or video call, a live meeting, a quick back-and-forth in chat while both people are at their keyboards. Information-systems researchers describe the quality that matters here as synchronicity, the degree to which a medium lets people work together on the same thing at the same time in a coordinated way.[^s1] The trade is the mirror image of asynchronous work: you gain instant feedback and the chance to repair misunderstandings as they happen, and you pay with everyone's time and attention at once.[^s1][^s4]

## Origin

Live talk is the oldest form of communication, but the sync/async distinction became a design choice only once email and groupware made delay optional. Alan Dennis and Joseph Valacich proposed media synchronicity theory in 1999, and in a 2008 *MIS Quarterly* paper Dennis, Robert Fuller and Valacich refined it.[^s1] They split communication into conveyance, getting information to someone, and convergence, reaching a shared understanding of what it means; higher-synchronicity media should serve convergence better, lower-synchronicity media should serve conveyance better, and the more familiar people are with the task and with each other, the less convergence they need.[^s1] They traced these differences to five media capabilities: symbol sets, parallelism, transmission velocity, rehearsability and reprocessability.[^s1] Remote-first companies later turned the idea into operating rules; GitLab's handbook frames sync and async as tools with different jobs rather than a hierarchy.[^s4]

## Why it matters

Choosing live communication changes how the exchange feels, not just how fast it goes. In a Group Decision and Negotiation experiment, Judee Burgoon, Fang Chen and Douglas Twitchell had pairs complete a decision task either in real time or over several days; the real-time pairs reported more involvement and mutuality and judged their partners more favourably.[^s2] That warmth is useful for trust and alignment, but the same study also found that pairs containing an instructed deceiver made poorer decisions, a reminder that feeling connected is not the same as being well informed.[^s2]

Live time is also expensive. In two surveys of 676 and 304 employees, Steven Rogelberg and colleagues found that the sheer number and length of meetings were only weakly related to well-being, but how effective people judged their meetings was strongly related to it, and people high in accomplishment striving felt worse as meetings piled up.[^s3] The design was cross-sectional and self-reported, so it shows association rather than cause.[^s3]

## What works here

Use synchronous communication for the jobs that need convergence. GitLab's guidance lists deciding under ambiguity, settling a real disagreement, building trust with new colleagues, early brainstorming and debugging when the context is not yet clear enough to write down.[^s4] It warns that an asynchronous thread that has run for days can be worse than about half an hour of live talk.[^s4]

1. **Ask what the exchange is for.** If you only need to convey information, write it; if people must agree on what it means, meet or call.[^s1][^s4]
2. **Send the goal and pre-read first.** State the decision you want, share material in advance, and expect people to have read it.[^s4]
3. **Keep the invite list tight** so live time is spent by people who can move the outcome.[^s4]
4. **Write the result down.** Record the decision and owners in a shared place within a day, so people who were not there can act.[^s4]
5. **Prune recurring meetings** regularly, because meeting value, not count, is what tracks how people feel about them.[^s3][^s4]

Example: a product lead and an engineer have traded 23 comments over four days on whether to cut a feature from a release. Before: another long comment restating positions. After: a 20-minute call with both options and the release date in a one-page pre-read, followed by a two-line decision note posted in the thread. Why: the disagreement needed convergence, which live talk supports, while the written note keeps the conveyance step for everyone else.[^s1][^s4]

## Pitfalls

- **Meetings for status updates.** Using live time to share information that could have been a document wastes everyone's attention.[^s4]
- **Sync as a substitute for thinking.** Calling a meeting before anyone has framed the problem can replace preparation instead of building on it.[^s4]
- **Mistaking rapport for accuracy.** Real-time exchanges raise involvement and favourable impressions, which do not by themselves guard against poor information.[^s2]
- **Undocumented outcomes.** Decisions made live and never written down leave absent colleagues guessing.[^s4]
- **Ignoring individual load.** More meetings weigh most on people who are driven to get their own work done, so protect blocks of focus time.[^s3]

## Connections

Synchronous communication **contrasts with** asynchronous communication (`cm:asynchronous-communication`), and media synchronicity theory (`cm:media-synchronicity-theory`) **explains** when each fits: high synchronicity for convergence, low for conveyance.[^s1] The Burgoon, Chen and Twitchell experiment (`cm:burgoon-chen-twitchell-2010`) **demonstrates** that real-time exchange increases involvement and partner regard.[^s2] The Rogelberg, Leach, Warr and Burnfield study (`cm:rogelberg-leach-burnfield-2006`) **demonstrates** that the quality of live meetings matters more to well-being than their number.[^s3] Its narrower channels include face-to-face conversation, phone calls and video calls, and it is related to workplace meetings, channel selection, meeting agendas and meeting recaps, the practices GitLab pairs with live time.[^s4]

## Sources

[^s1]: Dennis, A. R., Fuller, R. M. & Valacich, J. S. (2008). "Media, tasks, and communication processes: A theory of media synchronicity". *MIS Quarterly* 32(3), 575-600. https://experts.arizona.edu/en/publications/media-tasks-and-communication-processes-a-theory-of-media-synchro/ (accessed 2026-11-18)
[^s2]: Burgoon, J. K., Chen, F. & Twitchell, D. P. (2010). "Deception and its Detection Under Synchronous and Asynchronous Computer-Mediated Communication". *Group Decision and Negotiation* 19(4), 345-366. https://link.springer.com/doi/10.1007/s10726-009-9168-8 (accessed 2026-11-18)
[^s3]: Rogelberg, S. G., Leach, D. J., Warr, P. B. & Burnfield, J. L. (2006). "'Not Another Meeting!' Are Meeting Time Demands Related to Employee Well-Being?". *Journal of Applied Psychology* 91(1), 83-96. https://www.interruptions.net/literature/Rogelberg-JAP06-2006-00819-008.pdf (accessed 2026-11-18)
[^s4]: GitLab Handbook. "Sync vs. Async Culture". https://handbook.gitlab.com/handbook/communication/sync-vs-async-culture/ (accessed 2026-11-18)
