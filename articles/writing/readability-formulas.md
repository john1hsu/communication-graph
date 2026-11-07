---
id: cm:readability-formulas
type: Technique
title: Readability formulas
aliases: [readability scores, readability tests, Flesch Reading Ease, Flesch-Kincaid Grade Level, reading grade level]
domain: writing
summary: >-
  Equations such as Flesch Reading Ease and Flesch-Kincaid Grade Level that estimate how hard a text is
  from surface counts, mainly word and sentence length; useful as a quick screen for dense drafts, but a
  weak guide to whether real readers will understand and act on a document.
level: intermediate
evidenceStatus: contested
broader: [cm:editing-for-clarity]
related: [cm:plain-language, cm:clarity, cm:clarity-index, cm:effective-writing-for-army-leaders]
requires: [cm:audience-analysis]
relations:
  - {predicate: introducedBy, object: cm:rudolf-flesch, source: s2, confidence: medium}
  - {predicate: challengedBy, object: cm:duffy-kabance-1982, source: s2, confidence: high}
  - {predicate: challengedBy, object: cm:redish-selzer-1985, source: s3, confidence: high}
  - {predicate: alternativeTo, object: cm:usability-testing, source: s3, confidence: high}
  - {predicate: confusedWith, object: cm:plain-language, source: s4, confidence: medium}
steps:
  - Decide who the readers are and what they must find, understand and do before you look at any score.
  - Prepare the text for scoring by removing headings, bullet fragments, tables, URLs and other non-prose that calculators miscount.
  - Run one named formula in one tool and record which you used, so later scores are comparable.
  - Treat a high score only as a pointer to passages worth rereading for long sentences and unfamiliar terms; fix those for the reader, not for the number.
  - Never chop sentences or swap in short but vague words just to lower the score.
  - Check the revised draft with a few real or representative readers (ask them to find an answer or explain the next step) and let their results, not the score, decide whether it is ready.
example:
  situation: A policy team is told every staff notice must score at or below grade 8 before it goes out.
  before: "Leave. Approval needed. Submit form. Use portal. Manager signs. HR checks. Then booked."
  after: "To book leave, submit the leave form in the HR portal at least two weeks ahead. Your manager approves it, HR checks your balance, and you get an email when it is booked."
  why: The choppy version scores as very easy but leaves readers guessing about order, deadline and who acts; the revised version scores slightly harder yet answers the questions readers actually have.
selfCheck:
  - Did I change any sentence only to move the score rather than to help a reader?
  - Which formula and tool produced this number, and did I strip headings and lists before scoring?
  - Has anyone from the intended audience tried to use this document, and what did they get wrong?
sameAs: []
sources:
  - id: s1
    title: "Derivation of New Readability Formulas (Automated Readability Index, Fog Count and Flesch Reading Ease Formula) for Navy Enlisted Personnel"
    publisher: Kincaid, Fishburne, Rogers & Chissom, Research Branch Report 8-75, Chief of Naval Technical Training, 1975 (University of Central Florida STARS record)
    url: https://stars.library.ucf.edu/istlibrary/56
    type: primary
    accessed: 2026-11-07
  - id: s2
    title: "The Role of Word Difficulty and Sentence Length in Text Comprehension"
    publisher: Duffy & Kabance, Navy Personnel Research and Development Center, NPRDC TR 82-44, 1982 (DTIC)
    url: https://apps.dtic.mil/sti/pdfs/ADA114935.pdf
    type: primary
    accessed: 2026-11-07
  - id: s3
    title: "The Place of Readability Formulas in Technical Communication"
    publisher: Redish & Selzer, Technical Communication 32(4), 1985 (Penn State research portal record)
    url: https://pure.psu.edu/en/publications/place-of-readability-formulas-in-technical-communication/
    type: peer-reviewed
    accessed: 2026-11-07
  - id: s4
    title: "Readability formulas, programs and tools: Do they work for plain language?"
    publisher: Gael Spivak, Our Languages blog, Language Portal of Canada (Government of Canada), 2023
    url: https://www.noslangues-ourlanguages.gc.ca/en/blogue-blog/readability-formulas-eng
    type: government
    accessed: 2026-11-07
  - id: s5
    title: "Comparison of readability scores for written health information across formulas using automated vs manual measures"
    publisher: Sydney Health Literacy Lab, University of Sydney (summary of a JAMA Network Open study)
    url: https://www.sydneyhealthliteracylab.org.au/health-literacy-editor-publications/1-y9tp7-9mdxz-thy7z
    type: academic
    accessed: 2026-11-07
created: 2026-11-07
---

# Readability formulas

A readability formula turns a passage into a score, usually a school grade level or a 0–100 "ease" number, by counting surface features such as average sentence length and average word length in syllables or letters.[^s4] The assumption built into every such formula is that longer words and longer sentences make text harder.[^s4] Word processors and online checkers now print these scores instantly, which is why many organisations set targets such as "grade 8 or lower" for staff notices, policies and customer letters.[^s4] Used as a technique, the point is to run a score as a cheap first screen for dense prose, and then to judge the draft by whether readers can use it.[^s3][^s4]

## Origin

Rudolf Flesch published his reading-ease guidelines in 1948, and later research on plain writing built on them.[^s2] In 1975 J. Peter Kincaid and colleagues recalculated three existing formulas, the Automated Readability Index, the Fog Count and Flesch Reading Ease, for the U.S. Navy, testing 531 enlisted sailors at technical schools on 18 passages from training manuals against a standard reading test.[^s1] That recalculated Flesch formula is the Flesch-Kincaid grade level that most software reports today.[^s2][^s1] The formulas were built to predict how hard existing text would be for a group of readers, not to tell writers how to write.[^s2]

