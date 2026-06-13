# Experiment Summary

Synthetic 1D pinhole depth scenes model a robot RGB-D camera facing foreground occluders and background surfaces. Depth holes are placed next to occlusion boundaries, where passive interpolation can copy the wrong surface. HCPP estimates the occluder side from observed boundary depths and selects a lateral micro-motion that creates background witness rays.

## Main Condition
- Baseline: 0.1 m
- Clutter: 0.15
- Scenes: 700
- Passive mean RMSE: 1.0618 m
- Random motion mean RMSE: 0.6780 m
- Coverage-neutral motion mean RMSE: 0.6699 m
- HCPP mean RMSE: 0.3294 m
- HCPP reduction vs passive: 69.0%
- HCPP reduction vs random: 51.4%
- HCPP reduction vs coverage-neutral: 50.8%

## V2 Boundary-Cue Stress
- Stress protocol: corrupt the boundary-derived motion sign before executing the same 10 cm probe, across 20 seeds and 300 scenes per seed.
- 30% sign-error HCPP mean RMSE: 0.5440 m.
- 50% sign-error HCPP mean RMSE: 0.6931 m.
- 50% sign-error delta vs random-motion baseline: +0.0152 m.

## Files
- `episode_results.csv`: all condition-level results.
- `boundary_cue_stress.csv`: v2 sign-error stress rows.
- `boundary_cue_stress_summary.json`: v2 sign-error stress summary.
- `rmse_by_method.png`: main bar plot.
- `baseline_sensitivity.png`: motion-budget sensitivity.
- `example_scene.png`: qualitative hole example.

## Honest Scope
This is mechanism evidence, not a real-robot validation. It tests the broken assumption that depth holes can be repaired from a fixed observation and shows that directional parallax can matter under controlled occlusion geometry.
