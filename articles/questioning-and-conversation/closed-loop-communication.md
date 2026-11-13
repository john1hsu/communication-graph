---
id: cm:closed-loop-communication
type: Technique
title: Closed-loop communication
aliases: [check-back, repeat-back, read-back, readback-hearback, call-out and check-back]
domain: questioning-and-conversation
summary: >-
  A three-part exchange for messages that must be exact: the sender directs a call-out to a named
  person, the receiver repeats back what they heard, and the sender confirms it is correct or fixes
  it - and, for tasks, the receiver reports back when the action is done.
level: introductory
evidenceStatus: mixed
broader: [cm:checking-understanding]
related: [cm:teach-back, cm:paraphrasing, cm:illusion-of-transparency, cm:common-ground, cm:information-overload, cm:shannon-weaver-model, cm:hargestam-et-al-2013, cm:el-shafy-et-al-2018, cm:meeting-recaps]
requires: []
relations:
  - {predicate: develops, object: cm:checking-understanding, source: s1, confidence: high}
  - {predicate: partOf, object: cm:teamstepps, source: s1, confidence: high}
  - {predicate: appliedIn, object: cm:phone-call, source: s1, confidence: high}
  - {predicate: appliedIn, object: cm:email, source: s1, confidence: medium}
  - {predicate: complements, object: cm:shared-mental-models, source: s2, confidence: medium}
  - {predicate: supportedBy, object: cm:espevik-et-al-2021, source: s3, confidence: medium}
steps:
  - Decide which messages need a closed loop - instructions, numbers, names, deadlines or decisions where a mishearing would cause real harm - and use the full exchange only for those.
  - Address one named person ("Priya, ...") so someone owns the message, and keep each call-out short, with one to three items.
  - Ask the receiver to repeat back the critical details in full (the figure, the identifier, the deadline), not just "got it".
  - Listen to the repeat-back and close the loop out loud - "Correct" - or correct the wrong part and hear it repeated again.
  - For tasks, agree that the receiver reports back when the action is done ("Rollback complete"), so the sender is not left assuming.
  - In email or chat, ask for a reply that restates the key detail or next step, and confirm or correct it in the thread.
example:
  situation: During a production-incident video call, an incident lead asks an on-call engineer to roll back a recent release while four other people are talking.
  before: "Lead - 'Can someone roll back payments?' Engineer - 'On it.' (Twenty minutes later the team finds the engineer rolled back the wrong region, and the lead had assumed it was finished.)"
  after: "Lead - 'Sam, roll back payments-api in us-east to version 4.2.' Sam - 'Rolling back payments-api, us-east, to 4.2.' Lead - 'Correct.' ... Sam - 'Rollback of payments-api us-east to 4.2 is complete.' Lead - 'Thanks, noted.'"
  why: Naming one owner removes the "someone" ambiguity, the repeat-back exposes a wrong region or version before anyone acts, and the completion report replaces an assumption with a fact the lead can log.
selfCheck:
  - Which details in this message would cause damage if misheard, and did I hear each one repeated back?
  - Did I direct the instruction to one named person, or did I say it to the room?
  - When I heard the repeat-back, did I actually confirm or correct it, or did I let the loop stay open?
  - Was my call-out short enough to repeat accurately, or did I pack in several topics at once?
  - For a task, do I know it is done because someone told me, or because I assumed it?
