# Child Status

Stage: complete

Current facts:
- Literature matrix: `docs/related_work_matrix.csv` with 1000 rows.
- Required docs: `docs/literature_map.md`, `docs/hostile_prior_work.md`, `docs/novelty_boundary_map.md`, `docs/novelty_decision.md`, `docs/claims.md`, `docs/reviewer_attacks.md`, and `docs/final_audit.md`.
- Runnable evidence: `scripts/run_experiment.py`, `experiments/results/episode_results.csv`, `summary.json`, `summary.md`, and plots.
- Paper source: `paper/main.tex` using official ICLR 2026 style files fetched from the ICLR Master-Template zip.
- Local build output `paper/main.pdf` was removed after copying to the required Downloads path, to satisfy the exact final-PDF output rule.
- Required Downloads PDF: `C:/Users/wangz/Downloads/25.pdf` exists, size 296951 bytes.
- Public GitHub repo: `https://github.com/Jason-Wang313/25_interactive_depth_completion_for_robots`.
- Desktop copy state in final audit: pending orchestrator copy.

Commands run:
- `python scripts/fetch_literature.py`
- `python scripts/run_experiment.py`
- `python scripts/make_paper.py`
- `pdflatex -interaction=nonstopmode -halt-on-error main.tex`
- `bibtex main`
- `pdflatex -interaction=nonstopmode -halt-on-error main.tex`
- `pdflatex -interaction=nonstopmode -halt-on-error main.tex`
- `Copy-Item -LiteralPath paper/main.pdf -Destination C:/Users/wangz/Downloads/25.pdf -Force`
- `git rm paper/main.pdf`
- `powershell -ExecutionPolicy Bypass -File scripts/publish_github.ps1`
- `git rm --cached -- data/openalex_works.jsonl`
- `python scripts/finalize_audit.py`
- `git commit -m "Add final audit and trim raw cache from HEAD"`
- `git push`

Failures and recovery:
- First LaTeX build failed on Markdown-style filename backticks with underscores in the appendix. Recovered by replacing filenames with `\texttt{...}` and rerunning pdfLaTeX/BibTeX successfully.
- First GitHub publish script attempt failed before git/GitHub actions because a trailing PowerShell backtick escaped a closing quote. Recovered by replacing that string with a format expression.
- GitHub warned that the raw OpenAlex cache was larger than the recommended file size. Recovered by removing `data/openalex_works.jsonl` from the tracked HEAD and adding an explicit ignore rule; derived matrix and docs remain tracked.
- Compliance correction: removed tracked/local `paper/main.pdf` after verifying the exact Downloads PDF exists.

Next:
- none
