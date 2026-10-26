import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("closeout_gate", ROOT / "tools" / "validate_closeout_gate.py")
gate = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(gate)


class TestCloseoutGate(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.paths = {}
        for name in ("source", "import", "runtime", "input", "initial", "active", "reset", "failure"):
            path = self.root / "evidence" / f"{name}.json"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(name)
            self.paths[name] = str(path.relative_to(self.root))

    def tearDown(self):
        self.tmp.cleanup()

    def manifest(self):
        return {
            "version": 1,
            "candidate_id": "c001",
            "status": "provisional",
            "budget": {"max_candidates": 3, "lineage": [
                {"id": "c000", "parent": None},
                {"id": "c001", "parent": "c000", "repair": {
                    "source_observation": self.paths["failure"], "hypothesis": "fix framing", "scope": "camera only"}},
            ]},
            "evidence": {
                "source": {"result": "pass", "path": self.paths["source"]},
                "import": {"result": "pass", "path": self.paths["import"]},
                "automated_runtime": {"result": "pass", "path": self.paths["runtime"]},
                "real_interaction": {"result": "pass", "path": self.paths["input"]},
            },
            "meaningful_states": ["initial", "active", "reset"],
            "engine_frames": {"initial": self.paths["initial"], "active": self.paths["active"], "reset": self.paths["reset"]},
            "review": {"reviewer": "agent", "type": "agent", "verdict": "provisional", "limitations": ["human review pending"]},
            "execution_paths": ["evidence"],
        }

    def test_complete_provisional_manifest_passes(self):
        self.assertTrue(gate.validate(self.manifest(), self.root)["ok"])

    def test_missing_frame_fails(self):
        manifest = self.manifest()
        del manifest["engine_frames"]["active"]
        report = gate.validate(manifest, self.root)
        self.assertFalse(report["ok"])
        self.assertTrue(any("engine_frames.active" in error for error in report["errors"]))

    def test_accepted_requires_human_pass(self):
        manifest = self.manifest()
        manifest["status"] = "accepted"
        manifest["review"] = {"reviewer": "agent", "type": "agent", "verdict": "pass", "limitations": []}
        report = gate.validate(manifest, self.root)
        self.assertFalse(report["ok"])
        self.assertTrue(any("accepted requires a human" in error for error in report["errors"]))

    def test_human_pass_can_accept(self):
        manifest = self.manifest()
        manifest["status"] = "accepted"
        manifest["review"] = {"reviewer": "Paul", "type": "human", "verdict": "pass", "limitations": []}
        self.assertTrue(gate.validate(manifest, self.root)["ok"])

    def test_budget_and_lineage_are_bounded(self):
        manifest = self.manifest()
        manifest["budget"]["lineage"].append({"id": "c002", "parent": "c099", "repair": {
            "source_observation": self.paths["failure"], "hypothesis": "", "scope": ""}})
        manifest["candidate_id"] = "c002"
        report = gate.validate(manifest, self.root)
        self.assertFalse(report["ok"])
        self.assertTrue(any("lineage parent" in error for error in report["errors"]))

    def test_outside_execution_path_fails(self):
        manifest = self.manifest()
        manifest["execution_paths"] = ["/tmp/undeclared"]
        report = gate.validate(manifest, self.root)
        self.assertFalse(report["ok"])
        self.assertTrue(any("out-of-workspace" in error for error in report["errors"]))


if __name__ == "__main__":
    unittest.main()
