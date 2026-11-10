---
id: cm:wall-of-text
type: AntiPattern
title: Wall of text
aliases: [text wall, dense unbroken text, unformatted text block]
domain: writing
summary: >-
  Presenting a message as long, dense, unbroken paragraphs with no headings, lists, emphasis or white
  space, so busy readers who scan rather than read word by word miss key points and requests.
level: introductory
evidenceStatus: mixed
broader: [cm:message-structure]
related: [cm:bulleted-and-numbered-lists, cm:concise-writing, cm:plain-language, cm:bottom-line-up-front, cm:burying-the-lede, cm:information-overload, cm:email, cm:readability-formulas]
requires: []
relations:
  - {predicate: demonstratedBy, object: cm:nielsen-1997, source: s1, confidence: medium}
  - {predicate: supportedBy, object: cm:lorch-lorch-1996, source: s2, confidence: medium}
  - {predicate: challengedBy, object: cm:baker-chaparro-shaikh-2005, source: s3, confidence: medium}
  - {predicate: undermines, object: cm:clarity, source: s5, confidence: medium}
example:
  situation: A project lead emails six stakeholders about a delayed data migration and needs two of them to act by Thursday.
  before: "Hi all, following up on last week's steering call where we talked through the migration timeline and some of the issues the vendor raised about the legacy schema, which as you know has been a recurring theme since phase one, the team has now completed the mapping for most tables but we discovered that the customer-history table has about 40,000 records with inconsistent date formats, so the cutover will move from the 14th to the 21st, and to keep that date we will need Finance to confirm the archive cut-off and IT Security to approve the temporary service account by Thursday, otherwise we lose the weekend window..."
  after: "Subject: Migration moves to the 21st - 2 approvals needed by Thu\n\nCutover moves from the 14th to the 21st. To hold that date we need two things by Thursday:\n\n- **Finance (Priya):** confirm the archive cut-off date.\n- **IT Security (Marco):** approve the temporary service account.\n\n**Why the delay:** 40,000 customer-history records have inconsistent date formats and need cleaning.\n\n**If we miss Thursday:** we lose the weekend window and the next slot is the 4th."
  why: The original buries the new date and both requests mid-paragraph, so a scanning reader sees only the opening background; the rewrite front-loads the change, gives each request its own line with an owner, and uses short labelled chunks so every reader can find their part in seconds.
selfCheck:
  - If a colleague only read my first two lines and the bold text, would they know what changed and what I need from them?
  - Does any paragraph run longer than about five lines or cover more than one idea?
  - Is each request or deadline on its own line, with a named owner, instead of hidden in a sentence?
  - Have I used bold or headings sparingly enough that they still mark what matters most?
sameAs: []
sources:
  - id: s1
    title: "How Users Read on the Web"
    publisher: Jakob Nielsen, Nielsen Norman Group Alertbox (October 1997)
    url: https://www.nngroup.com/alertbox/9710a.html
    type: primary
    accessed: 2026-11-10
  - id: s2
    title: "Effects of Headings on Text Recall and Summarization"
    publisher: Robert F. Lorch Jr. & Elizabeth Pugzles Lorch, Contemporary Educational Psychology 21(3), 261-278 (1996), doi:10.1006/ceps.1996.0022 (University of Kentucky Scholars record)
    url: https://scholars.uky.edu/en/publications/effects-of-headings-on-text-recall-and-summarization/
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s3
    title: "Reading Online Text With a Poor Layout: Is Performance Worse?"
    publisher: J. Ryan Baker, Barbara S. Chaparro & A. Dawn Shaikh, Usability News 7(1), Software Usability Research Laboratory, Wichita State University (2005) (Embry-Riddle research portal record)
    url: https://portfolio.erau.edu/en/publications/reading-online-text-with-a-poor-layout-is-performance-worse/
    type: academic
    accessed: 2026-11-10
  - id: s4
    title: "Create a better user experience by changing the way you write"
    publisher: Christine Cawthorne, Government Digital Service blog, UK Government (14 November 2014)
    url: https://gds.blog.gov.uk/2014/11/14/create-a-better-user-experience-by-changing-the-way-you-write/
    type: government
    accessed: 2026-11-10
  - id: s5
    title: "F-Shaped Pattern of Reading on the Web: Misunderstood, But Still Relevant (Even on Mobile)"
    publisher: Kara Pernice, Nielsen Norman Group (2017, reviewed 2026)
    url: https://nngroup.com/articles/f-shaped-pattern-reading-web-content/
    type: institutional
    accessed: 2026-11-10
  - id: s6
    title: "Tips on how to connect with people who don't have time to read"
    publisher: Harvard Gazette, Harvard University (October 2023), on Todd Rogers & Jessica Lasky-Fink's Writing for Busy Readers
    url: https://news.harvard.edu/gazette/story/2023/10/tips-on-how-to-connect-with-people-who-dont-have-time-to-read
    type: news
    accessed: 2026-11-10
created: 2026-11-10
---

# Wall of text

A wall of text is a message delivered as long, dense paragraphs with no headings, lists, emphasis or white space to guide the eye. It is common in status emails, chat threads, tickets and reports written in one sitting. The problem is not length as such but the absence of visual cues: readers who scan, rather than read every word, have nothing to tell them where the important parts are.[^s5] Nielsen Norman Group's guidance describes exactly this situation, unformatted text with no bolding, bullets or subheadings, as one of the conditions under which readers fall back on skimming the first lines and the left edge of a page.[^s5]

