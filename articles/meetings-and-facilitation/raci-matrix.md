---
id: cm:raci-matrix
type: Technique
title: RACI matrix
aliases: [RACI chart, responsibility assignment matrix, responsible accountable consulted informed]
domain: meetings-and-facilitation
summary: >-
  A grid that lists a piece of work's tasks or decisions down one side and the people or roles
  across the top, marking for each who is Responsible for doing it, who is Accountable for it,
  who must be Consulted before it is done and who must be Informed after.
level: introductory
evidenceStatus: practitioner
broader: [cm:decision-rights]
related: [cm:meeting-agendas, cm:meeting-recaps, cm:group-decision-making]
requires: []
relations:
  - {predicate: addresses, object: cm:role-ambiguity, source: s2, confidence: medium}
  - {predicate: appliedIn, object: cm:communication-plan, source: s2, confidence: high}
  - {predicate: complements, object: cm:stakeholder-mapping, source: s2, confidence: medium}
  - {predicate: appliedIn, object: cm:project-planning, source: s4, confidence: medium}
  - {predicate: alternativeTo, object: cm:dare-decision-roles, source: s5, confidence: high}
steps:
  - List the recurring tasks and decisions that cause confusion as rows, and the roles involved as columns.
  - For each row, name exactly one Accountable owner - the person who signs off or makes the call.
  - Mark who is Responsible for doing the work, keeping it to as few people as possible.
  - Mark Consulted only for people whose input must be heard before the work is finished, and Informed for people who need the outcome afterwards.
  - Scan the finished grid for rows with no A, several As, many Rs or a long list of Cs, and fix them.
  - Share the grid with everyone named, agree it together, and use the C and I columns as the contact list for updates.
example:
  situation: A product team keeps arguing about who signs off on customer-facing release notes; marketing, support and engineering all edit them and the notes ship late.
  before: "Release notes - owners: Eng, Marketing, Support (everyone please review before we publish)."
  after: "Release notes - R: tech writer drafts. A: product manager approves and publishes. C: lead engineer checks accuracy by Wednesday. I: support team gets the final text on release day."
  why: One named approver ends the circular edits, the single consulted reviewer has a deadline, and support knows it will be told rather than needing to chase or review.
selfCheck:
  - For this decision, can everyone involved name the one person who makes the final call?
  - Is each person I have marked Consulted someone whose input could actually change the outcome?
  - Do the people marked Informed know when and how they will hear the result?
sameAs: []
sources:
  - id: s1
    title: "A meta-analysis of work demand stressors and job performance: examining main and moderating effects"
    publisher: Simona Gilboa, Arie Shirom, Yitzhak Fried & Cary L. Cooper, Personnel Psychology 61(2), 227-271, 2008 (Lancaster University repository author copy)
    url: https://eprints.lancs.ac.uk/id/eprint/45119/1/10.pdf
    type: peer-reviewed
    accessed: 2026-11-06
  - id: s2
    title: "RACI responsibility matrix"
    publisher: Focus Online Toolkit, University of Oxford, v1, July 2020
    url: https://focus.admin.ox.ac.uk/files/racipdf
    type: academic
    accessed: 2026-11-06
  - id: s3
    title: "Appendix A. RACI Chart (Pressure Injury Prevention Program Implementation Guide)"
    publisher: Agency for Healthcare Research and Quality (AHRQ), U.S. Department of Health and Human Services
    url: https://www.ahrq.gov/patient-safety/settings/hospital/resource/pressureinjury/guide/apa.html
    type: government
    accessed: 2026-11-06
  - id: s4
    title: "Topic resource 14: RACI matrix"
    publisher: Aged Care Quality and Safety Commission (Australian Government), governance toolkit
    url: https://www.agedcarequality.gov.au/sites/default/files/media/topic-resource-14-raci-matrix.pdf
    type: government
    accessed: 2026-11-06
  - id: s5
    title: "The limits of RACI - and a better way to make decisions"
    publisher: Aaron De Smet, Caitlin Hewes & Mengwei Luo, McKinsey & Company Organization Blog, July 2022
    url: https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/the-organization-blog/the-limits-of-raci-and-a-better-way-to-make-decisions
    type: institutional
    accessed: 2026-11-06
  - id: s6
    title: "Who has the 'D'? How clear decision roles enhance organizational performance"
    publisher: Paul Rogers & Marcia Blenko, Bain & Company (summary of the Harvard Business Review article, January 2006)
    url: https://www.bain.com/insights/who-has-the-d
    type: institutional
    accessed: 2026-11-06
created: 2026-11-06
---

# RACI matrix

A RACI matrix is a simple grid for making roles explicit: activities or decisions go down the side, people or roles go across the top, and each cell gets a letter. **R**esponsible is whoever does the work; **A**ccountable is the one person answerable for the result, with the authority to approve or veto; **C**onsulted are the people whose expertise or feedback is sought before the work is finished; **I**nformed are the people who need to know the decision or receive the output.[^s2] Its communication value is that it tells everyone, before work starts, whose voice is needed, who makes the call and who simply needs to be kept in the loop.[^s2][^s4]

## Origin

