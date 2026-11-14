---
id: cm:email-subject-lines
type: Technique
title: Email subject lines
aliases: [writing subject lines, informative subject lines, subject-line keywords]
domain: digital-and-async-communication
summary: >-
  Writing an email's subject line as a short, specific headline that states the topic, the action
  needed and any deadline, main point first, so recipients can triage, act on and later find the
  message without opening it.
level: introductory
evidenceStatus: mixed
broader: [cm:email]
related: [cm:informative-headings, cm:setting-reply-time-expectations, cm:scheduled-inbox-checks, cm:asynchronous-communication, cm:rfc-1855-netiquette-guidelines, cm:burying-the-lede]
requires: [cm:bottom-line-up-front]
relations:
  - {predicate: appliedIn, object: cm:email, source: s2, confidence: high}
  - {predicate: complements, object: cm:bottom-line-up-front, source: s4, confidence: high}
  - {predicate: addresses, object: cm:information-overload, source: s1, confidence: medium}
  - {predicate: supportedBy, object: cm:cox-et-al-2021, source: s1, confidence: medium}
  - {predicate: complements, object: cm:setting-reply-time-expectations, source: s1, confidence: medium}
steps:
  - Before writing the subject, decide what you need from the reader - an action, a decision, a signature or nothing - and by when.
  - Put the most important information first, because long subjects are cut off on phones and in narrow inbox panes.
  - Name the specific topic and context (project, meeting, document) rather than a generic word such as "Update" or "Question".
  - If your team uses them, start with an agreed keyword such as ACTION, DECISION, REQUEST or INFO, and add the deadline when there is one.
  - Flag urgency only when the deadline is real, and say how little effort a reply needs if that is true.
  - When a thread drifts to a new topic or the request changes, edit the subject or start a new email so it still matches the body.
example:
  situation: A project analyst needs a finance manager to approve a revised vendor quote before the purchase order deadline.
  before: "Subject: Quick question"
  after: "Subject: DECISION by Thu 3pm - approve revised Acme quote ($4.2K, +8%) for Q1 testing"
  why: The finance manager can see from the inbox list what is needed, by when and roughly how big the ask is, so the email gets triaged correctly and is easy to find later; "Quick question" forces an open just to learn whether it matters.
selfCheck:
  - If my reader saw only the subject line on a phone, would they know what I need and by when?
  - Does the subject still match what the email body now asks for?
  - Have I marked this urgent only because the deadline really is close?
