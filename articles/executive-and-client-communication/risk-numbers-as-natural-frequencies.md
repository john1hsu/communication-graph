---
id: cm:risk-numbers-as-natural-frequencies
type: Technique
title: Risk numbers as natural frequencies
aliases: [natural frequencies, natural frequency format, frequency format, count-based risk statements]
domain: executive-and-client-communication
summary: >-
  Restating percentages and conditional probabilities as whole-number counts drawn from one stated
  group ("of 10,000 orders, 20 are fraudulent and 18 of those get flagged"), so listeners can see
  base rates, hits and false alarms and work out what a result actually means.
level: intermediate
evidenceStatus: mixed
broader: [cm:risk-communication]
related: [cm:communicating-uncertainty, cm:words-of-estimative-probability, cm:plain-language, cm:executive-briefing]
requires: []
relations:
  - {predicate: develops, object: cm:communicating-uncertainty, source: s2, confidence: medium}
  - {predicate: addresses, object: cm:base-rate-neglect, source: s1, confidence: high}
  - {predicate: introducedBy, object: cm:gerd-gigerenzer, source: s1, confidence: high}
  - {predicate: demonstratedBy, object: cm:gigerenzer-hoffrage-1995, source: s1, confidence: high}
  - {predicate: supportedBy, object: cm:mcdowell-jacobs-2017, source: s4, confidence: high}
  - {predicate: challengedBy, object: cm:sirota-navarrete-juanchich-2024, source: s5, confidence: medium}
  - {predicate: appliedIn, object: cm:patient-education, source: s2, confidence: high}
steps:
  - Pick one reference group large enough that every count comes out as a whole number (1,000 or 10,000 is usual) and name it in the first sentence.
  - Split that group by the base rate first - how many have the condition, defect or event and how many do not.
  - Apply the detection or hit rate inside the first subgroup and the false-alarm rate inside the second, and write each result as a count.
  - Answer the decision question as "X out of Y" - for example, how many of all flagged cases are real - instead of quoting the test's accuracy.
  - Keep the same denominator for every option you compare, and give absolute changes ("from 20 to 10 in 1,000") rather than relative ones ("halved").
  - Tie every number to its group in the wording ("of the 9,980 legitimate orders, about 500 are flagged") and, for a live audience, sketch the counts as a simple frequency tree.
example:
  situation: A risk analyst briefs the head of operations on whether to auto-cancel every order a new fraud model flags.
  before: "The model catches 90% of fraud with only a 5% false-positive rate, so a flagged order is very likely fraudulent - I'd auto-cancel them."
  after: "Out of every 10,000 orders, about 20 are fraudulent and the model flags 18 of them. Of the other 9,980 legitimate orders it also flags about 500. So of roughly 518 flagged orders, only 18 - about 1 in 30 - are fraud. Auto-cancelling would block about 500 good customers to stop 18 bad ones; I suggest manual review instead."
  why: The before version quotes the model's accuracy and invites the listener to ignore how rare fraud is; the counts make the base rate and the false alarms visible, so the leader can see that most flags are wrong and decide on that basis.
selfCheck:
  - Have I stated the reference group ("out of every 1,000 ...") before giving any count?
  - Can my listener see how many cases are false alarms, not just how many real cases are caught?
  - Am I comparing options with the same denominator and in absolute terms rather than "doubled" or "halved"?
  - Does every number in my sentence clearly belong to one named group?
  - If someone asked "so of the ones flagged, how many are real?", have I already answered it?
