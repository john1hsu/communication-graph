---
id: cm:status-reporting
type: Genre
title: Project status reporting
aliases: [status report, project status report, RAG status report, progress report]
domain: executive-and-client-communication
summary: >-
  The recurring written or spoken update in which a project team tells its sponsor, client or
  oversight body where the work stands against its agreed time, cost, scope and benefits, what has
  changed, which risks and issues need attention, and what decisions are needed. Research on IT
  projects shows such reports are often selectively optimistic, so the genre only works when the
  rating criteria are shared and bad news is safe to send early.
level: intermediate
evidenceStatus: practitioner
broader: [cm:business-report, cm:organizational-communication]
related: [cm:managing-up, cm:communicating-uncertainty, cm:words-of-estimative-probability, cm:bottom-line-up-front, cm:delivering-bad-news, cm:psychological-safety, cm:executive-briefing, cm:deaf-effect, cm:delivery-confidence-assessment]
requires: [cm:audience-analysis]
relations:
  - {predicate: explainedBy, object: cm:mum-effect, source: s2, confidence: high}
  - {predicate: demonstratedBy, object: cm:smith-keil-depledge-2001, source: s2, confidence: high}
  - {predicate: demonstratedBy, object: cm:keil-et-al-2014, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: cm:tan-et-al-2003, source: s3, confidence: medium}
  - {predicate: complements, object: cm:delivering-bad-news, source: s6, confidence: medium}
steps:
  - Agree with the sponsor, in writing, what each status rating means (for example what turns a project amber or red) before the first report goes out.
  - Open with the overall rating, the one-line reason for it and any decision you need, with a date.
  - Report against the approved baseline for time, cost, scope and benefits, and show the change since the last report rather than only the current position.
  - For each significant issue, state the cause, what you have already done, the options and your recommendation.
  - Raise a slipping milestone in the first report where you believe it is at risk, not the one where it is missed.
  - After each review, ask the reader whether the report gave them what they needed and adjust the format, not the facts.
example:
  situation: A team lead on a six-month CRM migration sends a fortnightly status report to the steering group; a data-quality problem has put the go-live date at risk.
  before: "Status: GREEN. Good progress this sprint - 14 of 18 integration tests passing. Some data-quality items being worked through with the vendor; we remain confident about the timeline and will update next report."
  after: "Status: AMBER (was GREEN). Go-live on 2 March is at risk: 22% of migrated customer records fail validation, and at the current fix rate cleanup finishes about three weeks late. Done so far: vendor engaged, root cause traced to duplicate legacy IDs. Options: (a) add two analysts for four weeks (about $18K) and hold the date; (b) move go-live to 23 March at no extra cost. Recommendation: (a). Decision needed from the steering group by Friday."
  why: The rewrite applies the agreed rating honestly, quantifies the problem instead of hiding it in reassurance, shows what has already been done, and turns the bad news into a decision the readers can make while there is still time to act.
selfCheck:
  - Would someone who knew everything I know give this project the same rating I have?
  - Is there a risk I am privately worried about that does not appear in this report, and why have I left it out?
  - Does the first line tell a busy sponsor whether they need to act, and by when?
  - Am I reporting change against the approved baseline, or only selecting the numbers that look good this week?
sameAs: []
sources:
  - id: s1
    title: "The Dynamics of IT Project Status Reporting: A Self-Reinforcing Cycle of Distrust"
    publisher: Mark Keil, H. Jeff Smith, Charalambos L. Iacovou & Ronald L. Thompson, Journal of the Association for Information Systems 15(12), 879-912, 2014, doi:10.17705/1jais.00383 (author copy via CORE)
    url: https://core.ac.uk/download/301380673.pdf
    type: peer-reviewed
    accessed: 2026-11-06
  - id: s2
    title: "Keeping Mum as the Project Goes Under: Toward an Explanatory Model"
    publisher: H. Jeff Smith, Mark Keil & Gordon Depledge, Journal of Management Information Systems 18(2), 189-227, 2001
    url: https://jmis-web.org/articles/885
    type: peer-reviewed
    accessed: 2026-11-06
  - id: s3
    title: "Reporting Bad News About Software Projects: Impact of Organizational Climate and Information Asymmetry in an Individualistic and a Collectivistic Culture"
    publisher: Bernard C. Y. Tan, H. Jeff Smith, Mark Keil & Ramiro Montealegre, IEEE Transactions on Engineering Management 50(1), 64-77, 2003, doi:10.1109/TEM.2002.808292 (bibliographic record)
    url: https://manuscript.isc.ac/Inventory/49/1180559.htm
    type: peer-reviewed
    accessed: 2026-11-06
  - id: s4
    title: "Blowing the Whistle: How IS Auditors Can Turnaround Troubled Software Projects - And Why They Sometimes Don't!"
    publisher: Mark Keil, manuscript for IS Audit and Control Journal, 1998 (author copy, Middlesex University research archive)
    url: https://www.eis.mdx.ac.uk/research/SFC/Papers/BlowingWhistle.pdf
    type: primary
    accessed: 2026-11-06
  - id: s5
    title: "Delivery Confidence Assessment: Guide for Review Teams"
    publisher: Infrastructure and Projects Authority, UK Government (GOV.UK)
    url: https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/638436/delivery_confidence_guide_for_review_teams.pdf
    type: government
    accessed: 2026-11-06
  - id: s6
    title: "Bearer of Bad News"
    publisher: PM Network 30(1), 20-21, Project Management Institute, January 2016
    url: https://www.pmi.org/learning/library/bearer-bad-news-9840
    type: institutional
    accessed: 2026-11-06
created: 2026-11-06
---

# Project status reporting

