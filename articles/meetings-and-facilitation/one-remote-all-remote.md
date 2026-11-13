---
id: cm:one-remote-all-remote
type: Technique
title: One remote, all remote
aliases: [everyone on their own device, all-online meeting rule, no shared-room hybrid calls, remote-first meeting rule]
domain: meetings-and-facilitation
summary: >-
  A meeting norm under which, if any attendee is remote, everyone joins individually from their own
  device, camera and microphone, even colleagues sitting in the same office, so no shared conference
  room becomes a privileged hub and all participants meet on the same screen.
level: introductory
evidenceStatus: practitioner
broader: [cm:meeting-design]
related: [cm:hybrid-meetings, cm:video-call-communication, cm:unequal-participation, cm:facilitation, cm:channel-selection, cm:zoom-fatigue, cm:camera-optional-norm, cm:meeting-recaps]
requires: []
relations:
  - {predicate: appliedIn, object: cm:hybrid-meetings, source: s1, confidence: high}
  - {predicate: appliedIn, object: cm:video-call-communication, source: s3, confidence: medium}
  - {predicate: addresses, object: cm:unequal-participation, source: s2, confidence: medium}
  - {predicate: supportedBy, object: cm:saatci-et-al-2019, source: s2, confidence: low}
  - {predicate: supportedBy, object: cm:bos-et-al-2004, source: s5, confidence: medium}
steps:
  - Before sending the invite, check whether anyone will be remote; if even one person is, make the meeting all-online and say so in the invite.
  - Ask in-office attendees to join from their own laptop at their desk or in separate small rooms, each with a camera and a headset.
  - If several people must share one physical room, have them join with their laptop microphones and speakers off and only one room audio device live, so the call does not echo.
  - Put the agenda, slides and notes in one shared document everyone opens on their own screen, rather than on a wall display or whiteboard only the room can see.
  - Run turn-taking through the platform for everyone, using hand-raise, chat and an explicit speaking order, and post decisions and actions in a written recap afterwards.
  - Review the norm for meetings where nobody is remote or where the room's benefits are large, such as hands-on workshops or relationship-building sessions, and choose in person or hybrid there on purpose.
example:
  situation: A product team of eight holds its weekly planning meeting; five sit in the office and three, including a new hire, work from home.
  before: The five in the office gather in a conference room around one speakerphone and room camera, sketch the plan on the whiteboard and talk over each other, while the three remote colleagues see a wide shot of the room, miss side remarks and are asked "anything from the people online?" at the end.
  after: >-
    The organizer's invite says "One remote, all remote: please join from your own laptop." The five in the office join from their desks with headsets, everyone edits the same planning document, the facilitator takes updates in screen order and invites the new hire to go first, and the decisions are posted in the team channel.
  why: Everyone now hears, sees and gets the floor through the same channel, so the room no longer forms an in-group that leaves the remote three, and especially the newest member, on the margins.
selfCheck:
  - Is anyone joining remotely, and if so, have I asked everyone else to join from their own device?
  - Can every attendee see the same agenda, slides and notes on their own screen?
  - Does this meeting gain enough from being in one room to justify the cost to remote colleagues?
  - Will people in the office be adding more video hours than they can sustain this week?
