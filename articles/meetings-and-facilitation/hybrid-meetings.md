---
id: cm:hybrid-meetings
type: Context
title: Hybrid meetings
aliases: [hybrid meeting, mixed-mode meetings, mixed-presence meetings, partially distributed meetings]
domain: meetings-and-facilitation
summary: >-
  Meetings in which some participants share a room while others join remotely by video or audio;
  the two groups hear, see, take turns and wield influence unequally, so the organizer has to
  choose the format deliberately and run the meeting to offset the room's built-in advantage.
level: intermediate
evidenceStatus: mixed
broader: [cm:workplace-meetings]
related: [cm:video-call-communication, cm:facilitation, cm:unequal-participation, cm:proximity-bias, cm:conversational-turn-taking, cm:meeting-agendas, cm:meeting-recaps, cm:channel-selection, cm:chat-etiquette, cm:wait-time, cm:psychological-safety, cm:camera-optional-norm, cm:one-remote-all-remote]
requires: []
relations:
  - {predicate: demonstratedBy, object: cm:saatci-et-al-2020, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: cm:bos-et-al-2004, source: s3, confidence: medium}
  - {predicate: causes, object: cm:unequal-participation, source: s2, confidence: medium}
  - {predicate: alternativeTo, object: cm:video-call-communication, source: s2, confidence: medium}
  - {predicate: studiedIn, object: cm:computer-supported-cooperative-work, source: s1, confidence: high}
selfCheck:
  - Does this meeting need some people in the same room, or would an all-remote call put everyone on equal footing?
  - Can every remote attendee hear every speaker in the room and see what is being written or shown?
  - Who is watching the screen and the chat, and how will remote people get the floor without having to interrupt?
  - Did I invite a remote participant to speak first on at least one item?
  - Did anything get decided in a side conversation or after the call ended that remote attendees still have not heard?
sameAs: []
sources:
  - id: s1
    title: "(Re)Configuring Hybrid Meetings: Moving from User-Centered Design to Meeting-Centered Design"
    publisher: Banu Saatçi, Kaya Akyüz, Sean Rintel & Clemens Nylandsted Klokmose, Computer Supported Cooperative Work (CSCW), Springer (2020), doi:10.1007/s10606-020-09385-x (open-access copy hosted by Microsoft Research)
    url: https://microsoft.com/en-us/research/uploads/prod/2020/11/Saatci2020_Article_ReConfiguringHybridMeetingsMov.pdf
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s2
    title: "Hybrid Meetings Guide"
    publisher: Sean Rintel, Abigail Sellen, Sonia Jaffe, Brent Hecht, John Tang, Kori Inkpen & Bill Buxton, Microsoft Research, The New Future of Work (September 2021, updated November 2021)
    url: https://www.microsoft.com/en-us/research/articles/hybrid-meetings-guide
    type: institutional
    accessed: 2026-11-13
  - id: s3
    title: "In-group/out-group effects in distributed teams: An experimental simulation"
    publisher: Nathan Bos, N. Sadat Shami, Judith S. Olson, Arik Cheshin & Ning Nan, Proceedings of CSCW 2004, ACM, pp. 429-436, doi:10.1145/1031607.1031679 (University of Haifa research portal record)
    url: https://cris.haifa.ac.il/en/publications/in-groupout-group-effects-in-distributed-teams-an-experimental-si-2/
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s4
    title: "Hybridge: Bridging Spatiality for Inclusive and Equitable Hybrid Meetings"
    publisher: Payod Panda, Lev Tankelevitch, Becky Spittle, Kori Inkpen, John Tang, Sean Rintel et al., Proceedings of the ACM on Human-Computer Interaction 8 (CSCW2), Article 501 (2024)
    url: https://www.microsoft.com/en-us/research/?p=1096842
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s5
    title: "Why Showing Your Face at Work Matters"
    publisher: Kimberly D. Elsbach & Daniel M. Cable, MIT Sloan Management Review 53(4), Summer 2012 (author copy on eScholarship, University of California)
    url: https://escholarship.org/content/qt3jt344hk/qt3jt344hk.pdf?t=pudeck
    type: practitioner-journal
    accessed: 2026-11-13
  - id: s6
    title: "Virtual voices: Exploring individual differences in chat and verbal participation in virtual meetings"
    publisher: Liana M. Kreamer, Steven G. Rogelberg, Lev Tankelevitch & Sean Rintel, Journal of Vocational Behavior 152, 104015 (2024) (author copy hosted by Microsoft Research)
    url: https://www.microsoft.com/en-us/research/wp-content/uploads/2024/04/2024-jvb-virtualvoices.pdf
    type: peer-reviewed
    accessed: 2026-11-13
