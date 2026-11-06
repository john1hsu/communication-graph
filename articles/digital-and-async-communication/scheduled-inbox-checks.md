---
id: cm:scheduled-inbox-checks
type: Technique
title: Scheduled inbox checks
aliases: [email batching, batching email, checking email in batches, notification batching, batched notifications]
domain: digital-and-async-communication
summary: >-
  Processing email and message notifications at a few planned times a day, with the inbox closed
  and alerts off in between, instead of reacting to each message as it arrives - a way to cut
  interruptions and the stress of a constant stream of incoming information.
level: introductory
evidenceStatus: mixed
broader: [cm:attention-management]
related: [cm:information-overload, cm:email, cm:asynchronous-communication, cm:setting-reply-time-expectations, cm:channel-selection, cm:zoom-fatigue]
requires: []
relations:
  - {predicate: addresses, object: cm:information-overload, source: s1, confidence: medium}
  - {predicate: appliedIn, object: cm:email, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: cm:kushlev-dunn-2015, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: cm:fitz-et-al-2019, source: s2, confidence: high}
  - {predicate: challengedBy, object: cm:mark-et-al-2016, source: s3, confidence: medium}
  - {predicate: complements, object: cm:setting-reply-time-expectations, source: s1, confidence: medium}
steps:
  - Look at how often you check messages today and what your role genuinely needs; if you are on call or in a live-support role, agree an exception path before you change anything.
  - Pick a small number of fixed check-in times (three a day is the most-tested dose) and block them in your calendar, sized to your usual volume.
  - Between check-ins, close the email tab or app and switch off desktop and phone alerts for email and non-urgent chat.
  - During each check-in, triage in one pass - reply, delegate, schedule or archive - rather than reading messages and leaving them for later.
  - Tell your team and key stakeholders when you check messages and how to reach you for anything genuinely urgent (a phone call or a named chat channel).
  - Review after two weeks - stress, missed items, response complaints - and adjust the number of check-ins rather than abandoning the routine.
example:
  situation: A finance analyst gets 120 emails and a steady flow of chat pings a day and is preparing a quarterly forecast that needs long stretches of concentration.
  before: "Outlook open all day with pop-up alerts on; the analyst answers each message within minutes and does forecast work in the gaps between replies."
  after: "Email and chat alerts off; inbox processed at 9:00, 13:00 and 16:30. The analyst's status and email signature say: 'I check messages three times a day - for anything urgent on the forecast, call my desk line.'"
  why: Fewer checks cut the interruptions that fragment the forecast work, and the stated urgent path stops colleagues guessing or escalating, which addresses the co-worker expectations the original study could not control.
selfCheck:
  - Do the people who depend on me know when I will see their message and how to reach me if it cannot wait?
  - Did I actually close the inbox and turn off alerts between check-ins, or just check less while staying distracted?
  - In this check-in, did I decide what to do with each message, or did I just read and leave them?
  - Is my message volume high enough that batching helps, or am I adding rigidity for little gain?
  - Has turning alerts off made me more anxious about missing something, and if so would hourly checks suit me better?
sameAs: []
sources:
  - id: s1
    title: "Checking email less frequently reduces stress"
    publisher: Kostadin Kushlev & Elizabeth W. Dunn, Computers in Human Behavior 43, 220-228, 2015 (author copy, interruptions.net)
    url: https://www.interruptions.net/literature/Kushlev-ComputHumBehav15.pdf
    type: peer-reviewed
    accessed: 2026-11-06
  - id: s2
    title: "Batching smartphone notifications can improve well-being"
    publisher: Fitz, Kushlev, Jagannathan, Lewis, Paliwal & Ariely, Computers in Human Behavior 101, 84-94, 2019 (author-hosted copy)
    url: https://static1.squarespace.com/static/57a40c19414fb54f51f8095f/t/614a55faa7b89e25f4e48ad1/1632261627146/2019+Fitz+Batching.pdf
    type: peer-reviewed
    accessed: 2026-11-06
  - id: s3
    title: "Email Duration, Batching and Self-interruption: Patterns of Email Use on Productivity and Stress"
    publisher: Mark, Iqbal, Czerwinski, Johns & Sano, Proceedings of CHI 2016, ACM (Microsoft Research copy)
    url: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/06/Email20Duration20Camera20Ready20submission3-1.pdf
    type: peer-reviewed
    accessed: 2026-11-06
  - id: s4
    title: "Network Research Highlight: Batch Your Smartphone Notifications"
    publisher: Keaton Fletcher, Georgia Tech Work Science Center, 2019
    url: https://work21.gatech.edu/?p=402
    type: academic
    accessed: 2026-11-06
created: 2026-11-06
---

# Scheduled inbox checks

Scheduled inbox checks, often called email or notification batching, means dealing with incoming messages at a few planned points in the day, with the inbox closed and alerts silenced in between, rather than responding to each message the moment it lands.[^s1] It is a receiver-side habit: it changes how you take in information, not what other people send you.[^s2]

## Origin