sameAs: []
sources:
  - id: s1
    title: "Hybrid Meetings Guide"
    publisher: Sean Rintel, Abigail Sellen, Sonia Jaffe, Brent Hecht, John Tang, Kori Inkpen & Bill Buxton, Microsoft Research, The New Future of Work (2021)
    url: https://www.microsoft.com/en-us/research/articles/hybrid-meetings-guide
    type: institutional
    accessed: 2026-11-13
  - id: s2
    title: "Hybrid Meetings in the Modern Workplace: Stories of Success and Failure"
    publisher: Banu Saatçi, Roman Rädle, Sean Rintel, Kenton O'Hara & Clemens Nylandsted Klokmose, CRIWG+CollabTech 2019, Lecture Notes in Computer Science 11677, Springer, pp. 45-61, doi:10.1007/978-3-030-28011-6_4 (author copy)
    url: https://www.lri.fr/~mbl/ENS/CSCW/2012/papers/Saatci-CTSC19.pdf
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s3
    title: "How to use forcing functions to work remote-first"
    publisher: GitLab, The GitLab Handbook (all-remote section)
    url: https://handbook.gitlab.com/handbook/company/culture/all-remote/how-to-work-remote-first
    type: institutional
    accessed: 2026-11-13
  - id: s4
    title: "Hybrid working: digital communication and collaboration, Section 8: Hybrid meetings"
    publisher: The Open University, OpenLearn
    url: https://www.open.edu/openlearn/digital-computing/hybrid-working-digital-communication-and-collaboration/content-section-8
    type: academic
    accessed: 2026-11-13
  - id: s5
    title: "In-group/out-group effects in distributed teams: An experimental simulation"
    publisher: Nathan Bos, N. Sadat Shami, Judith S. Olson, Arik Cheshin & Ning Nan, Proceedings of CSCW 2004, ACM, pp. 429-436, doi:10.1145/1031607.1031679 (University of Haifa research portal record)
    url: https://cris.haifa.ac.il/en/publications/in-groupout-group-effects-in-distributed-teams-an-experimental-si-2/
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s6
    title: "Nonverbal Overload: A Theoretical Argument for the Causes of Zoom Fatigue"
    publisher: Jeremy N. Bailenson, Technology, Mind, and Behavior, American Psychological Association (2021), doi:10.1037/tmb0000030 (Stanford Virtual Human Interaction Lab record)
    url: https://vhil.stanford.edu/publications/social-interaction/nonverbal-overload-theoretical-argument-causes-zoom-fatigue
    type: peer-reviewed
    accessed: 2026-11-13
created: 2026-11-13
---

# One remote, all remote

"One remote, all remote" is a meeting rule: if even one attendee is joining from elsewhere, everyone joins individually from their own device, including colleagues who are sitting in the same office. Instead of a conference room full of people plus a few faces on a screen, the meeting becomes an all-online call in which everyone has the same view, the same microphone access and the same way to get the floor.[^s3][^s1] It is the simplest structural fix for the asymmetry that makes hybrid meetings hard to run fairly.

## Origin

The rule grew out of remote-first software companies. GitLab's public handbook lists it as a "forcing function" for teams with both office and remote staff: everyone must use their own webcam, with no shared-room hybrid calls, and it accepts that this feels awkward to people in the office because the awkwardness is what keeps remote colleagues on equal terms.[^s3] An Open University course on hybrid working draws on the same handbook, noting that when several people share one room's camera and microphone, remote attendees struggle to hear, see who is talking and get a word in, while the people in the room lose the ability to share their own screen or follow slides at their own pace.[^s4] Researchers reached a similar conclusion from field work: at one of two European software firms studied in 2019, the only meeting the team judged clearly successful was a large audio call in which even co-located colleagues dialled in from their own desks, and an interviewee there argued that joining from a device should be everyone's default.[^s2] Microsoft Research's 2021 guide turned this into a choice rule, recommending all-online meetings for updates, routine and information-sharing meetings, and suggesting the switch when a job candidate or new hire would otherwise be the lone remote person.[^s1]

## Why it matters

When some people share a room, the room forms an in-group. In a 2004 laboratory simulation, Nathan Bos and colleagues gave ten-person groups a trading game with five members together and five working alone; the co-located five favoured each other and left the isolates out, and the isolates ended up trading mainly among themselves.[^s5] Microsoft's guide describes the same imbalance in workplace terms: the room holds more visibility, access to whiteboards and objects, and power, and the cost falls hardest on new, junior and minority-group attendees when they are the ones remote.[^s1] Putting everyone on the same channel removes the hub. Turn-taking happens through the same interface for all, everyone sees the same shared document, and no decision can be made by a nod across the table that the screen never caught.[^s2][^s1]

## How to apply it

Make the call at invitation time. If anyone will be remote, say in the invite that the meeting is all-online and ask office-based colleagues to join from their own desk or a small room, with a camera and a headset.[^s3][^s4] When people do end up in one physical room, Microsoft's guide advises joining on a laptop with video on but audio off and system sounds muted, leaving one room audio device live, which avoids echo while still letting remote attendees see each face.[^s1] Move everything visual into shared digital resources that everyone opens on their own screen; the guide notes that even brainstorms can work online when they are well planned around the same shared materials.[^s1] Then facilitate as you would any video call: one speaker at a time, hand-raise and chat for everyone, and written notes or a recap so decisions are visible to the whole team.[^s3][^s1]

