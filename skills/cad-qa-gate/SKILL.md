---
name: cad-qa-gate
description: Run an agentic CAD design loop as a strict state machine — a mandatory per-turn status header, hard 3-iteration circuit breakers, a lean data-handoff protocol, and a numeric+visual acceptance gate driven by DESIGN_SPEC.md. Use to orchestrate any multi-agent build123d design run (single part, assembly, or chassis) so iterations stay bounded, context stays lean, and no failing geometry is ever faked to APPROVED.
---

# cad-qa-gate

The control layer for an orchestrated CAD loop. Keeps the orchestrator honest about iteration counts, prevents infinite "one more fix" loops, and stops raw CAD data from destroying the context window.

## 1. State header (every turn)
Begin EVERY orchestrator response with this, first line, inside a code fence:
```
[Phase: X | Active Target: Y | Internal QA Iteration: N/3 | Next Action: Z]
```
Increment `N` yourself. Reset to `0/3` on a new phase-stage, new concept, new component, or new revision tour. Fields that don't apply → `n/a`.

## 2. Circuit breaker (hard cap 3)
Internal QA loops are capped at **3 iterations per target**. If iteration 3 still fails a HARD gate: **HALT — do not attempt a 4th.** Report the specific geometric/numeric failure and the trade-off (e.g. "hitting mass makes the wall < 2 mm"), then wait for the human. Silent 4th attempts and faked APPROVED are forbidden.

## 3. Data-handoff protocol (lean context)
Subagents NEVER paste raw STEP data, full build123d scripts, or STL into chat. They return ONLY: file paths, measured numbers (bbox, volume, mass, clearance, interference mm³, wall thickness), boolean pass/fail, and a one-line summary. The QA agent reads the **report file + section/render images**, never the raw CAD code.

## 4. The gate (numeric blocking + visual blocking)
Read acceptance criteria from `DESIGN_SPEC.md` (the sole source of truth — edit it there first, never in a subagent). A verdict is APPROVED only if:
- NUMERIC (blocking): every measured criterion is inside tolerance. Any miss → REVISE, regardless of appearance.
- VISUAL (blocking): sections/renders read correctly AND are framed with margin (no clipping — see [[cad-section]]).
Write the outcome to `VERDICT.md`: `APPROVED` or `REVISE` + measured findings. On REVISE, pass findings to the designer verbatim.

## 5. Loop shape
```
for target in targets:
    reset N = 0
    repeat:
        designer builds/revises  (N += 1)         # returns paths + numbers only
        orchestrator eyeballs the section/render
        QA gates against DESIGN_SPEC -> VERDICT
    until APPROVED or N == 3
    if N == 3 and not APPROVED: HALT + report + wait   # circuit breaker
```

## 6. External gates
Client/human decision points (concept selection, mapping confirmation, dimension sign-off, revision-tour feedback) are HARD PAUSES. Wait for the human; never assume the choice.

## 7. Honesty
A halted target with a stated trade-off is a valid outcome. Report failures faithfully — wrong mass, unavoidable interference, an assumption that couldn't be reconciled. Never round a fail to PASS.

## Companion skills
[[step-registry]] (import/place/swap components) · [[interference-check]] (clash gate) · [[printability-check]] (manufacturability gate) · [[cad-section]] (non-clipping section images).
