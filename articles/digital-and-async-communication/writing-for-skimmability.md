---
id: cm:writing-for-skimmability
type: Technique
title: Writing for skimmability
aliases: [skimmable writing, scannable writing, writing for busy readers, designing messages for scanning]
domain: digital-and-async-communication
summary: >-
  Shaping emails, chat posts, tickets and documents so a reader who only scans still gets the point:
  key message and asks first, few words, descriptive headings, short chunks, lists and sparing emphasis.
level: introductory
evidenceStatus: mixed
broader: [cm:message-structure, cm:digital-communication]
related: [cm:informative-headings, cm:bulleted-and-numbered-lists, cm:bottom-line-up-front, cm:concise-writing, cm:plain-language, cm:email-subject-lines, cm:instant-messaging, cm:asynchronous-communication, cm:burying-the-lede, cm:editing-for-clarity]
requires: [cm:bottom-line-up-front]
relations:
  - {predicate: addresses, object: cm:wall-of-text, source: s4, confidence: high}
  - {predicate: appliedIn, object: cm:email, source: s1, confidence: high}
  - {predicate: explainedBy, object: cm:text-signaling, source: s3, confidence: high}
  - {predicate: supportedBy, object: cm:writing-for-busy-readers, source: s2, confidence: medium}
  - {predicate: challengedBy, object: cm:linos-et-al-2023-formality-effect, source: s6, confidence: medium}
steps:
  - Decide the one thing each reader must know or do, and put it in the subject line and first sentence.
  - Cut every sentence, idea and request that is not needed for that purpose; move background to a link or a later section.
  - Break the rest into short chunks of one idea each, and turn parallel items, options or steps into a list.
  - Give longer messages descriptive headings that start with the information-carrying words, so the headings alone tell the story.
  - Bold only the few words a reader must not miss, such as an owner, a decision or a deadline.
  - Make replying easy - say exactly what answer you need, by when, and offer the options if there are any.
  - Before sending, read only the first two lines, the headings and the bold text, and check that the message still works.
example:
  situation: An operations analyst posts in the team's chat channel about a software licence renewal that needs a manager decision by Friday.
  before: "Hey team, quick update on the analytics tool. I've been looking at our usage over the last few months and it looks like we only really use about half the seats, partly because the marketing folks moved to the other dashboard after the reorg. The vendor sent the renewal quote yesterday and it's up 12% on last year, though they said they might give us a discount if we commit to two years, which could be worth it if we think we'll still need it. Anyway the contract auto-renews on the 30th so we probably need to decide something soon, let me know what you think."
  after: "**Decision needed by Fri:** renew the analytics tool at 25 seats instead of 50?\n\n- **Cost:** the quote is up 12%; dropping to 25 seats saves about half.\n- **Usage:** only 24 of 50 seats were used in the last 3 months.\n- **Option:** a 2-year commitment may get a discount - worth asking only if we keep the tool.\n\n@Dana - reply **25**, **50** or **cancel**. The contract auto-renews on the 30th."
  why: The original hides the decision, the deadline and the person who must decide at the end of a long paragraph; the rewrite puts the ask and date in the first line, gives each fact its own short line, names the decider and makes the reply a one-word answer.
selfCheck:
  - If someone read only my first line, the headings and the bold words, would they know what I need and by when?
  - Is there any sentence, idea or second request I could cut or move to a follow-up message?
  - Have I bolded so much that the emphasis no longer marks what matters most?
  - Could the reader answer me in one word or one click?