created: 2026-11-13
---

# Hybrid meetings

A hybrid meeting is one where some people sit together in a room while others dial in by video or audio. Researchers define it simply as an audio- or video-based meeting among co-located and remote participants, and the defining feature is asymmetry: the two groups do not hear, see, take turns or carry influence on equal terms.[^s1][^s2] Running one well is less about the camera than about deliberately offsetting the room's built-in advantage.

## Origin

Mixed rooms long predate the pandemic. In a 2004 CSCW experiment, Nathan Bos, Judith Olson and colleagues gave ten-person groups a trading game with five members sharing a room and five working as simulated telecommuters; the co-located five formed an in-group that left the remote "isolates" out, and the isolates then clustered among themselves.[^s3] Field work at two European software firms in 2019, and a detailed video analysis of one 90-minute meeting with 11 people in the room and 2 remote, led Banu Saatçi, Sean Rintel and colleagues to argue that managing these asymmetries, not just fixing the technology, decides whether a hybrid meeting works.[^s1] When offices reopened after COVID-19, Microsoft Research turned this line of work into a practical guide (2021).[^s2]

## Why it matters

The remote side is structurally disadvantaged. The Microsoft guide groups the gaps into perception (how remote people come across), conversational cues (they struggle to follow overlapping talk or see who is speaking), access (to whiteboards and objects in the room) and power (the room usually holds more of it), and notes that new, junior and minority-group attendees lose most when they are the ones remote.[^s2] In Saatçi's recorded meeting, people in the room could predict their turn from where they sat, while remote colleagues found out only when summoned by name; a remote attendee with video off was treated as absent; and when audio broke, the chair sometimes cut the turn short instead of repairing it.[^s1] These moments add up beyond the meeting: in experiments by Kimberly Elsbach and Daniel Cable, managers spontaneously rated employees they simply saw at work as more dependable and committed, which suggests that being the person off-screen carries a cost to how one is judged (the studies measured office face time, not meetings as such).[^s5]

## What works here

- **Choose the format on purpose.** The guide suggests in-person for brainstorming, team building and work around shared objects, all-online for updates and all-hands, and hybrid only when the room's benefits outweigh the cost to remote people. If several people are remote, consider putting everyone on their own device so the field is level.[^s2]
- **Set up the space for the remote person.** Start the room system as soon as the first person arrives, seat people near microphones, aim cameras where remote people would sit, and give them a view of any whiteboard, for example with a spare laptop or content camera.[^s2]
- **Make turn order visible.** State the goal and conduct rules up front, use the hand-raise feature, allow one speaker at a time, invite remote attendees to speak first, signal when you finish a point, and wait longer for responses than you would in person.[^s2] Saatçi's chair repaired one breakdown by taking the status round in the order people appeared on the screen, so remote members knew when their turn was coming.[^s1]
- **Treat chat as a second floor.** Keep chat open on a screen and fold its highlights into the discussion and recap.[^s2] In a 2024 study of 291 employees and 33,812 meetings at one technology firm (all-virtual, not hybrid), women and some lower-level staff contributed relatively more by chat than by voice, so the authors recommend naming someone to bring chat points into the spoken discussion.[^s6]
- **Close for everyone.** Tell everyone where notes and recordings will be, say goodbye to the remote side, and make sure the room leaves the call; decisions made in the hallway afterwards never reach the remote half.[^s2]

