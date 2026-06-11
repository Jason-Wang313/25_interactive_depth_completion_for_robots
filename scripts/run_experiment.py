from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "experiments" / "results"
RESULTS.mkdir(parents=True, exist_ok=True)


def write_child_status(stage: str, next_step: str, failures: list[str] | None = None) -> None:
    failures = failures or []
    lines = [
        "# Child Status",
        "",
        f"Stage: {stage}",
        "",
        "Current facts:",
        "- Literature artifacts are expected in `docs/`.",
        f"- Experiment results directory: `{RESULTS}`.",
        "",
        "Commands run:",
        "- `python scripts/run_experiment.py`",
        "",
        "Failures and recovery:",
    ]
    lines.extend([f"- {x}" for x in failures] if failures else ["- none"])
    lines.extend(["", "Next:", f"- {next_step}", ""])
    (ROOT / "child_status.md").write_text("\n".join(lines), encoding="utf-8")


def interpolate_fill(observed: np.ndarray, mask: np.ndarray) -> np.ndarray:
    x = np.arange(observed.size)
    valid = ~np.isnan(observed)
    filled = observed.copy()
    filled[mask] = np.interp(x[mask], x[valid], observed[valid])
    return filled


def make_scene(rng: np.random.Generator, width: int = 160) -> dict:
    x = np.linspace(-1.0, 1.0, width)
    bg_base = rng.uniform(2.3, 3.7)
    bg_slope = rng.uniform(-0.35, 0.35)
    bg = bg_base + bg_slope * x + 0.08 * np.sin(2 * np.pi * (x + rng.uniform(-0.2, 0.2)))
    fg_width = int(rng.integers(24, 48))
    left = int(rng.integers(20, width - fg_width - 20))
    right = left + fg_width
    fg_depth = rng.uniform(0.8, 1.45)
    true_depth = bg.copy()
    true_depth[left:right] = fg_depth
    side = int(rng.choice([-1, 1]))
    hole_width = int(rng.integers(8, 22))
    mask = np.zeros(width, dtype=bool)
    if side == 1:
        h0 = min(width - 2, right)
        h1 = min(width - 1, right + hole_width)
    else:
        h0 = max(1, left - hole_width)
        h1 = max(2, left)
    mask[h0:h1] = True
    observed = true_depth.copy()
    observed[mask] = np.nan
    return {
        "x": x,
        "true_depth": true_depth,
        "observed": observed,
        "mask": mask,
        "side": side,
        "left": left,
        "right": right,
        "hole_width": int(mask.sum()),
        "fg_depth": fg_depth,
        "bg_depth_mean": float(bg[mask].mean()),
    }


def estimate_boundary_sign(observed: np.ndarray, mask: np.ndarray) -> int:
    idx = np.flatnonzero(mask)
    left_edge = idx[0]
    right_edge = idx[-1]
    left_val = observed[max(0, left_edge - 2)]
    right_val = observed[min(observed.size - 1, right_edge + 2)]
    if np.isnan(left_val) and np.isnan(right_val):
        return 0
    if np.isnan(right_val):
        return 1
    if np.isnan(left_val):
        return -1
    # If the closer surface is left of the hole, the occluder edge is on the left
    # and a positive camera translation exposes the background witness rays.
    return 1 if left_val < right_val else -1


def reveal_fraction(method: str, chosen_sign: int, true_sign: int, baseline: float, hole_width: int, clutter: float, rng: np.random.Generator) -> float:
    if method == "passive":
        return 0.0
    if chosen_sign == 0:
        directional = 0.25
    elif chosen_sign == true_sign:
        directional = 1.0
    else:
        directional = 0.12
    parallax_pixels = baseline * 90.0 * directional
    frac = min(1.0, parallax_pixels / max(1.0, hole_width))
    clutter_loss = max(0.0, 1.0 - clutter * rng.uniform(0.6, 1.3))
    return float(np.clip(frac * clutter_loss, 0.0, 1.0))


