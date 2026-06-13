# Final Audit

1. Chosen thesis: Robots should treat some depth holes as action targets. Hole-Conditioned Parallax Probing (HCPP) uses a small purposeful camera motion to make competing hole-depth hypotheses observably different before committing to completion.
2. Field assumption broken: Fixed-view depth completion is assumed to be enough for missing robot depth. The paper breaks that assumption for holes near occlusion boundaries.
3. New central mechanism: A hole-boundary witness operator that chooses a feasible parallax micro-motion and evidence-gated fusion, instead of passive imputation.
4. Genuine novelty: The novelty is not active perception in general or depth completion in general. It is the local identifiability framing and hole-conditioned motion primitive. Closest work makes view planning, fusion, and completion less novel.
5. Closest hostile prior work: passive sparse-to-dense depth completion, next-best-view active reconstruction, KinectFusion/volumetric fusion, scene completion, and transparent-object depth repair. See `docs/hostile_prior_work.md` for the 100-paper set.
6. Literature coverage: `docs/related_work_matrix.csv` contains the 1000-paper ranked landscape; top 300 are serious skim entries, top 240 are deep-read entries, and top 100 are hostile prior work.
7. Proof/formal-claim status if any: A simplified proposition proves first-view non-identifiability for two 2.5D scenes sharing the same observation and hole mask. It is a toy theorem, not a full real-world guarantee.
8. Strongest evidence: Controlled synthetic suite in `experiments/results/`. Main condition HCPP RMSE is 0.32941287931642194 m versus passive 1.0618394986336646 m, random 0.6779931337789411 m, and coverage-neutral 0.6698823215568944 m. V2 boundary-cue stress shows HCPP RMSE rises to 0.5439686092541434 m at 30% sign error and 0.6931432537936376 m at 50% sign error.
9. Biggest weaknesses: Synthetic-only evidence, simplified occlusion geometry, no hardware validation, minimal robot dynamics, and v2 stress shows HCPP depends on reliable hole-boundary sign cues; at high sign-error rates it can underperform random motion.
10. Paper-readiness judgment: workshop-only / strong-revise. The mechanism is coherent and runnable, but real-robot validation and a calibrated sign-confidence/fallback policy are needed for a full conference submission.
11. Exact Downloads PDF path: `C:/Users/wangz/Downloads/25.pdf` (exists, 300705 bytes).
12. GitHub URL: https://github.com/Jason-Wang313/25_interactive_depth_completion_for_robots
13. Desktop copy state: absent (expected; canonical PDF stays in Downloads)
14. Local repository PDF state: paper/main.pdf absent after canonical copy