## Pitfalls

- **Hub-and-satellite with no counterweight.** One large room and a few lone remotes is the most unequal layout; fewer remote people means less total disadvantage but more risk that they are forgotten.[^s2]
- **Letting trouble pass.** Moving on with "we got the gist" when a remote speaker's audio fails quietly removes them from the decision.[^s1]
- **Side conversations and room-only artifacts.** Two groups meeting in parallel, with a whiteboard only the room can read, recreate the in-group split seen in the 2004 experiment.[^s3][^s2]
- **Reading camera-off as absence.** Video became a marker of participation in Saatçi's meeting, and the remote colleague without it was teased until he turned it on.[^s1]

## Evidence

Most of the evidence is qualitative field work, design studies and laboratory simulations rather than controlled tests of meeting practices, so the asymmetries are well described but the advice for countering them is largely expert guidance.[^s1][^s2] A 2024 within-subjects study found that a redesigned room system reduced, but ordinary gallery-view hybrid setups did not remove, the gaps in co-presence and agency between in-room and remote participants; its authors argue designs should accept the asymmetry and tailor each side's setup rather than pretend everyone is equal.[^s4] The Bos experiment used a trading game with students, not a real team meeting, and the face-time findings concern office presence generally, so both indicate a direction of bias rather than its size in your meetings.[^s3][^s5]

## Connections

Hybrid meetings are a kind of workplace meeting (broader), and the field work that defines their problems comes from computer-supported cooperative work research.[^s1] The asymmetries are documented in Saatçi and colleagues' 2020 study and in Bos and colleagues' 2004 experiment, and they feed unequal participation, where the room dominates the airtime.[^s1][^s3][^s2] An all-remote video call is the main alternative when the room's advantages are small.[^s2] Practical remedies draw on facilitation, written agendas and recaps, chat etiquette and longer wait time after questions, while proximity bias explains why being remote can cost people beyond the meeting itself.[^s2][^s6][^s5]

## Sources

[^s1]: Saatçi, Akyüz, Rintel & Klokmose, "(Re)Configuring Hybrid Meetings: Moving from User-Centered Design to Meeting-Centered Design", Computer Supported Cooperative Work, 2020, doi:10.1007/s10606-020-09385-x. https://microsoft.com/en-us/research/uploads/prod/2020/11/Saatci2020_Article_ReConfiguringHybridMeetingsMov.pdf (accessed 2026-11-13)
[^s2]: Rintel, Sellen, Jaffe, Hecht, Tang, Inkpen & Buxton, "Hybrid Meetings Guide", Microsoft Research, 2021. https://www.microsoft.com/en-us/research/articles/hybrid-meetings-guide (accessed 2026-11-13)
[^s3]: Bos, Shami, Olson, Cheshin & Nan, "In-group/out-group effects in distributed teams: An experimental simulation", CSCW 2004, pp. 429-436, doi:10.1145/1031607.1031679. https://cris.haifa.ac.il/en/publications/in-groupout-group-effects-in-distributed-teams-an-experimental-si-2/ (accessed 2026-11-13)
[^s4]: Panda, Tankelevitch, Spittle, Inkpen, Tang, Rintel et al., "Hybridge: Bridging Spatiality for Inclusive and Equitable Hybrid Meetings", PACM HCI 8 (CSCW2), 2024. https://www.microsoft.com/en-us/research/?p=1096842 (accessed 2026-11-13)
[^s5]: Elsbach & Cable, "Why Showing Your Face at Work Matters", MIT Sloan Management Review 53(4), 2012. https://escholarship.org/content/qt3jt344hk/qt3jt344hk.pdf?t=pudeck (accessed 2026-11-13)
[^s6]: Kreamer, Rogelberg, Tankelevitch & Rintel, "Virtual voices: Exploring individual differences in chat and verbal participation in virtual meetings", Journal of Vocational Behavior 152, 2024. https://www.microsoft.com/en-us/research/wp-content/uploads/2024/04/2024-jvb-virtualvoices.pdf (accessed 2026-11-13)
