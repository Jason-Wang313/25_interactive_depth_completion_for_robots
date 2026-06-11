# Hostile Prior Work

This file records the closest 100 threats to novelty. Each entry is interpreted adversarially: what it already owns, what assumption it makes, and what remains open for an embodied depth-completion paper.

## 1. NBV-SC: Next Best View Planning Based on Shape Completion for Fruit Mapping and Reconstruction (2023)
- Family: `active_perception_next_best_view`
- Problem claimed: Select a view or sensing action that improves 3D reconstruction, coverage, or information gain.
- Actual mechanism introduced: Optimizes a candidate camera/view action by expected coverage, entropy reduction, reconstruction utility, or learned view value.
- Hidden assumptions: The objective is global reconstruction or map coverage; candidate views are evaluated at scene scale; individual depth holes are not treated as first-class decision objects.
- Variables treated as fixed: Utility granularity, candidate action set, scene representation, and reconstruction objective are usually fixed.
- Failure modes ignored: Can waste motion on global coverage while a small local hole remains decision-critical.
- What it makes less novel: Makes view selection for 3D perception, information gain, and active reconstruction less novel.
- What it leaves open: Hole-conditioned micro-actions that target ambiguous pixels rather than global map utility.

## 2. DepthGrasp: Depth Completion of Transparent Objects Using Self-Attentive Adversarial Network with Spectral Residual for Grasping (2021)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 3. Transparent Object Depth Completion (2024)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 4. Affordance-grounded Robot Perception and Manipulation in Adversarial, Translucent, and Cluttered Environments (2023)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 5. SLFNet: A Stereo and LiDAR Fusion Network for Depth Completion (2022)
- Family: `passive_depth_completion`
- Problem claimed: Infer dense metric depth from sparse, noisy, or partially missing RGB-D/LiDAR measurements.
- Actual mechanism introduced: Uses image/depth priors, sparse-to-dense networks, propagation, or local smoothness to fill missing depth from the current observation.
- Hidden assumptions: The current image and priors contain enough evidence; the camera pose is fixed at inference; missingness can be handled as statistical imputation.
- Variables treated as fixed: Camera pose, motion budget, viewpoint, and missingness process are fixed at completion time.
- Failure modes ignored: Can be provably non-identifiable when two 3D scenes induce the same first observation and hole mask.
- What it makes less novel: Makes dense depth imputation from RGB-D/LiDAR priors less novel.
- What it leaves open: Set-valued completion plus purposeful parallax to distinguish indistinguishable first-view hypotheses.

## 6. RGB-D Local Implicit Function for Depth Completion of Transparent Objects (2021)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 7. Attention-driven Next-best-view Planning for Efficient Reconstruction of Plants and Targeted Plant Parts (2022)
- Family: `active_perception_next_best_view`
- Problem claimed: Select a view or sensing action that improves 3D reconstruction, coverage, or information gain.
- Actual mechanism introduced: Optimizes a candidate camera/view action by expected coverage, entropy reduction, reconstruction utility, or learned view value.
- Hidden assumptions: The objective is global reconstruction or map coverage; candidate views are evaluated at scene scale; individual depth holes are not treated as first-class decision objects.
- Variables treated as fixed: Utility granularity, candidate action set, scene representation, and reconstruction objective are usually fixed.
- Failure modes ignored: Can waste motion on global coverage while a small local hole remains decision-critical.
- What it makes less novel: Makes view selection for 3D perception, information gain, and active reconstruction less novel.
- What it leaves open: Hole-conditioned micro-actions that target ambiguous pixels rather than global map utility.

## 8. NeuralLabeling: A versatile toolset for labeling vision datasets using Neural Radiance Fields (2024)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 9. RGB-D Local Implicit Function for Depth Completion of Transparent Objects (2021)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 10. TransCG: A Large-Scale Real-World Dataset for Transparent Object Depth Completion and a Grasping Baseline (2022)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 11. FDCT: Fast Depth Completion for Transparent Objects (2023)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 12. FuseGrasp: Radar-Camera Fusion for Robotic Grasping of Transparent Objects (2025)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 13. Tabletop Transparent Scene Reconstruction via Epipolar-Guided Optical Flow with Monocular Depth Completion Prior (2023)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 14. View Planning for Grape Harvesting Based on Active Vision Strategy Under Occlusion (2024)
- Family: `active_perception_next_best_view`
- Problem claimed: Select a view or sensing action that improves 3D reconstruction, coverage, or information gain.
- Actual mechanism introduced: Optimizes a candidate camera/view action by expected coverage, entropy reduction, reconstruction utility, or learned view value.
- Hidden assumptions: The objective is global reconstruction or map coverage; candidate views are evaluated at scene scale; individual depth holes are not treated as first-class decision objects.
- Variables treated as fixed: Utility granularity, candidate action set, scene representation, and reconstruction objective are usually fixed.
- Failure modes ignored: Can waste motion on global coverage while a small local hole remains decision-critical.
- What it makes less novel: Makes view selection for 3D perception, information gain, and active reconstruction less novel.
- What it leaves open: Hole-conditioned micro-actions that target ambiguous pixels rather than global map utility.

## 15. Depth completion of transparent objects based on convolutional attention mechanism (2023)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 16. FDCT: Fast Depth Completion for Transparent Objects (2023)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 17. Vision-Based Navigation and Perception for Autonomous Robots: Sensors, SLAM, Control Strategies, and Cross-Domain ApplicationsA Review (2025)
- Family: `scene_or_shape_completion`
- Problem claimed: Complete unobserved 3D structure from partial point clouds, RGB-D frames, or learned shape priors.
- Actual mechanism introduced: Fits learned implicit fields, voxels, point transformers, or shape priors to partial 3D evidence.
- Hidden assumptions: Category or scene priors dominate local observability; unobserved surfaces can be plausibly completed without testing alternatives.
- Variables treated as fixed: Sensor model, candidate actions, and representation family are usually fixed by the method.
- Failure modes ignored: Can hide ambiguity behind category priors and overconfident shape completion.
- What it makes less novel: Makes learned completion of unobserved 3D structure less novel.
- What it leaves open: Explicit tests for whether a completed surface is identifiable under feasible robot motion.

## 18. TranSplat: Surface Embedding-Guided 3D Gaussian Splatting for Transparent Object Manipulation (2025)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 19. View planning in robot active vision: A survey of systems, algorithms, and applications (2020)
- Family: `active_perception_next_best_view`
- Problem claimed: Select a view or sensing action that improves 3D reconstruction, coverage, or information gain.
- Actual mechanism introduced: Optimizes a candidate camera/view action by expected coverage, entropy reduction, reconstruction utility, or learned view value.
- Hidden assumptions: The objective is global reconstruction or map coverage; candidate views are evaluated at scene scale; individual depth holes are not treated as first-class decision objects.
- Variables treated as fixed: Utility granularity, candidate action set, scene representation, and reconstruction objective are usually fixed.
- Failure modes ignored: Can waste motion on global coverage while a small local hole remains decision-critical.
- What it makes less novel: Makes view selection for 3D perception, information gain, and active reconstruction less novel.
- What it leaves open: Hole-conditioned micro-actions that target ambiguous pixels rather than global map utility.

