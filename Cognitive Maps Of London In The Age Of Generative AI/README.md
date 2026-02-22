# Cognitive Maps of London in the Age of Generative AI  
## How Multimodal LLMs Perceive, Prioritise, and Distort Urban Space  
### Auditing Spatial Bias, Linguistic Salience, and Geographic Representation in Large Language Models  

---

## Executive Summary (For Recruiters & Hiring Managers)

**What this project is**  
A research-driven audit of how **multimodal Large Language Models (LLMs)** internally represent cities, using London as a controlled, policy-relevant case study.

Rather than training a new model, this project treats deployed foundation models as **real-world socio-technical systems**, analysing how spatial knowledge, salience, bias, and *reasoning* emerge from model behaviour across image and text.

**Why it matters**  
**LLMs are becoming spatial gatekeepers.**  
They increasingly shape mapping, navigation, travel discovery, local search, and urban analytics. If their internal “mental maps” are uneven, they can systematically amplify already-visible places while rendering peripheral communities digitally invisible — reinforcing spatial inequality at scale.

This project asks a simple but critical question:  
> *Do AI systems perceive cities the way humans do — or do they distort urban space even further?*

**What I built**
- Adapted **Stanley Milgram’s urban recognisability experiments** from human cognition to multimodal LLMs  
- Designed a **spatial auditing framework** that measures *what models predict*, *how often they do so*, *what they confuse*, and *what signals they rely on*  
- Introduced two complementary evaluation metrics:
  - **Recognisability** — how accurately places are identified  
  - **Visibility** — how strongly places dominate model predictions  
- Evaluated borough-level recognition and **systematic misclassification patterns** across **image and text modalities**  
- Analysed **model reasoning and descriptions** using NLP:
  - image-task **justifications**, and  
  - text-based **sensory descriptions**  
- Reconstructed **AI-generated cognitive maps** from confusion structure and benchmarked them against established human studies  

**Key findings**
- Both image-based and text-based models **systematically over-recognise central London**, closely mirroring classic human cognitive maps  
- **AI-generated cognitive maps amplify human centrality bias**, producing stronger central dominance and deeper peripheral suppression than observed in human experiments  
- Several outer boroughs are frequently misclassified or effectively invisible  
- **Specific boroughs act as cognitive defaults**, absorbing misclassifications from multiple distinct areas, revealing asymmetric confusion patterns rather than random error  
- Image and text modalities rely on **different cognitive signals**, leading to modality-dependent spatial understanding and inconsistent borough confusions  
- Recognition is driven primarily by **symbolic, cultural, and experiential cues** (e.g. transport, regeneration, “vibe”), rather than physical form alone  
- **Socio-economic advantage matters**: wealthier, less deprived boroughs are both predicted more often and recognised more accurately, with visibility and recognisability positively correlated with lower IMD scores  

**Skills demonstrated**
- Multimodal ML evaluation beyond accuracy  
- Confusion-matrix and misclassification analysis  
- Metric design for bias, visibility, and representation auditing  
- NLP: embeddings, topic modelling, semantic analysis  
- Dimensionality reduction and correlation analysis  
- End-to-end Python data and evaluation pipelines  
- Responsible AI and geographic fairness analysis  

---

![LLM borough recognisability and visibility across image and text modalities](LLM_Boroughs.png)

---

## Detailed Breakdown

## 1. Problem — Spatial Bias in AI City Perception

Cities are not perceived uniformly.  
Decades of urban psychology research show that **central, affluent, and symbolically salient areas dominate mental maps**, while peripheral and residential districts fade from awareness.

As LLMs increasingly mediate:
- mapping and navigation,
- travel and local discovery,
- real estate and urban analytics,

a critical question emerges:

> **How do AI systems “see” cities — and whose places become visible or invisible as a result?**

This project investigates whether multimodal LLMs:
- replicate known human spatial biases,
- amplify them,
- or introduce new distortions altogether.