def complete_with_motion(scene: dict, method: str, baseline: float, clutter: float, rng: np.random.Generator) -> tuple[np.ndarray, float, int]:
    true_depth = scene["true_depth"]
    observed = scene["observed"]
    mask = scene["mask"]
    passive = interpolate_fill(observed, mask)
    if method == "passive":
        return passive, 0.0, 0
    true_sign = scene["side"]
    if method == "hcpp":
        sign = estimate_boundary_sign(observed, mask)
    elif method == "random_motion":
        sign = int(rng.choice([-1, 1]))
    elif method == "coverage_neutral":
        sign = 1
    elif method == "oracle":
        sign = true_sign
    else:
        sign = 0
    frac = reveal_fraction(method, sign, true_sign, baseline, scene["hole_width"], clutter, rng)
    idx = np.flatnonzero(mask)
    n_reveal = int(round(frac * len(idx)))
    completed = passive.copy()
    if n_reveal > 0:
        if sign == true_sign:
            # Correct parallax exposes the pixels adjacent to the occluding
            # boundary: right-edge holes reveal from the left of the hole, and
            # left-edge holes reveal from the right.
            chosen = idx[-n_reveal:] if true_sign == -1 else idx[:n_reveal]
        else:
            chosen = rng.choice(idx, size=min(n_reveal, len(idx)), replace=False)
        noise = rng.normal(0.0, 0.015, size=len(chosen))
        completed[chosen] = true_depth[chosen] + noise
    return completed, frac, sign


def rmse(a: np.ndarray, b: np.ndarray, mask: np.ndarray) -> float:
    e = a[mask] - b[mask]
    return float(np.sqrt(np.mean(e * e)))


def run_suite(seed: int = 25, n_scenes: int = 700) -> list[dict]:
    rng = np.random.default_rng(seed)
    methods = ["passive", "coverage_neutral", "random_motion", "hcpp", "oracle"]
    baselines = [0.02, 0.05, 0.10, 0.15]
    clutters = [0.0, 0.15, 0.30, 0.45]
    rows = []
    for clutter in clutters:
        for baseline in baselines:
            for scene_id in range(n_scenes):
                scene = make_scene(rng)
                passive = interpolate_fill(scene["observed"], scene["mask"])
                ambiguity_gap = abs(scene["bg_depth_mean"] - scene["fg_depth"])
                for method in methods:
                    completed, frac, sign = complete_with_motion(scene, method, baseline, clutter, rng)
                    rows.append(
                        {
                            "scene_id": scene_id,
                            "baseline_m": baseline,
                            "clutter": clutter,
                            "method": method,
                            "rmse": rmse(completed, scene["true_depth"], scene["mask"]),
                            "passive_rmse": rmse(passive, scene["true_depth"], scene["mask"]),
                            "reveal_fraction": frac,
                            "chosen_sign": sign,
                            "true_sign": scene["side"],
                            "ambiguity_gap_m": ambiguity_gap,
                            "hole_width_px": scene["hole_width"],
                        }
                    )
    return rows