## 20. HDCNet: A Hybrid Depth Completion Network for Grasping Transparent and Reflective Objects (2025)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 21. Active vision in robotic systems: A survey of recent developments (2011)
- Family: `active_perception_next_best_view`
- Problem claimed: Select a view or sensing action that improves 3D reconstruction, coverage, or information gain.
- Actual mechanism introduced: Optimizes a candidate camera/view action by expected coverage, entropy reduction, reconstruction utility, or learned view value.
- Hidden assumptions: The objective is global reconstruction or map coverage; candidate views are evaluated at scene scale; individual depth holes are not treated as first-class decision objects.
- Variables treated as fixed: Utility granularity, candidate action set, scene representation, and reconstruction objective are usually fixed.
- Failure modes ignored: Can waste motion on global coverage while a small local hole remains decision-critical.
- What it makes less novel: Makes view selection for 3D perception, information gain, and active reconstruction less novel.
- What it leaves open: Hole-conditioned micro-actions that target ambiguous pixels rather than global map utility.

## 22. 3dDepthNet: Point Cloud Guided Depth Completion Network for Sparse Depth and Single Color Image (2020)
- Family: `passive_depth_completion`
- Problem claimed: Infer dense metric depth from sparse, noisy, or partially missing RGB-D/LiDAR measurements.
- Actual mechanism introduced: Uses image/depth priors, sparse-to-dense networks, propagation, or local smoothness to fill missing depth from the current observation.
- Hidden assumptions: The current image and priors contain enough evidence; the camera pose is fixed at inference; missingness can be handled as statistical imputation.
- Variables treated as fixed: Camera pose, motion budget, viewpoint, and missingness process are fixed at completion time.
- Failure modes ignored: Can be provably non-identifiable when two 3D scenes induce the same first observation and hole mask.
- What it makes less novel: Makes dense depth imputation from RGB-D/LiDAR priors less novel.
- What it leaves open: Set-valued completion plus purposeful parallax to distinguish indistinguishable first-view hypotheses.

## 23. Geometrically Consistent Monocular Metric-Semantic 3D Mapping for Indoor Environments with Transparent and Reflecting Objects (2023)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 24. A Dexterous Hand-Arm Teleoperation System Based on Hand Pose Estimation and Active Vision (2022)
- Family: `robotic_perception_general`
- Problem claimed: Improve robot perception of 3D geometry for planning, manipulation, or navigation.
- Actual mechanism introduced: Combines perception models with robot task context, motion, or geometry processing.
- Hidden assumptions: Task-level perception can tolerate local missing-depth assumptions.
- Variables treated as fixed: Sensor model, candidate actions, and representation family are usually fixed by the method.
- Failure modes ignored: Can treat holes as nuisance preprocessing rather than action-relevant evidence gaps.
- What it makes less novel: Makes generic robot depth perception less novel.
- What it leaves open: Treat missing depth as an action target, not only a perception output.

## 25. Attention-driven next-best-view planning for efficient reconstruction of plants and targeted plant parts (2024)
- Family: `active_perception_next_best_view`
- Problem claimed: Select a view or sensing action that improves 3D reconstruction, coverage, or information gain.
- Actual mechanism introduced: Optimizes a candidate camera/view action by expected coverage, entropy reduction, reconstruction utility, or learned view value.
- Hidden assumptions: The objective is global reconstruction or map coverage; candidate views are evaluated at scene scale; individual depth holes are not treated as first-class decision objects.
- Variables treated as fixed: Utility granularity, candidate action set, scene representation, and reconstruction objective are usually fixed.
- Failure modes ignored: Can waste motion on global coverage while a small local hole remains decision-critical.
- What it makes less novel: Makes view selection for 3D perception, information gain, and active reconstruction less novel.
- What it leaves open: Hole-conditioned micro-actions that target ambiguous pixels rather than global map utility.

## 26. Observe Then Act: Asynchronous Active Vision-Action Model for Robotic Manipulation (2025)
- Family: `active_perception_next_best_view`
- Problem claimed: Select a view or sensing action that improves 3D reconstruction, coverage, or information gain.
- Actual mechanism introduced: Optimizes a candidate camera/view action by expected coverage, entropy reduction, reconstruction utility, or learned view value.
- Hidden assumptions: The objective is global reconstruction or map coverage; candidate views are evaluated at scene scale; individual depth holes are not treated as first-class decision objects.
- Variables treated as fixed: Utility granularity, candidate action set, scene representation, and reconstruction objective are usually fixed.
- Failure modes ignored: Can waste motion on global coverage while a small local hole remains decision-critical.
- What it makes less novel: Makes view selection for 3D perception, information gain, and active reconstruction less novel.
- What it leaves open: Hole-conditioned micro-actions that target ambiguous pixels rather than global map utility.

## 27. SAID-NeRF: Segmentation-AIDed NeRF for Depth Completion of Transparent Objects (2024)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 28. ClearGrasp: 3D Shape Estimation of Transparent Objects for Manipulation (2019)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 29. DistillGrasp: Integrating Features Correlation With Knowledge Distillation for Depth Completion of Transparent Objects (2024)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 30. SCFusion: Real-time Incremental Scene Reconstruction with Semantic Completion (2020)
- Family: `scene_or_shape_completion`
- Problem claimed: Complete unobserved 3D structure from partial point clouds, RGB-D frames, or learned shape priors.
- Actual mechanism introduced: Fits learned implicit fields, voxels, point transformers, or shape priors to partial 3D evidence.
- Hidden assumptions: Category or scene priors dominate local observability; unobserved surfaces can be plausibly completed without testing alternatives.
- Variables treated as fixed: Sensor model, candidate actions, and representation family are usually fixed by the method.
- Failure modes ignored: Can hide ambiguity behind category priors and overconfident shape completion.
- What it makes less novel: Makes learned completion of unobserved 3D structure less novel.
- What it leaves open: Explicit tests for whether a completed surface is identifiable under feasible robot motion.

## 31. SAID-NeRF: Segmentation-AIDed NeRF for Depth Completion of Transparent Objects (2024)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 32. GAA-TSO: Geometry-Aware-Assisted Depth Completion for Transparent and Specular Objects (2026)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 33. GAA-TSO: Geometry-Aware Assisted Depth Completion for Transparent and Specular Objects (2025)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 34. A lightweight prior-encoding-decoding cascade framework for robust depth completion in robotic grasping of transparent objects using RGB-D sensors (2025)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 35. A New Era of Indoor Scene Reconstruction: A Survey (2024)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 36. SCVP: Learning One-Shot View Planning via Set Covering for Unknown Object Reconstruction (2022)
- Family: `active_perception_next_best_view`
- Problem claimed: Select a view or sensing action that improves 3D reconstruction, coverage, or information gain.
- Actual mechanism introduced: Optimizes a candidate camera/view action by expected coverage, entropy reduction, reconstruction utility, or learned view value.
- Hidden assumptions: The objective is global reconstruction or map coverage; candidate views are evaluated at scene scale; individual depth holes are not treated as first-class decision objects.
- Variables treated as fixed: Utility granularity, candidate action set, scene representation, and reconstruction objective are usually fixed.
- Failure modes ignored: Can waste motion on global coverage while a small local hole remains decision-critical.
- What it makes less novel: Makes view selection for 3D perception, information gain, and active reconstruction less novel.
- What it leaves open: Hole-conditioned micro-actions that target ambiguous pixels rather than global map utility.

