# Video Hook Template System

A small, structured-data system for the first **0–3 seconds** of e-commerce
short videos: turn scattered "hook" ideas into a reusable, promptable, and
independently reviewable catalog instead of one-off creative guesses.

The premise: a good opening is not a random video idea — it is a *repeatable
structure* that can be specified as data, generated from a prompt, and graded
against fixed checkpoints. This repo makes that loop explicit and
machine-checkable.

## Core traceability chain

```
reference-gallery audit → taxonomy pattern → opportunity gap → structured template → executable prompt → independent review
```

Every template must trace back to an audited observation and a named gap, so
nothing enters the catalog as an ungrounded idea.

## Scope

- Only the first 0–3 seconds are in scope.
- Output is reusable Hook Template **data**, not a full ad script.
- The worked category is **consumer electronics**.
- No internal APIs, paid generation keys, or proprietary performance data are
  used; mock or inferred assumptions are labeled as such.

## Layout

- `audit/audit_matrix.csv` — 10 reference hooks with first frame, motion, camera
  behavior, product timing, attention mechanism, category fit, generation risk,
  and a Keep/Revise/Drop decision.
- `taxonomy.md` — 5 observed hook patterns and 5 opportunity gaps.
- `schema/hook_template_schema.yaml` — the reusable contract: fields, timing
  boundaries, risks, and review outcomes.
- `hook_templates.yaml` — 10 structured templates in one category.
- `prompts/` — 3 executable video-generation prompts derived from templates.
- `evaluation/` — ranking method, ranked CSV, and an independent 0–3s review
  checklist.
- `scripts/validate_catalog.py` — a deterministic local validator (audit anchors,
  catalog structure, prompt traceability, ranking math).
- `PROCESS.md` — build narrative, limitations, and AI-tooling disclosure.

## What the audit found

Five reusable opening structures recur across the reference hooks:

1. **Product-present proof** — the product is visible immediately and performs one
   compact action.
2. **Problem-first reveal** — a visible pain state creates curiosity before the
   product enters.
3. **Interaction-first** — a hand, animal, or object interaction supplies the first
   attention event.
4. **Transformation-first** — a visible state change creates contrast within three
   seconds.
5. **Motion interruption** — a quick entry, placement, stretch, or adjustment
   interrupts passive scrolling.

The clearest opportunities are tighter delayed-reveal deadlines, single-action
proofs, material/texture-first electronics hooks, explicit motion-scale rules, and
reviewable negative constraints for text, screens, hands, liquids, hinges, and
small objects.

## Why consumer electronics

The audit contains a strong cluster of reusable functional structures — wireless
charger, tablet stand, portable blender, air fryer, desk lamp, robot vacuum — and
it surfaces generation risks that convert cleanly into concrete prompt constraints
and review checks: screen text, hinge geometry, liquids, navigation, controls, and
product identity.

## Schema design

Each template must define: source traceability; hook type and one observable
opening action; applicable products and exclusions; product-presence mode with a
latest-recognition deadline; first-frame composition; a continuous 0–3s timeline;
camera movement and limits; prompt variables; negative constraints; generation
risks and mitigations; and independent Keep / Revise / Drop criteria. This makes
each hook readable as data instead of a vague creative idea.

## Prompts and evaluation

Three executable prompts:

- `prompt_01_alignment_snap.yaml` — immediate product-present proof.
- `prompt_02_problem_floor_reveal.yaml` — delayed product reveal with a hard 2.0s
  deadline.
- `prompt_03_macro_surface_push.yaml` — texture-first material reveal.

Ranking uses four dimensions — expected attention, SKU reusability, generation
feasibility, and category fit — weighted and summed in `evaluation/ranking.csv`.
Generation and review are intentionally **separate**: a writer turns template
fields into a prompt; a reviewer judges rendered evidence at fixed checkpoints
without grading the prompt text itself.

## Local validation

The validator is deterministic and calls no API:

```bash
python -m pip install -r requirements.txt
python scripts/validate_catalog.py
```

It checks: exactly 10 catalog templates; exactly 10 audit rows with explicit
reference-card anchors; unique IDs, required fields, continuous 0–3s timelines,
reveal deadlines, risks and review rules; exactly 3 prompts each sourced from a
real template; and ranking coverage, order, score range, and weighted-score math.

## Honesty about limits

- Ranking scores are structured ordinal hypotheses from the audit, **not**
  measured conversion rates.
- The validator checks data quality — never whether a generated clip is visually
  good.
- No generated clips are presented as evidence here.
- The system is scoped to the opening three seconds, not a full advertisement.

**AI-assistance note:** AI tooling helped organize observations, draft field
structures, and check consistency. Direction-setting — category choice, audit
boundary, taxonomy, risk trade-offs, ranking priorities, and review rules — was
human. The artifacts are a reasoned system design, not an auto-generated list.

## License

MIT
