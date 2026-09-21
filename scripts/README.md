# Local Helpers

The repository includes a deterministic validator. It checks structure, traceability, and ranking math only; it does not render clips or claim performance.

## Run

From the repository root:

```text
python -m pip install -r requirements.txt
python scripts/validate_catalog.py
```

The validator requires PyYAML, reads the audit, catalog, prompts, and ranking files, and checks:

- exactly ten audited hooks with explicit reference-card source anchors;
- exactly ten templates;
- unique IDs and one category;
- source traceability;
- continuous 0.0-3.0 second timelines;
- product reveal deadlines;
- negative constraints;
- generation risks;
- Keep, Revise, and Drop criteria;
- exactly three executable prompts, each sourced from an existing template;
- ranking coverage, rank order, score ranges, and weighted-score math.
