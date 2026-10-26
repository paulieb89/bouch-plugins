import copy
import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("closeout_gate", ROOT / "tools" / "validate_closeout_gate.py")
gate = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(gate)


class TestCleanProjectOnboarding(unittest.TestCase):
    """The package must work from a project-owned workspace, not a reference checkout."""

    def test_project_owned_workspace_passes_and_seeded_fault_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            workspace = Path(tmp)
            (workspace / "project" / "adapter").mkdir(parents=True)
            (workspace / "project" / "CLAUDE.md").write_text("Project owns the adapter and evidence paths.\n")
            for name in ("source", "import", "runtime", "input", "frame"):
                path = workspace / "project" / "evidence" / f"{name}.json"
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(name)

            def evidence(name):
                return {"result": "pass", "path": f"project/evidence/{name}.json"}

            manifest = {
                "version": 1,
                "candidate_id": "c000",
                "status": "accepted",
                "budget": {"max_candidates": 3, "lineage": [{"id": "c000", "parent": None}]},
                "evidence": {
                    "source": evidence("source"),
                    "import": evidence("import"),
                    "automated_runtime": evidence("runtime"),
                    "real_interaction": evidence("input"),
                },
                "meaningful_states": ["active"],
                "engine_frames": {"active": "project/evidence/frame.json"},
                "review": {"reviewer": "Paul", "type": "human", "verdict": "pass", "limitations": []},
                "execution_paths": ["project/evidence", "project/adapter"],
            }
            self.assertTrue(gate.validate(manifest, workspace)["ok"])

            seeded_fault = copy.deepcopy(manifest)
            seeded_fault["evidence"]["import"]["result"] = "fail"
            self.assertFalse(gate.validate(seeded_fault, workspace)["ok"])


if __name__ == "__main__":
    unittest.main()
