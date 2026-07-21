# ICML 2026 Paper-Level Evidence Codes

This report adds heuristic evidence tags to each paper using title, topic, and official abstract text.
The tags are intended to guide manual review; they are not a substitute for reading the papers.

## Snapshot

- Papers coded: 6,628
- Areas summarized: 12
- Papers with benchmark-like mentions: 423
- Papers with dataset-like mentions: 36
- Papers with metric-like mentions: 2,426

## Area Evidence Summary

### LLM Reasoning, Post-Training, and RLVR
- Papers: 1099; benchmark mentions: 9.3%; dataset mentions: 0.3%; metric mentions: 50.8%; GitHub URL share: 31.8%
- Primary contribution types: Benchmark / evaluation (460); Method / algorithm (192); Dataset / data resource (142); Position / conceptual (112); Theory / proof (94); System / infrastructure (42); Uncoded (32); Application / domain study (25)
- Method families: Reasoning / test-time compute (608); RL / policy optimization (468); LLM post-training (468); Agents / tool use (290); Diffusion / flow (234); Compression / efficiency (180); Transformer / attention (154); Graphs / geometry (119)
- Evaluation settings: language/llm (1019); math/code/verifiable (308); theory/synthetic (226); robotics/embodied (120); security/safety (117); vision/video (66); science/domain (31)
- Result claim cues: state-of-the-art / improvement (757); scaling / efficiency (556); negative / limitation (466); robustness / safety (221)
- Evidence confidence: medium (1029); low (70)

### Multimodal, Vision, and Perception
- Papers: 889; benchmark mentions: 11.2%; dataset mentions: 0.8%; metric mentions: 35.2%; GitHub URL share: 29.5%
- Primary contribution types: Benchmark / evaluation (436); Dataset / data resource (141); Method / algorithm (126); Position / conceptual (76); Theory / proof (49); System / infrastructure (35); Application / domain study (16); Uncoded (10)
- Method families: Reasoning / test-time compute (297); LLM post-training (277); Agents / tool use (231); Graphs / geometry (217); Transformer / attention (189); Diffusion / flow (179); Compression / efficiency (138); RL / policy optimization (127)
- Evaluation settings: vision/video (763); language/llm (468); math/code/verifiable (181); security/safety (133); robotics/embodied (124); theory/synthetic (93); science/domain (58)
- Result claim cues: state-of-the-art / improvement (654); negative / limitation (435); scaling / efficiency (424); robustness / safety (256)
- Evidence confidence: medium (800); low (89)

### Theory, Optimization, and Algorithms
- Papers: 737; benchmark mentions: 1.2%; dataset mentions: 0.4%; metric mentions: 25.8%; GitHub URL share: 11.8%
- Primary contribution types: Theory / proof (372); Dataset / data resource (101); Benchmark / evaluation (99); Method / algorithm (78); Position / conceptual (53); Uncoded (15); System / infrastructure (12); Application / domain study (7)
- Method families: Bayesian / probabilistic (188); Transformer / attention (121); Diffusion / flow (115); Graphs / geometry (98); Agents / tool use (86); Compression / efficiency (82); RL / policy optimization (76); LLM post-training (52)
- Evaluation settings: theory/synthetic (475); language/llm (88); robotics/embodied (72); security/safety (65); math/code/verifiable (53); vision/video (45); science/domain (17)
- Result claim cues: state-of-the-art / improvement (313); scaling / efficiency (312); negative / limitation (227); robustness / safety (161)
- Evidence confidence: medium (476); low (260); very_low (1)

### AI for Science, Health, and Neuro
- Papers: 587; benchmark mentions: 2.0%; dataset mentions: 1.2%; metric mentions: 36.1%; GitHub URL share: 19.4%
- Primary contribution types: Benchmark / evaluation (194); Dataset / data resource (115); Method / algorithm (76); Theory / proof (63); System / infrastructure (47); Application / domain study (46); Position / conceptual (38); Uncoded (8)
- Method families: Diffusion / flow (180); Graphs / geometry (146); Transformer / attention (135); Agents / tool use (118); Compression / efficiency (110); LLM post-training (79); Bayesian / probabilistic (63); Reasoning / test-time compute (53)
- Evaluation settings: science/domain (252); theory/synthetic (169); vision/video (132); math/code/verifiable (93); language/llm (92); security/safety (58); robotics/embodied (48)
- Result claim cues: state-of-the-art / improvement (387); scaling / efficiency (309); negative / limitation (260); robustness / safety (137)
- Evidence confidence: medium (464); low (122); very_low (1)

