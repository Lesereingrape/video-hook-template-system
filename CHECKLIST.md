# Project Checklist

Definition-of-done for the hook-template system. Every item is verifiable from
the repository contents or by running the validator.

- [x] Ten public reference hooks audited against the 0–3s boundary
- [x] Five reusable patterns and five opportunity gaps documented (`taxonomy.md`)
- [x] One justified category selected: consumer electronics
- [x] Reusable YAML schema defined (`schema/hook_template_schema.yaml`)
- [x] Ten structured templates in that category (`hook_templates.yaml`)
- [x] Three executable prompts derived from real templates (`prompts/`)
- [x] Ten-template ranking across four weighted dimensions (`evaluation/`)
- [x] First-test priorities and deferred templates explained with reasons
- [x] Independent Keep/Revise/Drop review workflow
- [x] Deterministic local validator (`scripts/validate_catalog.py`)
- [x] Validator dependency pinned in `requirements.txt`
- [x] Ranking scores checked against the documented weighted formula
- [x] AI-assistance and limitations disclosed

## Running the checks

```bash
python -m pip install -r requirements.txt
python scripts/validate_catalog.py
```

The validator exits non-zero and prints the first structural violation it finds,
so this checklist is machine-enforced rather than self-asserted.
