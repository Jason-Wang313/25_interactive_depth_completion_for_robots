# Child Status

Stage: compiled PDF verified

Current facts:
- Literature matrix exists with 1000 rows.
- Required docs exist except `docs/final_audit.md`, which is written after GitHub publication status is known.
- pdfLaTeX/BibTeX/pdfLaTeX/pdfLaTeX completed with exit codes `0/0/0/0`.
- Final PDF copied to `C:/Users/wangz/Downloads/25.pdf` with size 296951 bytes.

Commands run:
- `python scripts/fetch_literature.py`
- `python scripts/run_experiment.py`
- `python scripts/make_paper.py`
- `pdflatex -interaction=nonstopmode -halt-on-error main.tex`
- `bibtex main`
- `pdflatex -interaction=nonstopmode -halt-on-error main.tex`
- `pdflatex -interaction=nonstopmode -halt-on-error main.tex`
- `Copy-Item -LiteralPath paper/main.pdf -Destination C:/Users/wangz/Downloads/25.pdf -Force`

Failures and recovery:
- First LaTeX build failed on Markdown-style filename backticks with underscores.
- Recovered by replacing appendix filenames with `\texttt{...}` and rerunning the build successfully.
- First GitHub publish script attempt failed before any git/GitHub action because a trailing PowerShell backtick escaped a closing quote.
- Recovered by replacing that status string with a PowerShell format expression.

Next:
- Create/push public GitHub repo or document authentication/push failure, then write final audit.
