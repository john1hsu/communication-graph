---
id: cm:audience-analysis
type: Technique
title: Audience analysis
aliases: [know your audience, reader analysis, audience profiling]
domain: foundations
summary: >-
  The practice of working out, before you write or speak, who will receive a message, what they
  already know, what they care about and what they need to do with it, and then shaping the
  content, structure, tone and channel to fit them.
level: introductory
evidenceStatus: practitioner
broader: [cm:audience]
related: [cm:plain-language, cm:curse-of-knowledge, cm:stakeholder-mapping, cm:bottom-line-up-front, cm:channel-selection]
requires: []
relations:
  - {predicate: addresses, object: cm:curse-of-knowledge, source: s3, confidence: medium}
  - {predicate: appliedIn, object: cm:email, source: s3, confidence: high}
  - {predicate: explainedBy, object: cm:audience-design, source: s4, confidence: medium}
  - {predicate: influencedBy, object: cm:aristotles-rhetoric, source: s6, confidence: medium}
  - {predicate: introducedIn, object: cm:aristotles-rhetoric, source: s6, confidence: medium}
steps:
  - List every audience, not just the addressee - the decision maker, technical reviewers, people who are copied, people the message may be forwarded to and people affected by the outcome.
  - For the primary audience, write down what they already know, what they care about, what attitude they are likely to bring and what they must decide or do after reading.
  - Check your assumptions against evidence - the questions people actually ask you, past replies, usage data or a short conversation with a typical reader.
  - Choose content, order, vocabulary, tone and channel to fit the primary audience, putting what matters to them first.
  - Give secondary audiences their own clearly labelled section instead of mixing material for different readers.
  - Reread the draft as each audience in turn - including someone it might be forwarded to - and fix what would confuse or alienate them.
example:
  situation: An engineering lead emails a delay notice about a data-platform migration to a list that includes the client's finance director.
  before: "Heads up - the ETL refactor slipped because the CDC connector kept OOMing on the backfill. New ETA is sprint 14, assuming infra gets us the bigger nodes."
  after: "Subject: Data migration finishing three weeks later than planned (no change to cost). The move to the new reporting system will finish on 4 December instead of 13 November. Your month-end reports will run on the old system as usual until then. Technical details for your IT team are in the section below."
  why: The finance director is the primary reader and needs the date, the impact on her work and the cost; the jargon and team shorthand move to a separate section for the technical secondary audience.
selfCheck:
  - Who will read or hear this - including people copied or forwarded to - and which of them is the one who must act?
  - What does my primary audience already know, and which of my terms or steps would they not recognise?
  - What is in this for them, and do they see it in the first few lines?
  - Have I checked my picture of the audience against something they actually said or did, or am I only guessing?