## 37. DistillGrasp: Integrating Features Correlation with Knowledge Distillation for Depth Completion of Transparent Objects (2024)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 38. Humanoid Robot Next Best View Planning Under Occlusions Using Body Movement Primitives (2019)
- Family: `active_perception_next_best_view`
- Problem claimed: Select a view or sensing action that improves 3D reconstruction, coverage, or information gain.
- Actual mechanism introduced: Optimizes a candidate camera/view action by expected coverage, entropy reduction, reconstruction utility, or learned view value.
- Hidden assumptions: The objective is global reconstruction or map coverage; candidate views are evaluated at scene scale; individual depth holes are not treated as first-class decision objects.
- Variables treated as fixed: Utility granularity, candidate action set, scene representation, and reconstruction objective are usually fixed.
- Failure modes ignored: Can waste motion on global coverage while a small local hole remains decision-critical.
- What it makes less novel: Makes view selection for 3D perception, information gain, and active reconstruction less novel.
- What it leaves open: Hole-conditioned micro-actions that target ambiguous pixels rather than global map utility.

## 39. Collaborative Multi-Robot Search and Rescue: Planning, Coordination, Perception, and Active Vision (2020)
- Family: `robot_mapping_and_exploration`
- Problem claimed: Build maps or inspect scenes while moving a robot under sensing and navigation constraints.
- Actual mechanism introduced: Plans trajectories or integrates RGB-D/LiDAR observations into maps with frontier, utility, or information objectives.
- Hidden assumptions: Information gain over map cells is the right granularity; small local repair motions are secondary to exploration.
- Variables treated as fixed: Sensor model, candidate actions, and representation family are usually fixed by the method.
- Failure modes ignored: Can optimize exploration progress while missing task-critical micro-geometry.
- What it makes less novel: Makes active mapping and informative motion less novel.
- What it leaves open: Local repair motions inserted into manipulation perception loops before global exploration.

## 40. Multi-Robot Hybrid Coverage Path Planning for 3D Reconstruction of Large Structures (2021)
- Family: `active_perception_next_best_view`
- Problem claimed: Select a view or sensing action that improves 3D reconstruction, coverage, or information gain.
- Actual mechanism introduced: Optimizes a candidate camera/view action by expected coverage, entropy reduction, reconstruction utility, or learned view value.
- Hidden assumptions: The objective is global reconstruction or map coverage; candidate views are evaluated at scene scale; individual depth holes are not treated as first-class decision objects.
- Variables treated as fixed: Utility granularity, candidate action set, scene representation, and reconstruction objective are usually fixed.
- Failure modes ignored: Can waste motion on global coverage while a small local hole remains decision-critical.
- What it makes less novel: Makes view selection for 3D perception, information gain, and active reconstruction less novel.
- What it leaves open: Hole-conditioned micro-actions that target ambiguous pixels rather than global map utility.

## 41. CAGT: Sim-to-Real Depth Completion With Interactive Embedding Aggregation and Geometry Awareness for Transparent Objects (2025)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 42. Two-Dimensional Frontier-Based Viewpoint Generation for Exploring and Mapping Underwater Environments (2019)
- Family: `active_perception_next_best_view`
- Problem claimed: Select a view or sensing action that improves 3D reconstruction, coverage, or information gain.
- Actual mechanism introduced: Optimizes a candidate camera/view action by expected coverage, entropy reduction, reconstruction utility, or learned view value.
- Hidden assumptions: The objective is global reconstruction or map coverage; candidate views are evaluated at scene scale; individual depth holes are not treated as first-class decision objects.
- Variables treated as fixed: Utility granularity, candidate action set, scene representation, and reconstruction objective are usually fixed.
- Failure modes ignored: Can waste motion on global coverage while a small local hole remains decision-critical.
- What it makes less novel: Makes view selection for 3D perception, information gain, and active reconstruction less novel.
- What it leaves open: Hole-conditioned micro-actions that target ambiguous pixels rather than global map utility.

## 43. TCRNet: Transparent Object Depth Completion With Cascade Refinements (2024)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 44. Seeing Glass: Joint Point Cloud and Depth Completion for Transparent\n Objects (2021)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 45. Learning Depth Completion of Transparent Objects using Augmented Unpaired Data (2023)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 46. A dataset for developing and benchmarking active vision (2017)
- Family: `tactile_or_multimodal_perception`
- Problem claimed: Use extra physical modalities such as touch to correct missing visual geometry.
- Actual mechanism introduced: Adds contact, proprioception, or extra sensors to constrain hidden geometry.
- Hidden assumptions: Physical contact or extra sensors are available and acceptable.
- Variables treated as fixed: Sensor model, candidate actions, and representation family are usually fixed by the method.
- Failure modes ignored: Can require contact that is slow, unsafe, or changes the scene.
- What it makes less novel: Makes multimodal physical sensing for geometry less novel.
- What it leaves open: Vision-only disambiguation when contact is unavailable or risky.

## 47. ClueDepth Grasp: Leveraging positional clues of depth for completing depth of transparent objects (2022)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 48. DenseLiDAR: A Real-Time Pseudo Dense Depth Guided Depth Completion Network (2021)
- Family: `passive_depth_completion`
- Problem claimed: Infer dense metric depth from sparse, noisy, or partially missing RGB-D/LiDAR measurements.
- Actual mechanism introduced: Uses image/depth priors, sparse-to-dense networks, propagation, or local smoothness to fill missing depth from the current observation.
- Hidden assumptions: The current image and priors contain enough evidence; the camera pose is fixed at inference; missingness can be handled as statistical imputation.
- Variables treated as fixed: Camera pose, motion budget, viewpoint, and missingness process are fixed at completion time.
- Failure modes ignored: Can be provably non-identifiable when two 3D scenes induce the same first observation and hole mask.
- What it makes less novel: Makes dense depth imputation from RGB-D/LiDAR priors less novel.
- What it leaves open: Set-valued completion plus purposeful parallax to distinguish indistinguishable first-view hypotheses.

## 49. Sparse to Dense Depth Completion using a Generative Adversarial Network with Intelligent Sampling Strategies (2021)
- Family: `passive_depth_completion`
- Problem claimed: Infer dense metric depth from sparse, noisy, or partially missing RGB-D/LiDAR measurements.
- Actual mechanism introduced: Uses image/depth priors, sparse-to-dense networks, propagation, or local smoothness to fill missing depth from the current observation.
- Hidden assumptions: The current image and priors contain enough evidence; the camera pose is fixed at inference; missingness can be handled as statistical imputation.
- Variables treated as fixed: Camera pose, motion budget, viewpoint, and missingness process are fixed at completion time.
- Failure modes ignored: Can be provably non-identifiable when two 3D scenes induce the same first observation and hole mask.
- What it makes less novel: Makes dense depth imputation from RGB-D/LiDAR priors less novel.
- What it leaves open: Set-valued completion plus purposeful parallax to distinguish indistinguishable first-view hypotheses.

## 50. DeepSmooth: Efficient and Smooth Depth Completion (2023)
- Family: `passive_depth_completion`
- Problem claimed: Infer dense metric depth from sparse, noisy, or partially missing RGB-D/LiDAR measurements.
- Actual mechanism introduced: Uses image/depth priors, sparse-to-dense networks, propagation, or local smoothness to fill missing depth from the current observation.
- Hidden assumptions: The current image and priors contain enough evidence; the camera pose is fixed at inference; missingness can be handled as statistical imputation.
- Variables treated as fixed: Camera pose, motion budget, viewpoint, and missingness process are fixed at completion time.
- Failure modes ignored: Can be provably non-identifiable when two 3D scenes induce the same first observation and hole mask.
- What it makes less novel: Makes dense depth imputation from RGB-D/LiDAR priors less novel.
- What it leaves open: Set-valued completion plus purposeful parallax to distinguish indistinguishable first-view hypotheses.

