# Submission Attack Log

Updated: 2026-06-13 04:16:24 +01:00

## Attack Rounds

1. Closest prior-work attack: next-best-view, active reconstruction, transparent-object depth repair, and passive depth completion already cover broad versions of sensing by motion. Response: keep novelty to hole-conditioned witness motion and local identifiability.
2. Baseline attack: passive interpolation is weak. Response: retain random and coverage-neutral active baselines, and keep the formal non-identifiability claim narrow.
3. Oracle-cue attack: v1 HCPP is nearly identical to the oracle sign selector, so the boundary-side cue is too clean. Response: add v2 boundary-cue sign-error stress.
4. Deployment attack: synthetic 1D pinhole geometry is not a robot system. Response: mark the paper workshop-only / strong-revise, with real hardware and sign-confidence fallback required.
5. Reproducibility attack: generated claims had a stale old result. Response: patch `scripts/run_experiment.py` so the claims row is rewritten deterministically from current summary data.

## V2 Outcome

The v2 stress narrows the paper: HCPP is useful when boundary-side estimation is reliable. At 50% sign error, HCPP reaches 0.693 m RMSE and is 0.015 m worse than the v1 random-motion baseline.