sameAs: []
sources:
  - id: s1
    title: "Audience Analysis: Overview"
    publisher: Purdue Online Writing Lab (Purdue University)
    url: https://owl.purdue.edu/owl/subject_specific_writing/professional_technical_writing/audience_analysis
    type: academic
    accessed: 2026-11-03
  - id: s2
    title: "Write for your reader"
    publisher: Digital.gov Plain Language Guide Series (U.S. General Services Administration)
    url: https://digital.gov/guides/plain-language/principles/write-for-reader
    type: government
    accessed: 2026-11-03
  - id: s3
    title: "3 Audience"
    publisher: Olds College OER Development Team, Professional Communications Open Curriculum (eCampusOntario Pressbooks, CC BY 4.0)
    url: https://ecampusontario.pressbooks.pub/profcommsontario/chapter/getting-to-know-your-audience/
    type: textbook
    accessed: 2026-11-03
  - id: s4
    title: "Audience design in meaning and reference"
    publisher: Clark & Murphy, in Le Ny & Kintsch (eds.), Language and Comprehension, North-Holland, 1982, pp. 287-299 (author's copy, Stanford)
    url: https://web.stanford.edu/~clark/1980s/Clark,%20H.H.%20&%20Murphy,%20G.L.%20_Audience%20design%20in%20meaning%20and%20reference_%201982.pdf
    type: primary
    accessed: 2026-11-03
  - id: s5
    title: "Speaker-external versus speaker-internal forces on utterance form: Do cognitive demands override threats to referential success?"
    publisher: Lane & Ferreira, Journal of Experimental Psychology - Learning, Memory, and Cognition 34(6), 2008 (PubMed Central)
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC2654616
    type: peer-reviewed
    accessed: 2026-11-03
  - id: s6
    title: "Aristotle's Rhetoric"
    publisher: Christof Rapp, Stanford Encyclopedia of Philosophy (Spring 2026 edition; substantive revision 2022)
    url: https://plato.stanford.edu/archives/spr2026/entries/aristotle-rhetoric/
    type: scholarly-encyclopedia
    accessed: 2026-11-03
created: 2026-11-03
modified: 2026-11-03
---

# Audience analysis

Audience analysis is the deliberate step of finding out who will receive a message and what they need from it before deciding what to say and how. Purdue's Online Writing Lab describes it as gathering as much information as you can about your readers so the document can be user-centred, and notes that one document often has several audiences with different needs.[^s1] In practice it answers a short set of questions: who receives the message, what they already know, what is in it for them, what attitude and setting they bring, what information they need and what they expect.[^s3]

## Origin

The idea that a speaker must fit the message to the listener is ancient. In Aristotle's *Rhetoric*, the kinds of public speech are defined partly by what the audience has to judge (a future policy, a past act), and Book II analyses the emotions and typical characters of listeners - the young, the old, the wealthy, the powerful - so that a speaker can anticipate how they will respond.[^s6] Modern professional-writing teaching turned this into a planning routine with named audience roles: Purdue's OWL distinguishes a primary reader who decides, secondary technical readers, a "shadow" audience of other readers and the stakeholders affected by the action that follows.[^s1] In psycholinguistics, Herbert Clark and Gregory Murphy (1982) gave the underlying behaviour a name, audience design: speakers shape each utterance for particular listeners based on the common ground they share.[^s4]

## Why it matters

Messages fail when they are written for the sender rather than the receiver. Federal plain-language guidance notes that readers want to know what applies to them, so writers should work out who their readers are, see the material from their side and tell them early why it matters to them.[^s2] Audience analysis is also how a writer catches the reader they forgot: a textbook case shows an executive's email that read well to its intended recipients but struck the wrong tone for copied and forwarded readers, and had to be rewritten.[^s3] The same message usually needs to change between a peer, a technical reviewer and an executive, and between a team presentation and a board meeting.[^s3]

## How to apply it

1. **Map every audience.** Start with the person who must act, then add technical reviewers, people on copy, likely forwards and the people affected by the decision.[^s1][^s3]
2. **Profile the primary reader.** Note their prior knowledge, interests, likely attitude, role and cultural background, and what they need to decide or do.[^s3]
3. **Use evidence, not intuition.** Review the questions people send you, ask readers what they need, and look at which pages or sections they actually use.[^s2]
4. **Shape the message.** Lead with what matters to the primary reader and choose words, tone and channel they will find natural.[^s2][^s3]
5. **Separate audiences.** When several groups read one document, give each its own section rather than blending material that confuses everyone.[^s2]
6. **Reread as each reader,** including the hidden audience who might see a forwarded copy.[^s3]

## Common mistakes

- **Analysing only the addressee.** Ignoring secondary and hidden readers is how sensitive or flippant wording reaches the wrong person.[^s1][^s3]
- **Profiling by demographics alone.** Age, role and education help, but what the reader already knows and what they must do with the message matter more.[^s3]
- **Assuming the analysis happens automatically.** Experiments on audience design show that speakers often let information only they know leak into what they say, especially when that information is salient to them.[^s5] Write the profile down instead of relying on a feeling that you know your reader.

## Evidence and limits

Audience analysis is long-standing expert practice in rhetoric and professional writing, but there is little direct testing of it as a method, so its status here is `practitioner`.[^s1][^s6] Research on the underlying behaviour supports both its value and its difficulty. Clark and Murphy argued that listeners interpret speech by assuming it was designed for them, using common ground built from community membership, shared experience and the conversation so far.[^s4] Yet in a 2008 series of four experiments, Lane and Ferreira found that speakers frequently described objects their partner could not see when that hidden information was relevant to the task, and partners then made errors on about a third of those descriptions; drawing speakers' attention to the hidden object made the leaks more common, not less.[^s5] The authors note their tasks were one-shot and non-interactive, and suggest live dialogue may reduce such failures.[^s5] The practical lesson is that adapting to an audience is effortful and fragile under load, which is why an explicit checklist and a check with real readers are worth the time.[^s2][^s5]

## Connections

- **Broader:** audience analysis is the working method behind the general concept of an audience - the people a message is for.[^s1]
- **Addresses the curse of knowledge:** asking explicitly what the reader already knows, and what information they still need, is a direct check on assuming they share your background.[^s3]
- **Applied in email:** the textbook's worked case uses primary, secondary and hidden audiences to rewrite a workplace email.[^s3]
- **Explained by audience design,** Clark and Murphy's account of how speakers tailor utterances to shared common ground.[^s4]
- **Introduced in, and influenced by, Aristotle's *Rhetoric*,** whose analysis of audience judgments, emotions and character types is an early systematic treatment of adapting to listeners.[^s6]
- **Related:** plain language treats writing for your audience as its first rule; stakeholder mapping extends the same thinking to who is affected by a decision; bottom line up front is one way to put what matters to the reader first.[^s2][^s1]

## Sources

[^s1]: Purdue Online Writing Lab. "Audience Analysis: Overview". Purdue University. https://owl.purdue.edu/owl/subject_specific_writing/professional_technical_writing/audience_analysis (accessed 2026-11-03)
[^s2]: Digital.gov (U.S. GSA). "Write for your reader". Plain Language Guide Series. https://digital.gov/guides/plain-language/principles/write-for-reader (accessed 2026-11-03)
[^s3]: Olds College OER Development Team. "3 Audience". *Professional Communications Open Curriculum*. eCampusOntario Pressbooks, CC BY 4.0. https://ecampusontario.pressbooks.pub/profcommsontario/chapter/getting-to-know-your-audience/ (accessed 2026-11-03)
[^s4]: Clark, H. H. & Murphy, G. L. (1982). "Audience design in meaning and reference". In J.-F. Le Ny & W. Kintsch (Eds.), *Language and Comprehension* (pp. 287-299). North-Holland. https://web.stanford.edu/~clark/1980s/Clark,%20H.H.%20&%20Murphy,%20G.L.%20_Audience%20design%20in%20meaning%20and%20reference_%201982.pdf (accessed 2026-11-03)
[^s5]: Lane, L. W. & Ferreira, V. S. (2008). "Speaker-external versus speaker-internal forces on utterance form: Do cognitive demands override threats to referential success?" *Journal of Experimental Psychology: Learning, Memory, and Cognition* 34(6), 1466-1481. https://pmc.ncbi.nlm.nih.gov/articles/PMC2654616 (accessed 2026-11-03)
[^s6]: Rapp, C. "Aristotle's Rhetoric". *Stanford Encyclopedia of Philosophy* (Spring 2026 edition). https://plato.stanford.edu/archives/spr2026/entries/aristotle-rhetoric/ (accessed 2026-11-03)
