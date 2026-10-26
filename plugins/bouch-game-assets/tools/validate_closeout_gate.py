#!/usr/bin/env python3
"""Validate a bounded, portable game/3D asset close-out manifest."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


REQUIRED_LAYERS = ("source", "import", "automated_runtime", "real_interaction")
TERMINAL_STATUSES = {"provisional", "accepted"}
VALID_STATUSES = TERMINAL_STATUSES | {"rejected", "blocked"}
VALID_REVIEW_TYPES = {"agent", "human"}
VALID_VERDICTS = {"pass", "provisional", "reject"}


def _inside(root: Path, value: str) -> bool:
    path = Path(value)
    if path.is_absolute():
        return False
    try:
        (root / path).resolve().relative_to(root.resolve())
    except ValueError:
        return False
    return True


def _path(root: Path, errors: list[str], label: str, value: Any) -> None:
    if not isinstance(value, str) or not value:
        errors.append(f"{label} must be a non-empty relative path")
        return
    if not _inside(root, value):
        errors.append(f"{label} escapes workspace root: {value}")
        return
    if not (root / value).is_file():
        errors.append(f"{label} does not exist: {value}")


def validate(manifest: dict[str, Any], workspace: Path) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    if manifest.get("version") != 1:
        errors.append("version must be 1")

    candidate_id = manifest.get("candidate_id")
    if not isinstance(candidate_id, str) or not candidate_id:
        errors.append("candidate_id is required")
    status = manifest.get("status")
    if status not in VALID_STATUSES:
        errors.append(f"status must be one of {sorted(VALID_STATUSES)}")

    budget = manifest.get("budget")
    if not isinstance(budget, dict):
        errors.append("budget object is required")
        budget = {}
    max_candidates = budget.get("max_candidates")
    lineage = budget.get("lineage")
    if not isinstance(max_candidates, int) or max_candidates < 1:
        errors.append("budget.max_candidates must be a positive integer")
        max_candidates = 0
    if not isinstance(lineage, list) or not lineage:
        errors.append("budget.lineage must contain the candidate chain")
        lineage = []
    if len(lineage) > max_candidates:
        errors.append(f"repair budget exceeded: {len(lineage)} candidates > {max_candidates}")

    ids: list[str] = []
    for index, item in enumerate(lineage):
        if not isinstance(item, dict) or not isinstance(item.get("id"), str):
            errors.append(f"budget.lineage[{index}] requires an id")
            continue
        item_id = item["id"]
        ids.append(item_id)
        expected_parent = None if index == 0 else ids[index - 1]
        if item.get("parent") != expected_parent:
            errors.append(f"lineage parent for {item_id} must be {expected_parent!r}")
        if index > 0:
            repair = item.get("repair")
            if not isinstance(repair, dict):
                errors.append(f"repair candidate {item_id} requires repair metadata")
            else:
                for key in ("source_observation", "hypothesis", "scope"):
                    if not isinstance(repair.get(key), str) or not repair[key].strip():
                        errors.append(f"repair candidate {item_id} requires repair.{key}")
                if isinstance(repair.get("source_observation"), str):
                    _path(workspace, errors, f"repair {item_id} source_observation", repair["source_observation"])
    if candidate_id and ids and candidate_id != ids[-1]:
        errors.append("candidate_id must be the final lineage entry")

    if status in TERMINAL_STATUSES:
        evidence = manifest.get("evidence")
        if not isinstance(evidence, dict):
            errors.append("evidence object is required for provisional/accepted")
            evidence = {}
        for layer in REQUIRED_LAYERS:
            item = evidence.get(layer)
            if not isinstance(item, dict):
                errors.append(f"missing required evidence layer: {layer}")
                continue
            if item.get("result") != "pass":
                errors.append(f"evidence layer {layer} must have result=pass")
            _path(workspace, errors, f"evidence.{layer}.path", item.get("path"))

        states = manifest.get("meaningful_states")
        frames = manifest.get("engine_frames")
        if not isinstance(states, list) or not states or not all(isinstance(s, str) and s for s in states):
            errors.append("meaningful_states must be a non-empty list of state names")
            states = []
        if not isinstance(frames, dict):
            errors.append("engine_frames object is required")
            frames = {}
        for state in states:
            _path(workspace, errors, f"engine_frames.{state}", frames.get(state))

        review = manifest.get("review")
        if not isinstance(review, dict):
            errors.append("review object is required")
            review = {}
        for key in ("reviewer", "type", "verdict", "limitations"):
            if key not in review:
                errors.append(f"review.{key} is required")
        if not isinstance(review.get("reviewer"), str) or not review.get("reviewer", "").strip():
            errors.append("review.reviewer must be a non-empty name")
        if review.get("type") not in VALID_REVIEW_TYPES:
            errors.append(f"review.type must be one of {sorted(VALID_REVIEW_TYPES)}")
        if review.get("verdict") not in VALID_VERDICTS:
            errors.append(f"review.verdict must be one of {sorted(VALID_VERDICTS)}")
        if not isinstance(review.get("limitations"), list):
            errors.append("review.limitations must be a list (empty is allowed)")
        if status == "accepted" and not (review.get("type") == "human" and review.get("verdict") == "pass"):
            errors.append("accepted requires a human review with verdict=pass")
        if status == "provisional" and review.get("type") == "agent" and review.get("verdict") == "pass":
            warnings.append("agent visual pass remains provisional until human review")

    execution_paths = manifest.get("execution_paths", [])
    if not isinstance(execution_paths, list) or not all(isinstance(p, str) for p in execution_paths):
        errors.append("execution_paths must be a list of relative paths")
    else:
        for value in execution_paths:
            if not _inside(workspace, value):
                errors.append(f"undeclared or out-of-workspace execution path: {value}")

    result = "pass" if not errors and status in TERMINAL_STATUSES else "fail"
    return {"ok": result == "pass", "result": result, "candidate_id": candidate_id,
            "status": status, "errors": errors, "warnings": warnings,
            "checked_layers": list(REQUIRED_LAYERS)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--workspace", type=Path, default=None)
    args = parser.parse_args(argv)
    try:
        manifest = json.loads(args.manifest.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"ok": False, "result": "fail", "errors": [str(exc)]}, indent=2))
        return 2
    if not isinstance(manifest, dict):
        print(json.dumps({"ok": False, "result": "fail", "errors": ["manifest must be a JSON object"]}, indent=2))
        return 2
    workspace = (args.workspace or args.manifest.parent).resolve()
    report = validate(manifest, workspace)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
