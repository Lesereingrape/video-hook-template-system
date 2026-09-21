# Ranking Method

## Scoring model

Each template receives a 1–5 score on four dimensions:

- `attention_potential`: How quickly and clearly the opening creates a measurable attention event.
- `sku_reusability`: How many product forms can use the same hook structure after variable substitution.
- `generation_feasibility`: How controllable the motion, geometry, timing, and negative constraints are for a video model.
- `category_fit`: How naturally the hook expresses a consumer-electronics product behavior.

The weighted score is:

`0.30 × attention_potential + 0.25 × sku_reusability + 0.25 × generation_feasibility + 0.20 × category_fit`

Scores are deliberately ordinal estimates based on the audit and documented generation risks. They are not conversion-rate claims and do not use paid APIs or hidden proprietary data. Scores are rounded to two decimals in `ranking.csv`. When two templates share the same weighted score, the ordering uses diagnosis simplicity as the tie-breaker: a template whose likely failures are easier to identify from fixed checkpoints appears first.

## First tests

1. `electronics_alignment_snap_001` — strongest combination of immediate attention, broad SKU reuse, simple geometry, and clear review checkpoints.
2. `electronics_light_switch_snap_003` — highly controllable fixed-camera state change with strong category fit.
3. `electronics_screenless_spec_pulse_007` — tests physical functional proof while avoiding the known screen-text failure mode.

## Not first

`electronics_liquid_vortex_macro_004` will not be tested first. It has a compelling tactile mechanism, but liquid continuity, vessel identity, and the delayed reveal create too many coupled failure modes for the first experiment. It remains valuable as a later frontier test after the simpler templates establish baseline generation quality.

`electronics_problem_to_product_floor_006` is also deferred despite strong attention potential because navigation and debris continuity make it difficult to diagnose if a generation fails.