## 51. Semantics-aware next-best-view planning for efficient search and detection of task-relevant plant parts (2024)
- Family: `active_perception_next_best_view`
- Problem claimed: Select a view or sensing action that improves 3D reconstruction, coverage, or information gain.
- Actual mechanism introduced: Optimizes a candidate camera/view action by expected coverage, entropy reduction, reconstruction utility, or learned view value.
- Hidden assumptions: The objective is global reconstruction or map coverage; candidate views are evaluated at scene scale; individual depth holes are not treated as first-class decision objects.
- Variables treated as fixed: Utility granularity, candidate action set, scene representation, and reconstruction objective are usually fixed.
- Failure modes ignored: Can waste motion on global coverage while a small local hole remains decision-critical.
- What it makes less novel: Makes view selection for 3D perception, information gain, and active reconstruction less novel.
- What it leaves open: Hole-conditioned micro-actions that target ambiguous pixels rather than global map utility.

## 52. Gradient-based Local Next-best-view Planning for Improved Perception of Targeted Plant Nodes (2024)
- Family: `active_perception_next_best_view`
- Problem claimed: Select a view or sensing action that improves 3D reconstruction, coverage, or information gain.
- Actual mechanism introduced: Optimizes a candidate camera/view action by expected coverage, entropy reduction, reconstruction utility, or learned view value.
- Hidden assumptions: The objective is global reconstruction or map coverage; candidate views are evaluated at scene scale; individual depth holes are not treated as first-class decision objects.
- Variables treated as fixed: Utility granularity, candidate action set, scene representation, and reconstruction objective are usually fixed.
- Failure modes ignored: Can waste motion on global coverage while a small local hole remains decision-critical.
- What it makes less novel: Makes view selection for 3D perception, information gain, and active reconstruction less novel.
- What it leaves open: Hole-conditioned micro-actions that target ambiguous pixels rather than global map utility.

## 53. ADDFNet: A Robotic Grasping Depth Map Completion Network Integrating Differential Enhancement Convolution and Hybrid Attention (2026)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 54. Nonmyopic View Planning for Active Object Classification and Pose Estimation (2014)
- Family: `active_perception_next_best_view`
- Problem claimed: Select a view or sensing action that improves 3D reconstruction, coverage, or information gain.
- Actual mechanism introduced: Optimizes a candidate camera/view action by expected coverage, entropy reduction, reconstruction utility, or learned view value.
- Hidden assumptions: The objective is global reconstruction or map coverage; candidate views are evaluated at scene scale; individual depth holes are not treated as first-class decision objects.
- Variables treated as fixed: Utility granularity, candidate action set, scene representation, and reconstruction objective are usually fixed.
- Failure modes ignored: Can waste motion on global coverage while a small local hole remains decision-critical.
- What it makes less novel: Makes view selection for 3D perception, information gain, and active reconstruction less novel.
- What it leaves open: Hole-conditioned micro-actions that target ambiguous pixels rather than global map utility.

## 55. Deep Reinforcement Learning for Next Best View Planning in Autonomous Robot-Based 3D Reconstruction (2025)
- Family: `active_perception_next_best_view`
- Problem claimed: Select a view or sensing action that improves 3D reconstruction, coverage, or information gain.
- Actual mechanism introduced: Optimizes a candidate camera/view action by expected coverage, entropy reduction, reconstruction utility, or learned view value.
- Hidden assumptions: The objective is global reconstruction or map coverage; candidate views are evaluated at scene scale; individual depth holes are not treated as first-class decision objects.
- Variables treated as fixed: Utility granularity, candidate action set, scene representation, and reconstruction objective are usually fixed.
- Failure modes ignored: Can waste motion on global coverage while a small local hole remains decision-critical.
- What it makes less novel: Makes view selection for 3D perception, information gain, and active reconstruction less novel.
- What it leaves open: Hole-conditioned micro-actions that target ambiguous pixels rather than global map utility.

## 56. Remote Telemanipulation with Adapting Viewpoints in Visually Complex Environments (2019)
- Family: `robot_mapping_and_exploration`
- Problem claimed: Build maps or inspect scenes while moving a robot under sensing and navigation constraints.
- Actual mechanism introduced: Plans trajectories or integrates RGB-D/LiDAR observations into maps with frontier, utility, or information objectives.
- Hidden assumptions: Information gain over map cells is the right granularity; small local repair motions are secondary to exploration.
- Variables treated as fixed: Sensor model, candidate actions, and representation family are usually fixed by the method.
- Failure modes ignored: Can optimize exploration progress while missing task-critical micro-geometry.
- What it makes less novel: Makes active mapping and informative motion less novel.
- What it leaves open: Local repair motions inserted into manipulation perception loops before global exploration.

## 57. Weakly-Supervised Depth Completion during Robotic Micromanipulation from a Monocular Microscopic Image (2024)
- Family: `passive_depth_completion`
- Problem claimed: Infer dense metric depth from sparse, noisy, or partially missing RGB-D/LiDAR measurements.
- Actual mechanism introduced: Uses image/depth priors, sparse-to-dense networks, propagation, or local smoothness to fill missing depth from the current observation.
- Hidden assumptions: The current image and priors contain enough evidence; the camera pose is fixed at inference; missingness can be handled as statistical imputation.
- Variables treated as fixed: Camera pose, motion budget, viewpoint, and missingness process are fixed at completion time.
- Failure modes ignored: Can be provably non-identifiable when two 3D scenes induce the same first observation and hole mask.
- What it makes less novel: Makes dense depth imputation from RGB-D/LiDAR priors less novel.
- What it leaves open: Set-valued completion plus purposeful parallax to distinguish indistinguishable first-view hypotheses.

## 58. STExplorer: A Hierarchical Autonomous Exploration Strategy with Spatio-temporal Awareness for Aerial Robots (2023)
- Family: `active_perception_next_best_view`
- Problem claimed: Select a view or sensing action that improves 3D reconstruction, coverage, or information gain.
- Actual mechanism introduced: Optimizes a candidate camera/view action by expected coverage, entropy reduction, reconstruction utility, or learned view value.
- Hidden assumptions: The objective is global reconstruction or map coverage; candidate views are evaluated at scene scale; individual depth holes are not treated as first-class decision objects.
- Variables treated as fixed: Utility granularity, candidate action set, scene representation, and reconstruction objective are usually fixed.
- Failure modes ignored: Can waste motion on global coverage while a small local hole remains decision-critical.
- What it makes less novel: Makes view selection for 3D perception, information gain, and active reconstruction less novel.
- What it leaves open: Hole-conditioned micro-actions that target ambiguous pixels rather than global map utility.

## 59. Autonomous Scene Exploration for Robotics: A Conditional Random View-Sampling and Evaluation Using a Voxel-Sorting Mechanism for Efficient Ray Casting (2020)
- Family: `active_perception_next_best_view`
- Problem claimed: Select a view or sensing action that improves 3D reconstruction, coverage, or information gain.
- Actual mechanism introduced: Optimizes a candidate camera/view action by expected coverage, entropy reduction, reconstruction utility, or learned view value.
- Hidden assumptions: The objective is global reconstruction or map coverage; candidate views are evaluated at scene scale; individual depth holes are not treated as first-class decision objects.
- Variables treated as fixed: Utility granularity, candidate action set, scene representation, and reconstruction objective are usually fixed.
- Failure modes ignored: Can waste motion on global coverage while a small local hole remains decision-critical.
- What it makes less novel: Makes view selection for 3D perception, information gain, and active reconstruction less novel.
- What it leaves open: Hole-conditioned micro-actions that target ambiguous pixels rather than global map utility.

