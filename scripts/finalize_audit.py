from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
DOWNLOADS_PDF = Path("C:/Users/wangz/Downloads/25.pdf")
DESKTOP_PDFS = [
    Path("C:/Users/wangz/OneDrive/Desktop/25.pdf"),
    Path("C:/Users/wangz/Desktop/25.pdf"),
]
SUMMARY_JSON = ROOT / "experiments" / "results" / "summary.json"
BOUNDARY_STRESS_JSON = ROOT / "experiments" / "results" / "boundary_cue_stress_summary.json"


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


def load_boundary_stress() -> list[dict]:
    if BOUNDARY_STRESS_JSON.exists():
        return json.loads(BOUNDARY_STRESS_JSON.read_text(encoding="utf-8"))
    return []


def stress_item(rows: list[dict], sign_error_rate: float) -> dict:
    for row in rows:
        if abs(float(row.get("sign_error_rate", -1.0)) - sign_error_rate) < 1e-12:
            return row
    return {}


def main() -> None:
    summary = load_summary()
    main_cond = summary.get("main_condition", {})
    boundary_stress = load_boundary_stress()
    stress_30 = stress_item(boundary_stress, 0.30)
    stress_50 = stress_item(boundary_stress, 0.50)
    github_url = get_remote_url()
    desktop_copies = [path for path in DESKTOP_PDFS if path.exists()]
    desktop_state = (
        "absent (expected; canonical PDF stays in Downloads)"
        if not desktop_copies
        else "present at " + ", ".join(str(path) for path in desktop_copies)
    )
    pdf_state = "exists" if DOWNLOADS_PDF.exists() else "missing"
    pdf_size = DOWNLOADS_PDF.stat().st_size if DOWNLOADS_PDF.exists() else 0
    local_pdf_state = "present" if (ROOT / "paper" / "main.pdf").exists() else "absent after canonical copy"
    audit = f"""# Final Audit

1. Chosen thesis: Robots should treat some depth holes as action targets. Hole-Conditioned Parallax Probing (HCPP) uses a small purposeful camera motion to make competing hole-depth hypotheses observably different before committing to completion.
2. Field assumption broken: Fixed-view depth completion is assumed to be enough for missing robot depth. The paper breaks that assumption for holes near occlusion boundaries.
3. New central mechanism: A hole-boundary witness operator that chooses a feasible parallax micro-motion and evidence-gated fusion, instead of passive imputation.
4. Genuine novelty: The novelty is not active perception in general or depth completion in general. It is the local identifiability framing and hole-conditioned motion primitive. Closest work makes view planning, fusion, and completion less novel.
5. Closest hostile prior work: passive sparse-to-dense depth completion, next-best-view active reconstruction, KinectFusion/volumetric fusion, scene completion, and transparent-object depth repair. See `docs/hostile_prior_work.md` for the 100-paper set.
6. Literature coverage: `docs/related_work_matrix.csv` contains the 1000-paper ranked landscape; top 300 are serious skim entries, top 240 are deep-read entries, and top 100 are hostile prior work.
7. Proof/formal-claim status if any: A simplified proposition proves first-view non-identifiability for two 2.5D scenes sharing the same observation and hole mask. It is a toy theorem, not a full real-world guarantee.
8. Strongest evidence: Controlled synthetic suite in `experiments/results/`. Main condition HCPP RMSE is {main_cond.get('hcpp_mean_rmse', 'n/a')} m versus passive {main_cond.get('passive_mean_rmse', 'n/a')} m, random {main_cond.get('random_mean_rmse', 'n/a')} m, and coverage-neutral {main_cond.get('coverage_neutral_mean_rmse', 'n/a')} m. V2 boundary-cue stress shows HCPP RMSE rises to {stress_30.get('mean_rmse', 'n/a')} m at 30% sign error and {stress_50.get('mean_rmse', 'n/a')} m at 50% sign error.
9. Biggest weaknesses: Synthetic-only evidence, simplified occlusion geometry, no hardware validation, minimal robot dynamics, and v2 stress shows HCPP depends on reliable hole-boundary sign cues; at high sign-error rates it can underperform random motion.
10. Paper-readiness judgment: workshop-only / strong-revise. The mechanism is coherent and runnable, but real-robot validation and a calibrated sign-confidence/fallback policy are needed for a full conference submission.
11. Exact Downloads PDF path: `C:/Users/wangz/Downloads/25.pdf` ({pdf_state}, {pdf_size} bytes).
12. GitHub URL: {github_url}
13. Desktop copy state: {desktop_state}
14. Local repository PDF state: paper/main.pdf {local_pdf_state}
"""
    DOCS.mkdir(exist_ok=True)
    (DOCS / "final_audit.md").write_text(audit, encoding="utf-8")
    lines = [
        "# Child Status",
        "",
        "Stage: v2 final audit written",
        "",
        "Current facts:",
        f"- Downloads PDF: `{DOWNLOADS_PDF}` ({pdf_state}, {pdf_size} bytes).",
        f"- V2 boundary-cue stress rows: {len(boundary_stress)} summary rows.",
        f"- GitHub URL: {github_url}",
        f"- Desktop copy state: {desktop_state}.",
        f"- Local paper/main.pdf state: {local_pdf_state}.",
        "",
        "Commands run:",
        "- `python scripts/finalize_audit.py`",
        "",
        "Failures and recovery:",
        "- none recorded by finalize script",
        "",
        "Next:",
        "- commit and push v2 hardening, then update batch trackers",
        "",
    ]
    (ROOT / "child_status.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