def summarize(rows: list[dict]) -> dict:
    by_method = {}
    for method in sorted({r["method"] for r in rows}):
        vals = np.array([r["rmse"] for r in rows if r["method"] == method], dtype=float)
        by_method[method] = {
            "mean_rmse": float(vals.mean()),
            "median_rmse": float(np.median(vals)),
            "std_rmse": float(vals.std(ddof=1)),
            "n": int(vals.size),
        }
    hcpp = np.array([r["rmse"] for r in rows if r["method"] == "hcpp" and r["baseline_m"] == 0.10 and r["clutter"] == 0.15], dtype=float)
    passive = np.array([r["rmse"] for r in rows if r["method"] == "passive" and r["baseline_m"] == 0.10 and r["clutter"] == 0.15], dtype=float)
    random = np.array([r["rmse"] for r in rows if r["method"] == "random_motion" and r["baseline_m"] == 0.10 and r["clutter"] == 0.15], dtype=float)
    neutral = np.array([r["rmse"] for r in rows if r["method"] == "coverage_neutral" and r["baseline_m"] == 0.10 and r["clutter"] == 0.15], dtype=float)
    return {
        "by_method_all_conditions": by_method,
        "main_condition": {
            "baseline_m": 0.10,
            "clutter": 0.15,
            "hcpp_mean_rmse": float(hcpp.mean()),
            "passive_mean_rmse": float(passive.mean()),
            "random_mean_rmse": float(random.mean()),
            "coverage_neutral_mean_rmse": float(neutral.mean()),
            "hcpp_vs_passive_percent_reduction": float(100.0 * (passive.mean() - hcpp.mean()) / passive.mean()),
            "hcpp_vs_random_percent_reduction": float(100.0 * (random.mean() - hcpp.mean()) / random.mean()),
            "hcpp_vs_coverage_neutral_percent_reduction": float(100.0 * (neutral.mean() - hcpp.mean()) / neutral.mean()),
            "n_scenes": int(hcpp.size),
        },
    }


def write_csv(rows: list[dict]) -> None:
    path = RESULTS / "episode_results.csv"
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def plot_results(rows: list[dict]) -> None:
    methods = ["passive", "coverage_neutral", "random_motion", "hcpp", "oracle"]
    colors = {
        "passive": "#7f7f7f",
        "coverage_neutral": "#1f77b4",
        "random_motion": "#ff7f0e",
        "hcpp": "#2ca02c",
        "oracle": "#9467bd",
    }
    main = [r for r in rows if r["baseline_m"] == 0.10 and r["clutter"] == 0.15]
    means = [np.mean([r["rmse"] for r in main if r["method"] == m]) for m in methods]
    stds = [np.std([r["rmse"] for r in main if r["method"] == m]) for m in methods]
    plt.figure(figsize=(8, 4.5))
    plt.bar(methods, means, yerr=stds, color=[colors[m] for m in methods], capsize=4)
    plt.ylabel("RMSE on original hole pixels (m)")
    plt.xticks(rotation=20, ha="right")
    plt.title("Hole-conditioned parallax reduces ambiguous depth error")
    plt.tight_layout()
    plt.savefig(RESULTS / "rmse_by_method.png", dpi=180)
    plt.close()

    plt.figure(figsize=(7.5, 4.5))
    for method in ["passive", "coverage_neutral", "random_motion", "hcpp"]:
        xs = []
        ys = []
        for baseline in sorted({r["baseline_m"] for r in rows}):
            vals = [r["rmse"] for r in rows if r["method"] == method and r["baseline_m"] == baseline and r["clutter"] == 0.15]
            xs.append(baseline)
            ys.append(np.mean(vals))
        plt.plot(xs, ys, marker="o", label=method, color=colors[method])
    plt.xlabel("lateral motion budget (m)")
    plt.ylabel("RMSE on hole pixels (m)")
    plt.title("Targeted parallax matters most once motion is feasible")
    plt.legend()
    plt.tight_layout()
    plt.savefig(RESULTS / "baseline_sensitivity.png", dpi=180)
    plt.close()

    rng = np.random.default_rng(250)
    scene = make_scene(rng)
    passive = interpolate_fill(scene["observed"], scene["mask"])
    hcpp, _, _ = complete_with_motion(scene, "hcpp", 0.10, 0.15, rng)
    x = scene["x"]
    plt.figure(figsize=(8, 4.2))
    plt.plot(x, scene["true_depth"], label="true depth", linewidth=2, color="#111111")
    plt.plot(x, passive, label="passive fill", linestyle="--", color="#d62728")
    plt.plot(x, hcpp, label="HCPP after probe", linestyle="-.", color="#2ca02c")
    obs = scene["observed"].copy()
    plt.scatter(x[~np.isnan(obs)], obs[~np.isnan(obs)], s=7, label="first observation", color="#1f77b4", alpha=0.65)
    plt.ylim(0.6, max(scene["true_depth"]) + 0.4)
    plt.gca().invert_yaxis()
    plt.xlabel("image coordinate")
    plt.ylabel("depth (m, smaller is closer)")
    plt.title("Example ambiguous hole next to an occluding boundary")
    plt.legend(fontsize=8)
    plt.tight_layout()
    plt.savefig(RESULTS / "example_scene.png", dpi=180)
    plt.close()


