"""End-to-end tests for scripts/kg.py against a throwaway tree of fixture articles.

Fixtures use example.org URLs and synthetic prose: they exercise the validator,
reasoner, SHACL shapes and exports, and are never part of the real graph.
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
KG = REPO / "scripts" / "kg.py"


def body(slug: str, sections: list[str]) -> str:
    def para(i: int) -> str:
        words = " ".join(f"{slug.replace('-', '')}{i}w{j}" for j in range(150))
        return f"Synthetic fixture prose for {slug} paragraph {i}: {words}.[^s1][^s2][^s3]"
    out = [f"# {slug}", "", para(0), "", para(1), ""]
    for k, s in enumerate(sections, 2):
        out += [s, "", para(k), ""]
    out += ["## Connections", "", para(99), "", "## Sources", "",
            "[^s1]: Fixture one. https://example.org/1", "[^s2]: Fixture two. https://example.org/2",
            "[^s3]: Fixture three. https://example.org/3"]
    return "\n".join(out) + "\n"


SOURCES = """sources:
  - {id: s1, title: Fixture one, publisher: Example, url: "https://example.org/SLUG/1", type: peer-reviewed, accessed: 2026-11-02}
  - {id: s2, title: Fixture two, publisher: Example, url: "https://example.org/SLUG/2", type: practitioner-journal, accessed: 2026-11-02}
  - {id: s3, title: Fixture three, publisher: Example, url: "https://example.org/SLUG/3", type: textbook, accessed: 2026-11-02}
created: 2026-11-02
"""

ARTICLES = {
    ("listening", "active-listening"): ("""id: cm:active-listening
type: Skill
title: Active listening
aliases: [empathic listening]
domain: listening
summary: Listening with full attention to understand the speaker's meaning and feelings, and showing that understanding.
level: introductory
evidenceStatus: robust
broader: [cm:listening]
related: [cm:empathy]
relations:
  - {predicate: demonstratedBy, object: cm:listening-quality-study, source: s1, confidence: high}
  - {predicate: introducedBy, object: cm:carl-rogers, source: s3}
selfCheck:
  - Could I summarise what they said to their satisfaction?
  - Was I planning my reply while they were still talking?
sameAs: [wd:Q1145298]
""", ["## What good looks like", "## How to practise it"]),
    ("listening", "paraphrasing"): ("""id: cm:paraphrasing
type: Technique
title: Paraphrasing
domain: listening
summary: Restating the other person's message in your own words to confirm understanding and show you listened.
level: introductory
evidenceStatus: practitioner
broader: [cm:active-listening-techniques]
requires: [cm:active-listening]
relations:
  - {predicate: develops, object: cm:active-listening, source: s1, confidence: high}
  - {predicate: addresses, object: cm:interrupting, source: s2}
  - {predicate: appliedIn, object: cm:one-on-one-meetings, source: s2}
  - {predicate: confusedWith, object: cm:parroting, source: s3, confidence: low}
steps:
  - Let the speaker finish their point completely.
  - Restate the core message in your own words, briefly.
  - Check accuracy with a question and invite correction.
example:
  situation: A colleague explains why a deadline slipped.
  before: "OK. Anyway, when can you get it done?"
  after: "So the vendor delivered late and that pushed testing back a week - is that right?"
  why: The restatement shows you understood the cause before moving to solutions.
selfCheck:
  - Did I restate their point before giving my own?
  - Did they confirm or correct my summary?
""", ["## How to apply it", "## Common mistakes"]),
    ("listening", "interrupting"): ("""id: cm:interrupting
type: AntiPattern
title: Interrupting
domain: listening
summary: Cutting into another person's turn before they have finished, which signals that their point matters less.
level: introductory
evidenceStatus: practitioner
broader: [cm:conversational-anti-patterns]
related: [cm:turn-taking]
relations:
  - {predicate: undermines, object: cm:rapport, source: s1, confidence: medium}
example:
  situation: A team member starts describing a risk in a stand-up.
  before: "Right, right, we know - next item."
  after: "Go on - what is the impact if it happens?"
  why: Letting them finish surfaces the actual risk and keeps them willing to raise issues.
selfCheck:
  - Did I let them finish before responding?
  - Did I talk over anyone in this meeting?
""", ["## How to spot it", "## How to fix it"]),
    ("barriers-and-psychology", "curse-of-knowledge"): ("""id: cm:curse-of-knowledge
type: Barrier
title: Curse of knowledge
domain: barriers-and-psychology
summary: The difficulty experts have imagining what it is like not to know something, which makes their explanations unclear.
level: intermediate
evidenceStatus: robust
broader: [cm:cognitive-barriers]
related: [cm:illusion-of-transparency]
requires: [cm:audience-analysis]
relations:
  - {predicate: demonstratedBy, object: cm:tappers-and-listeners-study, source: s1, confidence: high}
selfCheck:
  - Would a smart newcomer understand every term I used?
  - Have I tested this explanation on someone outside my team?