sameAs: []
sources:
  - id: s1
    title: "Prioritizing unread e-mails: people send urgent responses before important or short ones"
    publisher: Cox, A. L., Bird, J., Brumby, D. P., Cecchinato, M. E. & Gould, S. J. J., Human-Computer Interaction 36(5-6), 511-534, 2021 (UCL Discovery accepted manuscript)
    url: https://discovery.ucl.ac.uk/10115257/3/Cox_HCIJnl_Prioritizing%20Unread%20Emails_minors_v4.pdf
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s2
    title: "Emails and letters"
    publisher: Australian Government Style Manual
    url: https://www.stylemanual.gov.au/content-types/emails-and-letters
    type: government
    accessed: 2026-11-14
  - id: s3
    title: "How to Write Email with Military Precision"
    publisher: Sehgal, K., Harvard Business Review, November 2016 (author's copy at kabir.cc)
    url: https://kabir.cc/how-to-write-email-with-military-precision/
    type: practitioner-journal
    accessed: 2026-11-14
  - id: s4
    title: "How to write effective emails"
    publisher: Bhundiya, H., MIT AeroAstro Communication Lab
    url: https://mitcommlab.mit.edu/aeroastro/2025/03/17/how-to-write-effective-emails/
    type: academic
    accessed: 2026-11-14
  - id: s5
    title: "Exploring Email Triage: Challenges and Opportunities"
    publisher: Sarrafzadeh, B., Hassan Awadallah, A. & Shokouhi, M., Proceedings of CHIIR 2019, ACM (Microsoft Research)
    url: https://www.microsoft.com/en-us/research/uploads/prod/2019/02/Email_Triage_CHIIR19.pdf
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s6
    title: "Send users an email"
    publisher: UK Home Office, User-Centred Design Manual and Design System
    url: https://design.homeoffice.gov.uk/design-system/patterns/send-users/email
    type: government
    accessed: 2026-11-14
created: 2026-11-14
---

# Email subject lines

An email subject line is the headline a recipient sees in the inbox before deciding whether, when and how to deal with the message. The technique is to write it as a short, specific summary of the email's purpose - the topic, what you need and by when - with the most important words first, so the reader can triage the message, act on it and find it again without opening it.[^s2][^s6] Government writing guidance describes a good subject as a concise heading that tells people what is in the email and why they should read it.[^s2]

## Origin

Advice to make the subject say what a message is about dates from the early netiquette guides; public-sector style guides have since turned it into specific rules: the Australian Government Style Manual asks for a short but informative subject with the main idea first, because long subjects are truncated on small screens, and the UK Home Office design system asks for a concise subject with the most important information first.[^s2][^s6] A second strand comes from military staff writing. In a widely shared 2016 *Harvard Business Review* article, former US Navy officer Kabir Sehgal described how military emails open with a capitalised keyword - ACTION, SIGN, INFO, DECISION, REQUEST or COORD - that tells the reader at a glance what kind of response is expected.[^s3] University writing centres now teach the subject line as the first place to apply bottom line up front.[^s4]

## Why it matters

Recipients triage before they read. In a 2019 study of information workers at a large technology company, people said they decided quickly, and largely without deliberation, which emails to handle now and which to defer, weighing who sent the message, whether it asked them something directly, how urgent it was and how much effort it would take; 86% of survey respondents named urgency as a reason to deal with an email immediately.[^s5] The subject line is the main place a sender can signal urgency and the kind of ask before the message is opened. A 2021 field experiment that sent 16,200 controlled emails to the real inboxes of 45 participants over three weeks found that urgency cues in the subject line strongly increased how often and how fast people replied.[^s1] The authors concluded that blank or ambiguous subjects are a poor way to get the attention of people who handle a lot of email, and advised senders to make urgency, importance and the effort needed clear.[^s1] A specific subject also makes the email easier to find later by search.[^s2][^s4]

## How to apply it

Start from the reader's next action. Decide whether you need a decision, an approval, information or nothing at all, and whether there is a real deadline; then put that first. For example, "Feedback request for conference presentation" or "Scheduling committee meeting in March" both name the task and its context, where "Hi" or "Question" do not.[^s4] If a reply is needed by a time, state the deadline in the subject or the first line so the reader can prioritise it.[^s4] Keep it short but informative, front-loading the key words because the end may be cut off, and avoid spam-like wording that might look suspicious.[^s2][^s6] Teams that agree on keyword prefixes such as ACTION, INFO or REQUEST give everyone a shared code for sorting their inbox, as in the military example "REQUEST - Vacation".[^s3] Finally, keep subject and body in step: the subject should sum up what the body actually asks.[^s2]

Channel and seniority change the details. On a phone only the first few words may show, so the leading words matter most.[^s2] Senior readers and people with heavy inboxes are exactly those for whom ambiguous subjects fail, so the habit pays off most in upward and cross-team email.[^s1]

## Common mistakes

- **Vague or empty subjects** ("Update", "Following up", or no subject) that force the reader to open the email to learn whether it matters; the 2021 experiment found these ineffective with busy recipients.[^s1]
- **Crying urgent.** People answer urgent-looking emails first even when they matter little, so overusing urgency cues crowds out more important work and teaches readers to ignore the flag.[^s1]
- **Burying the point at the end** of a long subject that gets truncated on mobile.[^s2][^s6]
- **Stale thread subjects**, where a reply chain called "Budget" has turned into a request for a new hire; the subject no longer sums up the email's purpose.[^s2]
- **Assuming importance labels do the work.** In the 2021 experiment, stating how important an email was in the subject had no overall effect on response rate or time; urgency and low effort mattered more.[^s1]

## Evidence

The evidence is real but narrow, so the status is *mixed*. The 2021 *Human-Computer Interaction* field experiment by Cox and colleagues is the strongest direct test: urgency in the subject line reliably sped and increased replies, while displayed importance did not, and short, low-effort requests were favoured when nothing was urgent.[^s1] Its emails all came from a single sender and only 29 of 45 participants responded often enough for the main analysis, so effects of sender seniority and real organisational stakes were not tested.[^s1] Interview and survey work on email triage confirms that urgency, directness of the ask and sender drive what gets handled first, but did not study subject lines directly.[^s5] The specific advice on length, keywords and wording rests on government and practitioner guidance rather than controlled studies.[^s2][^s3][^s6]

## Connections

Subject lines are **applied in** email, where style guides treat them as a required part of every message.[^s2] They **complement** bottom line up front: writing guides call the subject line the natural place to state the bottom line, which then opens the body.[^s4] They **address** information overload by letting busy recipients triage without opening every message, which is why ambiguous subjects fail heavy email users.[^s1] They are **supported by** Cox et al.'s 2021 field experiment on how people prioritise unread email.[^s1] They **complement** setting reply-time expectations, since both tell the reader honestly how urgent a message is; the same study warns that false urgency displaces important work.[^s1] Subject lines are the inbox equivalent of informative headings, and the cure for burying the lede before the email is even opened; Sehgal's keyword prefixes show one way a team can standardise them.[^s3]

## Sources

[^s1]: Cox, A. L., Bird, J., Brumby, D. P., Cecchinato, M. E. & Gould, S. J. J. (2021), "Prioritizing unread e-mails: people send urgent responses before important or short ones", *Human-Computer Interaction* 36(5-6), 511-534. https://discovery.ucl.ac.uk/10115257/3/Cox_HCIJnl_Prioritizing%20Unread%20Emails_minors_v4.pdf (accessed 2026-11-14)
[^s2]: Australian Government Style Manual, "Emails and letters". https://www.stylemanual.gov.au/content-types/emails-and-letters (accessed 2026-11-14)
[^s3]: Sehgal, K. (2016), "How to Write Email with Military Precision", *Harvard Business Review* (author's copy). https://kabir.cc/how-to-write-email-with-military-precision/ (accessed 2026-11-14)
[^s4]: Bhundiya, H., "How to write effective emails", MIT AeroAstro Communication Lab. https://mitcommlab.mit.edu/aeroastro/2025/03/17/how-to-write-effective-emails/ (accessed 2026-11-14)
[^s5]: Sarrafzadeh, B., Hassan Awadallah, A. & Shokouhi, M. (2019), "Exploring Email Triage: Challenges and Opportunities", *Proceedings of CHIIR 2019*, ACM. https://www.microsoft.com/en-us/research/uploads/prod/2019/02/Email_Triage_CHIIR19.pdf (accessed 2026-11-14)
[^s6]: UK Home Office, "Send users an email", User-Centred Design Manual and Design System. https://design.homeoffice.gov.uk/design-system/patterns/send-users/email (accessed 2026-11-14)
