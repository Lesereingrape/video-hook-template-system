# Project Process and Presentation Notes

## What was built

This project turns the first three seconds of an e-commerce video into reusable, structured data. It starts with a public reference gallery audit, extracts reusable Hook patterns, selects consumer electronics as the working category, defines a data contract, creates ten templates, derives three prompts, and ranks the catalog for testing.

## Complete build sequence

1. **Repository scaffold** — established the 0–3 second boundary, directories, draft deliverables, and honest Git workflow.
2. **gallery audit** — reviewed ten public Hook entries and recorded first frame, motion, camera behavior, product timing, attention mechanism, category fit, generation risk, and Keep/Revise/Drop decisions.
3. **Taxonomy** — grouped observations into product-present proof, problem-first reveal, interaction-first, transformation-first, and motion interruption; identified five opportunity gaps.
4. **Schema** — formalized required fields, timing rules, product recognition deadlines, prompt variables, negative constraints, risks, and independent review criteria.
5. **Catalog** — created ten consumer-electronics templates with source traceability and exactly one opening action each.
6. **Prompt and evaluation layer** — created three executable prompts, scored all ten templates, selected three first tests, and documented a rendered-result review checklist.
7. **Final quality gate** — added a deterministic local validator, removed a duplicate YAML key, documented limitations, and consolidated the handoff.

## How to present the project

Start with the problem: a useful hook is not a random video idea; it is a repeatable opening structure that can be prompted and reviewed. Then explain the traceability chain:

`gallery observation → taxonomy pattern → opportunity gap → structured template → executable prompt → independent review`

Use `electronics_alignment_snap_001` as the simplest walkthrough. Explain its first frame, one alignment action, 1.5-second attention deadline, SKU variables, negative constraints, and Keep/Revise/Drop rules. Then contrast it with `electronics_problem_to_product_floor_006` to show why delayed reveal needs a hard 2.0-second product deadline.

## Important limitations to state honestly

- The audit uses public reference card names and preview references; it does not claim access to internal prompts, conversion data, or APIs.
- Ranking scores are structured hypotheses, not measured performance.
- The validator checks data quality, not whether a model-generated video is visually successful.
- No generated clips are presented as evidence in this repository.
- The system is intentionally scoped to the opening three seconds, not a complete advertisement.

## AI assistance disclosure

AI tools were used as an implementation and drafting assistant for organizing observations, proposing field structures, generating first-pass wording, and checking consistency. Human-directed decisions were retained for the category choice, audit boundary, taxonomy, risk trade-offs, ranking priorities, and final review rules. Generic ideas were narrowed or rejected when they were not traceable to the gallery, were too broad for three seconds, depended on unreadable text, or introduced unbounded generation risk.

The final artifacts should be described as a reasoned system design, not as an automatically generated list. The important work is the evidence chain, constraints, prioritization, and separation between generation and evaluation.

## With one more week

I would run a small labeled generation study across the Top 3 templates, collect timestamped Keep/Revise/Drop judgments from independent reviewers, calibrate the scoring weights against observed failure rates, and add category-specific validators for screen text, object identity, and product reveal timing. I would also test whether a single template can transfer between visually different SKUs without weakening the attention event.