## 60. High-quality indoor scene 3D reconstruction with RGB-D cameras: A brief review (2022)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 61. ClearDepth: Enhanced Stereo Perception of Transparent Objects for Robotic Manipulation (2024)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 62. MFF-Net: Towards Efficient Monocular Depth Completion With Multi-Modal Feature Fusion (2023)
- Family: `passive_depth_completion`
- Problem claimed: Infer dense metric depth from sparse, noisy, or partially missing RGB-D/LiDAR measurements.
- Actual mechanism introduced: Uses image/depth priors, sparse-to-dense networks, propagation, or local smoothness to fill missing depth from the current observation.
- Hidden assumptions: The current image and priors contain enough evidence; the camera pose is fixed at inference; missingness can be handled as statistical imputation.
- Variables treated as fixed: Camera pose, motion budget, viewpoint, and missingness process are fixed at completion time.
- Failure modes ignored: Can be provably non-identifiable when two 3D scenes induce the same first observation and hole mask.
- What it makes less novel: Makes dense depth imputation from RGB-D/LiDAR priors less novel.
- What it leaves open: Set-valued completion plus purposeful parallax to distinguish indistinguishable first-view hypotheses.

## 63. Active Visuo-Tactile Interactive Robotic Perception for Accurate Object Pose Estimation in Dense Clutter (2022)
- Family: `tactile_or_multimodal_perception`
- Problem claimed: Use extra physical modalities such as touch to correct missing visual geometry.
- Actual mechanism introduced: Adds contact, proprioception, or extra sensors to constrain hidden geometry.
- Hidden assumptions: Physical contact or extra sensors are available and acceptable.
- Variables treated as fixed: Sensor model, candidate actions, and representation family are usually fixed by the method.
- Failure modes ignored: Can require contact that is slow, unsafe, or changes the scene.
- What it makes less novel: Makes multimodal physical sensing for geometry less novel.
- What it leaves open: Vision-only disambiguation when contact is unavailable or risky.

## 64. PC-NBV: A Point Cloud Based Deep Network for Efficient Next Best View Planning (2020)
- Family: `active_perception_next_best_view`
- Problem claimed: Select a view or sensing action that improves 3D reconstruction, coverage, or information gain.
- Actual mechanism introduced: Optimizes a candidate camera/view action by expected coverage, entropy reduction, reconstruction utility, or learned view value.
- Hidden assumptions: The objective is global reconstruction or map coverage; candidate views are evaluated at scene scale; individual depth holes are not treated as first-class decision objects.
- Variables treated as fixed: Utility granularity, candidate action set, scene representation, and reconstruction objective are usually fixed.
- Failure modes ignored: Can waste motion on global coverage while a small local hole remains decision-critical.
- What it makes less novel: Makes view selection for 3D perception, information gain, and active reconstruction less novel.
- What it leaves open: Hole-conditioned micro-actions that target ambiguous pixels rather than global map utility.

## 65. Active Haptic Perception in Robots: A Review (2019)
- Family: `robot_mapping_and_exploration`
- Problem claimed: Build maps or inspect scenes while moving a robot under sensing and navigation constraints.
- Actual mechanism introduced: Plans trajectories or integrates RGB-D/LiDAR observations into maps with frontier, utility, or information objectives.
- Hidden assumptions: Information gain over map cells is the right granularity; small local repair motions are secondary to exploration.
- Variables treated as fixed: Sensor model, candidate actions, and representation family are usually fixed by the method.
- Failure modes ignored: Can optimize exploration progress while missing task-critical micro-geometry.
- What it makes less novel: Makes active mapping and informative motion less novel.
- What it leaves open: Local repair motions inserted into manipulation perception loops before global exploration.

## 66. Struct-MDC: Mesh-Refined Unsupervised Depth Completion Leveraging Structural Regularities From Visual SLAM (2022)
- Family: `passive_depth_completion`
- Problem claimed: Infer dense metric depth from sparse, noisy, or partially missing RGB-D/LiDAR measurements.
- Actual mechanism introduced: Uses image/depth priors, sparse-to-dense networks, propagation, or local smoothness to fill missing depth from the current observation.
- Hidden assumptions: The current image and priors contain enough evidence; the camera pose is fixed at inference; missingness can be handled as statistical imputation.
- Variables treated as fixed: Camera pose, motion budget, viewpoint, and missingness process are fixed at completion time.
- Failure modes ignored: Can be provably non-identifiable when two 3D scenes induce the same first observation and hole mask.
- What it makes less novel: Makes dense depth imputation from RGB-D/LiDAR priors less novel.
- What it leaves open: Set-valued completion plus purposeful parallax to distinguish indistinguishable first-view hypotheses.

## 67. High-Quality 3D Reconstruction With Depth Super-Resolution and Completion (2019)
- Family: `robotic_perception_general`
- Problem claimed: Improve robot perception of 3D geometry for planning, manipulation, or navigation.
- Actual mechanism introduced: Combines perception models with robot task context, motion, or geometry processing.
- Hidden assumptions: Task-level perception can tolerate local missing-depth assumptions.
- Variables treated as fixed: Sensor model, candidate actions, and representation family are usually fixed by the method.
- Failure modes ignored: Can treat holes as nuisance preprocessing rather than action-relevant evidence gaps.
- What it makes less novel: Makes generic robot depth perception less novel.
- What it leaves open: Treat missing depth as an action target, not only a perception output.

## 68. Stereo-augmented Depth Completion from a Single RGB-LiDAR image (2021)
- Family: `passive_depth_completion`
- Problem claimed: Infer dense metric depth from sparse, noisy, or partially missing RGB-D/LiDAR measurements.
- Actual mechanism introduced: Uses image/depth priors, sparse-to-dense networks, propagation, or local smoothness to fill missing depth from the current observation.
- Hidden assumptions: The current image and priors contain enough evidence; the camera pose is fixed at inference; missingness can be handled as statistical imputation.
- Variables treated as fixed: Camera pose, motion budget, viewpoint, and missingness process are fixed at completion time.
- Failure modes ignored: Can be provably non-identifiable when two 3D scenes induce the same first observation and hole mask.
- What it makes less novel: Makes dense depth imputation from RGB-D/LiDAR priors less novel.
- What it leaves open: Set-valued completion plus purposeful parallax to distinguish indistinguishable first-view hypotheses.

## 69. A Universal Semantic-Geometric Representation for Robotic Manipulation (2023)
- Family: `robot_mapping_and_exploration`
- Problem claimed: Build maps or inspect scenes while moving a robot under sensing and navigation constraints.
- Actual mechanism introduced: Plans trajectories or integrates RGB-D/LiDAR observations into maps with frontier, utility, or information objectives.
- Hidden assumptions: Information gain over map cells is the right granularity; small local repair motions are secondary to exploration.
- Variables treated as fixed: Sensor model, candidate actions, and representation family are usually fixed by the method.
- Failure modes ignored: Can optimize exploration progress while missing task-critical micro-geometry.
- What it makes less novel: Makes active mapping and informative motion less novel.
- What it leaves open: Local repair motions inserted into manipulation perception loops before global exploration.

## 70. Beyond Top-Grasps Through Scene Completion (2020)
- Family: `scene_or_shape_completion`
- Problem claimed: Complete unobserved 3D structure from partial point clouds, RGB-D frames, or learned shape priors.
- Actual mechanism introduced: Fits learned implicit fields, voxels, point transformers, or shape priors to partial 3D evidence.
- Hidden assumptions: Category or scene priors dominate local observability; unobserved surfaces can be plausibly completed without testing alternatives.
- Variables treated as fixed: Sensor model, candidate actions, and representation family are usually fixed by the method.
- Failure modes ignored: Can hide ambiguity behind category priors and overconfident shape completion.
- What it makes less novel: Makes learned completion of unobserved 3D structure less novel.
- What it leaves open: Explicit tests for whether a completed surface is identifiable under feasible robot motion.

