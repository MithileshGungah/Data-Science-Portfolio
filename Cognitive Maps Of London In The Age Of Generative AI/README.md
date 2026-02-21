# Cognitive Maps of London in the Age of Generative AI  
## How Multimodal LLMs Perceive, Prioritise, and Distort Urban Space  
### Auditing Spatial Bias, Linguistic Salience, and Geographic Representation in Large Language Models  

---

## Executive Summary (For Recruiters)

**What this project is**  
A research-driven audit of how **multimodal Large Language Models (LLMs)** internally represent cities, using London as a controlled, policy-relevant case study.

Rather than training a new model, this project **evaluates learned models as real-world socio-technical systems**, probing how spatial knowledge, bias, and salience emerge from model behaviour.

**Why it matters**  
**LLMs are becoming spatial gatekeepers.**  
They increasingly power mapping, navigation, travel discovery, and urban analytics. If their internal “mental maps” are uneven, they can systematically amplify central areas while rendering peripheral communities digitally invisible—reinforcing spatial inequality at scale.

This project asks a critical question:  
> *Do AI systems perceive cities the way humans do—or do they distort urban space even further?*

**What I built**
- Adapted **Stanley Milgram’s human urban recognisability experiments** to multimodal LLMs  
- Designed a **spatial auditing framework** using two complementary metrics:
  - **Recognisability** (how accurately places are identified)
  - **Visibility** (how often places dominate predictions)
- Evaluated borough-level recognition across **image and text modalities**
- Applied **NLP-based thematic analysis** to:
  - image-task **justifications**, and  
  - text-based **sensory descriptions**
- Reconstructed **AI-generated cognitive maps** and **benchmarked them against human studies**

**Key findings**
- **Both image-based and text-based models independently over-recognise central London boroughs**, mirroring classic human cognitive maps  
- **AI-generated cognitive maps amplify human centrality bias**, producing stronger central dominance and deeper peripheral suppression than observed in human studies  
- Several outer boroughs are frequently misclassified or entirely invisible  
- Image and text modalities produce **different spatial representations**, meaning the same borough can “look” different to the model depending on modality  
- NLP analysis shows recognition is driven by **culture, transport, and “vibe”**, not physical form alone  

**Skills demonstrated**
- Multimodal ML evaluation (beyond accuracy)
- NLP: embeddings, topic modeling, semantic analysis
- Bias and fairness auditing
- Metric design and statistical reasoning
- End-to-end Python data and evaluation pipelines

---

![LLM borough recognisability and visibility across image and text modalities](LLM_Boroughs.png)

---

## 1. Problem — Spatial Bias in AI City Perception

Cities are not perceived uniformly.  
Decades of urban psychology research show that **central and symbolically salient areas dominate mental maps**, while peripheral districts fade from memory.

As Large Language Models increasingly mediate **mapping, navigation, travel, and urban decision-making**, a critical question emerges:

> **How do AI systems “see” cities—and whose places become visible or invisible as a result?**

This project investigates whether multimodal LLMs:
- replicate known human spatial biases,
- amplify them,
- or introduce new distortions altogether.

### Business & Societal Context
- LLMs are embedded in location-based services and recommendation engines  
- Uneven digital representation risks reinforcing spatial inequality  
- Borough-level misrepresentation can affect:
  - travel and navigation recommendations  
  - cultural and commercial visibility  
  - urban planning and smart-city tools  
  - fairness in geographic AI systems  

### Research Objective
Develop a **replicable spatial auditing framework** that:
- measures how LLMs recognise urban areas across image and text,
- detects central amplification and peripheral suppression,
- reconstructs model-generated cognitive maps,
- benchmarks AI spatial perception against established human patterns.

---

## 2. Human Baseline — Urban Cognitive Maps

### Stanley Milgram’s Urban Recognisability Experiment

In the 1970s, social psychologist **Stanley Milgram** studied how people form mental representations of cities.

Rather than asking participants to draw maps, he tested whether individuals could identify locations from:
- partial visual scenes,  
- short descriptive cues.  

Human studies consistently show that:
- central and symbolic areas are over-recognised,
- peripheral and residential districts are overlooked,
- recognisability correlates with **centrality, affluence, and exposure**.

These asymmetries form **cognitive maps**—mental representations shaped by salience rather than geographic accuracy.

This project applies the same logic to **multimodal LLMs**, enabling direct **human–AI comparison**.

---

## 3. Data — Multimodal Urban Inputs

### Urban Coverage
- **Geography:** All 33 boroughs of Greater London  
- **Spatial unit:** Boroughs (authoritative, recognisable, policy-relevant)

### Multimodal Inputs

**Image-based**
- 495 Google Street View images  
- 15 images per borough  
- Random sampling within borough boundaries  
- Landmarks and transport hubs excluded to avoid trivial cues  

**Text-based**
- 495 borough-specific sensory descriptions  
- Generated by the model itself  
- Borough names withheld during inference  
- Focus on atmosphere, architecture, people, and movement  

### Dataset Summary

