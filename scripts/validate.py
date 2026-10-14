#!/usr/bin/env python3
"""P001B administrative and future session integrity checks (not mathematical proofs)."""
import json
import pathlib
import re
ROOT = pathlib.Path(__file__).resolve().parents[1]
REPO = "jfairfaxball-348/Four-Petal-Sunflower-Free-Triple-Extremal-Threshold"
REQUIRED = ["README.md","AGENTS.md","project_manifest.json","authoritative/START_HERE.md","authoritative/STATE.json","authoritative/SESSION_PROTOCOL.md","authoritative/STANDARDS.md","research/TARGET.md","research/CLAIMS.json","research/SOURCES.json","research/NOVELTY_LEDGER.md","research/DECISIONS_AND_RISKS.md","sessions/HISTORY.md","sessions/NEXT_SESSION.md","sessions/AI_USE.md","sessions/S000/CLOSEOUT.md","experiments/PRE_REGISTRATION.md","validation/GITHUB_EVIDENCE.json","formalisation/STATUS.json","publication/STATUS.json","scripts/validate.py","tests/test_integrity.py",".github/workflows/validate.yml"]
def check():
    for p in REQUIRED:
        assert (ROOT/p).is_file(), f"missing {p}"
    state = json.loads((ROOT/"authoritative/STATE.json").read_text())
    manifest = json.loads((ROOT/"project_manifest.json").read_text())
    claims = json.loads((ROOT/"research/CLAIMS.json").read_text())
    sources = json.loads((ROOT/"research/SOURCES.json").read_text())
    evidence = json.loads((ROOT/"validation/GITHUB_EVIDENCE.json").read_text())
    assert state["repo"] == manifest["repo"] == REPO
    assert state["repository_id"] == manifest["repository_id"] == 1418652673
    assert manifest["parent_repository"] == "jfairfaxball-348/sunflower-structures-programme"
    assert state["session_completed"] == "P001B-S001" and state["next_session"] == "P001B-S002"
    assert state["status"] == manifest["status"] == "RESEARCH_ACTIVE_NO_THRESHOLD_IMPROVEMENT"
    assert state["next_executed"] is False and state["first_mathematics_executed"] is True
    assert manifest["first_research_executed"] is True and state["mathematical_results"] >= 1
    assert any(c["id"] == "BASELINE-2026" and "ATTRIBUTED" in c["status"] for c in claims["claims"])
    assert len(sources["primary"]) >= 1 and sources["primary"][0]["url"] == "https://arxiv.org/abs/2609.06175"
    assert evidence["initial_main"] == "6cdfc0c8eec3ac4143966bb76f04447ad81e1b25"
    prompt = (ROOT/"sessions/NEXT_SESSION.md").read_text()
    for s in ("P001B-S002",REPO,"P001B-S001","39", "EMPTY","six","F39","PR","CI"):
        assert s.lower() in prompt.lower(), "missing handoff token "+s
    assert "P001B-S002" in prompt and "do not execute" in prompt.lower()
    assert (ROOT/"sessions/S001/CLOSEOUT.md").is_file(), "missing S001 closeout"
    assert re.fullmatch("[0-9a-f]{40}", state["historic_initial_main"])
    assert (ROOT/"experiments/S001_C1_CERTIFICATES.json").is_file()
    assert (ROOT/"experiments/S001_F39_edges.txt").is_file()
    assert (ROOT/"src/verify_s001_cert.py").is_file()
    return True
if __name__ == "__main__":
    assert check()
    print("P001B S001 governance integrity PASS (proof and hosted CI independently classified)")