### Data-Centric, Causal, and Federated ML
- Papers: 526; benchmark mentions: 3.6%; dataset mentions: 0.6%; metric mentions: 30.4%; GitHub URL share: 16.4%
- Primary contribution types: Benchmark / evaluation (166); Dataset / data resource (143); Method / algorithm (68); Theory / proof (61); Position / conceptual (54); System / infrastructure (14); Application / domain study (12); Uncoded (8)
- Method families: Causal / data-centric (127); LLM post-training (126); Compression / efficiency (83); Agents / tool use (79); Graphs / geometry (78); Reasoning / test-time compute (65); Transformer / attention (56); Bayesian / probabilistic (51)
- Evaluation settings: theory/synthetic (200); language/llm (170); security/safety (112); vision/video (80); math/code/verifiable (50); robotics/embodied (31); science/domain (26)
- Result claim cues: state-of-the-art / improvement (325); scaling / efficiency (222); negative / limitation (212); robustness / safety (170)
- Evidence confidence: medium (396); low (129); very_low (1)

### Systems and Efficient Foundation Models
- Papers: 515; benchmark mentions: 5.2%; dataset mentions: 0.4%; metric mentions: 59.2%; GitHub URL share: 24.5%
- Primary contribution types: Benchmark / evaluation (135); Theory / proof (103); System / infrastructure (98); Method / algorithm (72); Dataset / data resource (45); Position / conceptual (37); Application / domain study (19); Uncoded (6)
- Method families: Compression / efficiency (266); Transformer / attention (164); Agents / tool use (138); LLM post-training (130); Reasoning / test-time compute (68); Graphs / geometry (57); Diffusion / flow (52); RL / policy optimization (31)
- Evaluation settings: language/llm (324); theory/synthetic (129); math/code/verifiable (105); vision/video (69); security/safety (33); robotics/embodied (24); science/domain (8)
- Result claim cues: scaling / efficiency (403); state-of-the-art / improvement (348); negative / limitation (188); robustness / safety (72)
- Evidence confidence: medium (438); low (77)

### Safety, Governance, Privacy, and Society
- Papers: 502; benchmark mentions: 5.6%; dataset mentions: 0.0%; metric mentions: 26.7%; GitHub URL share: 19.9%
- Primary contribution types: Position / conceptual (153); Benchmark / evaluation (101); Method / algorithm (88); Dataset / data resource (71); Theory / proof (43); System / infrastructure (21); Uncoded (15); Application / domain study (10)
- Method families: Agents / tool use (169); LLM post-training (145); Reasoning / test-time compute (129); RL / policy optimization (79); Diffusion / flow (39); Transformer / attention (36); Compression / efficiency (34); Graphs / geometry (31)
- Evaluation settings: security/safety (360); language/llm (287); theory/synthetic (109); robotics/embodied (75); math/code/verifiable (65); vision/video (54); science/domain (9)
- Result claim cues: robustness / safety (362); state-of-the-art / improvement (210); negative / limitation (202); scaling / efficiency (158)
- Evidence confidence: medium (373); low (129)

### Agents, Code, and Tool Use
- Papers: 496; benchmark mentions: 15.5%; dataset mentions: 0.8%; metric mentions: 35.9%; GitHub URL share: 32.9%
- Primary contribution types: Benchmark / evaluation (276); Position / conceptual (55); Method / algorithm (48); Dataset / data resource (41); Theory / proof (35); System / infrastructure (27); Uncoded (7); Application / domain study (7)
- Method families: Agents / tool use (412); Reasoning / test-time compute (271); RL / policy optimization (150); LLM post-training (100); Graphs / geometry (63); Diffusion / flow (41); Compression / efficiency (35); Transformer / attention (24)
- Evaluation settings: language/llm (414); math/code/verifiable (213); theory/synthetic (90); robotics/embodied (79); security/safety (43); vision/video (30); science/domain (15)
- Result claim cues: state-of-the-art / improvement (323); negative / limitation (254); scaling / efficiency (241); robustness / safety (116)
- Evidence confidence: medium (466); low (30)

