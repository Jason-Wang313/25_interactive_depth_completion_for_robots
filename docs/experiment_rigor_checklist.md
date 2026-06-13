# Experiment Rigor Checklist

- [x] Main synthetic suite has deterministic regeneration.
- [x] Main condition compares passive fill, random motion, coverage-neutral motion, HCPP, and oracle sign.
- [x] Main result reports RMSE values rather than only percent improvement.
- [x] V2 stress attacks the boundary-side sign assumption.
- [x] V2 stress uses 20 seeds and 300 scenes per seed.
- [x] V2 stress reports seed-level standard deviation.
- [x] Negative boundary is explicit: at 50% sign error, HCPP is worse than random motion by 0.015 m.
- [ ] No real-robot validation.
- [ ] No high-fidelity RGB-D simulator validation.
- [ ] No learned depth-completion or NBV planner baseline.
- [ ] No physical safety or calibration experiment.

Decision: useful mechanism evidence, not full submission-ready evidence.
