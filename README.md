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
- `experiments/results/`: runnable synthetic evidence and figures.
- `paper/`: ICLR-style LaTeX source.
- `scripts/`: reproducible collection, experiment, paper, and publishing scripts.

## Reproduce

```powershell
python scripts/fetch_literature.py
python scripts/run_experiment.py
python scripts/make_paper.py
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The final PDF is copied to `C:/Users/wangz/Downloads/25.pdf` by the build step when compilation succeeds.
