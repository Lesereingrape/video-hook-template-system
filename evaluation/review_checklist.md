# Independent 0–3 Second Review Checklist

Review the rendered clip, not the prompt text. Record evidence at the listed checkpoint and return exactly one outcome: Keep, Revise, or Drop.

## Universal checks

- [ ] Duration is exactly 3.0 seconds.
- [ ] The clip contains only the opening Hook; no CTA, offer, subtitle, or full ad story.
- [ ] First-frame composition matches the template.
- [ ] The measurable attention event occurs by the template deadline.
- [ ] Product is visually identifiable by `visible_by_second`.
- [ ] Camera movement stays within the template movement limits.
- [ ] No logo, readable text, subtitle, extra product, or obvious geometry artifact is the focal point.

## Decision rules

### Keep

Use Keep only when all required checkpoints pass, the attention event is clear, the product recognition deadline is met, and no high-severity generation risk is visible.

### Revise

Use Revise when the hook mechanism is present and recoverable, but one bounded issue remains: late timing, weak framing, insufficient contrast, or a fixable camera/motion problem. State the exact timestamp and change required.

### Drop

Use Drop when the core attention event is absent, the product misses its recognition deadline, the clip becomes a full ad or static shot, or a high-severity artifact changes the product/action identity.

## Checkpoint record

```text
clip_id:
template_id:
0.0s evidence:
attention-event evidence:
product-recognition timestamp:
3.0s evidence:
visible risks:
outcome: Keep | Revise | Drop
revision, if any:
```

## Independence rule

The person or process that writes the generation prompt should not assign the outcome from the prompt alone. Reviewers must use rendered frames or video at fixed timestamps and the template's observable criteria. A separate reviewer can use the same checklist without seeing the prompt-generation rationale.
