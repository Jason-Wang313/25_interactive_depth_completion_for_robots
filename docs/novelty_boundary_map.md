# Novelty Boundary Map

## Hidden Assumptions That May Be False
1. A single RGB-D frame contains enough information to complete every important depth hole.
2. Depth holes are nuisance corruption, not action targets.
3. Global reconstruction utility is an adequate proxy for task-critical local depth repair.
4. A plausible completed surface is sufficient when the robot only needs one safe action.
5. Training priors can stand in for new physical evidence.
6. Missingness is independent of viewpoint, material, and depth discontinuity structure.
7. Sensor failures are spatially local and can be interpolated from neighboring pixels.
8. The robot's camera pose is fixed at completion time.
9. View planning should operate on map cells or objects, not on individual hole hypotheses.
10. A larger baseline is always better than a targeted feasible micro-motion.
11. The cost of a perception action is dominated by distance traveled, not by whether it resolves the right ambiguity.
12. Uncertainty maps identify what to do without specifying which motion creates a separating observation.
13. Occlusion boundaries are just artifacts to smooth over.
14. Transparent and specular object depth repair requires material-specific priors first.
15. Completion quality should be judged mainly by average dense depth metrics.
16. Benchmarks with static observations reflect embodied robot use.
17. Multi-view fusion only matters after a complete exploration plan has begun.
18. A robot can tolerate hallucinated geometry as long as it is visually plausible.
19. Depth completion and active perception can be modularly combined without changing either objective.
20. The failure mode of wrong-but-confident completion is less important than the mean error.
21. Observed boundaries around a hole provide no useful directional signal for where to move.
22. The target of sensing is the whole scene rather than the smallest intervention that breaks ambiguity.
23. Motion feasibility can be handled after perception rather than inside the completion mechanism.
24. Depth holes near contact regions have the same value as holes in the background.

## Candidate Directions Considered
1. Hole-Conditioned Parallax Probing: treat each missing-depth region as a set of 3D hypotheses, then move the robot camera in the direction predicted to create a witness ray that separates those hypotheses. This changes the central mechanism from imputation to intervention.
2. Contact-then-complete depth repair: use touch to resolve depth holes. Rejected as too dependent on contact availability and less purely active 3D perception.
3. Material-specialized transparent-object completion: train for transparent/specular depth. Rejected because the central move is better data or a material prior.
4. Uncertainty-driven next-best-view completion: score candidate views with an uncertainty map. Rejected as a weak combination unless the motion objective changes from global uncertainty to hole-specific identifiability.
5. LLM-planned perception actions: rejected by the assignment and by the field reading; planning language is not the bottleneck.

## Selected Boundary
The selected idea is Hole-Conditioned Parallax Probing (HCPP). It is only novel if the paper keeps the mechanism centered on local identifiability under feasible robot motion, not on a larger model, a benchmark, a verifier, or a generic active-learning loop.

## Novelty Boundary Against Close Families
- Against passive depth completion: HCPP refuses to output a single hallucinated depth when first-view evidence is non-identifying; it asks for a separating action.
- Against next-best-view planning: HCPP scores candidate motions by expected hole-hypothesis separation, not map coverage or object-scale reconstruction.
- Against transparent-object repair: HCPP is material-agnostic and uses parallax witness rays rather than material labels or synthetic material priors.
- Against multi-view fusion: HCPP chooses the next view because of the current hole geometry before fusing, rather than passively accepting whatever next view arrives.
- Against uncertainty maps: HCPP requires a directional witness operator; uncertainty alone is not the mechanism.
