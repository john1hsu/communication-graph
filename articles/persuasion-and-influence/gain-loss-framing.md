---
id: cm:gain-loss-framing
type: Technique
title: Gain-loss framing
aliases: [gain-framed and loss-framed messages, goal framing, gain versus loss message framing]
domain: persuasion-and-influence
summary: >-
  Choosing whether to present a recommendation in terms of what the audience gains by acting
  (a gain frame) or what it loses by not acting (a loss frame). Popular advice says loss frames
  persuade more, but meta-analyses find the choice of frame alone makes little or no difference.
level: intermediate
evidenceStatus: contested
broader: [cm:persuasion]
related: [cm:refutational-two-sided-messages, cm:elaboration-likelihood-model, cm:risk-numbers-as-natural-frequencies, cm:okeefe-hoeken-2021, cm:daniel-kahneman, cm:cognitive-bias]
requires: [cm:audience-analysis]
relations:
  - {predicate: challengedBy, object: cm:okeefe-jensen-2007, source: s3, confidence: high}
  - {predicate: challengedBy, object: cm:okeefe-wu-2012, source: s5, confidence: high}
  - {predicate: supportedBy, object: cm:gallagher-updegraff-2012, source: s4, confidence: medium}
  - {predicate: influencedBy, object: cm:amos-tversky, source: s2, confidence: medium}
  - {predicate: contrastsWith, object: cm:attribute-framing, source: s2, confidence: medium}
  - {predicate: develops, object: cm:persuasion, source: s6, confidence: low}
steps:
  - Write the core consequence of your recommendation once, as a plain fact with numbers - what changes, for whom, by how much, by when.
  - Draft it both ways - what the audience gains by acting and what it loses by not acting - and check that the two versions describe the same facts at the same size.
  - Pick the frame that fits your audience's actual decision (protecting something they already have, or adding something new), and say the other side once so the trade-off is visible.
  - Spend most of your effort on the substance - evidence, cost, risk and the objections you expect - not on the wording of the frame.
  - Where the message goes to many people and the stakes are real, test the two versions on a small group before deciding, rather than assuming loss frames win.
example:
  situation: An operations lead wants budget for automated nightly backups of the team's shared drive and is writing to the department head.
  before: "If we don't fix our backups, we could lose everything overnight, and it will be on all of us. We can't afford to wait."
  after: "With nightly automated backups, any file can be restored to the previous day's version within an hour. Today, a failed drive would cost us up to a week of rework, as it did in March. Setup is about two days of IT time and a small monthly storage fee."
  why: The first version leans on an exaggerated loss frame and gives the reader nothing to weigh. The rewrite states the gain and the loss at their real size, with cost, so the case rests on its substance - which matters more than the frame, since meta-analyses find the frame alone adds little.
selfCheck:
  - Do my gain and loss statements describe the same facts at the same size, or have I inflated one side?
  - Am I relying on "people hate losses" to do work my evidence should be doing?
  - Would my audience feel misled if they saw the other framing of the same numbers?
  - Have I stated the cost of acting, not only the cost of doing nothing?