## 71. Depth Completion of Transparent Objects Based on Feature Fusion (2024)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 72. Volumetric Next-best-view Planning for 3D Object Reconstruction with Positioning Error (2014)
- Family: `active_perception_next_best_view`
- Problem claimed: Select a view or sensing action that improves 3D reconstruction, coverage, or information gain.
- Actual mechanism introduced: Optimizes a candidate camera/view action by expected coverage, entropy reduction, reconstruction utility, or learned view value.
- Hidden assumptions: The objective is global reconstruction or map coverage; candidate views are evaluated at scene scale; individual depth holes are not treated as first-class decision objects.
- Variables treated as fixed: Utility granularity, candidate action set, scene representation, and reconstruction objective are usually fixed.
- Failure modes ignored: Can waste motion on global coverage while a small local hole remains decision-critical.
- What it makes less novel: Makes view selection for 3D perception, information gain, and active reconstruction less novel.
- What it leaves open: Hole-conditioned micro-actions that target ambiguous pixels rather than global map utility.

## 73. Active Vision via Extremum Seeking for Robots in Unstructured Environments: Applications in Object Recognition and Manipulation (2018)
- Family: `robotic_perception_general`
- Problem claimed: Improve robot perception of 3D geometry for planning, manipulation, or navigation.
- Actual mechanism introduced: Combines perception models with robot task context, motion, or geometry processing.
- Hidden assumptions: Task-level perception can tolerate local missing-depth assumptions.
- Variables treated as fixed: Sensor model, candidate actions, and representation family are usually fixed by the method.
- Failure modes ignored: Can treat holes as nuisance preprocessing rather than action-relevant evidence gaps.
- What it makes less novel: Makes generic robot depth perception less novel.
- What it leaves open: Treat missing depth as an action target, not only a perception output.

## 74. Are Theories of Imagery Theories of Imagination? An Active Perception Approach to Conscious Mental Content (1999)
- Family: `robotic_perception_general`
- Problem claimed: Improve robot perception of 3D geometry for planning, manipulation, or navigation.
- Actual mechanism introduced: Combines perception models with robot task context, motion, or geometry processing.
- Hidden assumptions: Task-level perception can tolerate local missing-depth assumptions.
- Variables treated as fixed: Sensor model, candidate actions, and representation family are usually fixed by the method.
- Failure modes ignored: Can treat holes as nuisance preprocessing rather than action-relevant evidence gaps.
- What it makes less novel: Makes generic robot depth perception less novel.
- What it leaves open: Treat missing depth as an action target, not only a perception output.

## 75. Autonomous Robotic Manipulation: Real-Time, Deep-Learning Approach for Grasping of Unknown Objects (2022)
- Family: `robotic_perception_general`
- Problem claimed: Improve robot perception of 3D geometry for planning, manipulation, or navigation.
- Actual mechanism introduced: Combines perception models with robot task context, motion, or geometry processing.
- Hidden assumptions: Task-level perception can tolerate local missing-depth assumptions.
- Variables treated as fixed: Sensor model, candidate actions, and representation family are usually fixed by the method.
- Failure modes ignored: Can treat holes as nuisance preprocessing rather than action-relevant evidence gaps.
- What it makes less novel: Makes generic robot depth perception less novel.
- What it leaves open: Treat missing depth as an action target, not only a perception output.

## 76. HTPE-Net: Monocular 6D Pose Estimation of Transparent Objects in Hand for Robot Manipulation (2024)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 77. LMSCNet: Lightweight Multiscale 3D Semantic Completion (2020)
- Family: `scene_or_shape_completion`
- Problem claimed: Complete unobserved 3D structure from partial point clouds, RGB-D frames, or learned shape priors.
- Actual mechanism introduced: Fits learned implicit fields, voxels, point transformers, or shape priors to partial 3D evidence.
- Hidden assumptions: Category or scene priors dominate local observability; unobserved surfaces can be plausibly completed without testing alternatives.
- Variables treated as fixed: Sensor model, candidate actions, and representation family are usually fixed by the method.
- Failure modes ignored: Can hide ambiguity behind category priors and overconfident shape completion.
- What it makes less novel: Makes learned completion of unobserved 3D structure less novel.
- What it leaves open: Explicit tests for whether a completed surface is identifiable under feasible robot motion.

## 78. Active Vision for Extraction of Physically Plausible Support Relations (2019)
- Family: `active_perception_next_best_view`
- Problem claimed: Select a view or sensing action that improves 3D reconstruction, coverage, or information gain.
- Actual mechanism introduced: Optimizes a candidate camera/view action by expected coverage, entropy reduction, reconstruction utility, or learned view value.
- Hidden assumptions: The objective is global reconstruction or map coverage; candidate views are evaluated at scene scale; individual depth holes are not treated as first-class decision objects.
- Variables treated as fixed: Utility granularity, candidate action set, scene representation, and reconstruction objective are usually fixed.
- Failure modes ignored: Can waste motion on global coverage while a small local hole remains decision-critical.
- What it makes less novel: Makes view selection for 3D perception, information gain, and active reconstruction less novel.
- What it leaves open: Hole-conditioned micro-actions that target ambiguous pixels rather than global map utility.

## 79. Animat vision: Active vision in artificial animals (2002)
- Family: `robotic_perception_general`
- Problem claimed: Improve robot perception of 3D geometry for planning, manipulation, or navigation.
- Actual mechanism introduced: Combines perception models with robot task context, motion, or geometry processing.
- Hidden assumptions: Task-level perception can tolerate local missing-depth assumptions.
- Variables treated as fixed: Sensor model, candidate actions, and representation family are usually fixed by the method.
- Failure modes ignored: Can treat holes as nuisance preprocessing rather than action-relevant evidence gaps.
- What it makes less novel: Makes generic robot depth perception less novel.
- What it leaves open: Treat missing depth as an action target, not only a perception output.

## 80. OccDepth: A Depth-Aware Method for 3D Semantic Scene Completion (2023)
- Family: `scene_or_shape_completion`
- Problem claimed: Complete unobserved 3D structure from partial point clouds, RGB-D frames, or learned shape priors.
- Actual mechanism introduced: Fits learned implicit fields, voxels, point transformers, or shape priors to partial 3D evidence.
- Hidden assumptions: Category or scene priors dominate local observability; unobserved surfaces can be plausibly completed without testing alternatives.
- Variables treated as fixed: Sensor model, candidate actions, and representation family are usually fixed by the method.
- Failure modes ignored: Can hide ambiguity behind category priors and overconfident shape completion.
- What it makes less novel: Makes learned completion of unobserved 3D structure less novel.
- What it leaves open: Explicit tests for whether a completed surface is identifiable under feasible robot motion.

## 81. Self-Supervised Sparse-to-Dense: Self-Supervised Depth Completion from LiDAR and Monocular Camera (2019)
- Family: `passive_depth_completion`
- Problem claimed: Infer dense metric depth from sparse, noisy, or partially missing RGB-D/LiDAR measurements.
- Actual mechanism introduced: Uses image/depth priors, sparse-to-dense networks, propagation, or local smoothness to fill missing depth from the current observation.
- Hidden assumptions: The current image and priors contain enough evidence; the camera pose is fixed at inference; missingness can be handled as statistical imputation.
- Variables treated as fixed: Camera pose, motion budget, viewpoint, and missingness process are fixed at completion time.
- Failure modes ignored: Can be provably non-identifiable when two 3D scenes induce the same first observation and hole mask.
- What it makes less novel: Makes dense depth imputation from RGB-D/LiDAR priors less novel.
- What it leaves open: Set-valued completion plus purposeful parallax to distinguish indistinguishable first-view hypotheses.

