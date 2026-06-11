# Claims

| Claim | Status | Support | Risk |
|---|---|---|---|
| Single-view depth completion is non-identifiable for certain hole masks near occlusion boundaries. | Formal toy claim supported. | The construction in the paper gives two scenes with identical first observations and different hole depths. | The proof is for a simplified pinhole/opaque-boundary model. |
| A hole-conditioned parallax action can distinguish those hypotheses with a small feasible lateral motion. | Supported in toy model and simulation. | `scripts/run_experiment.py` evaluates sign-conditioned motions and visibility. | Requires a visible boundary cue and enough motion budget. |
| HCPP is not just a larger completion model or a benchmark. | Supported by mechanism design and novelty map. | The method changes the central operation from passive imputation to active witness generation. | Closest NBV papers may argue the score is a special case of information gain. |
| HCPP improves hole RMSE over passive fill, random motion, and a coverage-neutral motion in the synthetic suite. | Supported in controlled simulation. | Main condition: HCPP 0.903 m vs passive 1.062 m, random 0.964 m, coverage-neutral 0.960 m. | Synthetic only. |
| HCPP is ready for direct real-robot deployment. | Unsupported and not claimed. | None. | Needs hardware validation, calibration, safety constraints, and real material failures. |