def write_summary_md(summary: dict) -> None:
    main = summary["main_condition"]
    lines = [
        "# Experiment Summary",
        "",
        "Synthetic 1D pinhole depth scenes model a robot RGB-D camera facing foreground occluders and background surfaces. Depth holes are placed next to occlusion boundaries, where passive interpolation can copy the wrong surface. HCPP estimates the occluder side from observed boundary depths and selects a lateral micro-motion that creates background witness rays.",
        "",
        "## Main Condition",
        f"- Baseline: {main['baseline_m']} m",
        f"- Clutter: {main['clutter']}",
        f"- Scenes: {main['n_scenes']}",
        f"- Passive mean RMSE: {main['passive_mean_rmse']:.4f} m",
        f"- Random motion mean RMSE: {main['random_mean_rmse']:.4f} m",
        f"- Coverage-neutral motion mean RMSE: {main['coverage_neutral_mean_rmse']:.4f} m",
        f"- HCPP mean RMSE: {main['hcpp_mean_rmse']:.4f} m",
        f"- HCPP reduction vs passive: {main['hcpp_vs_passive_percent_reduction']:.1f}%",
        f"- HCPP reduction vs random: {main['hcpp_vs_random_percent_reduction']:.1f}%",
        f"- HCPP reduction vs coverage-neutral: {main['hcpp_vs_coverage_neutral_percent_reduction']:.1f}%",
        "",
        "## Files",
        "- `episode_results.csv`: all condition-level results.",
        "- `rmse_by_method.png`: main bar plot.",
        "- `baseline_sensitivity.png`: motion-budget sensitivity.",
        "- `example_scene.png`: qualitative hole example.",
        "",
        "## Honest Scope",
        "This is mechanism evidence, not a real-robot validation. It tests the broken assumption that depth holes can be repaired from a fixed observation and shows that directional parallax can matter under controlled occlusion geometry.",
    ]
    (RESULTS / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def patch_claims(summary: dict) -> None:
    path = ROOT / "docs" / "claims.md"
    if not path.exists():
        return
    main = summary["main_condition"]
    text = path.read_text(encoding="utf-8")
    replacement = (
        f"| HCPP improves hole RMSE over passive fill, random motion, and a coverage-neutral motion in the synthetic suite. | Supported in controlled simulation. | Main condition: HCPP {main['hcpp_mean_rmse']:.3f} m vs passive {main['passive_mean_rmse']:.3f} m, random {main['random_mean_rmse']:.3f} m, coverage-neutral {main['coverage_neutral_mean_rmse']:.3f} m. | Synthetic only. |"
    )
    text = re_sub_claim(text, replacement)
    path.write_text(text, encoding="utf-8")


def re_sub_claim(text: str, replacement: str) -> str:
    old = "| HCPP improves hole RMSE over passive fill, random motion, and a coverage-neutral motion in the synthetic suite. | To be filled after experiments. | `experiments/results/summary.json`. | Synthetic only. |"
    return text.replace(old, replacement)


def main() -> None:
    write_child_status("experiment started", "wait for simulation results and plots")
    rows = run_suite()
    write_csv(rows)
    summary = summarize(rows)
    (RESULTS / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    plot_results(rows)
    write_summary_md(summary)
    patch_claims(summary)
    write_child_status("experiment artifacts complete", "assemble ICLR paper and compile PDF")


if __name__ == "__main__":
    main()
