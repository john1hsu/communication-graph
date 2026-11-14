---
id: cm:premortem
type: Technique
title: Premortem
aliases: [pre-mortem, project premortem, pre-mortem meeting]
domain: meetings-and-facilitation
summary: >-
  A short meeting exercise, usually run at a project kickoff, in which the leader tells the team
  to imagine the plan has already failed and each person writes down, then shares, the reasons why.
  It makes raising doubts the expected contribution instead of a disloyal one, so risks and
  warnings reach the decision maker before the commitment is locked in.
level: introductory
evidenceStatus: mixed
broader: [cm:facilitation, cm:group-decision-making]
related: [cm:devils-advocacy, cm:psychological-safety, cm:nominal-group-technique, cm:brainstorming, cm:workplace-meetings, cm:upward-dissent, cm:status-reporting, cm:escalation-of-commitment]
requires: [cm:facilitation]
relations:
  - {predicate: introducedBy, object: cm:gary-klein, source: s1, confidence: high}
  - {predicate: addresses, object: cm:employee-silence, source: s1, confidence: medium}
  - {predicate: addresses, object: cm:groupthink, source: s2, confidence: medium}
  - {predicate: addresses, object: cm:deaf-effect, source: s2, confidence: low}
  - {predicate: appliedIn, object: cm:group-decision-making, source: s3, confidence: high}
  - {predicate: demonstratedBy, object: cm:veinott-klein-wiggins-2010, source: s1, confidence: medium}
steps:
  - Schedule it once the plan is clear but before anything is signed, announced or funded, and invite the people who will do the work, not only the planners.
  - Briefly restate the plan, then say it as a certainty - "it is a year from now and this project has failed" - rather than asking whether it might fail.
  - Give everyone two to three minutes to write, silently and alone, every reason they can think of for the failure.
  - Go around the room taking one reason per person per round until the lists are exhausted, with the leader going first and offering a real weakness of their own plan.
  - Record every reason where all can see it without debating or defending, and stop anyone senior from dominating the round.
  - Rate the reasons for likelihood and impact, assign owners to the top few, and change, test or monitor the plan accordingly.
  - Send a short note of what was raised and what will change, so people see that their warnings were heard and acted on.
example:
  situation: A team lead is kicking off a migration of the company's billing system to a new platform, with a go-live date already promised to finance.
  before: "So that's the plan - we go live on 1 March. It's tight but I'm confident. Anyone see any problems? No? Great, let's get started."
  after: "Before we start, imagine it's April and the migration has failed badly. Take three minutes and write down every reason why - on your own. Then we'll go round one at a time; I'll go first: I think I've underestimated how long finance will need to sign off the test invoices."
  why: An open call for problems from a confident leader invites silence; declaring the failure as fact, writing alone first and having the leader model candor makes naming risks the task everyone is doing, so the doubts surface while the plan can still change.
selfCheck:
  - Am I running this before the decision is locked in, or only to look thorough after it is?
  - Did I state the failure as certain and give people time to write on their own before anyone spoke?
  - Did I go first with a real weakness in my own plan, and did I keep myself and other senior people from defending the plan during the round?
  - Which reasons changed the plan, and have I told the team what we are doing about them?
  - Is there someone who raised a concern quietly afterwards because the meeting still did not feel safe enough?
