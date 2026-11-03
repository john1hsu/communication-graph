# Communication Graph — run playbook

This repo is a citation-backed, reasoner-checked knowledge graph for improving communication skills: listening, questioning, writing, presenting, persuasion, feedback, difficult conversations, negotiation, meetings and facilitation, executive and client communication, digital/async communication, nonverbal communication, cross-cultural communication, the psychology of communication barriers, and the thinkers and studies behind them. A scheduled run adds **exactly one new, unique article** per run. Every article must help the reader *do* something better. Follow these steps in order. Read `SCHEMA.md` before writing.

## 1. Sync and orient
```bash
pip install -r requirements.txt --break-system-packages -q
git pull --rebase origin main
python3 scripts/kg.py build      # must print OK; fix the repo first if it doesn't
```
Read `graph/stats.md`, `graph/frontier.md`, `graph/competency.md` and `topics/seeds.yaml`. `graph/index.json` lists every node (ids, titles, aliases, edges, steps, examples, source URLs).

## 2. Pick the topic (graph-driven)
Use the current UTC hour modulo 3:
- **0 → depth.** Take the top node in `graph/frontier.md` that fits a domain. Use its *Expected type* (inferred by the reasoner) as the article's `type` unless it is clearly wrong.
- **1 → breadth.** Take the domain at the top of "Domain coverage" in `graph/stats.md` (fewest articles; skip the domain of the most recent commit on ties) and pick an unwritten seed or another important topic in it.
- **2 → gap.** Take the first row of the first non-empty *(gap)* section in `graph/competency.md` and write the article that closes it (a technique that fixes an unaddressed anti-pattern or barrier, a practice that develops a skill, guidance for a situation, the person or work behind an unattributed idea).
- If the chosen mode yields nothing, fall back to breadth.

Then prove it is unique:
```bash
python3 scripts/kg.py similar "<candidate title>"
```
If any score ≥ 0.5, or an existing title/alias names the same thing, pick a different topic. Never write a second article on an existing subject — not a rename, a sub-angle that restates it, an acronym (BLUF vs. bottom line up front), or a synonym. Record alternate names as `aliases`.

## 3. Research
- Run several web searches and read the actual pages (WebFetch). Don't rely on snippets or memory.
- Collect 3–6 credible sources: ≥ 1 scholarly and ≥ 2 strong (see `SCHEMA.md`). Prefer the original study or book, peer-reviewed research and meta-analyses, university research centres (Harvard PON, Stanford GSB), government plain-language and crisis-communication guidance, and *HBR* / *MIT SMR* articles written by researchers. **Never cite Wikipedia, wikiHow** or the other banned sources.
- Every URL you cite must be one you opened this run. Never invent a URL, DOI or Wikidata id. Only add `sameAs: [wd:Q…]` if you opened that Wikidata page and it is the same concept.
- A lot of communication advice is folklore. Check the evidence: look for replications and meta-analyses, and set `evidenceStatus` honestly. Popular advice that outruns its evidence (e.g. the "93% nonverbal" claim, power posing) is `contested` or `failed-replication`, with a `challengedBy` edge. Untested expert advice is `practitioner`.
- Attribute frameworks to their originators and note when a popular version differs from the original.
- Paraphrase. No quotation longer than 15 words; at most one quote per source.

## 4. Write the node
```bash
python3 scripts/kg.py new <domain> <slug> <Type>   # scaffold with the fields and sections the class requires
```
- 400–1,000 words, practitioner level, workplace-focused: definition, origin, why it matters, how to apply or practise it, common mistakes or pitfalls, evidence and limits, and **Connections**. Where relevant, note how it changes by channel (email vs. live), seniority (peer vs. executive) or culture.
- `steps` are concrete and imperative. `example` is a realistic workplace before/after with a short "why". `selfCheck` questions are ones a reader could ask themselves right before or after a real conversation.
- Every substantive paragraph carries footnote citations `[^sN]`; list every source in `## Sources`.
- Edges: 1–3 `broader`, `related` as needed, `requires` for genuine prerequisites, and ≥ 1 (ideally 2–5) typed `relations`, **each citing the source that supports it** and a confidence. Link to existing ids wherever they fit (`graph/index.json`); new target ids are fine and join the frontier. Match each predicate's domain and range (`SCHEMA.md`). Never write inverses — the reasoner adds them.
- If a needed class or predicate is missing, add it to `ontology/ontology.ttl` (label, domain/range, inverse/characteristics) in the same commit. Keep the ontology small; reuse first.
- Back-links: if `graph/suggested-links.md` or the new node shows an existing article should point to it, you may add the id to that article's `related` (or a sourced typed relation). Don't otherwise rewrite existing articles.

## 5. Validate, build, commit, push
```bash
python3 scripts/kg.py build    # fix every problem (structure, citations, reasoning contradictions, SHACL) and re-run until OK
git add -A
git commit -m "Add <Title> (<domain>, <mode> run)"
git pull --rebase origin main && python3 scripts/kg.py build && git push origin main
```
If the push is rejected, pull --rebase, rebuild, and push again (once). Commit regenerated `graph/` files with the article; CI fails if they are stale.

## Don'ts
- Don't add more than one article per run, delete articles, or rewrite history.
- Don't commit if validation fails; leave the repo clean.
- Don't cite a source you didn't open, or attach a source to an edge it doesn't support.
- Don't hand-edit anything in `graph/`.
- Don't teach manipulation or deception (e.g. dark-pattern persuasion, gaslighting scripts); persuasion and negotiation topics stay ethical and say where the line is.
- Don't use real, named private individuals or current partisan figures in examples; use neutral workplace scenarios.
