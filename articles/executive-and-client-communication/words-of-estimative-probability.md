---
id: cm:words-of-estimative-probability
type: Technique
title: Words of estimative probability
aliases: [estimative language, verbal probability expressions, calibrated likelihood words, probability lexicon]
domain: executive-and-client-communication
summary: >-
  Stating how likely something is with an agreed set of likelihood words, each tied to a numeric
  range that is shown next to the word, so that "likely" means the same thing to the writer and
  every reader.
level: intermediate
evidenceStatus: mixed
broader: [cm:communicating-uncertainty]
related: [cm:bottom-line-up-front, cm:executive-summary, cm:illusion-of-transparency, cm:plain-language]
requires: []
relations:
  - {predicate: introducedBy, object: cm:sherman-kent, source: s1, confidence: high}
  - {predicate: addresses, object: cm:vague-probability-language, source: s1, confidence: high}
  - {predicate: appliedIn, object: cm:executive-briefing, source: s2, confidence: medium}
  - {predicate: demonstratedBy, object: cm:wintle-et-al-2019, source: s3, confidence: high}
  - {predicate: supportedBy, object: cm:mandel-irwin-2021, source: s4, confidence: medium}
steps:
  - Agree a short likelihood scale with your team or client before you need it - for example remote (under 5%), unlikely (20-45%), roughly even (45-55%), likely (55-80%), very likely (80-95%) - with ranges that do not overlap.
  - Before writing a forecast, decide your own number or range first, then pick the one word on the scale whose range contains it.
  - Put the numeric range in brackets right after the word in the text itself ("likely (55-80%)"), not in a footnote, appendix or hover text.
  - Keep likelihood (how probable the event is) separate from confidence (how solid your evidence is), and say each in its own sentence.
  - Reserve "possible", "could" and "may" for cases where you genuinely cannot estimate the odds, and say so rather than using them as softeners.
  - Use the same words with the same meanings in every report, and add a short key whenever a new reader joins the distribution.
example:
  situation: A consultant updates a client steering committee on whether a system migration will hit its go-live date.
  before: "There is a real possibility we could miss the March 1 go-live, although the team is working hard and it may well still be achievable."
  after: "We judge it unlikely (20-45%) that we hit the March 1 go-live; very likely (80-95%) by March 22. We have moderate confidence: the estimate rests on two weeks of test-defect data. Decision needed by Friday: hold the date with reduced scope, or move it."
  why: The before version could be read anywhere from a small risk to a probable slip; the after version gives one shared range, separates odds from confidence, and turns the forecast into a decision the committee can make.
selfCheck:
  - If three readers each wrote down the percentage they think my likelihood word means, would their numbers land in the same range as mine?
  - Have I put the number next to the word, or am I relying on readers to look up a key they will probably skip?
  - Am I using "could", "may" or "possible" to hedge when I actually have an estimate I am reluctant to commit to?
  - Have I kept my confidence in the evidence separate from the likelihood of the event?
sameAs: []
sources:
  - id: s1
    title: "Words of Estimative Probability"
    publisher: Sherman Kent, Studies in Intelligence vol. 8 no. 4 (1964); CIA Center for the Study of Intelligence
    url: https://www.cia.gov/resources/csi/static/Words-of-Estimative-Probability.pdf
    type: primary
    accessed: 2026-11-03
  - id: s2
    title: "Intelligence Community Directive 203: Analytic Standards"
    publisher: Office of the Director of National Intelligence, signed 2 January 2015 (copy hosted by the Federation of American Scientists)
    url: https://irp.fas.org/dni/icd/icd-203.pdf
    type: government
    accessed: 2026-11-03
  - id: s3
    title: "Verbal probabilities: Very likely to be somewhat more confusing than numbers"
    publisher: "Wintle, Fraser, Wills, Nicholson & Fidler, PLOS ONE 14(4): e0213522 (2019), doi:10.1371/journal.pone.0213522 (University of Melbourne repository copy)"
    url: https://minerva-access.unimelb.edu.au/server/api/core/bitstreams/3d6edf87-1815-5d22-95d6-0b4510f8ea6b/content
    type: peer-reviewed
    accessed: 2026-11-03
  - id: s4
    title: "On measuring agreement with numerically bounded linguistic probability schemes: A re-analysis of data from Wintle, Fraser, Wills, Nicholson, and Fidler (2019)"
    publisher: Mandel & Irwin, PLOS ONE (2021), doi:10.1371/journal.pone.0248424
    url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7971511/
    type: peer-reviewed
    accessed: 2026-11-03
created: 2026-11-03
---

# Words of estimative probability

Words of estimative probability are a fixed vocabulary for saying how likely something is - "unlikely", "roughly even", "very likely" - where each word is pinned to a numeric range. The idea comes from intelligence analysis, where Sherman Kent argued that readers took the same phrase to mean wildly different odds, so estimates needed words with agreed numerical meanings.[^s1] U.S. intelligence analysts now work from a standard seven-band scale running from "almost no chance" (1-5%) to "almost certain" (95-99%).[^s2] The same discipline helps anyone who briefs executives or clients on risks, forecasts and deadlines.

## Origin

Sherman Kent, a senior CIA estimator, described the problem in a 1964 essay in *Studies in Intelligence*.[^s1] A 1951 National Intelligence Estimate had called an attack on Yugoslavia that year a "serious possibility". Kent himself meant odds of roughly 65 to 35 in favour, but when he asked fellow board members what they had understood, their answers ran from about 20-to-80 to 80-to-20 - the same words, read as anything from unlikely to likely.[^s1] He proposed a chart that tied a handful of terms to approximate odds (for example "probable" at about 75% and "almost certainly not" at about 5%), and argued that "possible" should be kept for outcomes whose odds could not be estimated at all.[^s1] He called supporters of fixed meanings the "mathematicians" and opponents who preferred flexible prose the "poets", and admitted the poets were winning in practice.[^s1] Decades later, Intelligence Community Directive 203 (2015) made a seven-band likelihood scale standard practice, discouraged mixing terms from different bands, and required that confidence in a judgment never be stated in the same sentence as its likelihood.[^s2]