sameAs: []
sources:
  - id: s1
    title: "Write shorter messages"
    publisher: Todd Rogers & Jessica Lasky-Fink, Harvard Kennedy School Executive Education (updated December 2020)
    url: https://www.hks.harvard.edu/sites/default/files/HKSEE/HKSEE%20PDFs/Write%20shorter%20messages.pdf
    type: academic
    accessed: 2026-11-21
  - id: s2
    title: "When Writing for Busy Readers, Less Is More"
    publisher: Todd Rogers & Jessica Lasky-Fink, Behavioral Scientist, 11 September 2023 (excerpt from their book Writing for Busy Readers, Dutton, 2023)
    url: https://behavioralscientist.org/when-writing-for-busy-readers-less-is-more/
    type: primary
    accessed: 2026-11-21
  - id: s3
    title: "Text-signaling devices and their effects on reading and memory processes"
    publisher: Robert F. Lorch Jr., Educational Psychology Review 1, 209-234 (1989), doi:10.1007/BF01320135
    url: https://link.springer.com/doi/10.1007/BF01320135
    type: peer-reviewed
    accessed: 2026-11-21
  - id: s4
    title: "Text Scanning Patterns: Eyetracking Evidence"
    publisher: Kara Pernice, Nielsen Norman Group (25 August 2019)
    url: https://nngroup.com/articles/text-scanning-patterns-eyetracking/
    type: institutional
    accessed: 2026-11-21
  - id: s5
    title: "Create a clear structure for your content"
    publisher: GOV.UK content and publishing guidance, Government Digital Service, UK Government
    url: https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-structure/
    type: government
    accessed: 2026-11-21
  - id: s6
    title: "The Formality Effect"
    publisher: Elizabeth Linos, Jessica Lasky-Fink, Chris Larkin, Lindsay Moore & Elspeth Kirkman, Harvard Kennedy School Faculty Research Working Paper RWP23-009 (2023), Harvard DASH repository
    url: https://dash.harvard.edu/server/api/core/bitstreams/81e2b42a-f7de-4813-b968-f0f091350dfa/content
    type: academic
    accessed: 2026-11-21
created: 2026-11-21
---

# Writing for skimmability

Writing for skimmability means designing a workplace message for the way it will actually be read: quickly, on a small screen, between other tasks. A skimmable email, chat post, ticket or document lets a reader who glances at it for a few seconds still pick up the main point and any request, and lets a reader who wants more find it fast.[^s1] It combines several narrower habits - putting the bottom line first, cutting words, chunking, lists, informative headings and sparing emphasis - into one design goal.[^s2][^s5]

## Origin

The advice has two roots. Usability researchers studying the web found that most people scan text rather than read it, and that the layout decides what they see: in Nielsen Norman Group's eyetracking work, Kara Pernice describes readers of unbroken text sliding into an F-shaped pattern that misses much of the content, while readers of pages with clear subheadings move from heading to heading and dip into the body only where it matters.[^s4] Government content designers turned this into rules: the UK Government Digital Service tells writers to put the most important information first, use descriptive front-loaded headings and break steps and options into lists.[^s5] The second root is behavioural science. In *Writing for Busy Readers* (2023), Harvard Kennedy School's Todd Rogers and Jessica Lasky-Fink argue that busy readers are the norm, and organise their advice into six principles: less is more, make reading easy, design for easy navigation, use enough formatting but no more, tell readers why they should care, and make responding easy.[^s2][^s1]

## Why it matters

Skimmed messages fail silently: the reader thinks they have the gist, misses the request and never returns. Rogers and Lasky-Fink report a randomized email to 7,002 school-district leaders in which a 49-word version drew 4.8% responses against 2.7% for a 127-word version with the same ask, even though two-thirds of a sample asked in advance predicted the longer email would do better.[^s1] They also describe readers abandoning long messages midway, and a survey in which professionals said they would deal with the concise email first.[^s2] The underlying mechanism is well studied in reading research: Lorch's 1989 review found that headings, previews, typographic cues and similar signals improve memory for the content they flag - but generally not for the content they leave unflagged, which is why it matters what you signal.[^s3]

## How to apply it

Start from purpose, not from your notes. Write down what each reader needs to know or do, put that in the subject line and opening sentence, and push background lower or behind a link.[^s5][^s1] Then remove words and, just as important, remove whole ideas: each extra request competes with the main one.[^s2] Chunk what remains, one idea per short paragraph, and use bulleted or numbered lists for options, steps and parallel facts - eyetracking shows scanners jump straight to lists and to styled words.[^s4] In anything longer than a screen, add descriptive headings that begin with the words carrying the information, so the headings alone summarise the message.[^s5] Finally, make responding easy: name who must act, state the deadline and, where you can, reduce the reply to a choice.[^s2]

