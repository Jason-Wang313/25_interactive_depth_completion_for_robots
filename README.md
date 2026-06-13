# Interactive Depth Completion for Robots

Anonymous ICLR-style paper package for paper 25 in the robotics batch.

## What is in this repo

- `docs/related_work_matrix.csv`: ranked 1000-paper landscape.
- `docs/literature_map.md`: field map and sweep summary.
- `docs/hostile_prior_work.md`: closest 100-paper hostile set.
- `docs/novelty_boundary_map.md`: assumptions, rejected directions, selected boundary.
- `docs/novelty_decision.md`: final thesis decision.
- `docs/claims.md`: claim support and unsupported claims.
- `docs/reviewer_attacks.md`: adversarial review checklist.
- `experiments/results/`: runnable synthetic evidence, v2 boundary-cue stress, and figures.
- `paper/`: ICLR-style LaTeX source.
- `scripts/`: reproducible collection, experiment, paper, and publishing scripts.

## Reproduce

```powershell
python scripts/fetch_literature.py
python scripts/run_experiment.py
python scripts/make_paper.py
powershell -ExecutionPolicy Bypass -File scripts/build_paper.ps1
```

The canonical final PDF is `C:/Users/wangz/Downloads/25.pdf`. The build script removes local `paper/main.pdf` after copying and does not create a Desktop copy.

## V2 Hardening

- Added `experiments/results/boundary_cue_stress.csv`.
- Added `experiments/results/boundary_cue_stress_summary.json`.
- Added `experiments/results/boundary_cue_stress_table.tex` and `paper/boundary_cue_stress_table.tex`.
- Main v2 limitation: HCPP depends on reliable hole-boundary sign cues; at 50% sign error it is 0.015 m worse than the random-motion baseline.