sameAs: []
sources:
  - id: s1
    title: "Tool: Check-Back (or Repeat-Back) - TeamSTEPPS Communication Module"
    publisher: Agency for Healthcare Research and Quality (U.S. Department of Health and Human Services)
    url: https://www.ahrq.gov/teamstepps-program/curriculum/communication/tools/checkback.html
    type: government
    accessed: 2026-11-13
  - id: s2
    title: "Is There a \"Big Five\" in Teamwork? (Salas, Sims & Burke, Small Group Research 36(5), 2005)"
    publisher: Small Group Research (SAGE), author copy hosted by Helse Stavanger
    url: https://www.helse-stavanger.no/4a923f/contentassets/c6f06d2b76544501a6d662b0631476d7/salas-big-five.pdf
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s3
    title: "Teamwork on Patrol: Investigating Teamwork Processes and Underlaying Coordinating Mechanisms in a Police Training Program (Espevik et al., Frontiers in Psychology, 2021)"
    publisher: Frontiers in Psychology
    url: https://www.frontiersin.org/articles/10.3389/fpsyg.2021.702347/full
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s4
    title: "The Outcome of ATC Message Length and Complexity on En Route Pilot Readback Performance (Prinzo, Hendrix & Hendrix, DOT/FAA/AM-09/2, 2009)"
    publisher: Federal Aviation Administration, Office of Aerospace Medicine
    url: https://www.faa.gov/data_research/research/med_humanfacs/oamtechreports/2000s/2009/200902
    type: government
    accessed: 2026-11-13
  - id: s5
    title: "Closed-loop communication in interprofessional emergency teams: a cross-sectional observation study (Gjøvikli & Valeberg, Journal of Patient Safety, 2023)"
    publisher: AHRQ Patient Safety Network (PSNet)
    url: https://psnet.ahrq.gov/issue/closed-loop-communication-interprofessional-emergency-teams-cross-sectional-observation-study
    type: government
    accessed: 2026-11-13
  - id: s6
    title: "Communication in interdisciplinary teams: exploring closed-loop communication during in situ trauma team training (Härgestam et al., BMJ Open, 2013)"
    publisher: AHRQ Patient Safety Network (PSNet)
    url: https://psnet.ahrq.gov/issue/communication-interdisciplinary-teams-exploring-closed-loop-communication-during-situ-trauma
    type: government
    accessed: 2026-11-13
created: 2026-11-13
---

# Closed-loop communication

Closed-loop communication is a short, structured exchange that proves a critical message arrived intact. The sender makes a call-out to a specific person, the receiver repeats back what they heard, and the sender confirms that the repeat is correct or corrects it; only then is the loop closed.[^s1][^s2] It is the formal, team version of the broader skill of checking understanding.[^s1]

## Origin

The pattern comes from military and aviation radio procedure, where a misheard heading or altitude can be fatal; Espevik and colleagues trace the team-research concept to military radio transmissions and to McIntyre and Salas's 1995 work on team performance.[^s3] In 2005, Eduardo Salas, Dana Sims and Shawn Burke made it one of three "coordinating mechanisms" of teamwork, alongside shared mental models and mutual trust, defining it as a sender's message, the receiver's acknowledgement and interpretation, and the sender's follow-up to make sure the intended meaning got through.[^s2] Healthcare then adopted it: the U.S. Agency for Healthcare Research and Quality's TeamSTEPPS curriculum teaches it as the check-back (or repeat-back), ending with the sender saying "Correct".[^s1]

## Why it matters

Spoken messages degrade more often than either side notices. In a 2009 Federal Aviation Administration analysis of 51 hours of en route pilot-controller radio traffic, longer messages produced more readback errors and more omitted items, and more complex messages produced more omissions; the authors advised limiting a transmission to about three topics.[^s4] Salas and colleagues list noise, language differences, stress and information overload as reasons teammates receive a different message from the one sent, and argue that closing the loop is how a team catches this before acting on it.[^s2] In office terms, it turns "I assumed you heard" into a few seconds of evidence.[^s1]

## How to apply it

Reserve the full exchange for messages where precision matters - figures, identifiers, owners, deadlines, go/no-go decisions - and name the person you are addressing.[^s1][^s3] Keep the call-out short enough to repeat; the FAA findings suggest that bundling many items into one message is where readbacks fail.[^s4] Listen to the repeat-back rather than treating it as ritual, then say "correct" or fix the wrong part.[^s1] AHRQ also recommends check-backs for email and text, where messages can go unread or be changed by typos and autocorrect; ask for a reply that restates the key detail, not a thumbs-up.[^s1]

## Common mistakes

