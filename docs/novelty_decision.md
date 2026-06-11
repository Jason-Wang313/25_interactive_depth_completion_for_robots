# Novelty Decision

## Chosen Thesis
Robots should not complete every depth hole from a fixed observation. For holes adjacent to depth discontinuities, the right primitive is a small purposeful camera motion that makes competing depth hypotheses observably different. The paper proposes Hole-Conditioned Parallax Probing (HCPP), a completion mechanism that chooses feasible micro-motions from the geometry of the hole boundary and then fuses only the newly witnessed rays.

## Why This Survived the Sweep
The 1000-paper landscape already contains passive completion, learned shape priors, active view planning, active SLAM, transparent-object depth repair, point-cloud completion, and uncertainty-aware planning. The stronger opening is not another model or benchmark. The opening is a change in the causal order: completion is allowed to ask the robot for a new observation before committing to a depth value.

## What Would Make It Not Novel
- If the method is described merely as next-best-view with a different score.
- If the evidence only shows better interpolation.
- If the mechanism depends on a larger learned model, more data, or a benchmark.
- If the robot action is generic exploration rather than a hole-conditioned witness motion.

## Decision
Proceed with HCPP as a workshop-to-borderline-conference paper: a formal non-identifiability argument plus controlled embodied simulation can honestly support the central claim, while real-robot validation remains future work.
