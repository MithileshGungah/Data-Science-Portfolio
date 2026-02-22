# Cognitive Maps of London in the Age of Generative AI  
## How Multimodal LLMs Perceive, Prioritise, and Distort Urban Space  
### Auditing Spatial Bias, Linguistic Salience, and Geographic Representation in Large Language Models  

---

## For Recruiters & Hiring Managers

**What this project is**  
A research-driven audit of how **multimodal Large Language Models (LLMs)** internally represent cities, using London as a controlled, policy-relevant case study.

Rather than training a new model, this project **evaluates deployed foundation models as socio-technical systems**, analysing how spatial knowledge, salience, bias, and *reasoning* emerge from model behaviour across image and text.

**Why it matters**  
**LLMs are becoming spatial gatekeepers.**  
They increasingly power mapping, navigation, travel discovery, local search, and urban analytics. If their internal “mental maps” are uneven, they risk systematically amplifying central areas while rendering peripheral communities digitally invisible — reinforcing spatial inequality at scale.

This project asks a critical question:  
> *Do AI systems perceive cities the way humans do — or do they distort urban space even further?*

**What I built**
- Adapted **Stanley Milgram’s urban recognisability experiments** from human cognition to multimodal LLMs  
- Designed a **spatial auditing framework** that evaluates *what models predict*, *how often*, and *why*  
- Introduced two complementary metrics:
  - **Recognisability** — how accurately places are identified  
  - **Visibility** — how strongly places dominate model predictions  
- Evaluated borough-level recognition across **image and text modalities**  
- Analysed **model reasoning and descriptions** using NLP:
  - image-task **justifications**, and  
  - text-based **sensory descriptions**  
- Reconstructed **AI-generated cognitive maps** and benchmarked them against established human studies  

**Key findings**
- Both image-based and text-based models **systematically over-recognise central London**, mirroring classic human cognitive maps  
- **AI-generated cognitive maps amplify human centrality bias**, producing stronger central dominance and deeper peripheral suppression than observed in human experiments  
- Several outer boroughs are frequently misclassified or effectively invisible  
- Image and text modalities rely on **different cognitive signals**, leading to inconsistent spatial understanding  
- NLP analysis shows recognition is driven by **symbolic, cultural, and experiential cues** (e.g. transport, regeneration, “vibe”), not physical form alone
- Wealthier, less deprived boroughs are both recognised more often and recognised more accurately: model visibility and recognisability are positively correlated with lower IMD scores, indicating that LLM spatial understanding aligns closely with existing socio-economic advantage  

**Skills demonstrated**
- Multimodal ML evaluation beyond accuracy  
- Metric design for bias and visibility auditing  
- NLP: embeddings, topic modelling, semantic analysis  
- Statistical analysis and dimensionality reduction  
- End-to-end Python data pipelines  
- Responsible AI and geographic fairness analysis  

---

![LLM borough recognisability and visibility across image and text modalities](LLM_Boroughs.png)

---

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

## 2. Human Baseline — Urban Cognitive Maps

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

## 3. Data — Multimodal Urban Inputs

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

## 4. Method — Multimodal Recognition Tasks

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

## 5. Modeling — Spatial Auditing Framework

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

## 6. NLP & Thematic Analysis (Image + Text)

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

## 7. Results — Human–AI Cognitive Maps

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

## 8. Impact — Why This Matters Beyond London

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

## 9. Future Work

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