- **Accepting "got it".** An acknowledgement without the content repeated proves only that sound arrived; Salas and colleagues separate acknowledging receipt from clarifying that the received message matches the intended one.[^s2]
- **Leaving the loop open.** Hearing the repeat-back and saying nothing leaves the receiver unsure whether it was right; the TeamSTEPPS check-back is complete only when the sender confirms.[^s1]
- **Talking to the room.** The model call-out is addressed to one receiver, by name where possible; a message to "someone" has no one to repeat it back.[^s3]
- **Overloading the message.** Long, multi-part call-outs are the ones most likely to come back wrong or incomplete.[^s4]
- **Knowing it but not doing it.** Observed teams under pressure close the loop far less often than training assumes (see below).[^s5][^s6]

## Evidence and limits

The evidence is real but mostly observational and concentrated in safety-critical teams, so its status here is mixed. In a 2021 study of 83 two-person police patrol teams in a training programme, Espevik and colleagues found that expert-rated closed-loop communication strongly predicted rated situation awareness and decision making, although shared mental models added further prediction and the design was correlational.[^s3] Adherence is the weak point: Härgestam and colleagues (*BMJ Open*, 2013) found closed-loop communication occurred infrequently in trauma teams during in-situ training, even in teams with prior teamwork training,[^s6] and a 2023 observation of 60 real emergency teams by Gjøvikli and Valeberg found only 45% of call-outs were closed.[^s5] Transfer to ordinary office work is plausible but largely untested.[^s3][^s5]

## Connections

Closed-loop communication develops the skill of checking understanding by giving it a concrete, repeatable script, and sits within it as a narrower technique; AHRQ teaches it as part of TeamSTEPPS.[^s1] AHRQ's examples apply it to telephone orders and extend it to email and text.[^s1] Salas and colleagues pair it with shared mental models: closing loops keeps the team's shared picture current, and the shared picture tells members what needs to be communicated.[^s2] Its value is supported by Espevik and colleagues' police-team findings.[^s3] It differs from teach-back, which asks someone to explain an idea in their own words; closed-loop communication asks for the exact detail back. Härgestam and colleagues' trauma-team study is part of its healthcare evidence base.[^s6]

## Sources

[^s1]: Agency for Healthcare Research and Quality, "Tool: Check-Back (or Repeat-Back) - TeamSTEPPS Communication Module". https://www.ahrq.gov/teamstepps-program/curriculum/communication/tools/checkback.html (accessed 2026-11-13)
[^s2]: Salas, Sims & Burke, "Is There a 'Big Five' in Teamwork?", *Small Group Research* 36(5), 555-599 (2005), doi:10.1177/1046496405277134. https://www.helse-stavanger.no/4a923f/contentassets/c6f06d2b76544501a6d662b0631476d7/salas-big-five.pdf (accessed 2026-11-13)
[^s3]: Espevik, Johnsen, Saus, Sanden & Olsen, "Teamwork on Patrol: Investigating Teamwork Processes and Underlaying Coordinating Mechanisms in a Police Training Program", *Frontiers in Psychology* 12 (2021), doi:10.3389/fpsyg.2021.702347. https://www.frontiersin.org/articles/10.3389/fpsyg.2021.702347/full (accessed 2026-11-13)
[^s4]: Prinzo, Hendrix & Hendrix, "The Outcome of ATC Message Length and Complexity on En Route Pilot Readback Performance", FAA Office of Aerospace Medicine, DOT/FAA/AM-09/2 (2009). https://www.faa.gov/data_research/research/med_humanfacs/oamtechreports/2000s/2009/200902 (accessed 2026-11-13)
[^s5]: AHRQ PSNet, summary of Gjøvikli & Valeberg, "Closed-loop communication in interprofessional emergency teams: a cross-sectional observation study on the use of closed-loop communication among anesthesia personnel", *Journal of Patient Safety* 19(2), 93-98 (2023), doi:10.1097/pts.0000000000001098. https://psnet.ahrq.gov/issue/closed-loop-communication-interprofessional-emergency-teams-cross-sectional-observation-study (accessed 2026-11-13)
[^s6]: AHRQ PSNet, summary of Härgestam et al., "Communication in interdisciplinary teams: exploring closed-loop communication during in situ trauma team training", *BMJ Open* 3(10) (2013), doi:10.1136/bmjopen-2013-003525. https://psnet.ahrq.gov/issue/communication-interdisciplinary-teams-exploring-closed-loop-communication-during-situ-trauma (accessed 2026-11-13)