### Business & Societal Context
- LLMs increasingly shape geographic visibility and recommendation  
- Uneven spatial representation risks reinforcing existing inequalities  
- Borough-level misrepresentation affects:
  - travel recommendations  
  - cultural and commercial discovery  
  - smart-city analytics  
  - fairness in geographic AI systems  

### Research Objective
Develop a **replicable spatial auditing framework** that:

- measures how LLMs recognise urban areas across image and text,  
- detects central amplification and peripheral suppression,  
- reconstructs model-generated cognitive maps,  
- benchmarks AI spatial perception against established human patterns, and  
- **examines the reasoning signals models rely on when making spatial predictions**.

---

## Human Baseline — Urban Cognitive Maps

### Stanley Milgram’s Urban Recognisability Experiments

In the 1970s, social psychologist **Stanley Milgram** studied how people form mental representations of cities.

Rather than asking participants to draw maps, he tested whether individuals could identify locations from:
- partial visual scenes,  
- short descriptive cues.  

Findings across cities consistently show:
- central and symbolic areas are over-recognised,  
- peripheral districts are overlooked,  
- recognisability correlates with **exposure, centrality, and cultural salience**, not geographic size.

These asymmetries form **cognitive maps** — mental representations shaped by salience rather than spatial accuracy.

This project applies the same logic to **multimodal LLMs**, enabling direct **human–AI comparison**.

---

## 2. Data — Multimodal Urban Inputs

### Urban Coverage
- **Geography:** All 33 boroughs of Greater London  
- **Spatial unit:** Boroughs (authoritative, recognisable, policy-relevant)

### Multimodal Inputs

#### Image-Based Inputs
- 495 Google Street View images  
- 15 images per borough  
- Random sampling within borough boundaries  

**Image preprocessing**
- Poor-quality or extreme-angle images removed  
- Visible textual cues (street names, signs) blurred or excluded  
- Major landmarks and transport hubs excluded to avoid trivial recognition  
- Focus retained on everyday urban form  

#### Text-Based Inputs
- 495 borough-specific sensory descriptions  
- Generated by the model itself  
- Borough names withheld during inference  
- Descriptions focused on atmosphere, movement, architecture, and daily life  

### Dataset Summary

| Component | Count |
|--------|-------|
| Boroughs | 33 |
| Images | 495 |
| Text descriptions | 495 |
| Total predictions | 990 |

### External Contextual Data
- Index of Multiple Deprivation (IMD 2019)  
- UK Census (2021)  
- Population density  
- Transport connectivity  
- Digital visibility proxies  

---

## 3. Method — Multimodal Recognition Tasks

Two complementary recognition tasks were designed.

### Image-Based Recognition
- **Input:** Street-level image  
- **Task:** Predict London borough  
- **Output:** Borough prediction + natural-language justification  

### Text-Based Recognition
- **Input:** Borough-specific sensory description  
- **Task:** Predict London borough  
- **Output:** Single borough prediction  

Each task produces a **confusion matrix**, treated as a behavioural proxy for a **cognitive map**.

---

## 3.1 Model Configuration & Generation Control

To ensure comparability and reproducibility across tasks and boroughs, all model queries were executed under fixed generation settings.

- **Temperature:** 0.0  
- **Decoding:** Deterministic  
- **Prompt structure:** Fixed templates per task  
- **No conversational memory or cross-sample context**

A zero-temperature setting was chosen to minimise stochastic variation and ensure that observed spatial patterns reflect **systematic model behaviour**, rather than sampling noise.

---

## 3.2 Prompt Design & Task Templates

All tasks used **fixed, task-specific prompt templates** to ensure consistent framing across samples and boroughs.

### Image-Based Recognition Prompt

~~~
You are an expert in London’s urban geography.

The image provided was taken somewhere in Greater London.
Your task is to identify the single most likely borough, from the 33 official London boroughs, where this location belongs, based solely on the visual information available in the image.