Channel changes the dose. In a chat post the whole message should usually fit one short screen, so front-loading and cutting carry most of the load; in a long email or report, headings and a short summary at the top do more of the work.[^s1][^s5] Rogers and Lasky-Fink's text-message experiment even found that splitting two sentences into two separate texts raised parent responses by 15%, a sign that shorter units get read.[^s1] For executives and other heavy-inbox readers the same principles apply with less room for background.

## Common mistakes

The most common mistake is over-formatting. Rogers and Lasky-Fink warn that bullets, bold and highlighting guide attention only while they are scarce; when everything is emphasised, nothing is.[^s1][^s2] A second is chopping a message into fragments that lose the logic connecting them - lists should hold parallel items, not a chain of reasoning. A third is treating skimmability as a substitute for thinking: a well-formatted message with three competing requests is still hard to act on.[^s2] A fourth is assuming informal always beats formal (see below).[^s6]

## Evidence

The evidence is real but uneven. Signalling research is mostly laboratory work on recall of instructional text, and Lorch notes that effects on comprehension and reading processes had been studied far less than effects on memory.[^s3] Eyetracking studies of scanning patterns use small samples and web pages rather than email.[^s4] The field experiments on shorter messages are large but come largely from the authors' own research and partner organisations.[^s1] A caution comes from the same research group: in "The Formality Effect", a 2023 working paper not yet peer-reviewed, Linos, Lasky-Fink and colleagues found across field experiments with tens of thousands of recipients that formal government letters outperformed shorter, simpler informal ones, while more than 84% of experts surveyed had predicted the reverse.[^s6] Skimmable structure seems to help, but surface style and context - who is writing, and how much the reader trusts them - also matter, so the evidence status is mixed.[^s6]

## Connections

Writing for skimmability **addresses** the wall of text, the dense, unbroken message that scanners mostly skip.[^s4] It is **applied in** email, where its field evidence on response rates was gathered.[^s1] It is **explained by** text signalling: headings, previews and typographic cues tell readers what is important and improve memory for it.[^s3] It is **supported by** Rogers and Lasky-Fink's *Writing for Busy Readers*, which packages the approach as six principles,[^s2] and **challenged by** the formality-effect experiments, which show that stripping a message down to a simple informal style can backfire.[^s6] It requires bottom line up front, and gathers informative headings, bulleted and numbered lists and concise writing under one goal, alongside plain language and email subject lines.[^s5][^s1]

## Sources

[^s1]: Rogers, T. & Lasky-Fink, J. (2020). "Write shorter messages". Harvard Kennedy School Executive Education. https://www.hks.harvard.edu/sites/default/files/HKSEE/HKSEE%20PDFs/Write%20shorter%20messages.pdf (accessed 2026-11-21)
[^s2]: Rogers, T. & Lasky-Fink, J. (2023). "When Writing for Busy Readers, Less Is More". *Behavioral Scientist*, excerpt from *Writing for Busy Readers* (Dutton). https://behavioralscientist.org/when-writing-for-busy-readers-less-is-more/ (accessed 2026-11-21)
[^s3]: Lorch, R. F., Jr. (1989). "Text-signaling devices and their effects on reading and memory processes". *Educational Psychology Review* 1, 209-234. https://link.springer.com/doi/10.1007/BF01320135 (accessed 2026-11-21)
[^s4]: Pernice, K. (2019). "Text Scanning Patterns: Eyetracking Evidence". Nielsen Norman Group. https://nngroup.com/articles/text-scanning-patterns-eyetracking/ (accessed 2026-11-21)
[^s5]: Government Digital Service. "Create a clear structure for your content". GOV.UK content and publishing guidance. https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-structure/ (accessed 2026-11-21)
[^s6]: Linos, E., Lasky-Fink, J., Larkin, C., Moore, L. & Kirkman, E. (2023). "The Formality Effect". HKS Faculty Research Working Paper RWP23-009. https://dash.harvard.edu/server/api/core/bitstreams/81e2b42a-f7de-4813-b968-f0f091350dfa/content (accessed 2026-11-21)