| Component | Count |
|---------|-------|
| Boroughs | 33 |
| Images | 495 |
| Text descriptions | 495 |
| Total model predictions | 990 |

### External Contextual Data
- Index of Multiple Deprivation (IMD 2019)  
- UK Census data (2021)  
- Population density  
- Transport connectivity  
- Digital visibility proxies (Google Maps imagery counts)  

---

## 4. Method — Multimodal Recognition Tasks

Two complementary recognition tasks were used.

### Image-Based Recognition
- Input: Street-level image  
- Task: Predict London borough  
- Output: Borough prediction **plus a natural-language justification**

### Text-Based Recognition
- Input: Borough-specific sensory description  
- Task: Predict London borough  
- Output: Single borough prediction  

Each task produces a **confusion matrix**, treated as a behavioural proxy for a **cognitive map**.

---

## 5. Modeling — Spatial Auditing Framework

LLMs do not expose explicit spatial representations.  
Urban cognition is therefore inferred **indirectly** from prediction structure.

### Core Metrics

**Recognisability**  
`TP / (TP + FN)`  
Measures how reliably a borough is correctly identified.

**Visibility**  
`(TP + FP) / (TP + FP + FN + TN)`  
Measures how often a borough dominates predictions, regardless of accuracy.

> Comparing recognisability and visibility reveals places that dominate AI attention despite weak understanding.

### Structural Analysis
- Confusion matrices (borough and regional levels)  
- Principal Component Analysis (PCA)  
- Co-confusion clustering (systematic “default guess” patterns)  
- Spearman rank correlation (human–AI alignment)  
- Frobenius norm (cross-modality divergence)

---

## 6. NLP & Thematic Analysis (Image + Text)

To explain *why* recognition patterns differ across modalities, NLP techniques were applied to **both**:
- image-task **justifications**, and  
- text-based **sensory descriptions**.

### Approach
- Sentence Transformer embeddings for all textual outputs  
- BERTopic for latent theme extraction  
- Correlation of theme prevalence with recognisability and visibility  

### Dominant Themes
- Culture and nightlife  
- Transport and connectivity  
- Food and commerce  
- Regeneration  
- Atmosphere (“vibe”)

**Key insight**  
Recognition (especially in text) is driven by **experiential and symbolic language**, not physical geometry.  
This helps explain why text-based recognition substantially outperforms image-only recognition and aligns more closely with human perception.

---

## 7. Results — Human–AI Cognitive Maps

![Summary of results: central amplification, peripheral suppression, and modality divergence](poster.jpg)

### Performance
- Image-based accuracy: **15.4%** (above chance for 33 classes)  
- Text-based accuracy: **39.0%**

### Human–AI Comparison
- Both modalities reproduce **human centrality bias**  
- AI **amplifies** this bias beyond human levels  

### Structural Findings (Recruiter-Friendly)
- **Central areas dominate predictions across both image and text**, receiving disproportionate attention regardless of modality  
- **Many outer boroughs are rarely or never identified correctly**, making them effectively invisible in AI perception  
- **Certain boroughs become “default guesses” under uncertainty**, absorbing misclassifications from many other areas  
- **Image-based and text-based reasoning rely on different signals**, leading to inconsistent spatial understanding across modalities  

*AI does not merely copy human cognitive maps—it reshapes and exaggerates them.*

---

## 8. Impact — Why This Matters Beyond London

When LLMs act as spatial gatekeepers:
- some places become hyper-visible,  
- others risk digital erasure,  
- inequalities scale automatically.

This has direct implications for:
- travel and mapping platforms,
- real estate and local discovery,
- urban analytics and policy tools,
- Responsible AI deployment.

### Recommended Actions
- Introduce spatial bias audits for geographic AI  
- Monitor recognisability **and** visibility, not accuracy alone  
- Balance geographic exposure in evaluation pipelines  
- Track representational drift over time  

---

## 9. Future Work — Research Extensions

- **Multi-city replication** (e.g. New York, Paris, Tokyo)  
- **Finer spatial granularity** (neighbourhoods, wards)  
- **Cross-model benchmarking** (closed vs open-source multimodal models)  
- **Temporal drift analysis** across model versions  
- **Direct human–AI alignment studies** using contemporary human data  

---

## Technology Stack

- **Language:** Python  
- **Models:** Gemini 2.5 Flash, GPT-4o, Claude (model-agnostic pipeline)  
- **NLP:** Sentence Transformers, BERTopic  
- **Analysis:** Pandas, NumPy, SciPy  
- **Evaluation:** Confusion matrices, PCA, Spearman correlation  
- **External Data:** UK Census, IMD, Google Maps APIs  

---

## Code

[![View Code](https://img.shields.io/badge/View%20Code-6F42C1?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mithileshgungah)

> Full datasets and imagery may be restricted due to licensing.  
> Reproducible evaluation pipelines, prompt templates, and metric code are available on request.

---

## Contact

[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:mithileshgungah@gmail.com)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mithilesh-gungah-331133215/)

---

**Author:** Mithilesh Gungah  
**Degree:** MSc Data Science, Middlesex University London  
**Supervisor:** Dr. Giovanni Quattrone