sameAs: ["https://github.com/john1hsu/critical-thinking-graph/id/premortem"]
sources:
  - id: s1
    title: "The Pre-Mortem Method"
    publisher: Gary Klein, Seeing What Others Don't (Psychology Today blog), 14 January 2021
    url: https://www.psychologytoday.com/ie/blog/seeing-what-others-dont/202101/the-pre-mortem-method
    type: primary
    accessed: 2026-11-14
  - id: s2
    title: "Pre-empting project failure by using a pre-mortem"
    publisher: Mills, J. K. A. & McKimm, J., British Journal of Hospital Medicine 78(10), 584-585, 2017 (publisher PDF)
    url: https://storage.imrpress.com/IMR/hmed/application/10.12968/hmed.2017.78.10.584.pdf
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s3
    title: "Improving Planning: Quantitative Evaluation of the Premortem Technique in Field and Laboratory Settings"
    publisher: Peabody, MS thesis, Michigan Technological University, 2017 (CORE record)
    url: https://core.ac.uk/works/49608374
    type: academic
    accessed: 2026-11-14
  - id: s4
    title: "How to Catch a Black Swan: Measuring the Benefits of the Premortem Technique for Risk Identification"
    publisher: George Washington University, electronic thesis/dissertation (ScholarSpace record)
    url: https://scholarspace.library.gwu.edu/concern/gw_etds/5712m6681
    type: academic
    accessed: 2026-11-14
  - id: s5
    title: "An Examination of the Deaf Effect Response to Bad News Reporting in Information Systems Projects"
    publisher: Cuellar, M. J., doctoral dissertation, Georgia State University, 2009
    url: https://scholarworks.gsu.edu/cis_diss/32
    type: primary
    accessed: 2026-11-14
created: 2026-11-14
---

# Premortem

A premortem is a short exercise for the start of a project or decision. The leader tells the team the plan has already failed, and each person writes down, then shares, why it failed.[^s1] The result is a list of "showstoppers" the team can fix while the plan can still change.[^s1] As a communication tool, its point is to make it normal, even expected, to say "this could go wrong" to the person who owns the plan.[^s1][^s2]

## Origin

The research psychologist Gary Klein says he developed the premortem about 30 years before his 2021 account, to cut down on problems in his own company's projects.[^s1] The idea draws on "prospective hindsight": imagining that an outcome has already happened. A 1989 study by Mitchell, Russo and Pennington is widely cited, for example by Mills and McKimm, as finding that this raises people's ability to identify reasons for an outcome by about 30%.[^s2] That figure is a second-hand summary of one study, so treat it as illustrative rather than as a reliable effect size.[^s2]

## Why it matters

Kickoff meetings usually end with a confident plan and a question like "Anyone see any problems?" In that setting there is quiet pressure not to raise doubts that would spoil the mood, so concerns stay unspoken.[^s1] Mills and McKimm describe the same pull toward consensus, where dissenters hold back, and note that leaders' overconfidence can lead them to dismiss alternatives.[^s2] Overconfidence matters for the listener too. Cuellar's experiments found decision makers were more likely to treat bad news as irrelevant when they felt in control and saw the risk of failure as low.[^s5] The premortem works on both sides at once. People are asked for reasons the plan failed, so naming problems becomes the task rather than an attack on the leader.[^s1] The leader has to hear those reasons before committing.[^s2]

## How to apply it

Klein's version is simple. After the team has discussed the plan, the leader announces that the project has failed, framed as certain rather than possible. Each member then spends two minutes writing down reasons.[^s1] The facilitator goes round the room taking one reason at a time and records them on a whiteboard. Klein recommends that the team leader goes first, to model candor, and that no senior person is allowed to dominate.[^s1] Later refinements add a second short round in which members propose actions for some of the risks. Teams also rate each problem for likelihood, impact and how easily it could be prevented.[^s1] Mills and McKimm suggest SWOT or risk-analysis prompts to widen the search.[^s2]

Channel and seniority change the details. In a hybrid or remote meeting, keep the silent writing step by having people type into a private note or form before anything is shared; the point, as in the room, is that no senior voice sets the agenda first.[^s1] The 2017 Michigan Tech experiments also found that groups produced more solutions than individuals, so a premortem done alone is a weaker substitute.[^s3] For an executive sponsor, a premortem gives a sanctioned, low-cost moment to hear warnings that might otherwise arrive late as escalations.[^s2][^s5]

## Common mistakes