sameAs: []
sources:
  - id: s1
    title: "The framing of decisions and the psychology of choice"
    publisher: Amos Tversky & Daniel Kahneman, Science 211(4481), 453-458, 1981, doi:10.1126/science.7455683 (NC State University course copy)
    url: https://www.csc2.ncsu.edu/faculty/mpsingh/local/Social/f24/wrap/readings/Tversky+Kahneman-framing-1981.pdf
    type: primary
    accessed: 2026-11-15
  - id: s2
    title: "All Frames Are Not Created Equal: A Typology of Framing Effects"
    publisher: Irwin P. Levin, Sandra L. Schneider & Gary J. Gaeth, Organizational Behavior and Human Decision Processes 76(2), 149-188, 1998, doi:10.1006/obhd.1998.2804 (University of South Florida Digital Commons)
    url: https://digitalcommons.usf.edu/psy_facpub/1886/
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s3
    title: "The relative persuasiveness of gain-framed and loss-framed messages for encouraging disease prevention behaviors: a meta-analytic review"
    publisher: Daniel J. O'Keefe & Jakob D. Jensen, Journal of Health Communication, 2007, PMID 17934940 (Read by QxMD abstract page)
    url: https://read.qxmd.com/read/17934940/the-relative-persuasiveness-of-gain-framed-and-loss-framed-messages-for-encouraging-disease-prevention-behaviors-a-meta-analytic-review
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s4
    title: "Health Message Framing Effects on Attitudes, Intentions, and Behavior: A Meta-analytic Review"
    publisher: Kristel M. Gallagher & John A. Updegraff, Annals of Behavioral Medicine 43, 101-116, 2012, doi:10.1007/s12160-011-9308-7
    url: https://link.springer.com/content/pdf/10.1007/s12160-011-9308-7.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s5
    title: "Gain-Framed Messages Do Not Motivate Sun Protection: A Meta-Analytic Review of Randomized Trials Comparing Gain-Framed and Loss-Framed Appeals for Promoting Skin Cancer Prevention"
    publisher: Daniel J. O'Keefe & Daisy Wu, International Journal of Environmental Research and Public Health 9(6), 2121-2133, 2012, doi:10.3390/ijerph9062121
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC3397368
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s6
    title: "Normatively Responsible Advocacy: Some Provocations from Persuasion Effects Research"
    publisher: Daniel J. O'Keefe, Proceedings of the International Society for the Study of Argumentation (ISSA) 2006, republished by Rozenberg Quarterly
    url: https://rozenbergquarterly.com/issa-proceedings-2006-normatively-responsible-advocacy-some-provocations-from-persuasion-effects-research/?print=pdf
    type: primary
    accessed: 2026-11-15
created: 2026-11-15
---

# Gain-loss framing

Gain-loss framing is the choice between presenting a recommendation as the advantages of doing what you propose (a gain frame: "backups let us restore any file within an hour") or the disadvantages of not doing it (a loss frame: "without backups, a failed drive costs us a week").[^s6] Both versions carry the same underlying consideration, which is why persuasion researchers treat the choice as a matter of presentation rather than substance.[^s6] Levin and colleagues classify it as *goal framing*: the type of valence framing that bears on how persuasive a communication is.[^s2]

## Origin

The idea grew out of Amos Tversky and Daniel Kahneman's 1981 paper in *Science*. In their "Asian disease" problem, 72% of 152 respondents chose a sure option when it was described as saving 200 of 600 people, but 78% of a second group of 155 chose the gamble when the same outcomes were described as deaths.[^s1] They argued that the way a problem is worded shapes the decision frame people adopt, and that this produces predictable reversals of preference.[^s1] Popular advice later turned this, and the related idea that losses weigh more than gains, into a rule of thumb: tell people what they stand to lose. In 1998 Irwin Levin, Sandra Schneider and Gary Gaeth showed that "framing" had been used for three different things - risky choice framing, attribute framing and goal framing - and that these tap different processes, which helps explain why findings about framing seemed to conflict.[^s2]

## Why it matters

Every proposal, status update or change announcement at work comes with this choice, often made by habit. Getting it wrong is rarely about the frame itself. The common failure is believing the loss frame will do the persuading, then exaggerating the loss to make it bite. Daniel O'Keefe notes that frames can sway audiences in ways they do not notice and would not endorse, which is why a frame chosen to hide the real size of a risk crosses an ethical line.[^s6] Knowing that the frame matters less than folklore claims lets you put your effort where it pays: evidence, cost and the objections your reader will raise.[^s3][^s4]

## How to apply it

Start by writing the consequence of your recommendation as a plain fact with numbers, then draft it as a gain and as a loss and check the two match.[^s6] Choose whichever frame reads most naturally for the decision - the research gives no reliable reason to prefer one in general - and mention the other side once so the trade-off is visible.[^s3][^s4] When a message goes to many people - a policy change, a safety reminder, an enrolment campaign - test both versions on a small group instead of assuming a winner, because the meta-analytic averages hide wide variation between topics.[^s3][^s5]

**Where the ethical line is.** Choosing between two honest and equivalent descriptions is ordinary message design. Inflating a loss, dropping the cost of acting, or picking the frame because the audience will not notice the switch moves into manipulation.[^s6]

## Common mistakes