## Why it matters

Leaders act on forecasts: whether a launch will slip, a deal will close or a risk will materialise. If you write "likely" meaning 60% and your director reads 90%, you have miscommunicated even though every word was accurate. Kent's own board showed that this gap appears even among expert colleagues reading the same text.[^s1] A 2019 experiment with 924 members of the public found that, without numerical guidance, readers' ranges for the intelligence terms matched the official ranges only about a third of the time, and that they pulled extreme words such as "very unlikely" toward the middle.[^s3] Pinning words to numbers turns a vague hedge into a judgment that can be acted on, questioned and later checked.

## How to apply it

1. **Agree the scale first.** Adopt a short, non-overlapping scale - ICD 203's bands are a ready-made starting point - and share it with the people you report to.[^s2][^s3]
2. **Think in numbers, then translate.** Settle on your estimate before choosing the word, so the word reports a judgment rather than a mood.[^s1]
3. **Bracket the range in the sentence.** In the 2019 experiment, numbers placed in brackets next to the word were the only format that substantially improved agreement; a linked table or hover tooltip helped little, partly because only about half of readers consulted them.[^s3]
4. **Separate likelihood from confidence.** ICD 203 treats confidence as a judgment about the quality and quantity of evidence, and forbids combining it with a likelihood term in one sentence.[^s2]
5. **Use "possible" honestly.** Following Kent, keep it for odds you cannot estimate, not as a softer way to say a number you would rather not commit to.[^s1]

## Common mistakes

- **Relying on a key nobody reads.** Putting the scale in an appendix or glossary assumes readers will look it up; most do not.[^s3]
- **Stacked hedges.** Phrases such as "may well", "could possibly" or "a real possibility" are exactly the "poet" language Kent showed readers decode inconsistently.[^s1]
- **Negative wording.** "Unlikely" produced more disagreement than its positive counterparts in the 2019 study and the weakest agreement in a 2021 re-analysis, so pair it with its range every time.[^s3][^s4]
- **Overusing extremes.** Readers soften "very likely" and "very unlikely", so state the range when the extremity matters.[^s3]
- **Mixing scales.** Switching between "probable", "likely" and "good chance" within one report implies different meanings; ICD 203 asks writers to stay within one row of terms or say explicitly that they are equivalent.[^s2]

## Evidence and limits

The core finding - that people assign widely different numbers to the same probability word - has a long record, from Kent's informal 1950s poll to controlled experiments.[^s1][^s3] The evidence for the fix is more qualified, so its status here is `mixed`. Wintle and colleagues found bracketed numbers raised average agreement with the official ranges from about 32% to about 66%, echoing earlier work on climate-report language in which bracketing raised consistency from about 27% to 40%.[^s3] Mandel and Irwin re-analysed the same data in 2021 with a measure that does not penalise readers for being more precise than the standard; agreement was higher in every condition (about 82% with brackets), but the ranking of formats held.[^s4] They warned that readers might mistake a bracketed band for the analyst's own interval for that specific event, and suggested numbers alone as an alternative worth testing.[^s4] Both studies used general-public samples reading intelligence statements rather than executives reading business forecasts, so effects in a boardroom are an extrapolation.[^s3][^s4]

## Connections

- **Broader:** a technique for communicating uncertainty, the wider practice of conveying what is and is not known.[^s1][^s2]
- **Introduced by Sherman Kent,** whose 1964 essay named the problem and proposed the first word-to-odds chart.[^s1]
- **Addresses vague probability language** - hedges such as "serious possibility" that readers decode into incompatible odds.[^s1]
- **Applied in executive briefings:** ICD 203 governs analytic products written for senior decision-makers and sets the likelihood scale they use.[^s2]
- **Demonstrated by Wintle et al. (2019),** the experiment showing in-text numerical brackets improve shared understanding,[^s3] and **supported by Mandel and Irwin (2021),** whose re-analysis confirmed the ordering of formats while questioning how agreement is scored.[^s4]
- **Related:** bottom line up front and executive summaries put the forecast first, and this technique makes the forecast itself unambiguous; the illusion of transparency explains why writers assume their "likely" is obvious to readers; plain language shares the goal of one reading, one meaning.[^s1][^s3]

## Sources

[^s1]: Kent, S. (1964). "Words of Estimative Probability". *Studies in Intelligence* 8(4). CIA Center for the Study of Intelligence. https://www.cia.gov/resources/csi/static/Words-of-Estimative-Probability.pdf (accessed 2026-11-03)
[^s2]: Office of the Director of National Intelligence (2015). *Intelligence Community Directive 203: Analytic Standards*. https://irp.fas.org/dni/icd/icd-203.pdf (accessed 2026-11-03)
[^s3]: Wintle, B. C., Fraser, H., Wills, B. C., Nicholson, A. E. & Fidler, F. (2019). "Verbal probabilities: Very likely to be somewhat more confusing than numbers". *PLOS ONE* 14(4): e0213522. https://minerva-access.unimelb.edu.au/server/api/core/bitstreams/3d6edf87-1815-5d22-95d6-0b4510f8ea6b/content (accessed 2026-11-03)
[^s4]: Mandel, D. R. & Irwin, D. (2021). "On measuring agreement with numerically bounded linguistic probability schemes: A re-analysis of data from Wintle, Fraser, Wills, Nicholson, and Fidler (2019)". *PLOS ONE*. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7971511/ (accessed 2026-11-03)