## Origin

The term comes from online forums, but the evidence behind the advice comes from usability and reading research. In a 1997 Nielsen Norman Group study, users completed tasks on five versions of the same website; the version formatted for scanning, with the same text, scored 47% better on usability than the promotional control, and a concise, scannable and objective version scored 124% better.[^s1] The same report found that 79% of test users always scanned new pages and only 16% read word by word.[^s1] Government content designers took up the lesson: the UK Government Digital Service trains writers to use short sentences, frequent paragraph breaks and subheadings because people scan online text rather than read it.[^s4]

## Why it matters

When text arrives as a block, readers concentrate on the opening lines and the start of each line, and they skip content further down or further right without noticing what they missed.[^s5] In a workplace message that means the request, the deadline or the risk buried in the middle of paragraph two is the part most likely to be lost. Todd Rogers and Jessica Lasky-Fink, drawing on dozens of randomized experiments for their 2023 book, argue that most readers skim, so writers should take responsibility for making messages easy to navigate, for example with headings and fewer requests per message.[^s6] Dense text also costs effort and goodwill: GDS notes that white space and short sections signal that content is easy to get through and encourage people to keep reading.[^s4]

## How to spot it

- A paragraph runs past five or six lines, or covers several topics, decisions or requests at once.[^s4]
- The key change, ask or deadline does not appear in the first two paragraphs.[^s5]
- There are no headings, bullet points, numbered steps or bold key phrases anywhere in a message of more than a screen.[^s5]
- Readers reply asking a question the message already answered, or only act on the first item.[^s6]

## How to fix it

- **Front-load.** Put the most important point and any request in the first two lines, because attention is highest at the top.[^s4][^s5]
- **Chunk.** Break text into short paragraphs of one idea each, and add descriptive headings that start with the most informative words.[^s5]
- **List discrete items.** Turn parallel items, steps and requests into bullets or numbered lists, one per line with an owner.[^s5]
- **Emphasise sparingly.** Bold only the few phrases that must be seen; Rogers and Lasky-Fink report that highlighting one passage makes it more likely to be read but makes the rest less likely to be read.[^s6]
- **Cut.** Remove background the reader does not need; in the 1997 study, halving the word count improved usability by 58% on its own.[^s1]

## Evidence

The benefits of breaking up text are clearest for finding information and for satisfaction, and more mixed for comprehension. Headings improved recall of unfamiliar topics but not familiar ones in Lorch and Lorch's 1996 experiments, and they mainly helped readers notice briefly discussed topics when summarising.[^s2] A 2005 Wichita State study found that an enhanced layout with headers and indentation did not change reading speed or comprehension, though readers were more satisfied and found it less tiring.[^s3] The 1997 usability figures come from a single industry study and are not peer-reviewed.[^s1] The practical conclusion is that formatting helps busy readers find and act on what matters; it does not rescue a message whose content is unclear.[^s2][^s3]

## Connections

A wall of text is a failure of **message structure** (`cm:message-structure`). It is **demonstrated by** Nielsen's 1997 web-writing study (`cm:nielsen-1997`), where scannable layout beat dense promotional text,[^s1] and **supported by** Lorch and Lorch's heading experiments (`cm:lorch-lorch-1996`),[^s2] while Baker, Chaparro and Shaikh 2005 (`cm:baker-chaparro-shaikh-2005`) **challenge** the idea that layout alone improves comprehension.[^s3] Because readers skip what they cannot see, it **undermines clarity** (`cm:clarity`).[^s5] Remedies include **bulleted and numbered lists**, **concise writing**, **plain language** and **bottom line up front**; it often travels with **burying the lede** and adds to **information overload**, especially in **email**.[^s4][^s5][^s6]

## Sources

[^s1]: Nielsen, "How Users Read on the Web", Nielsen Norman Group (1997). https://www.nngroup.com/alertbox/9710a.html (accessed 2026-11-10)
[^s2]: Lorch & Lorch, "Effects of Headings on Text Recall and Summarization", Contemporary Educational Psychology (1996). https://scholars.uky.edu/en/publications/effects-of-headings-on-text-recall-and-summarization/ (accessed 2026-11-10)
[^s3]: Baker, Chaparro & Shaikh, "Reading Online Text With a Poor Layout: Is Performance Worse?", Usability News (2005). https://portfolio.erau.edu/en/publications/reading-online-text-with-a-poor-layout-is-performance-worse/ (accessed 2026-11-10)
[^s4]: Cawthorne, "Create a better user experience by changing the way you write", GDS blog (2014). https://gds.blog.gov.uk/2014/11/14/create-a-better-user-experience-by-changing-the-way-you-write/ (accessed 2026-11-10)
[^s5]: Pernice, "F-Shaped Pattern of Reading on the Web: Misunderstood, But Still Relevant (Even on Mobile)", Nielsen Norman Group (2017). https://nngroup.com/articles/f-shaped-pattern-reading-web-content/ (accessed 2026-11-10)
[^s6]: Harvard Gazette, "Tips on how to connect with people who don't have time to read" (2023). https://news.harvard.edu/gazette/story/2023/10/tips-on-how-to-connect-with-people-who-dont-have-time-to-read (accessed 2026-11-10)