- **Asking "what could go wrong?"** Klein's method relies on stating failure as a fact, not a possibility.[^s1]
- **Skipping the solo writing.** Talking first lets the loudest or most senior person set the agenda, which the method warns against.[^s1]
- **Defending the plan during the round.** If the owner rebuts each point, people learn that doubts are still unwelcome.[^s1][^s2]
- **Running it after the decision is locked.** Its value is in changing the plan before failure, not documenting it.[^s2]
- **Collecting risks and doing nothing.** The list of showstoppers is only useful if owners act on it.[^s1] Mills and McKimm also note the opposite cost: time and money spent on risks that never happen.[^s2]

## Evidence

The evidence is encouraging but thin, so `mixed` fits. In a 2010 study Klein describes, Veinott, Klein and Wiggins asked 178 college students to evaluate a plan for responding to an H1N1 outbreak. The premortem reduced overconfidence more than a simple critique or a pros-and-cons list.[^s1] A 2017 Michigan Tech thesis ran three experiments. Army cadet teams using a premortem had fewer fouls and less fixation than teams using a standard military review. Against a worst-case-scenario method it produced more reasons in one experiment but not in another, and it changed the kinds of reasons people raised.[^s3] A George Washington University dissertation compared premortems with brainstorming for a technology upgrade and found the premortem did better on three of its hypothesis tests.[^s4] These are small studies, mostly student or single-setting samples, run partly by the method's developer and his colleagues. No large independent replication was found this run. The claim that a premortem reduces the deaf effect is an inference from these mechanisms, not something tested directly.[^s2][^s5]

## Connections

- **Introduced by** Gary Klein, who developed the method for his own company's projects and has written about it since.[^s1]
- **Addresses** employee silence: it reverses the quiet pressure not to surface doubts at kickoffs.[^s1] It **addresses** groupthink by giving a safe setting for concerns that consensus pressure would suppress.[^s2] It plausibly **addresses** the deaf effect, because it checks the leader overconfidence that Cuellar found makes warnings easier to ignore.[^s2][^s5]
- **Applied in** group decision making: the 2017 experiments tested it on teams and individuals evaluating plans.[^s3]
- **Demonstrated by** Veinott, Klein and Wiggins's 2010 H1N1 planning study.[^s1]
- **Broader:** facilitation and group decision making. **Requires** basic facilitation, since the round only works if someone keeps senior voices from dominating.[^s1]
- **Related:** devil's advocacy is another way to build challenge into a decision, and it outperformed ordinary brainstorming for risk identification in one dissertation study.[^s4] The nominal group technique shares its silent-writing and round-robin steps.[^s1] Psychological safety, upward dissent and status reporting are the conditions and habits that let the warnings keep flowing after kickoff, and escalation of commitment is what happens when they are not heard.[^s2][^s5]

## Sources

[^s1]: Klein, G. (2021). "The Pre-Mortem Method". *Seeing What Others Don't*, Psychology Today, 14 January 2021. https://www.psychologytoday.com/ie/blog/seeing-what-others-dont/202101/the-pre-mortem-method (accessed 2026-11-14)
[^s2]: Mills, J. K. A. & McKimm, J. (2017). "Pre-empting project failure by using a pre-mortem". *British Journal of Hospital Medicine* 78(10), 584-585. https://storage.imrpress.com/IMR/hmed/application/10.12968/hmed.2017.78.10.584.pdf (accessed 2026-11-14)
[^s3]: Peabody (2017). *Improving Planning: Quantitative Evaluation of the Premortem Technique in Field and Laboratory Settings*. MS thesis, Michigan Technological University. https://core.ac.uk/works/49608374 (accessed 2026-11-14)
[^s4]: "How to Catch a Black Swan: Measuring the Benefits of the Premortem Technique for Risk Identification". Electronic thesis/dissertation, George Washington University. https://scholarspace.library.gwu.edu/concern/gw_etds/5712m6681 (accessed 2026-11-14)
[^s5]: Cuellar, M. J. (2009). *An Examination of the Deaf Effect Response to Bad News Reporting in Information Systems Projects*. Doctoral dissertation, Georgia State University. https://scholarworks.gsu.edu/cis_diss/32 (accessed 2026-11-14)
