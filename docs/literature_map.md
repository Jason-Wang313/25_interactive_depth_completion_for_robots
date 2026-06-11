# Literature Map

## Field Box
Active 3D perception for robots: methods that decide how an embodied sensor should move, what geometry to infer, and how missing depth affects downstream manipulation, navigation, inspection, or mapping.

## Sweep Protocol
- Landscape sweep: 1000 ranked papers in `docs/related_work_matrix.csv`.
- Serious skim: top 300 metadata/abstract records with extracted problem, mechanism, assumptions, fixed variables, ignored failures, novelty erosion, and open space.
- Deep read: top 240 records, read at abstract/mechanism level with attention to threat against the selected thesis.
- Hostile prior-work set: top 100 records, selected to maximize novelty pressure.

## Method Families
- `robotic_perception_general`: 478
- `robot_mapping_and_exploration`: 157
- `tactile_or_multimodal_perception`: 98
- `passive_depth_completion`: 90
- `transparent_reflective_depth`: 74
- `active_perception_next_best_view`: 51
- `scene_or_shape_completion`: 43
- `general_3d_vision`: 6
- `autonomous_driving_depth`: 3

## Highest-Ranked Threats
|rank|year|title|family|what_it_makes_less_novel|what_it_leaves_open|
|---|---|---|---|---|---|
|1|2023|NBV-SC: Next Best View Planning Based on Shape Completion for Fruit Mapping and Reconstruction|active_perception_next_best_view|Makes view selection for 3D perception, information gain, and active reconstruction less novel.|Hole-conditioned micro-actions that target ambiguous pixels rather than global map utility.|
|2|2021|DepthGrasp: Depth Completion of Transparent Objects Using Self-Attentive Adversarial Network with Spectral Residual f...|transparent_reflective_depth|Makes material-aware missing-depth repair less novel.|A material-agnostic motion probe that asks for new rays before hallucinating surface depth.|
|3|2024|Transparent Object Depth Completion|transparent_reflective_depth|Makes material-aware missing-depth repair less novel.|A material-agnostic motion probe that asks for new rays before hallucinating surface depth.|
|4|2023|Affordance-grounded Robot Perception and Manipulation in Adversarial, Translucent, and Cluttered Environments|transparent_reflective_depth|Makes material-aware missing-depth repair less novel.|A material-agnostic motion probe that asks for new rays before hallucinating surface depth.|
|5|2022|SLFNet: A Stereo and LiDAR Fusion Network for Depth Completion|passive_depth_completion|Makes dense depth imputation from RGB-D/LiDAR priors less novel.|Set-valued completion plus purposeful parallax to distinguish indistinguishable first-view hypotheses.|
|6|2021|RGB-D Local Implicit Function for Depth Completion of Transparent Objects|transparent_reflective_depth|Makes material-aware missing-depth repair less novel.|A material-agnostic motion probe that asks for new rays before hallucinating surface depth.|
|7|2022|Attention-driven Next-best-view Planning for Efficient Reconstruction of Plants and Targeted Plant Parts|active_perception_next_best_view|Makes view selection for 3D perception, information gain, and active reconstruction less novel.|Hole-conditioned micro-actions that target ambiguous pixels rather than global map utility.|
|8|2024|NeuralLabeling: A versatile toolset for labeling vision datasets using Neural Radiance Fields|transparent_reflective_depth|Makes material-aware missing-depth repair less novel.|A material-agnostic motion probe that asks for new rays before hallucinating surface depth.|
|9|2021|RGB-D Local Implicit Function for Depth Completion of Transparent Objects|transparent_reflective_depth|Makes material-aware missing-depth repair less novel.|A material-agnostic motion probe that asks for new rays before hallucinating surface depth.|
|10|2022|TransCG: A Large-Scale Real-World Dataset for Transparent Object Depth Completion and a Grasping Baseline|transparent_reflective_depth|Makes material-aware missing-depth repair less novel.|A material-agnostic motion probe that asks for new rays before hallucinating surface depth.|
|11|2023|FDCT: Fast Depth Completion for Transparent Objects|transparent_reflective_depth|Makes material-aware missing-depth repair less novel.|A material-agnostic motion probe that asks for new rays before hallucinating surface depth.|
|12|2025|FuseGrasp: Radar-Camera Fusion for Robotic Grasping of Transparent Objects|transparent_reflective_depth|Makes material-aware missing-depth repair less novel.|A material-agnostic motion probe that asks for new rays before hallucinating surface depth.|
|13|2023|Tabletop Transparent Scene Reconstruction via Epipolar-Guided Optical Flow with Monocular Depth Completion Prior|transparent_reflective_depth|Makes material-aware missing-depth repair less novel.|A material-agnostic motion probe that asks for new rays before hallucinating surface depth.|
|14|2024|View Planning for Grape Harvesting Based on Active Vision Strategy Under Occlusion|active_perception_next_best_view|Makes view selection for 3D perception, information gain, and active reconstruction less novel.|Hole-conditioned micro-actions that target ambiguous pixels rather than global map utility.|
|15|2023|Depth completion of transparent objects based on convolutional attention mechanism|transparent_reflective_depth|Makes material-aware missing-depth repair less novel.|A material-agnostic motion probe that asks for new rays before hallucinating surface depth.|
|16|2023|FDCT: Fast Depth Completion for Transparent Objects|transparent_reflective_depth|Makes material-aware missing-depth repair less novel.|A material-agnostic motion probe that asks for new rays before hallucinating surface depth.|
|17|2025|Vision-Based Navigation and Perception for Autonomous Robots: Sensors, SLAM, Control Strategies, and Cross-Domain App...|scene_or_shape_completion|Makes learned completion of unobserved 3D structure less novel.|Explicit tests for whether a completed surface is identifiable under feasible robot motion.|
|18|2025|TranSplat: Surface Embedding-Guided 3D Gaussian Splatting for Transparent Object Manipulation|transparent_reflective_depth|Makes material-aware missing-depth repair less novel.|A material-agnostic motion probe that asks for new rays before hallucinating surface depth.|
|19|2020|View planning in robot active vision: A survey of systems, algorithms, and applications|active_perception_next_best_view|Makes view selection for 3D perception, information gain, and active reconstruction less novel.|Hole-conditioned micro-actions that target ambiguous pixels rather than global map utility.|
|20|2025|HDCNet: A Hybrid Depth Completion Network for Grasping Transparent and Reflective Objects|transparent_reflective_depth|Makes material-aware missing-depth repair less novel.|A material-agnostic motion probe that asks for new rays before hallucinating surface depth.|

## Field Reading
The field is rich in passive depth completion, next-best-view planning, active mapping, transparent-object depth repair, and point/scene completion. The common center of gravity is either a better completion model for a fixed observation or a view planner for global reconstruction utility. The gap that repeatedly remains is local, embodied, and causal: a robot can often take a small feasible motion whose only purpose is to make two hole-depth hypotheses produce different observations.