sameAs: []
sources:
  - id: s1
    title: "How to improve Bayesian reasoning without instruction: Frequency formats"
    publisher: "Gigerenzer & Hoffrage, Psychological Review 102(4): 684-704 (1995) (course copy, UC San Diego)"
    url: https://pages.ucsd.edu/~scoulson/203/GG_How_1995.pdf
    type: peer-reviewed
    accessed: 2026-11-05
  - id: s2
    title: "Helping doctors and patients make sense of health statistics"
    publisher: "Gigerenzer, Gaissmaier, Kurz-Milcke, Schwartz & Woloshin, Psychological Science in the Public Interest 8(2): 53-96 (2007) (copy hosted by UC Berkeley Statistics)"
    url: https://www.stat.berkeley.edu/~aldous/157/Papers/health_stats.pdf
    type: peer-reviewed
    accessed: 2026-11-05
  - id: s3
    title: "Why can only 24% solve Bayesian reasoning problems in natural frequencies: Frequency phobia in spite of probability blindness"
    publisher: "Weber, Binder & Krauss, Frontiers in Psychology 9: 1833 (2018), doi:10.3389/fpsyg.2018.01833"
    url: https://www.frontiersin.org/articles/10.3389/fpsyg.2018.01833/pdf
    type: peer-reviewed
    accessed: 2026-11-05
  - id: s4
    title: "When, why, and for whom are natural frequency formats most effective? A meta-analysis"
    publisher: "McDowell & Jacobs (Max Planck Institute for Human Development), Society for Medical Decision Making meeting abstract"
    url: https://smdm.confex.com/smdm/16BEC/webprogram/Paper9915.html
    type: primary
    accessed: 2026-11-05
  - id: s5
    title: "When intuitive Bayesians need to be good readers: The problem-wording effect on Bayesian reasoning"
    publisher: "Sirota, Navarrete & Juanchich, Cognition 245: 105722 (2024), doi:10.1016/j.cognition.2024.105722 (University of Essex repository copy)"
    url: https://repository.essex.ac.uk/37751/1/1-s2.0-S0010027724000088-main.pdf
    type: peer-reviewed
    accessed: 2026-11-05
created: 2026-11-05
---

# Risk numbers as natural frequencies

Natural frequencies are plain counts taken from one stated group - "of every 1,000 people, 10 have the condition, and 8 of those test positive" - used instead of percentages and conditional probabilities such as "the test has an 80% hit rate and a 9.6% false-positive rate".[^s1][^s2] The technique is to translate any risk statement that depends on a base rate (a screening result, a fraud flag, a defect alarm, a forecast hit rate) into such counts before you present it, so the listener can see how the numbers fit together.[^s2] Because the counts in a natural-frequency statement add up to the whole group, while the conditional probabilities do not sum to 100%, the arithmetic becomes simple enough to do in your head.[^s2]

## Origin

The psychologists Gerd Gigerenzer and Ulrich Hoffrage introduced the approach in a 1995 *Psychological Review* paper.[^s1] Earlier research had concluded that people ignore base rates and are poor intuitive statisticians; Gigerenzer and Hoffrage argued that this partly reflected the probability format the problems were given in.[^s1] They proposed that counts acquired by "natural sampling" - tallying cases as you meet them - make Bayesian inference computationally easier, and showed that rewriting the same problems as frequencies roughly doubled or tripled correct answers in their first study (from 16% to 46% with the standard wording).[^s1] Gigerenzer and colleagues later carried the idea into medicine, recommending natural frequencies, absolute risks and frequency statements over conditional probabilities, relative risks and single-event probabilities.[^s2]

## Why it matters

Decisions at work often rest on a test or signal plus a base rate: a fraud model, a quality inspection, a candidate-screening score, an alert from a monitoring tool. When such evidence is stated as percentages, even experts misread it. In one workshop, only 21% of 160 gynaecologists picked the right answer to a mammography problem given as conditional probabilities - most grossly overestimated the chance of cancer after a positive result - but after training in translating the figures into natural frequencies, 87% did.[^s2] The same review showed how relative-risk framing inflates benefits: a fall from 20% to 10% and one from 0.0002% to 0.0001% are both "a 50% reduction".[^s2] A leader who hears "95% accurate" or "risk halved" without the underlying counts cannot judge whether to act.[^s2]

## How to apply it

Start from a round reference group, split it by the base rate, then apply the hit and false-alarm rates inside each subgroup so that everything becomes a count.[^s1] State the answer to the real question - how many of the flagged cases are genuine - as "X out of Y", and use the same denominator and absolute numbers when comparing options.[^s2] For a live briefing, a simple tree that branches the group into "has it / does not" and then "flagged / not flagged" shows the same structure visually.[^s2] Wording matters as much as format: a 2024 series of seven experiments found that natural frequencies helped mainly when each number was unambiguously linked to its reference group and the text was simplified.[^s5]

## Common mistakes