""", ["## Evidence", "## How to spot it", "## How to fix it"]),
}


def make_tree(tmp: Path, articles=ARTICLES) -> Path:
    for d in ("ontology", "topics", "queries"):
        shutil.copytree(REPO / d, tmp / d)
    for (dom, slug), (fm, secs) in articles.items():
        p = tmp / "articles" / dom / f"{slug}.md"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(f"---\n{fm}{SOURCES.replace('SLUG', slug)}---\n{body(slug, secs)}")
    return tmp


def run(tmp: Path, *args: str, hashseed: str = "random") -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(KG), *args], cwd=tmp, env={"PYTHONHASHSEED": hashseed, "CM_KG_ROOT": str(tmp), "PATH": ""},
                          capture_output=True, text=True)


def test_valid_tree_builds(tmp_path):
    t = make_tree(tmp_path)
    r = run(t, "build")
    assert r.returncode == 0, r.stdout + r.stderr
    g = t / "graph"
    inferred = (g / "inferred.nt").read_text()
    ns = "https://github.com/john1hsu/communication-graph/"
    # inverse property materialised by the reasoner
    assert f"interrupting> <{ns}ontology#addressedBy> <{ns}id/paraphrasing>" in inferred
    assert f"active-listening> <{ns}ontology#developedBy> <{ns}id/paraphrasing>" in inferred
    # symmetric property materialised
    assert f"parroting> <{ns}ontology#confusedWith>" in inferred
    # range axioms type unwritten frontier nodes
    assert f"tappers-and-listeners-study> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <{ns}ontology#Study>" in inferred
    frontier = (g / "frontier.md").read_text()
    assert "`cm:carl-rogers`" in frontier and "Person" in frontier
    assert "<< <" in (g / "edge-evidence.ttls").read_text()
    play = (g / "playbook.md").read_text()
    assert "| Before | After |" in play and "1. Let the speaker finish" in play and "Ask yourself:" in play
    assert "HowToStep" in (g / "triples.nt").read_text()
    idx = json.loads((g / "index.json").read_text())
    assert {x["id"] for x in idx} == {"cm:active-listening", "cm:paraphrasing", "cm:interrupting",
                                      "cm:curse-of-knowledge"}
    comp = (g / "competency.md").read_text()
    assert "cm:curse-of-knowledge" in comp  # barrier with no fix -> gap
    path = (g / "learning-path.md").read_text()
    assert path.index("Active listening") < path.index("Paraphrasing")
    # deterministic: rebuilding under different hash seeds (as CI and scheduled runs do) is byte-identical
    before = {p.name: p.read_text() for p in g.iterdir()}
    for seed in ("1", "2", "3", "4"):
        assert run(t, "build", hashseed=seed).returncode == 0
        assert before == {p.name: p.read_text() for p in g.iterdir()}, f"output changed with PYTHONHASHSEED={seed}"


def mutate(key, old, new):
    arts = dict(ARTICLES)
    fm, secs = arts[key]
    assert old in fm
    arts[key] = (fm.replace(old, new), secs)
    return arts


@pytest.mark.parametrize("key,old,new,expect", [
    (("listening", "paraphrasing"), "type: Technique", "type: AntiPattern", "develops expects subject"),
    (("listening", "active-listening"), "source: s3}", "source: s9}", "unknown source"),
    (("listening", "active-listening"), "evidenceStatus: robust", "evidenceStatus: contested", "needs a challengedBy"),
    (("listening", "paraphrasing"), "  - Let the speaker finish their point completely.\n", "", ">= 3 steps"),
    (("listening", "interrupting"), "  - Did I talk over anyone in this meeting?\n", "", ">= 2 selfCheck"),
    (("listening", "interrupting"), "after: \"Go on - what is the impact if it happens?\"",
     "after: \"Right, right, we know - next item.\"", "before and after are the same"),
    (("listening", "paraphrasing"), "title: Paraphrasing", "title: Paraphrasing\naliases: [empathic listening]",
     "collides"),
    (("listening", "active-listening"), "introducedBy, object: cm:carl-rogers",
     "introducedBy, object: cm:listening-quality-study", "contradiction"),
])
def test_rejections(tmp_path, key, old, new, expect):
    t = make_tree(tmp_path, mutate(key, old, new))
    r = run(t, "check")
    assert r.returncode == 1 and expect in r.stdout, r.stdout


def test_requires_cycle(tmp_path):
    arts = mutate(("listening", "active-listening"), "related: [cm:empathy]",
                  "related: [cm:empathy]\nrequires: [cm:paraphrasing]")
    r = run(make_tree(tmp_path, arts), "check")
    assert r.returncode == 1 and "cycle in 'requires'" in r.stdout


def test_banned_source(tmp_path):
    t = make_tree(tmp_path)
    p = t / "articles" / "listening" / "interrupting.md"
    p.write_text(p.read_text().replace("https://example.org/interrupting/1", "https://www.wikihow.com/X"))
    r = run(t, "check")
    assert r.returncode == 1 and "banned domain" in r.stdout


def test_similar_and_new(tmp_path):
    t = make_tree(tmp_path)
    r = run(t, "similar", "empathic listening")
    assert r.returncode == 0 and r.stdout.splitlines()[1].split()[3] == "cm:active-listening"
    r = run(t, "new", "writing", "bottom-line-up-front", "Technique")
    assert r.returncode == 0
    text = (t / "articles" / "writing" / "bottom-line-up-front.md").read_text()
    assert "steps:" in text and "example:" in text and "selfCheck:" in text and "## Common mistakes" in text


def test_empty_tree(tmp_path):
    t = make_tree(tmp_path, {})
    r = run(t, "build")
    assert r.returncode == 0, r.stdout
