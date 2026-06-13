# Hostile Reviewer Response

## Likely Rejection

The paper is a synthetic, low-dimensional active-perception demonstration. It does not validate HCPP on a real RGB-D camera, does not compare against learned depth completion or modern NBV planners in a shared benchmark, and originally relied on a nearly perfect boundary-side cue.

## Honest Response

We agree. The paper should not claim deployment readiness or broad superiority over active reconstruction. Its contribution is a narrow mechanism: some hole depths are not identifiable from one view, so a robot can choose a local parallax motion to create witness rays before completing the hole.

The v2 stress quantifies the most important hidden assumption. At 30% corrupted boundary signs, HCPP RMSE rises to 0.544 m; at 50%, it reaches 0.693 m and is 0.015 m worse than random motion. The supported claim is conditional on reliable boundary-side estimation or a fallback policy.

## Required Upgrade For Main-Track Submission

- Evaluate on real or photorealistic RGB-D holes.
- Add learned depth-completion and NBV baselines.
- Estimate boundary-side confidence from real sensor data.
- Add multi-direction fallback when the sign cue is ambiguous.
- Report safety constraints and robot-motion feasibility.