- **Normalised frequencies.** "8% of positives are true" or "80 per 100 with the condition" restore the conditional structure; the gain comes from counts that nest inside one group.[^s1][^s5]
- **Switching denominators.** Giving one figure per 1,000 and another per 100,000 forces the listener back into arithmetic.[^s2]
- **Relative risk alone.** "Halves the risk" without the absolute counts exaggerates small effects.[^s2]
- **Assuming the format does all the work.** Many people still convert frequencies back into probabilities and then get them wrong, so spell out the final count rather than leaving the listener to compute it.[^s3]

## Evidence and limits

The evidence is `mixed`. A meta-analysis by Michelle McDowell and Perke Jacobs of 90 effects from 30 papers found that natural frequencies improve Bayesian reasoning on average compared with conditional probabilities, while a substantial minority still struggles.[^s4] Researchers summarising that meta-analysis report average accuracy of about 24% with natural frequencies against about 4% with probabilities - a large relative gain from a low starting point.[^s3] The benefit shrank when both formats used visual aids or when the question and answer formats matched.[^s4] In a 2018 study of 180 students, about half the people given frequencies switched to probabilities to calculate, and accuracy depended more on the format they calculated in than on the one they were shown.[^s3] Most strikingly, Sirota, Navarrete and Juanchich (2024), across seven experiments with 4,909 adults, found that natural frequencies beat single-event probabilities only when the problem was clearly worded; with standard textbook wording the advantage often vanished.[^s5] Why frequencies help - an evolved preference for counts, as Gigerenzer argues, or simply clearer set structure - is still debated.[^s1][^s5] Nearly all of this research uses medical-test puzzles with students or online panels, so its use in business briefings is a reasonable extrapolation rather than a tested result.[^s3][^s5]

## Connections

- **Broader:** a technique of risk communication, the practice of explaining hazards and probabilities to people who must act on them.[^s2]
- **Develops** the skill of communicating uncertainty to decision makers: translating probabilities into counts is the core skill Gigerenzer and colleagues trained doctors in.[^s2]
- **Addresses base-rate neglect,** the tendency to ignore how rare an event is when interpreting a signal; frequencies make the base rate visible.[^s1]
- **Introduced by Gerd Gigerenzer** and **demonstrated by Gigerenzer and Hoffrage (1995),** whose experiments showed the frequency-format advantage.[^s1]
- **Supported by McDowell and Jacobs (2017),** the meta-analysis confirming the average benefit.[^s4]
- **Challenged by Sirota, Navarrete and Juanchich (2024),** who found the benefit depends on clear wording.[^s5]
- **Applied in patient education,** where doctors explain screening results and treatment effects as counts.[^s2]
- **Related:** words of estimative probability, which fixes verbal likelihood terms rather than numeric ones; plain language; and the executive briefing, where such numbers usually have to land.[^s2]

## Sources

[^s1]: Gigerenzer, G. & Hoffrage, U. (1995). "How to improve Bayesian reasoning without instruction: Frequency formats". *Psychological Review* 102(4): 684-704. https://pages.ucsd.edu/~scoulson/203/GG_How_1995.pdf (accessed 2026-11-05)
[^s2]: Gigerenzer, G., Gaissmaier, W., Kurz-Milcke, E., Schwartz, L. M. & Woloshin, S. (2007). "Helping doctors and patients make sense of health statistics". *Psychological Science in the Public Interest* 8(2): 53-96. https://www.stat.berkeley.edu/~aldous/157/Papers/health_stats.pdf (accessed 2026-11-05)
[^s3]: Weber, P., Binder, K. & Krauss, S. (2018). "Why can only 24% solve Bayesian reasoning problems in natural frequencies: Frequency phobia in spite of probability blindness". *Frontiers in Psychology* 9: 1833. https://www.frontiersin.org/articles/10.3389/fpsyg.2018.01833/pdf (accessed 2026-11-05)
[^s4]: McDowell, M. & Jacobs, P. "When, why, and for whom are natural frequency formats most effective? A meta-analysis". Society for Medical Decision Making meeting abstract. https://smdm.confex.com/smdm/16BEC/webprogram/Paper9915.html (accessed 2026-11-05)
[^s5]: Sirota, M., Navarrete, G. & Juanchich, M. (2024). "When intuitive Bayesians need to be good readers: The problem-wording effect on Bayesian reasoning". *Cognition* 245: 105722. https://repository.essex.ac.uk/37751/1/1-s2.0-S0010027724000088-main.pdf (accessed 2026-11-05)