## Common mistakes

- **Treating it as a law rather than a default.** The guide still prefers in-person time for debate, relationship building, starting work with new people and handling physical objects, and suggests hybrid when the room's benefits clearly outweigh the cost to remote people.[^s1]
- **Several laptops, open microphones, one room.** Joining individually from a shared room without managing audio produces echo; GitLab's handbook recommends separate rooms where possible.[^s4][^s1]
- **Ignoring who is remote.** The guide notes less need to go all-online when the remote person is the manager or organizer, who is unlikely to be ignored, and that groups may treat someone remote by necessity differently from someone remote by choice.[^s1]
- **Piling on video hours.** All-online meetings add screen time for office staff. Jeremy Bailenson's 2021 analysis argues that features of the video interface itself can overload people with nonverbal demands and leave them exhausted after long call-heavy days, so pair the rule with fewer and shorter meetings and camera-optional slots.[^s6]

## Evidence and limits

Support for the rule is mostly practitioner experience and qualitative field work rather than controlled comparison. The 2019 field study rests on a handful of observed meetings at two companies and on short interviews, and its one successful all-device meeting also involved people already practised at remote etiquette.[^s2] The in-group findings come from a trading simulation with students, which shows the direction of the bias that the rule targets but not how much an all-online format reduces it in real teams.[^s5] The fatigue argument is theoretical and was not tested in the paper that proposed it.[^s6] Evidence status is therefore practitioner: a coherent, widely recommended norm whose benefits are plausible but not yet measured head to head against well-run hybrid meetings.[^s1][^s2]

## Connections

The rule is applied in hybrid meetings, turning them into video calls, and it sits under meeting design as a choice about format.[^s1][^s3] It addresses unequal participation by removing the room's advantage in airtime and turn-taking, a link supported only weakly by Saatçi and colleagues' 2019 field observations.[^s2] Bos and colleagues' 2004 in-group experiment supports the underlying rationale.[^s5] It relates to channel selection, because the alternative to a mixed room may be no meeting at all, and to Zoom fatigue and the camera-optional norm, which manage the costs of more time on video.[^s1][^s6] Meeting recaps and facilitation carry the rest of the load once everyone is on screen.[^s3]

## Sources

[^s1]: Rintel, Sellen, Jaffe, Hecht, Tang, Inkpen & Buxton, "Hybrid Meetings Guide", Microsoft Research, 2021. https://www.microsoft.com/en-us/research/articles/hybrid-meetings-guide (accessed 2026-11-13)
[^s2]: Saatçi, Rädle, Rintel, O'Hara & Klokmose, "Hybrid Meetings in the Modern Workplace: Stories of Success and Failure", CRIWG+CollabTech 2019, LNCS 11677, pp. 45-61, doi:10.1007/978-3-030-28011-6_4. https://www.lri.fr/~mbl/ENS/CSCW/2012/papers/Saatci-CTSC19.pdf (accessed 2026-11-13)
[^s3]: GitLab, "How to use forcing functions to work remote-first", The GitLab Handbook. https://handbook.gitlab.com/handbook/company/culture/all-remote/how-to-work-remote-first (accessed 2026-11-13)
[^s4]: The Open University, "Hybrid working: digital communication and collaboration", Section 8: Hybrid meetings, OpenLearn. https://www.open.edu/openlearn/digital-computing/hybrid-working-digital-communication-and-collaboration/content-section-8 (accessed 2026-11-13)
[^s5]: Bos, Shami, Olson, Cheshin & Nan, "In-group/out-group effects in distributed teams: An experimental simulation", CSCW 2004, pp. 429-436, doi:10.1145/1031607.1031679. https://cris.haifa.ac.il/en/publications/in-groupout-group-effects-in-distributed-teams-an-experimental-si-2/ (accessed 2026-11-13)
[^s6]: Bailenson, "Nonverbal Overload: A Theoretical Argument for the Causes of Zoom Fatigue", Technology, Mind, and Behavior, 2021, doi:10.1037/tmb0000030. https://vhil.stanford.edu/publications/social-interaction/nonverbal-overload-theoretical-argument-causes-zoom-fatigue (accessed 2026-11-13)