## Why it matters

A score is fast, objective-looking and easy to put in a policy, so it often becomes the definition of "plain" in an organisation.[^s4] That makes it worth knowing exactly what the number can and cannot tell you. It can flag a draft full of 40-word sentences and polysyllabic jargon.[^s3] It cannot tell whether the words are familiar to your readers, whether the content is relevant, whether the order makes sense, or whether headings help people find things.[^s4] Redish and Selzer warned that writing to the formula pulls attention towards word and sentence length and away from what actually trips readers up.[^s3]

## How to apply it

Start from the audience, not the tool: know who will read the document and what they need to do with it.[^s4] Before scoring, strip out headings, bullet points, tables and links, because calculators count text from full stop to full stop, so a bulleted list can register as one enormous sentence.[^s4][^s5] Pick one formula in one tool and stick to it; a JAMA Network Open study summarised by the University of Sydney's Health Literacy Lab found that the same formula applied to the same health text gave grade levels up to 12.9 apart depending on the calculator, and preparing the text first cut the spread to about two grades.[^s5] Read the passages that score worst and fix them for the reader, by splitting tangled sentences and replacing terms the audience may not know.[^s3] Then test the draft with people like your readers, the step Redish and Selzer proposed as the real measure of readability, and which plain-language practitioners still recommend.[^s3][^s4]

## Common mistakes

- **Writing to the number.** Writers can learn to raise a score without making text any easier to understand.[^s4] In the Navy experiments, rewrites that cut readability by about six grade levels barely changed comprehension.[^s2]
- **Equating short with easy.** Short words can be abstract or ambiguous, and formulas score them as easy anyway.[^s4]
- **Penalising good layout.** Lists, white space and headings help readers but can make the score worse.[^s4]
- **Trusting one calculator.** Most automated tools in that comparison agreed poorly with a manual reference score.[^s5]
- **Ignoring everything else.** Formulas say nothing about graphics, organisation or formatting.[^s2]

## Evidence

The formulas do what they were designed for: Kincaid's team fitted them to the measured reading levels of real sailors.[^s1] The contested part is their use as a writing target. In five experiments with Navy recruits, Duffy and Kabance simplified vocabulary and sentences by readable-writing rules; scores fell sharply but comprehension hardly moved, with a small gain only from easier vocabulary for weaker readers, and they concluded the formula was neither a good guideline nor a good criterion.[^s2] Their study used one set of passages and one population, so it is not the last word.[^s2] Redish and Selzer reached the same practical conclusion from the technical-communication side, and in 2023 the ISO plain-language standard, drafted by experts from 25 countries, left readability formulas out.[^s3][^s4] Automated scoring adds its own error on top.[^s5]

## Connections

- **Introduced by** Rudolf Flesch, whose 1948 reading-ease work underlies the Flesch-Kincaid grade level.[^s2]
- **Challenged by** Duffy and Kabance (1982), whose rewrite experiments found that lowering scores did little for comprehension, and by Redish and Selzer (1985), who argued formulas mismeasure difficulty for adult readers.[^s2][^s3]
- **Alternative to** usability testing with real readers, which Redish and Selzer proposed as the better way to judge readability.[^s3]
- **Confused with** plain language: a low score is often treated as proof a text is plain, but the ISO standard defines plain language by whether content is relevant, findable, understandable and usable.[^s4]
- **Related:** clarity and plain language are the goals a score only gestures at, and the Army's clarity index in *Effective Writing for Army Leaders* belongs to the same family of counts (see those articles for their sources). Knowing your audience comes first, because a score cannot tell you whether words are familiar to them.[^s4]

## Sources

[^s1]: Kincaid, J. P., Fishburne, R. P., Rogers, R. L. & Chissom, B. S. (1975). *Derivation of New Readability Formulas (Automated Readability Index, Fog Count and Flesch Reading Ease Formula) for Navy Enlisted Personnel*. Research Branch Report 8-75. https://stars.library.ucf.edu/istlibrary/56 (accessed 2026-11-07)
[^s2]: Duffy, T. M. & Kabance, P. (1982). *The Role of Word Difficulty and Sentence Length in Text Comprehension*. NPRDC TR 82-44, Navy Personnel Research and Development Center. https://apps.dtic.mil/sti/pdfs/ADA114935.pdf (accessed 2026-11-07)
[^s3]: Redish, J. C. & Selzer, J. (1985). "The Place of Readability Formulas in Technical Communication". *Technical Communication* 32(4), 46–52. https://pure.psu.edu/en/publications/place-of-readability-formulas-in-technical-communication/ (accessed 2026-11-07)
[^s4]: Spivak, G. (2023). "Readability formulas, programs and tools: Do they work for plain language?" Our Languages blog, Language Portal of Canada. https://www.noslangues-ourlanguages.gc.ca/en/blogue-blog/readability-formulas-eng (accessed 2026-11-07)
[^s5]: Sydney Health Literacy Lab, University of Sydney. "Comparison of readability scores for written health information across formulas using automated vs manual measures" (JAMA Network Open). https://www.sydneyhealthliteracylab.org.au/health-literacy-editor-publications/1-y9tp7-9mdxz-thy7z (accessed 2026-11-07)
