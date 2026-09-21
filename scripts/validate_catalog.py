"""Deterministic local validator for the Video Hook Template catalog.

This script validates structure only. It does not call an API, render video, or
claim that a generated clip will perform well.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Any

try:
    import yaml
except ModuleNotFoundError as exc:
    raise SystemExit(
        "Missing dependency: PyYAML. Run `python -m pip install -r requirements.txt` "
        "from the repository root, then rerun this validator."
    ) from exc


REQUIRED_FIELDS = {
    "template_id",
    "version",
    "category",
    "source_traceability",
    "hook_type",
    "objective",
    "applicable_products",
    "product_presence",
    "first_frame",
    "timeline_0_3s",
    "camera",
    "attention_mechanism",
    "prompt_variables",
    "negative_constraints",
    "generation_risks",
    "review_rules",
}
REVIEW_OUTCOMES = {"keep_criteria", "revise_criteria", "drop_criteria"}
ALLOWED_HOOK_TYPES = {
    "product_present_proof",
    "problem_first_reveal",
    "interaction_first",
    "transformation_first",
    "motion_interrupt",
    "texture_first",
}
RANKING_WEIGHTS = {
    "attention_potential": 0.30,
    "sku_reusability": 0.25,
    "generation_feasibility": 0.25,
    "category_fit": 0.20,
}
RANKING_COLUMNS = {
    "rank",
    "template_id",
    "attention_potential",
    "sku_reusability",
    "generation_feasibility",
    "category_fit",
    "weighted_score",
    "test_priority",
    "reason",
}
AUDIT_COLUMNS = {
    "audit_id",
    "source_reference",
    "hook_summary",
    "first_frame",
    "motion_0_3s",
    "camera_behavior",
    "product_timing",
    "attention_mechanism",
    "applicable_category",
    "generation_risk",
    "decision",
    "reasoning",
    "reusable_pattern",
}


def fail(message: str) -> None:
    raise ValueError(message)


def validate_timeline(template_id: str, timeline: list[dict[str, Any]]) -> None:
    if len(timeline) < 2:
        fail(f"{template_id}: timeline needs at least two segments")
    previous_end = 0.0
    for index, segment in enumerate(timeline):
        required = {"start_seconds", "end_seconds", "action", "product_state", "review_checkpoint"}
        missing = required - segment.keys()
        if missing:
            fail(f"{template_id}: timeline segment {index} missing {sorted(missing)}")
        start = float(segment["start_seconds"])
        end = float(segment["end_seconds"])
        if abs(start - previous_end) > 1e-9:
            fail(f"{template_id}: timeline gap/overlap before segment {index}")
        if end <= start:
            fail(f"{template_id}: timeline segment {index} has non-positive duration")
        previous_end = end
    if abs(previous_end - 3.0) > 1e-9:
        fail(f"{template_id}: timeline ends at {previous_end}, expected 3.0")


def validate_catalog(path: Path) -> set[str]:
    document = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(document, dict) or not isinstance(document.get("templates"), list):
        fail("catalog must contain a templates list")

    templates = document["templates"]
    if len(templates) != 10:
        fail(f"expected exactly 10 templates, found {len(templates)}")

    ids: set[str] = set()
    for template in templates:
        if not isinstance(template, dict):
            fail("each template must be a mapping")
        template_id = template.get("template_id", "<missing>")
        missing = REQUIRED_FIELDS - template.keys()
        if missing:
            fail(f"{template_id}: missing fields {sorted(missing)}")
        if template_id in ids:
            fail(f"duplicate template_id: {template_id}")
        ids.add(template_id)
        if template["category"] != "consumer_electronics":
            fail(f"{template_id}: category must be consumer_electronics")
        if template["hook_type"] not in ALLOWED_HOOK_TYPES:
            fail(f"{template_id}: unsupported hook_type")
        trace = template["source_traceability"]
        for key in ("audited_hook_ids", "taxonomy_patterns", "opportunity_gaps"):
            if not trace.get(key):
                fail(f"{template_id}: source_traceability.{key} is empty")
        presence = template["product_presence"]
        deadline = float(presence["visible_by_second"])
        if not 0.0 <= deadline <= 3.0:
            fail(f"{template_id}: visible_by_second outside 0–3")
        validate_timeline(template_id, template["timeline_0_3s"])
        if len(template["negative_constraints"]) < 4:
            fail(f"{template_id}: fewer than four negative constraints")
        constraints = " ".join(template["negative_constraints"]).lower()
        if "logo" not in constraints or not any(token in constraints for token in ("text", "screen", "display")):
            fail(f"{template_id}: logo and text/screen constraints are required")
        risks = template["generation_risks"]
        if len(risks) < 2 or any(not all(key in risk for key in ("risk", "severity", "mitigation")) for risk in risks):
            fail(f"{template_id}: generation risks are incomplete")
        rules = template["review_rules"]
        if set(rules) != REVIEW_OUTCOMES or any(len(rules[key]) < 2 for key in REVIEW_OUTCOMES):
            fail(f"{template_id}: Keep/Revise/Drop rules are incomplete")

    print(f"VALID: {path} ({len(templates)} templates)")
    return ids


def validate_prompts(directory: Path, template_ids: set[str]) -> None:
    prompt_paths = sorted(directory.glob("*.yaml"))
    if len(prompt_paths) != 3:
        fail(f"expected exactly 3 executable prompts, found {len(prompt_paths)}")

    for path in prompt_paths:
        document = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(document, dict):
            fail(f"{path}: prompt file must contain a mapping")
        source_template_id = document.get("source_template_id")
        if source_template_id not in template_ids:
            fail(f"{path}: source_template_id does not exist in catalog")
        if not document.get("prompt") or not document.get("review_anchor"):
            fail(f"{path}: prompt and review_anchor are required")

    print(f"VALID: {directory} ({len(prompt_paths)} prompts)")


def validate_ranking(path: Path, template_ids: set[str]) -> None:
    rows = list(csv.DictReader(path.read_text(encoding="utf-8").splitlines()))
    if not rows:
        fail(f"{path}: ranking file is empty")
    missing_columns = RANKING_COLUMNS - set(rows[0].keys())
    if missing_columns:
        fail(f"{path}: missing columns {sorted(missing_columns)}")
    if len(rows) != len(template_ids):
        fail(f"{path}: expected {len(template_ids)} ranking rows, found {len(rows)}")

    ranked_ids: set[str] = set()
    previous_score = float("inf")
    for index, row in enumerate(rows, start=1):
        template_id = row["template_id"]
        if template_id not in template_ids:
            fail(f"{path}: unknown template_id {template_id}")
        if template_id in ranked_ids:
            fail(f"{path}: duplicate template_id {template_id}")
        ranked_ids.add(template_id)
        if int(row["rank"]) != index:
            fail(f"{path}: row {index} has rank {row['rank']}")

        component_scores = [float(row[column]) for column in RANKING_WEIGHTS]
        if any(score < 1 or score > 5 for score in component_scores):
            fail(f"{path}: {template_id} has a component score outside 1..5")
        expected_score = sum(float(row[column]) * weight for column, weight in RANKING_WEIGHTS.items())
        listed_score = float(row["weighted_score"])
        if abs(listed_score - round(expected_score, 2)) > 1e-9:
            fail(
                f"{path}: {template_id} weighted_score is {listed_score:.2f}, "
                f"expected {expected_score:.2f}"
            )
        if listed_score > previous_score:
            fail(f"{path}: {template_id} is ranked above a higher-scoring template")
        previous_score = listed_score

    if ranked_ids != template_ids:
        fail(f"{path}: ranking IDs do not match catalog IDs")

    print(f"VALID: {path} ({len(rows)} ranked templates)")


def validate_audit(path: Path) -> None:
    rows = list(csv.DictReader(path.read_text(encoding="utf-8").splitlines()))
    if len(rows) != 10:
        fail(f"{path}: expected 10 audited hooks, found {len(rows)}")
    missing_columns = AUDIT_COLUMNS - set(rows[0].keys())
    if missing_columns:
        fail(f"{path}: missing columns {sorted(missing_columns)}")

    audit_ids: set[str] = set()
    for row in rows:
        audit_id = row["audit_id"]
        if audit_id in audit_ids:
            fail(f"{path}: duplicate audit_id {audit_id}")
        audit_ids.add(audit_id)
        if row["decision"] not in {"Keep", "Revise", "Drop"}:
            fail(f"{path}: {audit_id} has unsupported decision {row['decision']}")
        if "https://" in row["source_reference"]:
            fail(f"{path}: {audit_id} still uses a placeholder-style source reference")
        if not row["source_reference"].startswith("Reference card: "):
            fail(f"{path}: {audit_id} source_reference should cite a reference card anchor")

    print(f"VALID: {path} ({len(rows)} audited hooks)")


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate the Hook Template catalog")
    parser.add_argument("catalog", nargs="?", default="hook_templates.yaml", type=Path)
    args = parser.parse_args()
    validate_audit(Path("audit/audit_matrix.csv"))
    template_ids = validate_catalog(args.catalog)
    validate_prompts(Path("prompts"), template_ids)
    validate_ranking(Path("evaluation/ranking.csv"), template_ids)


if __name__ == "__main__":
    main()