## 82. DeepDNet: Deep Dense Network for Depth Completion Task (2021)
- Family: `passive_depth_completion`
- Problem claimed: Infer dense metric depth from sparse, noisy, or partially missing RGB-D/LiDAR measurements.
- Actual mechanism introduced: Uses image/depth priors, sparse-to-dense networks, propagation, or local smoothness to fill missing depth from the current observation.
- Hidden assumptions: The current image and priors contain enough evidence; the camera pose is fixed at inference; missingness can be handled as statistical imputation.
- Variables treated as fixed: Camera pose, motion budget, viewpoint, and missingness process are fixed at completion time.
- Failure modes ignored: Can be provably non-identifiable when two 3D scenes induce the same first observation and hole mask.
- What it makes less novel: Makes dense depth imputation from RGB-D/LiDAR priors less novel.
- What it leaves open: Set-valued completion plus purposeful parallax to distinguish indistinguishable first-view hypotheses.

## 83. Learning Guided Convolutional Network for Depth Completion (2020)
- Family: `passive_depth_completion`
- Problem claimed: Infer dense metric depth from sparse, noisy, or partially missing RGB-D/LiDAR measurements.
- Actual mechanism introduced: Uses image/depth priors, sparse-to-dense networks, propagation, or local smoothness to fill missing depth from the current observation.
- Hidden assumptions: The current image and priors contain enough evidence; the camera pose is fixed at inference; missingness can be handled as statistical imputation.
- Variables treated as fixed: Camera pose, motion budget, viewpoint, and missingness process are fixed at completion time.
- Failure modes ignored: Can be provably non-identifiable when two 3D scenes induce the same first observation and hole mask.
- What it makes less novel: Makes dense depth imputation from RGB-D/LiDAR priors less novel.
- What it leaves open: Set-valued completion plus purposeful parallax to distinguish indistinguishable first-view hypotheses.

## 84. ReFlow6D: Refraction-Guided Transparent Object 6D Pose Estimation via Intermediate Representation Learning (2024)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 85. A sliding window approach to exploration for 3D map building using a biologically inspired bridge inspection robot (2015)
- Family: `active_perception_next_best_view`
- Problem claimed: Select a view or sensing action that improves 3D reconstruction, coverage, or information gain.
- Actual mechanism introduced: Optimizes a candidate camera/view action by expected coverage, entropy reduction, reconstruction utility, or learned view value.
- Hidden assumptions: The objective is global reconstruction or map coverage; candidate views are evaluated at scene scale; individual depth holes are not treated as first-class decision objects.
- Variables treated as fixed: Utility granularity, candidate action set, scene representation, and reconstruction objective are usually fixed.
- Failure modes ignored: Can waste motion on global coverage while a small local hole remains decision-critical.
- What it makes less novel: Makes view selection for 3D perception, information gain, and active reconstruction less novel.
- What it leaves open: Hole-conditioned micro-actions that target ambiguous pixels rather than global map utility.

## 86. Deep Depth Completion of a Single RGB-D Image (2018)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.

## 87. ManipulaTHOR: A Framework for Visual Object Manipulation (2021)
- Family: `robotic_perception_general`
- Problem claimed: Improve robot perception of 3D geometry for planning, manipulation, or navigation.
- Actual mechanism introduced: Combines perception models with robot task context, motion, or geometry processing.
- Hidden assumptions: Task-level perception can tolerate local missing-depth assumptions.
- Variables treated as fixed: Sensor model, candidate actions, and representation family are usually fixed by the method.
- Failure modes ignored: Can treat holes as nuisance preprocessing rather than action-relevant evidence gaps.
- What it makes less novel: Makes generic robot depth perception less novel.
- What it leaves open: Treat missing depth as an action target, not only a perception output.

## 88. An information gain formulation for active volumetric 3D reconstruction (2016)
- Family: `active_perception_next_best_view`
- Problem claimed: Select a view or sensing action that improves 3D reconstruction, coverage, or information gain.
- Actual mechanism introduced: Optimizes a candidate camera/view action by expected coverage, entropy reduction, reconstruction utility, or learned view value.
- Hidden assumptions: The objective is global reconstruction or map coverage; candidate views are evaluated at scene scale; individual depth holes are not treated as first-class decision objects.
- Variables treated as fixed: Utility granularity, candidate action set, scene representation, and reconstruction objective are usually fixed.
- Failure modes ignored: Can waste motion on global coverage while a small local hole remains decision-critical.
- What it makes less novel: Makes view selection for 3D perception, information gain, and active reconstruction less novel.
- What it leaves open: Hole-conditioned micro-actions that target ambiguous pixels rather than global map utility.

## 89. Semantic Scene Completion from a Single 360-Degree Image and Depth Map (2020)
- Family: `scene_or_shape_completion`
- Problem claimed: Complete unobserved 3D structure from partial point clouds, RGB-D frames, or learned shape priors.
- Actual mechanism introduced: Fits learned implicit fields, voxels, point transformers, or shape priors to partial 3D evidence.
- Hidden assumptions: Category or scene priors dominate local observability; unobserved surfaces can be plausibly completed without testing alternatives.
- Variables treated as fixed: Sensor model, candidate actions, and representation family are usually fixed by the method.
- Failure modes ignored: Can hide ambiguity behind category priors and overconfident shape completion.
- What it makes less novel: Makes learned completion of unobserved 3D structure less novel.
- What it leaves open: Explicit tests for whether a completed surface is identifiable under feasible robot motion.

## 90. S3CNet: A Sparse Semantic Scene Completion Network for LiDAR Point Clouds (2020)
- Family: `scene_or_shape_completion`
- Problem claimed: Complete unobserved 3D structure from partial point clouds, RGB-D frames, or learned shape priors.
- Actual mechanism introduced: Fits learned implicit fields, voxels, point transformers, or shape priors to partial 3D evidence.
- Hidden assumptions: Category or scene priors dominate local observability; unobserved surfaces can be plausibly completed without testing alternatives.
- Variables treated as fixed: Sensor model, candidate actions, and representation family are usually fixed by the method.
- Failure modes ignored: Can hide ambiguity behind category priors and overconfident shape completion.
- What it makes less novel: Makes learned completion of unobserved 3D structure less novel.
- What it leaves open: Explicit tests for whether a completed surface is identifiable under feasible robot motion.

## 91. Robot@Home, a robotic dataset for semantic mapping of home environments (2017)
- Family: `robot_mapping_and_exploration`
- Problem claimed: Build maps or inspect scenes while moving a robot under sensing and navigation constraints.
- Actual mechanism introduced: Plans trajectories or integrates RGB-D/LiDAR observations into maps with frontier, utility, or information objectives.
- Hidden assumptions: Information gain over map cells is the right granularity; small local repair motions are secondary to exploration.
- Variables treated as fixed: Sensor model, candidate actions, and representation family are usually fixed by the method.
- Failure modes ignored: Can optimize exploration progress while missing task-critical micro-geometry.
- What it makes less novel: Makes active mapping and informative motion less novel.
- What it leaves open: Local repair motions inserted into manipulation perception loops before global exploration.