### Graphs, Geometry, and Representation Learning
- Papers: 391; benchmark mentions: 1.8%; dataset mentions: 0.8%; metric mentions: 23.3%; GitHub URL share: 19.4%
- Primary contribution types: Benchmark / evaluation (104); Dataset / data resource (104); Method / algorithm (55); Theory / proof (51); Position / conceptual (44); System / infrastructure (15); Uncoded (10); Application / domain study (8)
- Method families: Graphs / geometry (331); LLM post-training (80); Transformer / attention (74); Diffusion / flow (73); Agents / tool use (62); Compression / efficiency (57); Reasoning / test-time compute (47); Bayesian / probabilistic (22)
- Evaluation settings: theory/synthetic (122); vision/video (108); language/llm (64); math/code/verifiable (48); security/safety (37); robotics/embodied (27); science/domain (21)
- Result claim cues: state-of-the-art / improvement (236); negative / limitation (186); scaling / efficiency (157); robustness / safety (101)
- Evidence confidence: medium (279); low (112)

### Generative Modeling
- Papers: 379; benchmark mentions: 4.0%; dataset mentions: 0.8%; metric mentions: 27.2%; GitHub URL share: 30.3%
- Primary contribution types: Method / algorithm (101); Benchmark / evaluation (80); Dataset / data resource (65); Theory / proof (59); Position / conceptual (31); System / infrastructure (19); Application / domain study (14); Uncoded (10)
- Method families: Diffusion / flow (333); Graphs / geometry (91); Bayesian / probabilistic (89); LLM post-training (82); Transformer / attention (72); Compression / efficiency (60); Agents / tool use (46); RL / policy optimization (39)
- Evaluation settings: vision/video (220); theory/synthetic (120); language/llm (83); robotics/embodied (49); security/safety (39); science/domain (36); math/code/verifiable (33)
- Result claim cues: state-of-the-art / improvement (251); scaling / efficiency (182); negative / limitation (144); robustness / safety (88)
- Evidence confidence: medium (329); low (50)

### Reinforcement Learning and Control
- Papers: 312; benchmark mentions: 5.1%; dataset mentions: 0.0%; metric mentions: 37.2%; GitHub URL share: 20.5%
- Primary contribution types: Benchmark / evaluation (105); Theory / proof (82); Method / algorithm (53); Position / conceptual (26); System / infrastructure (15); Application / domain study (14); Dataset / data resource (12); Uncoded (5)
- Method families: RL / policy optimization (305); Agents / tool use (116); Diffusion / flow (82); Graphs / geometry (48); Compression / efficiency (45); Reasoning / test-time compute (38); LLM post-training (36); Bayesian / probabilistic (27)
- Evaluation settings: robotics/embodied (154); theory/synthetic (109); security/safety (50); math/code/verifiable (33); language/llm (30); vision/video (24); science/domain (1)
- Result claim cues: state-of-the-art / improvement (206); scaling / efficiency (126); negative / limitation (125); robustness / safety (94)
- Evidence confidence: medium (274); low (38)

### Robotics, Embodiment, and World Models
- Papers: 195; benchmark mentions: 5.6%; dataset mentions: 0.5%; metric mentions: 33.9%; GitHub URL share: 37.4%
- Primary contribution types: Benchmark / evaluation (91); Application / domain study (34); Dataset / data resource (24); Method / algorithm (15); Position / conceptual (10); System / infrastructure (10); Theory / proof (9); Uncoded (2)
- Method families: RL / policy optimization (104); Agents / tool use (81); Reasoning / test-time compute (59); Diffusion / flow (44); LLM post-training (42); Graphs / geometry (22); Compression / efficiency (21); Transformer / attention (21)
- Evaluation settings: robotics/embodied (171); vision/video (130); language/llm (103); theory/synthetic (55); math/code/verifiable (33); security/safety (19); science/domain (17)
- Result claim cues: state-of-the-art / improvement (146); scaling / efficiency (111); negative / limitation (101); robustness / safety (50)
- Evidence confidence: medium (186); low (8); very_low (1)

## Caveats

- Coding is regex/keyword based and intentionally conservative.
- Benchmark and dataset mentions are extracted from naming patterns and will miss many plain-language references.
- `evidence_confidence` measures how much text evidence and tag signal the heuristic found, not whether a paper is correct or important.
- Publication-grade synthesis still requires manual paper review for representative and boundary papers.