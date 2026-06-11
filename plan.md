# Plan

## Goal
Produce a complete, runnable, anonymous ICLR-style robotics paper package for paper 25, including a serious prior-work landscape, an honest novelty decision, runnable evidence, compiled PDF at `C:/Users/wangz/Downloads/25.pdf`, public GitHub push, and final audit.

## Execution Stages
1. Initialize run hygiene
   - Keep `child_status.md` compact and current.
   - Inspect any existing artifacts without deleting useful caches.
   - Record every important command, failure, and recovery.

2. Literature landscape before choosing the final direction
   - Build `docs/related_work_matrix.csv` with at least 1000 relevant robotics / embodied-perception papers.
   - Do a 300-paper serious skim from ranked metadata.
   - Do a 200-250-paper deep read via abstracts and available metadata.
   - Build a 100-paper hostile prior-work set focused on closest threats.
   - Extract problem, mechanism, assumptions, fixed variables, ignored failures, novelty erosion, and open space for important papers.

3. Novelty and thesis selection
   - Define the field box.
   - Identify at least 20 fragile assumptions.
   - Generate candidate paper directions that break those assumptions.
   - Reject weak moves unless there is a genuinely different central mechanism.
   - Choose the strongest direction and document the boundary.

4. Runnable evidence
   - Implement a small, reproducible embodied active-depth-completion experiment.
   - Demonstrate why the broken assumption matters with controlled synthetic robot motion, occlusions, and depth holes.
   - Save scripts, configs, results, and plots.
   - Mark unsupported claims honestly.

5. Paper writing and audit
   - Retrieve or recreate the latest official ICLR LaTeX template available at runtime.
   - Write a complete anonymous ICLR-style paper.
   - Build `docs/literature_map.md`, `docs/hostile_prior_work.md`, `docs/novelty_boundary_map.md`, `docs/novelty_decision.md`, `docs/claims.md`, `docs/reviewer_attacks.md`, and `docs/final_audit.md`.
   - Compile with pdfLaTeX/BibTeX where available, fixing LaTeX/BibTeX safety issues.

6. Delivery
   - Save final PDF only to `C:/Users/wangz/Downloads/25.pdf`.
   - Create public GitHub repo `25_interactive_depth_completion_for_robots`.
   - Push the complete runnable repo or document any authenticated GitHub failure.
   - Finish with status and final audit complete.

## Safety Notes
- Use bounded scripts for complex parsing, ranking, plotting, and literature processing.
- Avoid brittle inline PowerShell for complex data work.
- Use explicit long timeouts for experiments and builds.
- Do not delete existing useful artifacts.
- If optional lookups fail, record and continue with cached or fallback sources.
