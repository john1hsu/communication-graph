# Communication Graph

A growing, citation-backed knowledge graph for communicating better at work: listening, questioning, writing, presenting, persuasion, feedback, difficult conversations, negotiation, facilitation, executive and client communication, async and digital communication, nonverbal and cross-cultural communication, and the psychology of what gets in the way. A scheduled run researches one new topic, writes it as a practice-ready node with evidenced, typed edges, and only commits it if the validator, the OWL reasoner and the SHACL shapes all agree it is sound.

**Read it online: https://john1hsu.github.io/communication-graph/** (rebuilt automatically on every new article by `.github/workflows/pages.yml` from `site/build.py`).

Start with **[`graph/playbook.md`](graph/playbook.md)**: every step-by-step technique, before/after rewrite and self-check question in the graph, grouped by domain.

## Architecture

```
articles/<domain>/<slug>.md          Markdown + YAML frontmatter (one node each)
        │  scripts/kg.py
        ▼
 1. structural validation      citations, uniqueness (shingles + TF-IDF), practice rules, acyclicity
 2. RDF assembly               SKOS + PROV-O + schema.org HowTo + before/after rewrites, one named graph per article
 3. OWL 2 RL reasoning         inverse / symmetric / transitive properties, domain & range typing
 4. consistency checking       disjoint-class contradictions, domain/range violations
 5. SHACL validation           ontology/shapes.ttl (semantic contract on the exported RDF)
 6. exports + analytics        graph/  (regenerated on every commit; CI fails if stale)
```

| Layer | What | Where |
|---|---|---|
| Ontology | OWL 2 RL classes (Skill, Technique, Framework, Principle, Disposition, Barrier, AntiPattern, Context, Channel, Genre, Theory, Phenomenon, Study, …) and typed relations (`develops`, `addresses`, `structures`, `appliedIn`, `undermines`, `challengedBy`, …) with inverses, symmetry, transitivity, domains, ranges and disjointness; aligned with SKOS, PROV-O and schema.org | `ontology/ontology.ttl` |
| Shapes | SHACL: every node defined, sourced, levelled and evidence-rated; techniques carry ≥ 3 steps and a rewrite; anti-patterns carry a rewrite; skills, techniques, anti-patterns and barriers carry self-check questions | `ontology/shapes.ttl` |
| Nodes | One Markdown article per entity: id, class, hierarchy, prerequisites, evidenced typed edges, steps, before/after example, self-check questions, evidence status, entity links and sources | `articles/<domain>/` |
| Practice playbook | All procedures, rewrites and self-checks in one place | `graph/playbook.md` |
| Linked data | N-Triples (asserted and OWL-RL inferred), TriG with per-article named graphs and provenance, Turtle-star edge evidence (RDF 1.2), JSON-LD, JSON index | `graph/triples.nt`, `graph/inferred.nt`, `graph/graph.trig`, `graph/edge-evidence.ttls`, `graph/graph.jsonld`, `graph/index.json` |
| Analytics | PageRank, betweenness, Louvain communities, k-core, coverage by type/domain/level/evidence | `graph/stats.md` |
| Frontier | Unwritten nodes ranked by referrers weighted by their centrality, with the **type the reasoner expects** | `graph/frontier.md` |
| Link prediction | Adamic-Adar scores for written nodes that should probably be connected | `graph/suggested-links.md` |
| Competency questions | SPARQL over asserted + inferred triples: highest-leverage techniques, toolkit by situation, myths and contested advice; *gap* queries (unfixed anti-patterns, unpractised skills, situations without guidance, orphans, unattributed ideas) drive gap-filling runs | `queries/*.rq` → `graph/competency.md` |
| Learning path | Topological layers of the `requires` prerequisite DAG | `graph/learning-path.md` |

## What makes it more than a link list

- **Practice-ready.** Techniques have ordered steps (published as schema.org `HowTo`), techniques and anti-patterns have workplace before/after rewrites, and skills, techniques, anti-patterns and barriers have self-check questions.
- **Evidence-aware.** Every node has an `evidenceStatus` (robust, mixed, contested, failed-replication, practitioner, theoretical, historical). Popular advice that outruns its evidence is flagged and linked to what challenges it.
- **Every typed edge is evidenced.** Each relation cites the source that supports it and carries a confidence, published as RDF-star annotations on the edge.
- **Reasoning, not just storage.** Writers state one direction (`paraphrasing addresses interrupting`); the OWL-RL reasoner materialises `addressedBy`, symmetric and transitive relations, and types unwritten nodes from property ranges. Contradictory typing fails the build.
- **Self-directing growth.** Runs rotate between depth (frontier), breadth (least-covered domain) and gap (SPARQL competency gaps).
- **Reproducible.** Outputs are byte-for-byte deterministic; CI re-runs tests and the build and fails if `graph/` is stale.

## Usage

```bash
pip install -r requirements.txt
python3 scripts/kg.py check                          # validate + reason + SHACL
python3 scripts/kg.py build                          # ...and regenerate graph/
python3 scripts/kg.py similar "BLUF"                 # duplicate check for a candidate topic
python3 scripts/kg.py new writing bottom-line-up-front Technique   # scaffold
python3 scripts/kg.py query queries/05-toolkit-by-situation.rq      # or an inline SPARQL string
python3 -m pytest -q tests                           # end-to-end tests on fixture articles
```

Steer what gets written by editing `topics/seeds.yaml`. The run playbook is `CLAUDE.md`; the article format is `SCHEMA.md`. The `.nt`, `.trig` and `.jsonld` exports load into Apache Jena/Fuseki, GraphDB, Oxigraph, rdflib, or Neo4j via n10s; `.ttls` needs an RDF 1.2 / RDF-star aware store.
