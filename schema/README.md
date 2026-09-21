# Hook Template Schema

The contract in `hook_template_schema.yaml` is the source of truth for the ten catalog entries.

## Why these fields exist

- `source_traceability` forces every new template to respond to the gallery audit rather than become an isolated video idea.
- `product_presence.visible_by_second` converts delayed product reveal into a reviewable deadline.
- `timeline_0_3s` makes the hook boundary explicit and prevents full-ad scope creep.
- `prompt_variables` separates reusable SKU data from the fixed hook structure.
- `negative_constraints` and `generation_risks` turn common generation failures into prompt and review inputs.
- `review_rules` requires independent Keep, Revise, and Drop outcomes.

## Catalog authoring rule

Every catalog entry must satisfy the required fields, use the `consumer_electronics` category, cover exactly 0.0–3.0 seconds, and include at least two concrete criteria for each review outcome. The final catalog will contain exactly ten entries.

## Generation versus evaluation

The generation side uses the frame, timeline, camera, variables, and negative constraints. The evaluation side checks the rendered result at fixed time checkpoints against the recognition standard, measurable attention event, risks, and review criteria. This separation prevents a prompt from receiving a good score merely because it is well written.