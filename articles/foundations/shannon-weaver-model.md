---
id: cm:shannon-weaver-model
type: Theory
title: Shannon-Weaver model
aliases: [Shannon-Weaver model of communication, Shannon and Weaver's model, transmission model of communication, linear model of communication]
domain: foundations
summary: >-
  The linear model of communication drawn from Claude Shannon's 1948 information theory and
  popularised by Warren Weaver: a source's message is encoded by a transmitter into a signal, sent
  over a channel where noise can corrupt it, and decoded by a receiver for a destination; it is the
  basis of the sender-message-channel-receiver picture used in communication textbooks.
level: introductory
evidenceStatus: theoretical
broader: [cm:communication-models]
related: [cm:common-ground, cm:feedback, cm:channel-selection, cm:media-richness-theory, cm:clarity, cm:teach-back, cm:grices-maxims, cm:interpersonal-communication, cm:norbert-wiener, cm:plain-language]
requires: []
relations:
  - {predicate: introducedBy, object: cm:claude-shannon, source: s1, confidence: high}
  - {predicate: introducedBy, object: cm:warren-weaver, source: s2, confidence: high}
  - {predicate: introducedIn, object: cm:a-mathematical-theory-of-communication, source: s1, confidence: high}
  - {predicate: contrastsWith, object: cm:transactional-model-of-communication, source: s4, confidence: high}
  - {predicate: contrastsWith, object: cm:common-ground, source: s3, confidence: medium}
  - {predicate: complements, object: cm:feedback, source: s5, confidence: medium}
  - {predicate: studiedIn, object: cm:communication-studies, source: s3, confidence: high}
sameAs: []
sources:
  - id: s1
    title: "A Mathematical Theory of Communication"
    publisher: Claude E. Shannon, The Bell System Technical Journal 27, 379-423 and 623-656 (July and October 1948) (Yale University course copy)
    url: https://www.cs.yale.edu/homes/yry/readings/general/shannon1948.pdf
    type: primary
    accessed: 2026-11-11
  - id: s2
    title: "The Mathematics of Communication"
    publisher: Warren Weaver, Scientific American 181(1), 11-15 (July 1949) (archive copy)
    url: https://mt-archive.net/50/SciAm-1949-Weaver.pdf
    type: primary
    accessed: 2026-11-11
  - id: s3
    title: "Chapter 4: Traditional Models of Human Communication"
    publisher: R. Kelly Aune, in Gasiorek & Aune, Message Processing - The Science of Creating Understanding, University of Hawai'i OER Pressbooks (CC BY 4.0)
    url: https://pressbooks.oer.hawaii.edu/messageprocessing/?p=56
    type: textbook
    accessed: 2026-11-11
  - id: s4
    title: "1.2: The Communication Process"
    publisher: Communication in the Real World - An Introduction to Communication Studies, Social Sci LibreTexts (open textbook, CC BY-NC-SA 3.0)
    url: https://socialsci.libretexts.org/Bookshelves/Communication/Introduction_to_Communication/Communication_in_the_Real_World_-_An_Introduction_to_Communication_Studies/01%3A_Introduction_to_Communication_Studies/1.02%3A_The_Communication_Process
    type: textbook
    accessed: 2026-11-11
  - id: s5
    title: "Communication - Models of communication"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/communication/Models-of-communication
    type: encyclopedia
    accessed: 2026-11-11
created: 2026-11-11
---

# Shannon-Weaver model

The Shannon-Weaver model describes communication as a chain: an information source produces a message, a transmitter turns it into a signal, the signal travels over a channel, a receiver rebuilds the message from the signal, and the message reaches its destination; along the way a noise source can corrupt the signal.[^s1] Communication textbooks call this the transmission model and summarise it as a linear, one-way process in which a sender encodes a message and a receiver decodes it.[^s4] For people at work it is the simplest checklist for asking where a message could break: in the wording, in the medium, in the conditions around it, or in the reader's head.[^s4][^s5]

## Origin

Claude Shannon set out the five-part diagram in "A Mathematical Theory of Communication", published in two parts in the *Bell System Technical Journal* in July and October 1948.[^s1] His aim was an engineering one: getting a selected message from one point to another accurately. He stated plainly that the meaning of messages was irrelevant to that engineering problem, and treated noise as a random variable that alters the received signal.[^s1] Warren Weaver carried the work to a general audience. In a 1949 *Scientific American* article he split communication problems into three levels: the technical accuracy of transmission, the semantic question of whether the receiver takes the meaning the sender intended, and the effectiveness question of whether that meaning changes the receiver's conduct.[^s2] Weaver suggested adding a "semantic receiver" and "semantic noise", distortions of meaning that the source introduces, to Shannon's diagram.[^s2] Their work appeared together as *The Mathematical Theory of Communication* in 1949, and because Shannon himself set meaning aside, the human-communication reading that textbooks teach rests on Weaver's extension.[^s3][^s1][^s2] Later versions relabelled the parts as source, encoder, message, channel, decoder and receiver.[^s5]

## Why it matters

The model gives a shared vocabulary for diagnosing failed messages. Textbooks distinguish environmental noise, such as other people talking in a crowded room, from semantic noise, such as jargon or a word that means different things to different people.[^s4] Weaver's levels separate three questions a sender often blurs: did they get it, did they understand it as I meant it, and did it change what they do.[^s2] The model also explains why repetition helps. Weaver reported Shannon's estimate that English is about half redundant, which is why readers can correct a garbled word, and Britannica describes redundancy as the main safeguard against distortion in a message.[^s2][^s5] At work that justifies restating a deadline in the subject line and the body, or confirming a number in two forms.[^s5]

The model's main lesson for practitioners is also its blind spot. Because the receiver is an end point, the sender is left to presume the message was understood and carries most of the responsibility for getting it across.[^s4]

## How to use it at work

- **Walk the chain before an important message.** Ask where noise could enter: an ambiguous term (semantic), a noisy room or a weak call line (environmental), or the wrong medium for the content (channel).[^s4][^s5]
- **Separate Weaver's three levels.** Delivery, understanding and action are different outcomes; a read receipt proves only the first.[^s2]
- **Add deliberate redundancy where errors are costly.** Repeat the key figure, date or owner, or show it in a second form, such as a table plus a sentence.[^s2][^s5]
- **Close the loop.** The linear model has no return path, so add one: ask for a reply, a read-back or a next step, since feedback is what turns transmission into conversation.[^s5][^s4]

## Evidence

The Shannon-Weaver model is a conceptual model, not an empirical finding, so its status is `theoretical`: it is judged by how much it helps explain communication rather than by experiments that test it.[^s3] Its strength for engineering is beyond dispute, but its fit to human talk is limited.[^s1][^s5] Britannica notes that the model is linear and essentially static, concerned with messages passing from point to point rather than their effects on the people involved, and that conversation needs feedback, a notion drawn from Norbert Wiener's cybernetics.[^s5] Aune argues that human communication is interactive rather than a single one-way transmission, and that a code-based picture of encoding and decoding struggles with non-literal language, ambiguous nonverbal cues and meaning that people work out on the spot without a shared code.[^s3] Introductory textbooks therefore present the transmission model alongside an interaction model, in which participants take turns and give feedback, and Barnlund's 1970 transaction model, in which communicators send and receive at once and build shared meaning together.[^s4] The model is best used as a first diagnostic, not as a full account of how understanding is created.[^s3][^s4]

## Connections

- **Introduced by** Claude Shannon in "A Mathematical Theory of Communication" (1948),[^s1] and by Warren Weaver, whose 1949 three-level reading extended it to meaning and effect.[^s2]
- **Contrasts with** the transactional model of communication, which treats both parties as simultaneous senders and receivers.[^s4]
- **Contrasts with** common ground and grounding theory, one of the interactive views of understanding that critics of code-based models favour.[^s3]
- **Complements** feedback, the return path that turns one-way transmission into a loop.[^s5]
- **Studied in** communication studies, where it is taught as the classic linear model.[^s3]
- **Related to** channel selection and media richness theory (the channel step), clarity and plain language (reducing semantic noise), teach-back (verifying decoding), Grice's cooperative principle and Norbert Wiener's cybernetics.[^s4][^s5]

## Sources

[^s1]: Shannon, "A Mathematical Theory of Communication", Bell System Technical Journal (1948). https://www.cs.yale.edu/homes/yry/readings/general/shannon1948.pdf (accessed 2026-11-11)
[^s2]: Weaver, "The Mathematics of Communication", Scientific American (1949). https://mt-archive.net/50/SciAm-1949-Weaver.pdf (accessed 2026-11-11)
[^s3]: Aune, "Traditional Models of Human Communication", in Message Processing, University of Hawai'i OER. https://pressbooks.oer.hawaii.edu/messageprocessing/?p=56 (accessed 2026-11-11)
[^s4]: "The Communication Process", Communication in the Real World, LibreTexts. https://socialsci.libretexts.org/Bookshelves/Communication/Introduction_to_Communication/Communication_in_the_Real_World_-_An_Introduction_to_Communication_Studies/01%3A_Introduction_to_Communication_Studies/1.02%3A_The_Communication_Process (accessed 2026-11-11)
[^s5]: Encyclopaedia Britannica, "Communication: Models of communication". https://www.britannica.com/topic/communication/Models-of-communication (accessed 2026-11-11)
