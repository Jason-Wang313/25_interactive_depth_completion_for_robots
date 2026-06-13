# Reproducibility Checklist

- [x] Dependencies are listed in `requirements.txt`.
- [x] Literature artifacts are tracked as derived CSV/docs.
- [x] Main experiment script is `scripts/run_experiment.py`.
- [x] Paper generator is `scripts/make_paper.py`.
- [x] Final audit generator is `scripts/finalize_audit.py`.
- [x] Build script is `scripts/build_paper.ps1`.
- [x] Main outputs are `experiments/results/episode_results.csv`, `experiments/results/summary.json`, and generated figures.
- [x] V2 outputs are `experiments/results/boundary_cue_stress.csv`, `experiments/results/boundary_cue_stress_summary.json`, and `experiments/results/boundary_cue_stress_table.tex`.
- [x] Paper source is `paper/main.tex`.
- [x] Canonical PDF path is `C:/Users/wangz/Downloads/25.pdf`.
- [x] Local `paper/main.pdf` is removed after canonical copy.
- [x] Visible Desktop PDF copies are absent.

Recommended verification commands:

```powershell
python scripts\run_experiment.py
python scripts\make_paper.py
powershell -ExecutionPolicy Bypass -File scripts\build_paper.ps1
python scripts\finalize_audit.py
```
