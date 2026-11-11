---
id: cm:death-by-powerpoint
type: AntiPattern
title: Death by PowerPoint
aliases: [death by slides, bullet-point overload, slideument, text-heavy slides]
domain: presenting-and-public-speaking
summary: >-
  A presentation in which dense, bullet-heavy slides take over from the speaker and the argument:
  the audience reads crowded text while the presenter reads it aloud, and the main point gets lost
  in fragments, nested bullets and irrelevant detail.
level: introductory
evidenceStatus: mixed
broader: [cm:slide-design]
related: [cm:presentation, cm:assertion-evidence-slides, cm:bulleted-and-numbered-lists, cm:wall-of-text, cm:burying-the-lede, cm:presentation-rehearsal, cm:executive-briefing, cm:status-reporting]
requires: []
relations:
  - {predicate: demonstratedBy, object: cm:kosslyn-et-al-2012, source: s1, confidence: high}
  - {predicate: causes, object: cm:information-overload, source: s1, confidence: medium}
  - {predicate: undermines, object: cm:clarity, source: s2, confidence: high}
  - {predicate: supportedBy, object: cm:columbia-accident-investigation-board-report, source: s2, confidence: high}
  - {predicate: explainedBy, object: cm:cognitive-load, source: s5, confidence: medium}
  - {predicate: challengedBy, object: cm:farkas-2006, source: s6, confidence: medium}
example:
  situation: A team lead presents a quarterly operations review to the leadership team and needs approval to hire two support engineers.
  before: "Slide title: 'Q3 Support Update'. Nine bullets in 16-point type - 'Ticket volume up', 'New product launch in August', 'Tier 2 backlog', 'Response-time SLA - see appendix', 'Staffing considerations', and four more - which the lead reads aloud line by line before moving to the next identical-looking slide."
  after: "Slide title: 'Missed response-time targets doubled after the August launch - two hires would restore them'. Body: one chart of weekly SLA misses with the launch week marked. The lead explains the chart in their own words, then asks for the hiring decision; the detailed ticket data goes in a one-page handout sent before the meeting."
  why: The first version leaves leaders to dig the problem and the request out of fragments while competing with the speaker's voice. The second states the conclusion and the ask in the headline, shows the one piece of evidence that proves it, and moves the detail to a document that can be read at the reader's pace.
selfCheck:
  - Could someone read only my slide titles and know my conclusion and what I need from them?
  - Am I planning to read any slide aloud word for word, and if so, why does that text need to be on screen?
  - Is there any slide with more than about four bullets, or bullets nested more than two levels deep?
  - Is this material really a document that should be sent and read, rather than a talk that needs slides?
