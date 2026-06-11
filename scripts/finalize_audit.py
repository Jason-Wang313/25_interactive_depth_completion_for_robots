from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
DOWNLOADS_PDF = Path("C:/Users/wangz/Downloads/25.pdf")
DESKTOP_PDF = Path("C:/Users/wangz/OneDrive/Desktop/25.pdf")
SUMMARY_JSON = ROOT / "experiments" / "results" / "summary.json"


def run(cmd: list[str]) -> tuple[int, str]:
    try:
        p = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, timeout=30)
        return p.returncode, (p.stdout + p.stderr).strip()
    except Exception as exc:
        return 999, str(exc)


def get_remote_url() -> str:
    code, out = run(["git", "remote", "get-url", "origin"])
    if code == 0 and out:
        if out.startswith("git@github.com:"):
            return "https://github.com/" + out.split(":", 1)[1].replace(".git", "")
        if out.startswith("https://github.com/"):
            return out.replace(".git", "")
        return out
    return "not available - GitHub push failed or no origin remote"


def load_summary() -> dict:
    if SUMMARY_JSON.exists():
        return json.loads(SUMMARY_JSON.read_text(encoding="utf-8"))
    return {}


def main() -> None:
    summary = load_summary()
    main_cond = summary.get("main_condition", {})
    github_url = get_remote_url()
    desktop_state = "pending orchestrator copy"
    pdf_state = "exists" if DOWNLOADS_PDF.exists() else "missing"
    audit = f"""# Final Audit

1. Chosen thesis: Robots should treat some depth holes as action targets. Hole-Conditioned Parallax Probing (HCPP) uses a small purposeful camera motion to make competing hole-depth hypotheses observably different before committing to completion.
2. Field assumption broken: Fixed-view depth completion is assumed to be enough for missing robot depth. The paper breaks that assumption for holes near occlusion boundaries.
3. New central mechanism: A hole-boundary witness operator that chooses a feasible parallax micro-motion and evidence-gated fusion, instead of passive imputation.
4. Genuine novelty: The novelty is not active perception in general or depth completion in general. It is the local identifiability framing and hole-conditioned motion primitive. Closest work makes view planning, fusion, and completion less novel.
5. Closest hostile prior work: passive sparse-to-dense depth completion, next-best-view active reconstruction, KinectFusion/volumetric fusion, scene completion, and transparent-object depth repair. See `docs/hostile_prior_work.md` for the 100-paper set.
6. Literature coverage: `docs/related_work_matrix.csv` contains the 1000-paper ranked landscape; top 300 are serious skim entries, top 240 are deep-read entries, and top 100 are hostile prior work.
7. Proof/formal-claim status if any: A simplified proposition proves first-view non-identifiability for two 2.5D scenes sharing the same observation and hole mask. It is a toy theorem, not a full real-world guarantee.
8. Strongest evidence: Controlled synthetic suite in `experiments/results/`. Main condition HCPP RMSE is {main_cond.get('hcpp_mean_rmse', 'n/a')} m versus passive {main_cond.get('passive_mean_rmse', 'n/a')} m, random {main_cond.get('random_mean_rmse', 'n/a')} m, and coverage-neutral {main_cond.get('coverage_neutral_mean_rmse', 'n/a')} m.
9. Biggest weaknesses: Synthetic-only evidence, simplified occlusion geometry, no hardware validation, minimal robot dynamics, and nearest-boundary depth cues can fail when the boundary itself is unobserved or dynamic.
10. Paper-readiness judgment: workshop / revise. The mechanism is coherent and runnable, but real-robot validation is needed for a full conference submission.
11. Exact Downloads PDF path: `C:/Users/wangz/Downloads/25.pdf` ({pdf_state}).
12. GitHub URL: {github_url}
13. Desktop copy state: {desktop_state}
"""
    DOCS.mkdir(exist_ok=True)
    (DOCS / "final_audit.md").write_text(audit, encoding="utf-8")
    lines = [
        "# Child Status",
        "",
        "Stage: final audit written",
        "",
        "Current facts:",
        f"- Downloads PDF: `{DOWNLOADS_PDF}` ({pdf_state}).",
        f"- GitHub URL: {github_url}",
        f"- Desktop copy state: {desktop_state}.",
        "",
        "Commands run:",
        "- `python scripts/finalize_audit.py`",
        "",
        "Failures and recovery:",
        "- none recorded by finalize script",
        "",
        "Next:",
        "- final response",
        "",
    ]
    (ROOT / "child_status.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