RACI comes from project-management practice rather than from a single study or author, and it is now a standard planning tool in public-sector and university guidance. Oxford's Focus toolkit presents it for use within and between teams and for strategic and project work,[^s2] the U.S. Agency for Healthcare Research and Quality includes a sample RACI chart in a hospital implementation guide,[^s3] and Australia's Aged Care Quality and Safety Commission uses one in its governance toolkit.[^s4] Variants differ in detail: AHRQ, for instance, reads the A as "Approver" and treats R as the person who researches options and recommends.[^s3] Consultancies have since proposed decision-focused alternatives - Bain's RAPID roles (Recommend, Agree, Input, Decide, Perform), published in *Harvard Business Review* in 2006,[^s6] and McKinsey's DARE roles (Deciders, Advisors, Recommenders, Execution stakeholders).[^s5]

## Why it matters

Unclear roles are costly. A 2008 meta-analysis in *Personnel Psychology* pooled 169 samples (about 35,000 people) and found that role ambiguity was among the work stressors most strongly linked to lower job performance; across 114 samples its corrected correlation with general performance was about -.24.[^s1] That is evidence for clarifying roles in general, not for RACI in particular. Practitioner guidance makes the more specific claim: filling in the grid exposes tasks nobody owns and tasks too many people think they own, prevents duplicated effort, and gives a ready-made basis for a communication plan.[^s2] Bain's survey of more than 350 organisations similarly traced stalled decisions to bottlenecks where no one was clearly accountable - between functions, between head office and business units, and with outside partners.[^s6]

## How to apply it

Build the matrix with the people who actually do the work and the key stakeholders, not alone at your desk.[^s2] List activities as rows and roles as columns, then assign letters.[^s2] Hold to one rule above all: each row has exactly one Accountable owner, so decisions and communication do not get split.[^s2][^s4] R and A are mandatory for every row; C and I are optional, and on a small task the same person can be both R and A.[^s4] Do it early, during planning and before detailed scheduling, and reserve it for work that is complex, involves many stakeholders, has overlapping responsibilities or has gone wrong before.[^s4] Then use the grid as a communication tool: the C column tells you whose input to seek before a deadline, and the I column is your distribution list when the decision is made.[^s2][^s3]

## Common mistakes

- **Several As, or none.** Shared accountability reproduces the confusion the grid was meant to remove; give every row one owner.[^s2][^s4]
- **Too many Rs.** Several people responsible for the same task is a sign of duplicated effort to resolve, not a safe default.[^s2]
- **Treating C as a vote.** McKinsey's critics argue that RACI often lets so many stakeholders weigh in or veto that no one clearly decides, and that delegated owners then escalate anyway because they feel they need everyone's backing.[^s5]
- **No timing for input.** RACI says who is consulted but not when or how, which can add bureaucracy; pair it with deadlines for input and an agreed escalation route.[^s5]
- **Filing it away.** The grid sets roles at a high level; detailed roles still belong in terms of reference, and the matrix only helps if people see and use it.[^s4]

## Evidence

RACI itself has little formal testing; the support is practitioner and public-sector guidance, so `practitioner` is the honest status.[^s2][^s3][^s4] The case for role clarity rests on correlational meta-analytic evidence, which cannot show that drawing a RACI chart is what improves performance.[^s1] The sharpest critique comes from McKinsey, which cites its finding that 80 percent of organisations struggle with decision-making and argues that a four-letter grid does not stop vetoes, slow consultation or unfocused meetings; its fix is to give more people a voice but fewer people a vote.[^s5] Bain's authors add that no role scheme can rescue a decision-maker who will not decide.[^s6]

## Connections

RACI sits under decision rights, the broader practice of settling who decides what.[^s5][^s6] It addresses role ambiguity by exposing gaps and overlaps in who does and owns each task.[^s2] It is applied in communication plans - its C and I columns define who to engage and who to inform - and complements stakeholder mapping, which identifies those people in the first place.[^s2] It is applied in project planning, where it is normally completed.[^s4] DARE is an alternative scheme proposed to fix RACI's weaknesses in decision-making, and RAPID is a similar decision-role model.[^s5][^s6] It is related to meeting agendas, which should say whether an item is for decision, discussion or information,[^s5] to meeting recaps, which tell the Informed what was decided, and to group decision making generally.[^s2][^s5]

## Sources

[^s1]: Gilboa, Shirom, Fried & Cooper, "A meta-analysis of work demand stressors and job performance: examining main and moderating effects", Personnel Psychology, 2008. https://eprints.lancs.ac.uk/id/eprint/45119/1/10.pdf (accessed 2026-11-06)
[^s2]: University of Oxford Focus Online Toolkit, "RACI responsibility matrix", 2020. https://focus.admin.ox.ac.uk/files/racipdf (accessed 2026-11-06)
[^s3]: AHRQ, "Appendix A. RACI Chart", Pressure Injury Prevention Program Implementation Guide. https://www.ahrq.gov/patient-safety/settings/hospital/resource/pressureinjury/guide/apa.html (accessed 2026-11-06)
[^s4]: Aged Care Quality and Safety Commission, "Topic resource 14: RACI matrix". https://www.agedcarequality.gov.au/sites/default/files/media/topic-resource-14-raci-matrix.pdf (accessed 2026-11-06)
[^s5]: De Smet, Hewes & Luo, "The limits of RACI - and a better way to make decisions", McKinsey & Company, 2022. https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/the-organization-blog/the-limits-of-raci-and-a-better-way-to-make-decisions (accessed 2026-11-06)
[^s6]: Rogers & Blenko, "Who has the 'D'? How clear decision roles enhance organizational performance", Bain & Company, 2006. https://www.bain.com/insights/who-has-the-d (accessed 2026-11-06)