sameAs: []
sources:
  - id: s1
    title: "PowerPoint Presentation Flaws and Failures: A Psychological Analysis"
    publisher: Kosslyn, S. M., Kievit, R. A., Russell, A. G. & Shephard, J. M., Frontiers in Psychology 3, 230, 2012 (PubMed Central)
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3398435
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s2
    title: "Columbia Accident Investigation Board Report, Volume I (Chapter 7, 'Engineering by viewgraphs')"
    publisher: Columbia Accident Investigation Board / NASA, August 2003
    url: https://www.nasa.gov/wp-content/uploads/static/history/columbia/reports/CAIBreportv1.pdf
    type: government
    accessed: 2026-11-11
  - id: s3
    title: "The Cognitive Style of PowerPoint: Pitching Out Corrupts Within (eBook)"
    publisher: Tufte, E. R., Graphics Press
    url: https://www.edwardtufte.com/?p=579
    type: primary
    accessed: 2026-11-11
  - id: s4
    title: "Slip-sliding-away: A review of the literature on the constraining qualities of PowerPoint"
    publisher: Kernbach, S., Bresciani, S. & Eppler, M. J., Business and Professional Communication Quarterly 78(3), 292-313, 2015 (University of St. Gallen repository)
    url: https://www.alexandria.unisg.ch/244083/
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s5
    title: "Verbal redundancy in multimedia learning environments: A meta-analysis"
    publisher: Adesope, O. O. & Nesbit, J. C., Journal of Educational Psychology 104(1), 250-263, 2012 (Washington State University research exchange)
    url: https://rex.libraries.wsu.edu/esploro/outputs/journalArticle/Verbal-Redundancy-in-Multimedia-Learning-Environments/99900601157101842
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s6
    title: "Toward a better understanding of PowerPoint deck design"
    publisher: Farkas, D. K., Information Design Journal + Document Design 14(2), 2006 (author's copy, University of Washington)
    url: https://faculty.washington.edu/farkas/dfpubs/Farkas-Toward%20A%20Better%20Understanding%20of%20PowerPoint.pdf
    type: peer-reviewed
    accessed: 2026-11-11
created: 2026-11-11
---

# Death by PowerPoint

"Death by PowerPoint" is the everyday name for a presentation in which the slides, not the speaker, carry the talk: screen after screen of nested bullet points in small type, often read aloud word for word, with the main point buried somewhere in the middle.[^s1] Critics aim at slideware in general rather than one product, and much of the debate is about whether the fault lies in the tool or in the habit of treating a slide as a container for every sentence the presenter might say.[^s3][^s4][^s6]

## Origin

The label is informal, but the critique behind it took shape in the early 2000s, as slide talks built from lists became the standard format in corporate and government bureaucracies.[^s3][^s4] Yale information-design scholar Edward Tufte's 2003 essay *The Cognitive Style of PowerPoint* argued that template-driven bullet outlines weaken verbal and spatial reasoning and nearly always damage statistical analysis.[^s3][^s2] The same year, the board investigating the loss of the space shuttle Columbia reproduced Tufte's analysis of an engineering slide and criticised NASA's endemic use of briefing slides in place of technical papers.[^s2] A 2015 systematic review traced the literature from this early criticism, through a heated debate, to a phase of experimental research, and catalogued 18 cognitive, emotional and social constraints of slideware.[^s4]

## Why it matters

The Columbia slide is the extreme case. Its title claimed the test data showed the damage models were conservative, while the fact that the debris was far larger than anything tested - 640 times, by one estimate - sat in the last, lowest-level bullet.[^s2] The board noted that six levels of bullet hierarchy had chopped up what amounted to 11 simple sentences, and that a senior manager could read the slide without realising it described a life-threatening situation.[^s2] Most workplace decks carry lower stakes, but the same mechanism - key facts losing their priority as analysis is compressed into fragments and passed up a hierarchy - hides risks, requests and decisions in status reviews and executive briefings.[^s2][^s1]

## How to spot it

Kosslyn and colleagues checked 140 slideshows from research, education, government and business against eight perception and memory principles; none was free of flaws, and every one overloaded the audience's limited capacity.[^s1] The most common faults were bullet lists shown all at once, more than four bullets per list, bullets running over two lines and lists with no visible hierarchy.[^s1] In their survey of 205 audience members, the most annoying problems were a main point obscured by irrelevant detail, presenters reading their slides word for word, too little support for the main point, and slides with more than people could absorb before the next one appeared.[^s1] Warning signs in your own deck:

- Titles that name a topic ("Q3 update") rather than state a point.[^s1]
- Text you intend to read aloud verbatim.[^s1][^s5]
- Slides that only make sense if someone talks over them, yet are also emailed as the record.[^s2][^s6]
- Numbers and caveats squeezed into the lowest bullet level.[^s2]

## How to fix it

- **Separate the document from the talk.** For dense analysis, write a short paper or handout people can read at their own pace, and keep the slides for what you say live; the Columbia board and Tufte both pointed to technical writing as the better vehicle for complex reasoning.[^s2][^s3]
- **Put the point in the headline.** Make each slide title a sentence that states its conclusion, so the deck's argument survives a skim.[^s1]
- **Cut on-screen text that repeats your words.** A 2012 meta-analysis of 57 studies found that adding written text to spoken narration helped mainly when there were no pictures, and that showing key terms rather than full verbatim text did better.[^s5]
- **Reveal and limit.** Build lists one item at a time, keep them to about four short items, and remove detail that does not support the main point.[^s1]
- **Rehearse and check equipment.** Kosslyn's team advise reviewing every slide against the principles, rehearsing, and not counting on delivery skill to rescue overloaded slides.[^s1]

## Evidence

The evidence that overloaded, text-heavy slides frustrate audiences is fairly consistent, but the evidence on comprehension is thinner.[^s1][^s4] Kosslyn's principles rest on established perception and memory research, yet the authors acknowledge their effect on comprehension and recall was not tested directly, two of their three studies judged slides without a presenter, and the survey drew on self-reported memories of past talks.[^s1] Experimental work on verbal redundancy is more direct: presenting the same words both spoken and written shows no advantage over written text alone, and the benefit of adding text depends on learners' prior knowledge, pacing and whether visuals are present.[^s5] Tufte's stronger claim, that the software itself corrupts thinking, is disputed.[^s4] Technical-communication scholar David Farkas argued in 2006 that it judges slides as free-standing documents, sets up a false choice between slides and handouts, and blames the tool for what are largely problems of unskilled use and organisational culture.[^s6] The practical reading is that bad slide habits, not slides themselves, are the anti-pattern.[^s6][^s4]

## Connections

- **Demonstrated by** Kosslyn et al. (2012), whose content analysis and audience survey document how common and annoying these flaws are.[^s1]
- **Causes** information overload, since crowded slides exceed what an audience can take in while also listening.[^s1]
- **Undermines** clarity: the Columbia slide's fragments, vague wording and hierarchy hid the most important fact.[^s2]
- **Supported by** the Columbia Accident Investigation Board report, the best-known official critique of briefing slides replacing technical papers.[^s2]
- **Explained by** cognitive load and the verbal-redundancy research on reading and listening to the same words at once.[^s5]
- **Challenged by** Farkas (2006), who argues the blame lies more with users and organisations than with the tool.[^s6]
- **Related:** assertion-evidence slides are a targeted remedy; bulleted lists, wall of text and burying the lede are the same failures in writing; presentation rehearsal and executive briefings are where the fix gets applied.[^s1][^s2]

## Sources

[^s1]: Kosslyn, S. M., Kievit, R. A., Russell, A. G. & Shephard, J. M. (2012). "PowerPoint Presentation Flaws and Failures: A Psychological Analysis". *Frontiers in Psychology* 3, 230. https://pmc.ncbi.nlm.nih.gov/articles/PMC3398435 (accessed 2026-11-11)
[^s2]: Columbia Accident Investigation Board (2003). *Report, Volume I*, Chapter 7, pp. 191. NASA. https://www.nasa.gov/wp-content/uploads/static/history/columbia/reports/CAIBreportv1.pdf (accessed 2026-11-11)
[^s3]: Tufte, E. R. (2003). *The Cognitive Style of PowerPoint: Pitching Out Corrupts Within*. Graphics Press. https://www.edwardtufte.com/?p=579 (accessed 2026-11-11)
[^s4]: Kernbach, S., Bresciani, S. & Eppler, M. J. (2015). "Slip-sliding-away: A review of the literature on the constraining qualities of PowerPoint". *Business and Professional Communication Quarterly* 78(3), 292-313. https://www.alexandria.unisg.ch/244083/ (accessed 2026-11-11)
[^s5]: Adesope, O. O. & Nesbit, J. C. (2012). "Verbal redundancy in multimedia learning environments: A meta-analysis". *Journal of Educational Psychology* 104(1), 250-263. https://rex.libraries.wsu.edu/esploro/outputs/journalArticle/Verbal-Redundancy-in-Multimedia-Learning-Environments/99900601157101842 (accessed 2026-11-11)
[^s6]: Farkas, D. K. (2006). "Toward a better understanding of PowerPoint deck design". *Information Design Journal + Document Design* 14(2). https://faculty.washington.edu/farkas/dfpubs/Farkas-Toward%20A%20Better%20Understanding%20of%20PowerPoint.pdf (accessed 2026-11-11)