The advice circulated for years in productivity writing before it was tested. Kushlev and Dunn ran one of the first controlled tests in 2015: 124 adults spent one week limited to three email checks a day with alerts off and another week checking as often as they liked, in random order.[^s1] Fitz, Kushlev, Ariely and colleagues extended the idea to all smartphone notifications in a 2019 randomized field experiment with 237 participants, comparing notifications as usual, hourly batches, three batches a day and no notifications at all.[^s2]

## Why it matters

Constant checking turns every message into an interruption. In the 2015 study, limiting checks cut self-reported checks from about 12.5 to about 4.7 a day, and participants reported lower daily stress (d = 0.37) and less email distraction (d = 0.51), while sending and answering about the same number of emails.[^s1] In the 2019 study, three daily notification batches lowered inattention (d = -0.65) and stress (d = -0.56) and raised perceived productivity and sense of control over the phone compared with the usual stream.[^s2] For anyone feeling buried by volume, that makes batching one of the few individual remedies with experimental support.[^s1]

## How to apply it

Start with your role: a person on a service desk or on call cannot go dark for four hours, so set an explicit urgent route before reducing checks.[^s1] Three check-ins a day is the dose tested in both experiments, so it is a sensible default, adjusted to your volume.[^s2] Between check-ins, close the mailbox and switch alerts off; the experimental condition did both, not just one.[^s1] Because Kushlev and Dunn could not control colleagues' expectations of quick replies, tell the people who rely on you when you check and how to reach you urgently.[^s1] The Georgia Tech Work Science Center summary of the 2019 study suggests managers can support this by building in regular message breaks and protected focus time.[^s4] In live meetings and on chat, the same logic applies: decide when you will look, rather than letting each ping decide for you.[^s2]

## Common mistakes

Going to zero is not better. Participants with no notifications at all did not gain attention, and they reported more anxiety and fear of missing out than the control group.[^s2] Even three batches a day raised fear of missing out, so expect some unease in the first days.[^s2] Another mistake is batching while still opening the inbox "just to look", which keeps the interruptions and drops the benefit; the tested condition kept the mailbox closed between checks.[^s1] Finally, batching without telling anyone shifts the cost to colleagues, who may escalate or resend when replies slow down.[^s1]

## Evidence

The evidence is real but modest and mixed. Kushlev and Dunn describe their analysis as exploratory with many tests, based on a convenience sample (about two-thirds students) and self-reported checking; they found no change in self-rated productivity and no difference in weekly recalled stress.[^s1] The 2019 experiment ran for two weeks on a sample of Indian smartphone users recruited online, without corrections for multiple comparisons.[^s2] A 2016 CHI field study of 40 information workers that logged computer use and measured heart-rate variability found that people who naturally batched email were no less stressed than steady checkers; batchers rated themselves more productive only when email volume was high, and the correlational design rules out causal claims.[^s3] Read together, batching reliably reduces interruptions and probably reduces perceived stress, with larger payoffs for heavy message volume, but it is not a proven productivity booster.[^s3]

## Connections

- **Addresses information overload** by cutting how often incoming messages break into other work.[^s1]
- **Applied in email**, where both experiments' manipulation was a closed mailbox and alerts switched off between checks.[^s1]
- **Demonstrated by** Kushlev and Dunn's 2015 email experiment and by Fitz and colleagues' 2019 notification-batching experiment.[^s1][^s2]
- **Challenged by** Mark and colleagues' 2016 field study, which found natural batchers no less stressed than steady checkers.[^s3]
- **Complements setting reply-time expectations**: senders who state real deadlines make it safer to check less often, the co-worker expectation Kushlev and Dunn flagged as untested.[^s1]
- **Broader** concept is attention management; the Georgia Tech Work Science Center frames batching alongside scheduled focus time.[^s4]
- **Related to** asynchronous communication, channel selection (routing true emergencies to a phone call) and Zoom fatigue, another cost of always-on digital work.[^s2][^s4]

## Sources

[^s1]: Kushlev & Dunn, "Checking email less frequently reduces stress", Computers in Human Behavior 43, 2015. https://www.interruptions.net/literature/Kushlev-ComputHumBehav15.pdf (accessed 2026-11-06)
[^s2]: Fitz et al., "Batching smartphone notifications can improve well-being", Computers in Human Behavior 101, 2019. https://static1.squarespace.com/static/57a40c19414fb54f51f8095f/t/614a55faa7b89e25f4e48ad1/1632261627146/2019+Fitz+Batching.pdf (accessed 2026-11-06)
[^s3]: Mark et al., "Email Duration, Batching and Self-interruption: Patterns of Email Use on Productivity and Stress", CHI 2016. https://www.microsoft.com/en-us/research/wp-content/uploads/2016/06/Email20Duration20Camera20Ready20submission3-1.pdf (accessed 2026-11-06)
[^s4]: Fletcher, "Network Research Highlight: Batch Your Smartphone Notifications", Georgia Tech Work Science Center, 2019. https://work21.gatech.edu/?p=402 (accessed 2026-11-06)