If the image appears ambiguous or lacks distinctive features, you must still make the most plausible guess based on whatever details are present.
Do not state that identification is not possible.

Respond using this exact format only:

Borough: <your answer>
Confidence: <Low / Medium / High>
Justification: <What features in the image led you to this conclusion?>

Do not include any additional commentary, explanation, or text outside the exact format specified.
~~~

### Text-Based Description Prompt

~~~
Imagine you’re taking a slow walk through [borough], a borough in London.
Describe everything you see, hear, and smell on a typical weekday afternoon.
Include details about the shops, the people, the architecture, and the general atmosphere.
Write it as if you’re observing it moment by moment, using vivid, sensory language.

Please do not mention or explicitly infer the borough name in the description.
~~~

After generating sensory descriptions for all boroughs, each description is submitted to the model in a separate, stateless inference call for a single-choice borough identification task, using the prompt shown below. All predictions are generated via the API with no conversational memory or shared session state, ensuring that each classification is independent and free from in-memory or carry-over bias.

~~~
Where am I?

TASK:
Read the description and identify which SINGLE London borough it most likely refers to.

RULES:
1) Choose exactly ONE London borough.
2) Do NOT name neighbourhoods, areas, or landmarks.
3) You must make a choice even if the description is ambiguous.
4) Do NOT state that identification is not possible.

Respond with the borough name only.
~~~

---

## 4. Modeling — Spatial Auditing Framework

LLMs do not expose explicit spatial representations.  
Urban cognition is therefore inferred **indirectly** from structured prediction behaviour.

### Core Metrics

**Recognisability**  
`TP / (TP + FN)`  
How reliably a borough is correctly identified.

**Visibility**  
`(TP + FP) / (TP + FP + FN + TN)`  
How often a borough dominates model predictions, regardless of correctness.

> Comparing recognisability and visibility reveals boroughs that attract disproportionate AI attention despite weak understanding.

### Structural Analysis
- Borough- and region-level confusion matrices  
- **Principal Component Analysis (PCA)**  
  - Used to identify boroughs that occupy similar positions in the model’s “mental space”  
  - Boroughs that cluster closely are treated as cognitively interchangeable by the model  
- Co-confusion analysis (systematic default predictions)  
- Spearman rank correlation (human–AI alignment)  
- Frobenius norm (cross-modality divergence)

---

## 4.1 Representation Analysis & Dimensionality Reduction

To analyse the structure of the model’s spatial behaviour, borough-level performance metrics were treated as numerical features in a shared analytical space.

### Representation Space
For each borough, **recognisability** and **visibility** scores were computed from the confusion matrices. These metrics form a low-dimensional feature representation capturing how frequently and how accurately each borough is identified by the model.

This representation serves as a behavioural proxy for the model’s spatial priorities and biases, rather than a direct analysis of internal model activations.

### Dimensionality Reduction
**Principal Component Analysis (PCA)** was applied to the borough-level metric space to identify dominant patterns of variation across boroughs. PCA enables visualisation of similarities and differences in how boroughs are treated by the model, revealing groups of boroughs with comparable recognition and visibility profiles.

Boroughs that cluster closely in PCA space are interpreted as being treated similarly by the model in terms of spatial prominence and recognisability.

### Correlation Analysis
Correlation analysis was used to relate:
- recognisability and visibility metrics,  
- positions in PCA space, and  
- external socio-economic indicators (e.g. Index of Multiple Deprivation).

This analysis tests whether systematic patterns in model behaviour align with real-world socio-economic structure.

### Key Insight
Metric-space analysis shows that AI-generated cognitive maps are **structured rather than random**.  
Variation in borough treatment reflects consistent behavioural patterns linked to visibility, recognisability, and socio-economic salience, rather than uniform or purely geographic representation.

---

## 4.2 NLP & Thematic Analysis (Image + Text)

To understand *why* recognition patterns differ across modalities, NLP techniques were applied to:

- image-task **justifications**, and  
- text-based **sensory descriptions**.

### Approach
- Sentence Transformer embeddings for all textual outputs  
- BERTopic for latent theme extraction  
- Correlation of theme prevalence with recognisability and visibility  

### Dominant Themes by Modality

**Image-based reasoning**
- Architecture and built form  
- Regeneration and redevelopment  
- Land use (residential vs commercial)  
- Green space and openness  

**Text-based reasoning**
- Atmosphere and “vibe”  
- Culture and nightlife  
- Transport and connectivity  
- Land use and regeneration  

### Key Insight
Spatial recognition in LLMs is driven less by geometric accuracy and more by **symbolic, experiential, and narrative cues**.  
Text inputs encode these signals far more explicitly than images, explaining why text-based recognition both outperforms image-only recognition and aligns more closely with human cognitive maps.

---

## 5. Results — Human–AI Cognitive Maps

![Summary of results: central amplification, peripheral suppression, and modality divergence](poster.jpg)

### Overall Performance
- Image-based accuracy: **15.4%** (above chance for 33 classes)  
- Text-based accuracy: **39.0%**

Text-based recognition substantially outperforms image-based recognition, but both exhibit uneven spatial understanding.

### Key Findings
- **Central London boroughs dominate predictions** across both modalities, regardless of input origin  
- **Outer boroughs are frequently misclassified or never predicted correctly**, resulting in effective digital invisibility  
- Certain boroughs act as **default cognitive anchors**, absorbing misclassifications from diverse locations  
- PCA reveals that geographically distant boroughs are often **cognitively collapsed** into similar representations  
- Image and text modalities show **structurally different cognitive maps**, indicating modality-dependent spatial reasoning
- Socio-economic status is strongly linked to model performance: boroughs with lower deprivation levels are not only predicted more frequently, but are also identified more correctly, while higher-deprivation areas suffer from both lower visibility and lower accuracy  

### Human–AI Comparison
- AI systems replicate known human centrality bias  
- However, they **amplify it**, producing stronger central dominance and deeper peripheral suppression than observed in human experiments  

LLMs do not merely mirror human cognitive maps — they **reshape and intensify them**.

---

## 6. Impact — Why This Matters Beyond London

When LLMs act as spatial gatekeepers:
- some places become hyper-visible,  
- others risk digital erasure,  
- inequalities scale automatically.

This has implications for:
- travel and mapping platforms,  
- local discovery and recommendation,  
- urban analytics and policy tools,  
- Responsible AI deployment.

### Recommended Actions
- Introduce spatial bias audits for geographic AI  
- Evaluate visibility alongside accuracy  
- Balance geographic exposure in evaluation pipelines  
- Monitor representational drift across model versions  

---

## 7. Future Work

- Multi-city replication (e.g. New York, Paris, Tokyo)  
- Finer spatial granularity (neighbourhoods, wards)  
- Cross-model benchmarking  
- Temporal drift analysis  
- Direct contemporary human–AI alignment studies  

---

## Technology Stack

- **Language:** Python  
- **Models:** Gemini 2.5 Flash, GPT-4o, Claude  
- **NLP:** Sentence Transformers, BERTopic  
- **Analysis:** Pandas, NumPy, SciPy  
- **Evaluation:** Confusion matrices, PCA, rank correlation  
- **External Data:** UK Census, IMD, Google Maps APIs  

---

## Code

[![View Code](https://img.shields.io/badge/View%20Code-6F42C1?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mithileshgungah)

> Full datasets and imagery may be restricted due to licensing.  
> Reproducible evaluation pipelines, prompt templates, and metric code are available on request.

---

## Contact

[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:mithileshgungah@gmail.com) &nbsp;&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mithilesh-gungah-331133215/)

---

**Author:** Mithilesh Gungah  
**Degree:** MSc Data Science, Middlesex University London  
**Supervisor:** Dr. Giovanni Quattrone
