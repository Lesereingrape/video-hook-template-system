# Hook Taxonomy and Opportunity Gaps

## Scope

This taxonomy is derived from the ten public Video Generation Hook entries documented in `audit/audit_matrix.csv`. It describes reusable opening structures, not full ad formats. Every pattern stops at the opening three seconds.

## Existing patterns in the gallery

### 1. Product-present proof

The product is recognizable in the first frame and performs one compact, legible action: placement, alignment, adjustment, or operation. Examples include the wireless charger, tablet stand, portable blender, and air fryer demonstrations.

**Strength:** high product clarity and strong SKU substitution potential.

**Risk:** the opening can feel like a generic product demo if the first-second action is not visually distinct.

### 2. Problem-first reveal

The opening begins with a recognizable pain state, then introduces the product or its action. The pet-hair remover and robot-vacuum pain hooks represent this structure.

**Strength:** creates an unanswered question before the product reveal.

**Risk:** the video can become an unbranded problem clip if the product is not identifiable by a fixed deadline.

### 3. Interaction-first

The first attention event is a human, animal, or object interaction with the product. The cat water fountain, resistance bands, and board-game scenario use this family.

**Strength:** gives the product a use context rather than presenting a passive object.

**Risk:** hands, animal anatomy, small objects, and interaction continuity increase generation failure risk.

### 4. Transformation-first

The opening makes a visible state change the reason to continue watching: lighting changes, ingredients move toward a blended state, or a scene shifts from problem to improved state.

**Strength:** creates strong visual contrast within a short time window.

**Risk:** continuity of lighting, materials, liquids, and object identity can drift.

### 5. Motion interruption

The hook begins with a quick movement, placement, stretch, or entry that interrupts passive scrolling. This is often a modifier layered onto product-present, proof, or interaction-first structures rather than a complete category on its own.

**Strength:** gives the first second a measurable attention event.

**Risk:** fast motion can hide the product or create blur and geometry artifacts.

## Gaps and opportunities

### Gap A — Texture/material-first for electronics

The current audit is dominated by utility, problem, and interaction beats. A controlled macro material or surface-detail opening could make electronics, accessories, and appliances feel tactile before the functional proof. It should still reveal the product identity by a defined deadline.

### Gap B — Delayed reveal with a hard deadline

Problem-first hooks delay product visibility, but the audit does not provide a consistent reveal rule. New templates should specify `visible_by_second` and fail review if the product is not identifiable by that time.

### Gap C — Single-action proof instead of broad demonstrations

Several product demos could be made more reusable by reducing them to one observable proof action, such as “aligns,” “folds,” “lights,” or “blends.” This limits prompt ambiguity and makes Keep/Revise/Drop decisions more consistent.

### Gap D — Motion scale and camera interruption

The gallery uses product and context shots, but there is room for explicit scale contrast: a macro detail, a sudden push-in, or a clean object entry that changes the visual scale within three seconds. This should be designed with safe camera limits rather than generic “dynamic camera” language.

### Gap E — Reviewable negative constraints

Screen text, small pieces, hands, liquid, hair, and animal behavior recur as generation risks. A reusable template should turn these risks into explicit negative constraints and observable review checks instead of leaving them as prose warnings.

## Category decision

The catalog category will be **consumer electronics**.

This category is selected because the audit contains the strongest cluster of reusable functional structures: wireless charger, tablet stand, portable blender, air fryer, desk lamp, and robot vacuum. It supports multiple SKU forms while making product timing and proof criteria measurable. The category also exposes useful generation risks—screens, hinges, liquids, navigation, and controls—that can be converted into concrete prompt constraints and independent review rules.

The catalog will not claim that every template fits every electronic SKU. Each entry will state its applicable product forms and exclusions.

## Traceability commitments

Each final template will cite one or more source patterns from this document and one opportunity gap. This prevents the ten templates from becoming an unrelated list of video ideas.