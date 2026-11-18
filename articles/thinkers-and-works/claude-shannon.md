---
id: cm:claude-shannon
type: Person
title: Claude Shannon
aliases: [Claude E. Shannon, Claude Elwood Shannon, father of information theory]
domain: thinkers-and-works
summary: >-
  American mathematician and Bell Labs engineer (1916-2001) whose 1948 paper "A Mathematical
  Theory of Communication" founded information theory and supplied the source-transmitter-channel-
  noise-receiver diagram behind the linear model that opens textbook accounts of communication; he later warned
  against stretching that theory to human affairs without testing it.
level: introductory
evidenceStatus: historical
broader: []
related: [cm:shannon-weaver-model, cm:warren-weaver, cm:norbert-wiener, cm:communication-models, cm:feedback, cm:transactional-model-of-communication, cm:channel-selection, cm:common-ground]
requires: []
relations:
  - {predicate: authored, object: cm:a-mathematical-theory-of-communication, source: s1, confidence: high}
  - {predicate: introduced, object: cm:information-theory, source: s3, confidence: high}
  - {predicate: introduced, object: cm:communication-models, source: s5, confidence: medium}
  - {predicate: influencedBy, object: cm:harry-nyquist, source: s1, confidence: high}
  - {predicate: influencedBy, object: cm:ralph-hartley, source: s1, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "A Mathematical Theory of Communication"
    publisher: Claude E. Shannon, The Bell System Technical Journal 27, 379-423 and 623-656 (July and October 1948) (Yale University course copy)
    url: https://www.cs.yale.edu/homes/yry/readings/general/shannon1948.pdf
    type: primary
    accessed: 2026-11-18
  - id: s2
    title: "The Bandwagon"
    publisher: Claude E. Shannon, IRE Transactions on Information Theory (1956), p. 3 (scanned copy hosted by gwern.net)
    url: https://www.Gwern.net/doc/cs/algorithm/1956-shannon.pdf
    type: primary
    accessed: 2026-11-18
  - id: s3
    title: "Claude Shannon"
    publisher: Encyclopaedia Britannica (print version of biography article 538577)
    url: https://www.britannica.com/print/article/538577
    type: encyclopedia
    accessed: 2026-11-18
  - id: s4
    title: "The Mathematics of Communication"
    publisher: Warren Weaver, Scientific American 181(1), 11-15 (July 1949) (archive copy)
    url: https://mt-archive.net/50/SciAm-1949-Weaver.pdf
    type: primary
    accessed: 2026-11-18
  - id: s5
    title: "Chapter 4: Traditional Models of Human Communication"
    publisher: Jessica Gasiorek and R. Kelly Aune, Message Processing - The Science of Creating Understanding, University of Hawai'i OER Pressbooks (CC BY 4.0)
    url: https://pressbooks.oer.hawaii.edu/messageprocessing/?p=56
    type: textbook
    accessed: 2026-11-18
  - id: s6
    title: "Models of Communication"
    publisher: Lisa Schreiber and Morgan Hartranft, Principles of Public Speaking, Millersville University via Lumen Learning (CC BY-NC-ND 4.0)
    url: https://courses.lumenlearning.com/publicspeakingprinciples/?p=354
    type: textbook
    accessed: 2026-11-18
created: 2026-11-18
---

# Claude Shannon

Claude Shannon was an American mathematician and electrical engineer whose 1948 paper "A Mathematical Theory of Communication" established the basic results of information theory and supplied the diagram behind the linear model with which textbook accounts of communication models begin.[^s3][^s5][^s6] He was not studying conversation: his problem was how to send signals accurately over telephone, radio and other channels.[^s1] But the five-box diagram he drew for that problem, borrowed by Warren Weaver and later by communication scholars, gave the field its standard vocabulary of sender, message, channel, noise and receiver.[^s4][^s5][^s6]

## Origin

Shannon was born in Petoskey, Michigan, in 1916 and died in Medford, Massachusetts, in 2001.[^s3] He took bachelor's degrees in mathematics and electrical engineering at the University of Michigan, then a master's and a PhD at MIT; his master's thesis used Boolean algebra to lay the theoretical basis of digital switching circuits.[^s3] He joined the mathematics department of Bell Telephone Laboratories in 1941, stayed affiliated until 1972, and became a permanent MIT faculty member in 1958.[^s3]

The 1948 paper built on earlier Bell Labs work by Harry Nyquist and Ralph Hartley, extending it to include channel noise and the statistical structure of messages.[^s1][^s3] Its Figure 1 shows an information source that produces a message, a transmitter that turns it into a signal, a channel that carries it, a noise source that disturbs it, a receiver that reconstructs the message, and a destination.[^s1] The paper also contains what appears to be the first published use of "bit", a word Shannon credited to his colleague J. W. Tukey.[^s1][^s3] Shannon deliberately set meaning aside, writing that the semantic side of communication was irrelevant to the engineering problem.[^s1]

## How his model reached workplace communication

Weaver's 1949 *Scientific American* essay mapped Shannon's diagram onto ordinary speech: the speaker's brain is the source, the vocal system the transmitter, air the channel, the listener's ear the receiver and the listener's brain the destination.[^s4] Weaver also split communication problems into three levels - technical (did the symbols arrive accurately?), semantic (was the intended meaning understood?) and effectiveness (did the meaning change conduct as intended?) - and sketched a "semantic noise" box for distortions of meaning the speaker adds.[^s4] That expanded version, published with Shannon's paper as a 1949 book, became the linear model taught in communication textbooks and the starting point that later interactive and transactional models revised.[^s5][^s6]

## Why it matters

Shannon's diagram is still a useful checklist for diagnosing a message that failed, as long as you keep Weaver's three levels apart.[^s1][^s4]

- **Technical level:** did the message actually reach the person, intact and on a channel they monitor? A buried attachment, a muted chat channel or a bad call line is noise in Shannon's original sense.[^s1][^s4]
- **Semantic level:** did they decode the meaning you intended? Jargon and ambiguous wording are semantic noise, which no amount of resending fixes.[^s4]
- **Effectiveness level:** did they do what you needed? A message can arrive and be understood and still not change behaviour.[^s4]

A workplace example. Before: a team lead posts a changed release date once in a busy chat channel, and when two teams miss it, she reposts the same message louder. After: she checks which level failed - one team never saw the post (technical), the other read "freeze on the 12th" as a code freeze rather than a release date (semantic) - and responds with a direct message to the first team and a reworded definition for the second. Why: separating delivery from meaning tells you whether the fix is a better channel or clearer words.[^s1][^s4]

## Evidence and limits

Shannon's work is mathematics, not a psychological finding, so it is rated historical here; its value for communicators is as a diagnostic frame. Shannon himself pushed back on the rush to apply it everywhere: in his 1956 editorial "The Bandwagon" he warned that information theory was being oversold, that importing its terms into psychology or the social sciences was no panacea, and that whether a human behaves like an ideal decoder is a question for experiments rather than definitions.[^s2][^s3] Textbook critics make a related point about the linear model built from his diagram: much human communication is not a single one-way transmission, and the model assumes a message has a fixed meaning shared by both sides, which is why later models added feedback, context and joint meaning-making.[^s5][^s6]

## Connections

- **Authored** "A Mathematical Theory of Communication" (1948), the paper that defined the source-channel-noise-receiver system.[^s1]
- **Introduced** information theory, and through the diagram Weaver popularised, the family of **communication models** that begins with the linear model.[^s3][^s5]
- **Influenced by** Harry Nyquist and Ralph Hartley, whose Bell Labs papers he named as the basis of his theory.[^s1]
- **Related:** the Shannon-Weaver model and Warren Weaver, who extended the diagram to meaning and effect; Norbert Wiener, whose feedback loop the later interactive models added; and the transactional model that replaced one-way transmission with jointly built meaning.[^s4][^s5][^s6]

## Sources

[^s1]: Claude E. Shannon, "A Mathematical Theory of Communication", The Bell System Technical Journal (1948). https://www.cs.yale.edu/homes/yry/readings/general/shannon1948.pdf (accessed 2026-11-18)
[^s2]: Claude E. Shannon, "The Bandwagon", IRE Transactions on Information Theory (1956). https://www.Gwern.net/doc/cs/algorithm/1956-shannon.pdf (accessed 2026-11-18)
[^s3]: Encyclopaedia Britannica, "Claude Shannon". https://www.britannica.com/print/article/538577 (accessed 2026-11-18)
[^s4]: Warren Weaver, "The Mathematics of Communication", Scientific American (July 1949). https://mt-archive.net/50/SciAm-1949-Weaver.pdf (accessed 2026-11-18)
[^s5]: Gasiorek and Aune, "Chapter 4: Traditional Models of Human Communication", Message Processing. https://pressbooks.oer.hawaii.edu/messageprocessing/?p=56 (accessed 2026-11-18)
[^s6]: Schreiber and Hartranft, "Models of Communication", Principles of Public Speaking. https://courses.lumenlearning.com/publicspeakingprinciples/?p=354 (accessed 2026-11-18)