## 92. Active Vision for Robot Manipulators Using the Free Energy Principle (2021)
- Family: `robotic_perception_general`
- Problem claimed: Improve robot perception of 3D geometry for planning, manipulation, or navigation.
- Actual mechanism introduced: Combines perception models with robot task context, motion, or geometry processing.
- Hidden assumptions: Task-level perception can tolerate local missing-depth assumptions.
- Variables treated as fixed: Sensor model, candidate actions, and representation family are usually fixed by the method.
- Failure modes ignored: Can treat holes as nuisance preprocessing rather than action-relevant evidence gaps.
- What it makes less novel: Makes generic robot depth perception less novel.
- What it leaves open: Treat missing depth as an action target, not only a perception output.

## 93. Multi-robot geometric task-and-motion planning for collaborative manipulation tasks (2023)
- Family: `robot_mapping_and_exploration`
- Problem claimed: Build maps or inspect scenes while moving a robot under sensing and navigation constraints.
- Actual mechanism introduced: Plans trajectories or integrates RGB-D/LiDAR observations into maps with frontier, utility, or information objectives.
- Hidden assumptions: Information gain over map cells is the right granularity; small local repair motions are secondary to exploration.
- Variables treated as fixed: Sensor model, candidate actions, and representation family are usually fixed by the method.
- Failure modes ignored: Can optimize exploration progress while missing task-critical micro-geometry.
- What it makes less novel: Makes active mapping and informative motion less novel.
- What it leaves open: Local repair motions inserted into manipulation perception loops before global exploration.

## 94. Semantic-Guided Depth Completion From Monocular Images and 4D Radar Data (2024)
- Family: `passive_depth_completion`
- Problem claimed: Infer dense metric depth from sparse, noisy, or partially missing RGB-D/LiDAR measurements.
- Actual mechanism introduced: Uses image/depth priors, sparse-to-dense networks, propagation, or local smoothness to fill missing depth from the current observation.
- Hidden assumptions: The current image and priors contain enough evidence; the camera pose is fixed at inference; missingness can be handled as statistical imputation.
- Variables treated as fixed: Camera pose, motion budget, viewpoint, and missingness process are fixed at completion time.
- Failure modes ignored: Can be provably non-identifiable when two 3D scenes induce the same first observation and hole mask.
- What it makes less novel: Makes dense depth imputation from RGB-D/LiDAR priors less novel.
- What it leaves open: Set-valued completion plus purposeful parallax to distinguish indistinguishable first-view hypotheses.

## 95. Grasp Stability Prediction for a Dexterous Robotic Hand Combining Depth Vision and Haptic Bayesian Exploration (2021)
- Family: `robot_mapping_and_exploration`
- Problem claimed: Build maps or inspect scenes while moving a robot under sensing and navigation constraints.
- Actual mechanism introduced: Plans trajectories or integrates RGB-D/LiDAR observations into maps with frontier, utility, or information objectives.
- Hidden assumptions: Information gain over map cells is the right granularity; small local repair motions are secondary to exploration.
- Variables treated as fixed: Sensor model, candidate actions, and representation family are usually fixed by the method.
- Failure modes ignored: Can optimize exploration progress while missing task-critical micro-geometry.
- What it makes less novel: Makes active mapping and informative motion less novel.
- What it leaves open: Local repair motions inserted into manipulation perception loops before global exploration.

## 96. Precise Robotic Manipulation of Bulky Components (2020)
- Family: `tactile_or_multimodal_perception`
- Problem claimed: Use extra physical modalities such as touch to correct missing visual geometry.
- Actual mechanism introduced: Adds contact, proprioception, or extra sensors to constrain hidden geometry.
- Hidden assumptions: Physical contact or extra sensors are available and acceptable.
- Variables treated as fixed: Sensor model, candidate actions, and representation family are usually fixed by the method.
- Failure modes ignored: Can require contact that is slow, unsafe, or changes the scene.
- What it makes less novel: Makes multimodal physical sensing for geometry less novel.
- What it leaves open: Vision-only disambiguation when contact is unavailable or risky.

## 97. 360ORB-SLAM: A Visual SLAM System for Panoramic Images with Depth Completion Network (2024)
- Family: `passive_depth_completion`
- Problem claimed: Infer dense metric depth from sparse, noisy, or partially missing RGB-D/LiDAR measurements.
- Actual mechanism introduced: Uses image/depth priors, sparse-to-dense networks, propagation, or local smoothness to fill missing depth from the current observation.
- Hidden assumptions: The current image and priors contain enough evidence; the camera pose is fixed at inference; missingness can be handled as statistical imputation.
- Variables treated as fixed: Camera pose, motion budget, viewpoint, and missingness process are fixed at completion time.
- Failure modes ignored: Can be provably non-identifiable when two 3D scenes induce the same first observation and hole mask.
- What it makes less novel: Makes dense depth imputation from RGB-D/LiDAR priors less novel.
- What it leaves open: Set-valued completion plus purposeful parallax to distinguish indistinguishable first-view hypotheses.

## 98. 3D Lidar Reconstruction with Probabilistic Depth Completion for Robotic Navigation (2022)
- Family: `passive_depth_completion`
- Problem claimed: Infer dense metric depth from sparse, noisy, or partially missing RGB-D/LiDAR measurements.
- Actual mechanism introduced: Uses image/depth priors, sparse-to-dense networks, propagation, or local smoothness to fill missing depth from the current observation.
- Hidden assumptions: The current image and priors contain enough evidence; the camera pose is fixed at inference; missingness can be handled as statistical imputation.
- Variables treated as fixed: Camera pose, motion budget, viewpoint, and missingness process are fixed at completion time.
- Failure modes ignored: Can be provably non-identifiable when two 3D scenes induce the same first observation and hole mask.
- What it makes less novel: Makes dense depth imputation from RGB-D/LiDAR priors less novel.
- What it leaves open: Set-valued completion plus purposeful parallax to distinguish indistinguishable first-view hypotheses.

## 99. Learning Guided Convolutional Network for Depth Completion (2019)
- Family: `passive_depth_completion`
- Problem claimed: Infer dense metric depth from sparse, noisy, or partially missing RGB-D/LiDAR measurements.
- Actual mechanism introduced: Uses image/depth priors, sparse-to-dense networks, propagation, or local smoothness to fill missing depth from the current observation.
- Hidden assumptions: The current image and priors contain enough evidence; the camera pose is fixed at inference; missingness can be handled as statistical imputation.
- Variables treated as fixed: Camera pose, motion budget, viewpoint, and missingness process are fixed at completion time.
- Failure modes ignored: Can be provably non-identifiable when two 3D scenes induce the same first observation and hole mask.
- What it makes less novel: Makes dense depth imputation from RGB-D/LiDAR priors less novel.
- What it leaves open: Set-valued completion plus purposeful parallax to distinguish indistinguishable first-view hypotheses.

## 100. RFTrans: Leveraging Refractive Flow of Transparent Objects for Surface Normal Estimation and Manipulation (2023)
- Family: `transparent_reflective_depth`
- Problem claimed: Recover missing or corrupted depth on transparent, reflective, or specular objects.
- Actual mechanism introduced: Uses learned normals, shape priors, polarization/geometry cues, or synthetic training to repair unreliable depth.
- Hidden assumptions: Problem-specific appearance or material priors transfer; the robot does not need to move specifically to expose witness rays.
- Variables treated as fixed: Material class, illumination assumptions, and training distribution are often fixed.
- Failure modes ignored: Can hallucinate plausible but wrong geometry when material priors fail or the object is novel.
- What it makes less novel: Makes material-aware missing-depth repair less novel.
- What it leaves open: A material-agnostic motion probe that asks for new rays before hallucinating surface depth.
