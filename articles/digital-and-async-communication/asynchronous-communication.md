---
id: cm:asynchronous-communication
type: Channel
title: Asynchronous communication
aliases: [async communication, async work, asynchronous messaging]
domain: digital-and-async-communication
summary: >-
  Communication in which sender and receiver are not engaged at the same moment - email, chat
  threads, shared documents, recorded video - so each side can compose and respond in its own
  time; it suits conveying information and protecting focus, but needs complete, self-contained
  messages and a switch to live conversation when people must converge on a shared meaning.
level: introductory
evidenceStatus: mixed
broader: [cm:digital-communication]
related: [cm:email, cm:channel-selection, cm:media-richness-theory, cm:zoom-fatigue, cm:common-ground, cm:bottom-line-up-front, cm:meeting-agendas, cm:information-overload, cm:setting-reply-time-expectations, cm:murray-turoff]
requires: []
relations:
  - {predicate: explainedBy, object: cm:media-synchronicity-theory, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: cm:yang-et-al-2022, source: s3, confidence: high}
  - {predicate: demonstratedBy, object: cm:perlow-1999, source: s4, confidence: medium}
  - {predicate: demonstratedBy, object: cm:email-urgency-bias-study, source: s5, confidence: medium}
  - {predicate: alternativeTo, object: cm:workplace-meetings, source: s6, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "Media, Tasks, and Communication Processes: A Theory of Media Synchronicity"
    publisher: Dennis, A. R., Fuller, R. M. & Valacich, J. S., MIS Quarterly 32(3), 575-600, 2008 (AIS eLibrary abstract page)
    url: https://aisel.aisnet.org/misq/vol32/iss3/8/
    type: peer-reviewed
    accessed: 2026-11-06
  - id: s2
    title: "The effects of remote work on collaboration among information workers"
    publisher: Yang, L., Holtz, D., Jaffe, S., Suri, S., Sinha, S., Weston, J., Joyce, C., Shah, N. P., Sherman, K., Hecht, B. & Teevan, J., Nature Human Behaviour (Microsoft Research publication page)
    url: https://www.microsoft.com/en-us/research/?p=772330
    type: primary
    accessed: 2026-11-06
  - id: s3
    title: "The effects of remote work on collaboration among information workers"
    publisher: Nature Human Behaviour 6(1), 43-54, 2022 (PubMed record 34504299)
    url: https://www.pubmed.gov/34504299/
    type: peer-reviewed
    accessed: 2026-11-06
  - id: s4
    title: "The Time Famine: Toward a Sociology of Work Time"
    publisher: Perlow, L. A., Administrative Science Quarterly 44(1), 57-81, 1999 (author copy hosted by interruptions.net)
    url: https://www.interruptions.net/literature/Perlow-ASQ99.pdf
    type: peer-reviewed
    accessed: 2026-11-06
  - id: s5
    title: "You don't need to answer right away! Receivers overestimate how quickly senders expect responses to non-urgent work emails"
    publisher: Giurge, L. M. & Bohns, V. K., Organizational Behavior and Human Decision Processes 167, 114-128, 2021 (RePEc/IDEAS abstract page)
    url: https://ideas.repec.org/a/eee/jobhdp/v167y2021icp114-128.html
    type: peer-reviewed
    accessed: 2026-11-06
  - id: s6
    title: "How to embrace asynchronous communication for remote work"
    publisher: GitLab Handbook (GitLab Inc.)
    url: https://handbook.gitlab.com/handbook/company/culture/all-remote/asynchronous/
    type: institutional
    accessed: 2026-11-06
created: 2026-11-06
---

# Asynchronous communication

Asynchronous communication is any exchange in which the sender and the receiver are not attending at the same time: an email, a chat thread, a comment on a shared document, a recorded video walkthrough. GitLab's remote-work handbook describes it as communication where the two parties are unlikely to be engaged at the same moment, and pairs it with a way of working in which you do what you can with what you have, document it, and hand off to the next person.[^s6] The defining trade-off is time for interaction: each side gets to think, draft and re-read before responding, but loses the instant back-and-forth that resolves confusion in a live conversation.[^s1][^s6]

## Origin

Information-systems researchers turned the sync/async distinction into theory. Alan Dennis, Robert Fuller and Joseph Valacich's media synchronicity theory, first proposed in 1999 and refined in *MIS Quarterly* in 2008, argues that communication involves two processes: conveyance, getting information to someone, and convergence, reaching a shared understanding of what it means.[^s1] Lower-synchronicity media should serve conveyance better, and higher-synchronicity media should serve convergence better. The theory names capabilities such as rehearsability (polishing a message before sending) and reprocessability (re-reading it later) that make asynchronous media good for conveyance, and it predicts that most team tasks go best with a mix of media rather than one.[^s1] The shift to remote work after 2020 moved the idea from theory into daily practice, and all-remote companies such as GitLab wrote "async-first" norms into their handbooks.[^s6]

## Why it matters

Remote and hybrid work has made asynchronous channels the default. In a study of 61,182 US Microsoft employees over the first half of 2020, Longqi Yang and colleagues found that firm-wide remote work reduced synchronous communication and increased asynchronous communication such as email and instant messaging.[^s3][^s2] The same work also became more siloed: the share of collaboration time spent with people in other groups fell by about a quarter, and people added fewer new collaborators.[^s2] Drawing on earlier research rather than a direct test, the authors suggested that leaner media may make complex information harder to convey and process.[^s2]

Done well, async protects focus. In Leslie Perlow's nine-month study of a 17-person software team, engineers rated almost all their interruptions as helpful but only about one in ten as urgent, and most could have waited; scheduling protected "quiet time" raised the share of engineers reporting above-average productivity.[^s4] Done badly, async creates hidden stress: across eight preregistered studies with about 4,000 participants, Laura Giurge and Vanessa Bohns found that people receiving non-urgent work email out of hours overestimated how quickly senders expected a reply.[^s5]

## What works here

Async suits conveyance - status updates, decisions already made, documents for review, requests the reader can handle alone - and work across time zones.[^s1][^s6]

1. **Send complete messages.** Give the recipient the context, the ask, next steps and links in one message, because a follow-up question can cost hours or days.[^s6]
2. **State the response time you need.** A one-line note that a reply can wait reduced receivers' overestimate of urgency in Giurge and Bohns's studies.[^s5]
3. **Batch interaction and protect focus time.** Agree on windows for questions and discussion so that the remaining hours stay uninterrupted, as Perlow's team did.[^s4]
4. **Switch to live conversation for convergence.** Move to a call for urgent issues, troubleshooting, brainstorming, relationship building, or when a thread shows people talking past each other.[^s6][^s1]
5. **Write down the outcome of every live discussion** in a shared, searchable place so that people who were not there can act on it asynchronously.[^s6]

## Pitfalls

- **Endless threads.** A long chat exchange that a ten-minute call would settle wastes more time than it saves.[^s6]
- **Thin messages** that force a round of clarifying questions.[^s6]
- **Using async for convergence.** Negotiating meaning or resolving disagreement in low-synchronicity media works against what the theory predicts.[^s1]
- **Silent urgency.** Messages sent out of hours with no stated deadline are read as more urgent than intended.[^s5]
- **Losing cross-team ties.** Leaning only on async channels within your own group can deepen silos; deliberately reach across groups.[^s2]
- **Rules without incentives.** Perlow found that quiet time faded once the project ended, because crises and rewards for visible heroics were unchanged.[^s4]

## Evidence

The evidence supports async as a tool, not as a universal default. Yang and colleagues' estimates come from one company and depend on a parallel-trends assumption to separate remote work from other pandemic effects.[^s2] Perlow's study was a single action-research case with self-reported productivity and effects that did not last.[^s4] Giurge and Bohns's studies were preregistered but mostly used scenarios and recall.[^s5] Media synchronicity theory is a model whose predictions are about fitting media to the process, not about sync or async being better overall.[^s1] Status is `mixed`.

## Connections

- **Explained by media synchronicity theory**, which links asynchronous media to conveyance and synchronous media to convergence.[^s1]
- **Demonstrated by** Yang et al. (2022), on the shift to async under remote work; Perlow (1999), on the cost of constant interruption; and the email urgency bias studies, on unstated response expectations.[^s3][^s4][^s5]
- **Alternative to workplace meetings** for updates and conveyance, with live meetings kept for the cases above.[^s6]
- **Related to** email, its most common channel; channel selection and media richness theory, which help choose between async and live media; common ground, which async exchanges build more slowly; bottom line up front and meeting agendas, which make async messages and the sync meetings around them more useful; and information overload, the cost of too many async messages.[^s1][^s6]

## Sources

[^s1]: Dennis, A. R., Fuller, R. M. & Valacich, J. S. (2008). "Media, Tasks, and Communication Processes: A Theory of Media Synchronicity". *MIS Quarterly* 32(3), 575-600. https://aisel.aisnet.org/misq/vol32/iss3/8/ (accessed 2026-11-06)
[^s2]: Yang, L., Holtz, D., Jaffe, S. et al. "The effects of remote work on collaboration among information workers". Microsoft Research publication page. https://www.microsoft.com/en-us/research/?p=772330 (accessed 2026-11-06)
[^s3]: Yang, L. et al. (2022). "The effects of remote work on collaboration among information workers". *Nature Human Behaviour* 6(1), 43-54. PubMed 34504299. https://www.pubmed.gov/34504299/ (accessed 2026-11-06)
[^s4]: Perlow, L. A. (1999). "The Time Famine: Toward a Sociology of Work Time". *Administrative Science Quarterly* 44(1), 57-81. https://www.interruptions.net/literature/Perlow-ASQ99.pdf (accessed 2026-11-06)
[^s5]: Giurge, L. M. & Bohns, V. K. (2021). "You don't need to answer right away! Receivers overestimate how quickly senders expect responses to non-urgent work emails". *Organizational Behavior and Human Decision Processes* 167, 114-128. https://ideas.repec.org/a/eee/jobhdp/v167y2021icp114-128.html (accessed 2026-11-06)
[^s6]: GitLab Handbook. "How to embrace asynchronous communication for remote work". https://handbook.gitlab.com/handbook/company/culture/all-remote/asynchronous/ (accessed 2026-11-06)
