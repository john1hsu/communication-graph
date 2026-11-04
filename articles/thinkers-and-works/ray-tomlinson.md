---
id: cm:ray-tomlinson
type: Person
title: Ray Tomlinson
aliases: [Raymond S. Tomlinson, Raymond Tomlinson, Tomlinson]
domain: thinkers-and-works
summary: >-
  BBN engineer (1941-2016) who in 1971 sent the first messages between users on different ARPANET
  computers, chose the "@" that still separates user from host in every address, and co-wrote the
  1973 header standard that made From, Subject and Date part of every message.
level: introductory
evidenceStatus: historical
broader: []
related: [cm:email, cm:asynchronous-communication, cm:channel-selection, cm:information-overload, cm:bottom-line-up-front]
requires: []
relations:
  - {predicate: introduced, object: cm:email, source: s1, confidence: medium}
  - {predicate: introduced, object: cm:email-address, source: s2, confidence: high}
  - {predicate: authored, object: cm:rfc-561, source: s1, confidence: high}
  - {predicate: contrastsWith, object: cm:ctss-mail, source: s4, confidence: medium}
sameAs: []
sources:
  - id: s1
    title: "The Technical Development of Internet Email"
    publisher: Partridge, C., IEEE Annals of the History of Computing, April-June 2008 (author's copy hosted by gwern.net)
    url: https://www.Gwern.net/doc/cs/2008-partridge.pdf
    type: peer-reviewed
    accessed: 2026-11-04
  - id: s2
    title: "Ray Tomlinson"
    publisher: Lemelson-MIT Program, Massachusetts Institute of Technology
    url: https://lemelson.mit.edu/resources/ray-tomlinson
    type: academic
    accessed: 2026-11-04
  - id: s3
    title: "Meet the Man Who Put the '@' in Your E-Mail"
    publisher: Internet Hall of Fame (Internet Society), 2012
    url: https://internethalloffame.org/?p=260
    type: institutional
    accessed: 2026-11-04
  - id: s4
    title: "The History of Electronic Mail"
    publisher: Van Vleck, T., co-author of CTSS MAIL (multicians.org, first posted 2001, updated 2026)
    url: https://multicians.org/thvv/mail-history.html
    type: primary
    accessed: 2026-11-04
  - id: s5
    title: "Raymond S. Tomlinson - 1963"
    publisher: School of Engineering, Rensselaer Polytechnic Institute
    url: https://eng.rpi.edu/person/raymond-s-tomlinson-1963
    type: academic
    accessed: 2026-11-04
created: 2026-11-04
---

# Ray Tomlinson

Raymond S. Tomlinson (1941-2016) was the engineer at Bolt Beranek and Newman (BBN) who, in 1971, made it possible to send a message to a person on a different computer on the ARPANET, the forerunner of the internet.[^s2][^s5] He trained in electrical engineering at Rensselaer Polytechnic Institute and MIT, joined BBN in 1967 and stayed there for the rest of his career.[^s2] He was inducted into the Internet Society's first Internet Hall of Fame class in 2012.[^s3] For anyone who writes email at work, his choices explain several features of the channel that are easy to take for granted: the address, the mailbox the reader controls, and the required subject line.[^s1][^s2]

## Origin

Electronic mail predates Tomlinson. In 1965 Tom Van Vleck and Noel Morris wrote CTSS MAIL at MIT, which let users of one time-sharing computer leave persistent, asynchronous messages in each other's mailbox files; it had no subject headers and could not leave that machine.[^s4] Tomlinson's step was to cross the network. In 1971 he read a proposed ARPANET protocol for sending documents to remote printers and judged it overcomplicated; he thought a document should go to the person's mailbox, where the recipient could decide what to do with it.[^s1] He joined SNDMSG, a local mail program on the TENEX operating system, to CPYNET, a file-transfer program he had written, so that a message could be appended to a mailbox on another host.[^s1][^s5] By 1972 BBN had shipped SNDMSG to about a dozen ARPANET sites.[^s3]

To name a remote mailbox he needed a separator between the user's name and the host computer. He picked "@" because it could not be mistaken for part of a name and it signalled where the user was; the user@host format is still standard.[^s2][^s3] In 1973 he co-authored RFC 561, the first standard for message headers, which required From, Subject and Date fields at the top of every message.[^s1] Others then added To, CC and reply-to fields, and John Vittal's "answer" command, which filled in recipients and subject automatically, turned one-way memos into back-and-forth conversation.[^s1]

Calling Tomlinson "the inventor of email" is common but contested: the Internet Hall of Fame notes that others credit different people, and Van Vleck's account dates single-machine mail to 1965.[^s3][^s4] The defensible claim is narrower: he built the first network email and its addressing convention.[^s1][^s4]

## Why it matters

Three of the design decisions still shape good practice. First, email was built around a mailbox the recipient reads when they choose, not a live interruption; Tomlinson's own objection to the printer protocol was that the reader, not the sender, should decide.[^s1] That is why email suits messages a reader can absorb and act on alone, and why a sender who needs an answer within the hour should usually pick a faster channel or say the deadline plainly.[^s1] Second, the Subject field has been mandatory since the first header standard, so it is meant to tell the reader what a message is about before they open it; a subject such as "Decision needed by Fri: Q3 vendor renewal" uses the field as designed, while "Quick question" wastes it.[^s1] Third, the early systems had no guardrails against mass mailing; Van Vleck recalls one unsolicited message sent to every user around 1971 as the moment he saw that mail needed limits, a problem that later became spam and reply-all storms.[^s4]

Tomlinson himself said email was being used, by and large, the way he had pictured it, and that people use it in whatever way works for them.[^s2] Email only spread widely once affordable personal computers and online services arrived in the late 1980s and 1990s.[^s2]

## Applying the history at work

Consider a team lead who sends "Thoughts?" with a 12-page attachment to a 40-person list and expects replies by end of day. Read against the channel's design, three fixes follow: put the request and deadline in the subject line, send it only to the people who must act, and move the same-day discussion to a meeting or chat while keeping email for the record.[^s1][^s4] The mailbox model also cuts the other way: recipients can reasonably take time to reply unless the sender says otherwise.[^s1]

## Limits

Most accounts of the first network message rest on Tomlinson's recollection; he did not remember its content, which he described as test text.[^s3] The original code did little: senders had to know the exact location of a recipient's mailbox, failed deliveries were not retried, and reading meant printing the mailbox file.[^s1] The practical lessons above are interpretations of the design history, not findings tested by Tomlinson or his colleagues.[^s1][^s4]

## Connections

- **Introduced email** as a network channel between computers, building on earlier single-machine mail; the confidence is medium because the "first" title is disputed.[^s1][^s3]
- **Introduced the email address** in its user@host form.[^s2]
- **Authored RFC 561** (1973) with Abhay Bhushan, Ken Pogran and Jim White, the first email header standard.[^s1]
- **Contrasts with CTSS MAIL**, the 1965 MIT system that delivered mail only within one computer.[^s4]
- **Related to asynchronous communication, channel selection and information overload**, which describe how the channel he built is best used and where it strains; and to **bottom line up front**, the writing habit that makes the subject line and first sentence do their job.[^s1][^s4]

## Sources

[^s1]: Partridge, C. (2008). "The Technical Development of Internet Email". *IEEE Annals of the History of Computing*, April-June 2008. https://www.Gwern.net/doc/cs/2008-partridge.pdf (accessed 2026-11-04)
[^s2]: Lemelson-MIT Program, "Ray Tomlinson". https://lemelson.mit.edu/resources/ray-tomlinson (accessed 2026-11-04)
[^s3]: Internet Hall of Fame (2012). "Meet the Man Who Put the '@' in Your E-Mail". https://internethalloffame.org/?p=260 (accessed 2026-11-04)
[^s4]: Van Vleck, T. "The History of Electronic Mail". multicians.org. https://multicians.org/thvv/mail-history.html (accessed 2026-11-04)
[^s5]: Rensselaer Polytechnic Institute, School of Engineering, "Raymond S. Tomlinson - 1963". https://eng.rpi.edu/person/raymond-s-tomlinson-1963 (accessed 2026-11-04)