A project status report is the regular update - a written report, a dashboard with commentary, or a slot in a steering meeting - that tells a sponsor, client or oversight body how the work is tracking against what was approved, and what they need to decide.[^s5] Its job is to let people with authority intervene while intervention is still cheap. Research on information-systems projects shows it often fails at exactly that job: people delay or soften negative status information, and troubled projects stay invisible to senior management until the options have narrowed.[^s1][^s2]

## Origin

Status reporting grew out of project governance practice rather than from a single author, but its failure modes have a well-defined research lineage. Mark Keil and colleagues spent two decades studying why IT projects escalate, and kept finding that bad news was not passed upward. Keil's 1998 interviews with 42 IS auditors described auditors who saw speaking up as career-threatening, and executives who sometimes ignored warnings even when they were given.[^s4] Smith, Keil and Depledge (2001) then built and experimentally tested a model of this reluctance - the "mum effect" applied to projects - showing that the perceived impact of staying silent and the level of observed wrongdoing explained a significant share of whether people would report.[^s2] Government assurance bodies formalised the output side: the UK Infrastructure and Projects Authority, for example, publishes standard definitions for each delivery-confidence rating from Green to Red so that reviewers judge projects against the same scale.[^s5]

## Why it matters

A status report is a decision aid, and a biased one is worse than none because it creates false confidence. In a field study of nine state-government IT projects (118 interviews), Keil, Smith, Iacovou and Thompson (2014) found some misreporting in eight of them, through tactics such as highlighting only favourable items, redefining deliverables, reclassifying spend and choosing which numbers to show; they also cite earlier estimates that reports on high-risk projects are biased about 60% of the time, mostly in the optimistic direction.[^s1] Heavier auditing did not fix this: teams who found scrutiny unfair became more defensive, auditors read that as deception and scrutinised harder, and a self-reinforcing cycle of distrust set in.[^s1] Culture shapes the pressures too: in matched experiments in the United States and Singapore, American respondents were more swayed by whether the organisational climate rewarded or punished bad news, while Singaporean respondents were more swayed by whether the bad news could stay hidden.[^s3]

## What works here

Shared definitions come first. The IPA guide defines Green as successful delivery highly likely with no major outstanding issues, Amber as feasible but with significant issues needing management attention, and Red as delivery appearing unachievable; it also stresses that the rating is an evidence-based professional judgment, not a calculation.[^s5] Agreeing a scale like that up front removes much of the room for selective reporting. Keil's team observed that the one project in their study where reporters and auditors had reached a shared understanding of reporting expectations was also the one with honest reporting.[^s1]

Structure each problem as a decision. Practitioners interviewed by PMI recommend stating the issue, its cause, what has been done and the result, then offering options with a recommendation, and delivering serious news in person before it lands in writing.[^s6] Put the overall rating and any decision needed in the first line, so a sponsor scanning twenty reports can see which ones need them. Senior leaders matter as much as authors: Keil and colleagues recommend that management visibly reward honest reporting, give reviewers a helpful rather than purely inspecting role, and hold joint sessions on lessons learned to build trust.[^s1]

## Pitfalls

The "watermelon" report - green on the outside, red inside - is the classic failure: the rating stays green while the narrative fills with hedged phrases about items "being worked through". Optimism of the "fixed next month" kind is the most common bias, and it compounds when each report is judged only against the last one rather than the approved baseline.[^s1] A second pitfall is assuming that sending the warning is enough; Keil's auditors described executives who were deaf to bad news, so escalate with evidence and a clear ask rather than a buried caveat.[^s4] Finally, oversight that feels punitive breeds the defensive tactics it is trying to catch; tighten the relationship and the definitions before you tighten the scrutiny.[^s1]

## Connections

The reluctance that distorts status reports is explained by the mum effect, tested experimentally by Smith, Keil and Depledge (2001).[^s2] Keil et al. (2014) demonstrate how audit pressure and defensive reporting reinforce each other,[^s1] and Tan et al. (2003) show that national culture changes which pressures dominate.[^s3] Status reporting complements delivering bad news: the same issue-cause-action-options structure applies when the report carries a problem.[^s6] It is a kind of business report and a core part of managing up; it draws on communicating uncertainty and words of estimative probability when a forecast is unclear, and on bottom line up front for its opening. Formal rating scales such as the IPA delivery confidence assessment give it a shared vocabulary.[^s5]

## Sources

[^s1]: Keil, Smith, Iacovou & Thompson, "The Dynamics of IT Project Status Reporting: A Self-Reinforcing Cycle of Distrust", JAIS 15(12), 2014. https://core.ac.uk/download/301380673.pdf (accessed 2026-11-06)
[^s2]: Smith, Keil & Depledge, "Keeping Mum as the Project Goes Under: Toward an Explanatory Model", JMIS 18(2), 2001. https://jmis-web.org/articles/885 (accessed 2026-11-06)
[^s3]: Tan, Smith, Keil & Montealegre, "Reporting Bad News About Software Projects", IEEE TEM 50(1), 2003. https://manuscript.isc.ac/Inventory/49/1180559.htm (accessed 2026-11-06)
[^s4]: Keil, "Blowing the Whistle: How IS Auditors Can Turnaround Troubled Software Projects", 1998. https://www.eis.mdx.ac.uk/research/SFC/Papers/BlowingWhistle.pdf (accessed 2026-11-06)
[^s5]: Infrastructure and Projects Authority, "Delivery Confidence Assessment: Guide for Review Teams". https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/638436/delivery_confidence_guide_for_review_teams.pdf (accessed 2026-11-06)
[^s6]: PMI, "Bearer of Bad News", PM Network, January 2016. https://www.pmi.org/learning/library/bearer-bad-news-9840 (accessed 2026-11-06)
