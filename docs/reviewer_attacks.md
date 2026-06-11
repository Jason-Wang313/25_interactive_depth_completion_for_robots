# Reviewer Attacks

1. This is just next-best-view planning with another utility. Response: the paper must emphasize the representational change: candidate actions are generated from hole-boundary hypotheses and scored by local witness-ray separation, not global map coverage.
2. The experiment is synthetic. Response: accept this as the biggest weakness; claim mechanism evidence, not deployment readiness.
3. Passive depth completion baselines are too weak. Response: the formal ambiguity result says no passive method can solve both indistinguishable first-view worlds; the experiment illustrates the operational consequence.
4. Random motion eventually works. Response: HCPP is about motion efficiency and directionality under small robot budgets.
5. Uncertainty-aware active learning already does this. Response: uncertainty maps identify where ambiguity is high but do not specify the parallax sign or witness geometry unless the proposed mechanism is added.
6. Multi-view fusion already fixes holes. Response: HCPP decides which second view to take because of a specific hole; fusion is a downstream estimator.
7. Transparent-object methods are closer than the paper admits. Response: HCPP is material-agnostic but weaker; it should not claim to solve all transparent-object sensing.
8. The formal theorem is too narrow. Response: keep it as a clean impossibility witness and rely on simulation for breadth.
9. The robot feasibility model is minimal. Response: frame the action set as a replaceable local feasible-action sampler, not a full controller.
10. The paper overclaims novelty. Response: restrict novelty to the central mechanism and boundary conditions documented in `docs/novelty_boundary_map.md`.
