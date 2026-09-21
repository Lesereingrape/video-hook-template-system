# Existing Hook Audit

This directory contains the audit of ten existing hook entries from a public reference gallery.

## Audit Boundary

Only the first three seconds of each source are analyzed. Each row records the first frame, 0-3 second motion, camera behavior, product timing, attention mechanism, category fit, generation risk, Keep/Revise/Drop decision, and reusable pattern.

## Evidence Standard

The source anchors are public reference card names and preview slugs. They are not claims of access to internal prompts, production assets, APIs, or performance data.

Descriptions are limited to the opening three seconds. Later product story, CTA, conversion performance, or full-ad structure is out of scope. Interpretations are separated from directly observed structure, and uncertain details are treated conservatively.

## Audit Set

The audit set uses ten public video-generation hook entries exposed by the gallery:

- Air Fryer Demo
- Cat Water Fountain Routine
- Desk Lamp Transformation
- Pet Hair Remover Pain Hook
- Robot Vacuum Pain Hook
- Resistance Bands Demo
- Wireless Charger Demo
- Board Game Scenario
- Portable Blender Demo
- Tablet Stand Demo

## Initial Findings

- The gallery already covers product-present demonstrations, transformations, interaction-first scenes, and problem-first pain hooks.
- Functional demonstrations are generally easier to parameterize across SKUs than scenes depending on animal behavior, readable screens, or many small objects.
- Several pain hooks delay product identification. This is useful for attention, but needs a hard reveal deadline in the reusable schema.
- The strongest next step is not more generic product hero footage; it is a controlled taxonomy for problem, proof, transformation, and interaction beats with explicit generation-risk gates.

## Traceability Correction

The workflow requires the audit to drive the catalog, so the catalog uses this chain:

`audited hook -> taxonomy pattern -> opportunity gap -> catalog template`

Each final template carries source traceability, a reveal deadline, and independent review criteria. This prevents a visually attractive idea from becoming a template that cannot be prompted or consistently graded.
