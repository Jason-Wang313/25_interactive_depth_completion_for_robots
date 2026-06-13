# Submission Readiness Decision

Decision: workshop-only / strong-revise.

## Why Not Submit-Ready

- Evidence is synthetic and one-dimensional.
- The central boundary-side sign cue is assumed rather than perceived.
- V2 shows HCPP can underperform random motion when sign cues are badly corrupted.
- There is no hardware validation, learned completion baseline, or NBV benchmark comparison.

## Why Not Kill

- The first-view non-identifiability argument is crisp and honest.
- The mechanism is distinct from passive completion and global NBV when framed as local witness motion.
- The v2 stress makes the failure boundary explicit rather than hiding it.

## Required Next Work

- Add calibrated sign confidence from realistic depth/RGB observations.
- Use a multi-direction fallback when the sign cue is uncertain.
- Compare against learned depth completion and next-best-view methods.
- Validate on real or photorealistic RGB-D holes near robot-relevant contact regions.