- **Treating "losses loom larger" as a law of persuasion.** The risky-choice findings of Tversky and Kahneman do not transfer directly to goal-framed messages.[^s1][^s2]
- **Unequal frames.** O'Keefe points out that gain and loss versions are often not logically equivalent conditionals, so one quietly claims more than the other.[^s6]
- **Fear in place of facts.** A vivid loss with no magnitude, cost or evidence gives a careful reader nothing to weigh, and the frame alone is not where persuasive force lies.[^s3][^s5]
- **Ignoring the topic.** In health research the small advantage that appeared for gain frames was concentrated in particular behaviours, such as dental hygiene, rather than spread evenly.[^s3][^s4]

## Evidence

The evidence is rated contested because popular advice outruns it. O'Keefe and Jensen's 2007 meta-analysis of 93 studies (N = 21,656) found gain frames only slightly more persuasive for disease prevention (r = .03), an edge driven mainly by dental hygiene messages; safer sex, skin cancer and diet messages showed no difference.[^s3] Gallagher and Updegraff's 2012 review of 94 studies found a small gain-frame advantage for prevention behaviour (r = .083) but no framing effect on attitudes or intentions, and none for detection behaviours such as screening.[^s4] O'Keefe and Wu's 2012 meta-analysis of 33 skin-cancer trials (4,168 participants) found no significant difference (r = -.020), with high statistical power.[^s5] Nearly all of this research tested health messages, so workplace effects are inferred rather than measured.[^s3][^s4]

## Connections

Gain-loss framing is a narrower choice within **persuasion** (`cm:persuasion`); O'Keefe treats it as one of the presentational devices advocates use, and Levin and colleagues class it as goal framing.[^s6][^s2] It is **challenged by O'Keefe and Jensen 2007** (`cm:okeefe-jensen-2007`) and **O'Keefe and Wu 2012** (`cm:okeefe-wu-2012`), whose meta-analyses found little or no persuasive difference between frames,[^s3][^s5] and only weakly **supported by Gallagher and Updegraff 2012** (`cm:gallagher-updegraff-2012`), which found a small gain-frame edge for prevention behaviour.[^s4] It is **influenced by Amos Tversky** (`cm:amos-tversky`), whose risky-choice framing work with Kahneman Levin and colleagues took as the starting point for the typology,[^s2][^s1] and it **contrasts with attribute framing** (`cm:attribute-framing`), which changes how a single feature is evaluated rather than how persuasive an appeal is.[^s2] Refutational two-sided messages and presenting risk as natural frequencies are related ways to make a case honestly with the same facts.[^s6]

## Sources

[^s1]: Tversky & Kahneman, "The framing of decisions and the psychology of choice", Science (1981). https://www.csc2.ncsu.edu/faculty/mpsingh/local/Social/f24/wrap/readings/Tversky+Kahneman-framing-1981.pdf (accessed 2026-11-15)
[^s2]: Levin, Schneider & Gaeth, "All Frames Are Not Created Equal: A Typology of Framing Effects", Organizational Behavior and Human Decision Processes (1998). https://digitalcommons.usf.edu/psy_facpub/1886/ (accessed 2026-11-15)
[^s3]: O'Keefe & Jensen, "The relative persuasiveness of gain-framed and loss-framed messages for encouraging disease prevention behaviors: a meta-analytic review", Journal of Health Communication (2007). https://read.qxmd.com/read/17934940/the-relative-persuasiveness-of-gain-framed-and-loss-framed-messages-for-encouraging-disease-prevention-behaviors-a-meta-analytic-review (accessed 2026-11-15)
[^s4]: Gallagher & Updegraff, "Health Message Framing Effects on Attitudes, Intentions, and Behavior: A Meta-analytic Review", Annals of Behavioral Medicine (2012). https://link.springer.com/content/pdf/10.1007/s12160-011-9308-7.pdf (accessed 2026-11-15)
[^s5]: O'Keefe & Wu, "Gain-Framed Messages Do Not Motivate Sun Protection...", International Journal of Environmental Research and Public Health (2012). https://pmc.ncbi.nlm.nih.gov/articles/PMC3397368 (accessed 2026-11-15)
[^s6]: O'Keefe, "Normatively Responsible Advocacy: Some Provocations from Persuasion Effects Research", ISSA Proceedings (2006). https://rozenbergquarterly.com/issa-proceedings-2006-normatively-responsible-advocacy-some-provocations-from-persuasion-effects-research/?print=pdf (accessed 2026-11-15)
