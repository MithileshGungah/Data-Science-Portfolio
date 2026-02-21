# Cognitive Maps of London in the Age of Generative AI  
## How Multimodal LLMs Perceive, Prioritise, and Distort Urban Space  

### Auditing Spatial Bias, Linguistic Salience, and Geographic Representation in Large Language Models  

---

## Executive Summary (For Recruiters)

**What this project is**  
A research-driven audit of how **multimodal Large Language Models (LLMs)** internally represent cities, using London as a controlled, policy-relevant case study.

Rather than training a new model, this project **interrogates learned models** to understand how spatial knowledge, bias, and salience emerge in real-world AI systems.

**Why it matters**  
**LLMs are becoming spatial gatekeepers.**  
They increasingly power mapping, navigation, travel discovery, and urban analytics. If their internal “mental maps” are uneven, they can systematically amplify central areas while rendering peripheral communities digitally invisible — reinforcing spatial inequality at scale.

This project asks a simple but critical question:

> *Do AI systems see cities the way humans do — or do they distort them further?*

**What I built**
- Adapted **Stanley Milgram’s human urban recognisability experiments** to multimodal LLMs  
- Designed a **spatial auditing framework** using novel metrics:
  - **Recognisability** (correct identification)
  - **Visibility** (prediction dominance)
- Evaluated borough-level recognition across **image and text modalities**
- Applied **NLP-based thematic analysis** to explain *why* certain places are recognised
- Reconstructed **AI-generated cognitive maps** and benchmarked them against human studies

**Key findings**
- **Both image-based and text-based models independently over-recognise central London boroughs**, mirroring classic human cognitive maps  
- **AI-generated cognitive maps amplify human centrality bias**, producing sharper central dominance and deeper peripheral suppression than observed in human studies  
- Several outer boroughs are frequently misclassified or entirely invisible  
- Image-based and text-based reasoning produce **structurally different spatial maps**
- NLP analysis shows text recognition is driven by **culture, transport, and “vibe”**, not physical form alone  

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

> **How do AI systems “see” cities — and whose places become visible or invisible as a result?**

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
Develop a **replicable auditing framework** that:
- measures how LLMs recognise urban areas across image and text,
- detects central amplification and peripheral suppression,
- reconstructs model-generated cognitive maps,
- benchmarks AI spatial perception against established human patterns.

---

## 2. Data — Human Baselines and Multimodal Inputs

### Human Baseline: Urban Cognitive Maps

#### Stanley Milgram’s Urban Recognisability Experiment

In the 1970s, social psychologist **Stanley Milgram** studied how people form mental representations of cities.

Rather than asking participants to draw maps, he tested whether individuals could identify locations from:
- partial visual scenes,
- short descriptive cues.

Human studies consistently show that:
- central and symbolic areas are over-recognised,
- peripheral and residential districts are overlooked,
- recognisability correlates with **centrality, affluence, and exposure**.

These asymmetries form **cognitive maps** — mental representations shaped by salience rather than geographic accuracy.

This project applies the same logic to **multimodal LLMs**, enabling direct **human–AI comparison**.

---

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

---

## 3. Method — Experimental Design

Two complementary recognition tasks were used.

### Image-Based Recognition
- Input: Street-level image  
- Task: Predict London borough  
- Output: Borough prediction plus justification  

### Text-Based Recognition
- Input: Borough-specific sensory description  
- Task: Predict London borough  
- Output: Single borough prediction  

Each task produces a **confusion matrix**, which functions as a **behavioural proxy for a cognitive map**.

---

## 4. Modeling — Auditing & NLP Framework

LLMs do not expose internal spatial representations.  
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
- Co-confusion clustering (attractor detection)  
- Spearman rank correlation (human–AI alignment)  
- Frobenius norm (cross-modality divergence)

---

## NLP & Thematic Analysis

To explain *why* text-based recognition outperforms image-based recognition, NLP methods were applied.

### Approach
- Sentence Transformer embeddings for borough descriptions  
- BERTopic for latent theme extraction  
- Correlation of themes with recognisability and visibility  

### Dominant Themes
- Culture and nightlife  
- Transport and connectivity  
- Food and commerce  
- Regeneration  
- Atmosphere (“vibe”)

**Key insight:**  
Text-based recognition is driven by **experiential and symbolic language**, not physical geometry — aligning closely with human urban perception.

---

## 5. Results — Human–AI Cognitive Maps

![Summary of results: central amplification, peripheral suppression, and modality divergence](poster.jpg)

### Performance
- Image-based accuracy: **15.4%** (above chance for 33 classes)  
- Text-based accuracy: **39.0%**

### Human–AI Comparison
- Both modalities reproduce **human centrality bias**  
- AI **amplifies** this bias beyond human levels  

### Structural Findings
- Strong central amplification across both modalities  
- Peripheral suppression and invisibility  
- Attractor boroughs absorbing misclassification  
- Fragmented multimodal representations  

*AI does not merely copy human cognitive maps — it reshapes and exaggerates them.*

---

## 6. Impact — Why This Matters Beyond London

When LLMs act as spatial gatekeepers:
- some places become hyper-visible,
- others risk digital erasure,
- inequalities scale automatically.

This matters for:
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

## 7. Future Work — Research and Extensions

- **Multi-city replication** (e.g. New York, Paris, Tokyo)  
- **Finer spatial granularity** (neighbourhoods, wards)  
- **Cross-model benchmarking** (closed vs open-source multimodal models)  
- **Temporal drift analysis** across model versions  
- **Direct human–AI alignment studies** with contemporary human data  

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

[View Code](https://github.com/mithileshgungah)

> Full datasets and imagery may be restricted due to licensing.  
> Reproducible evaluation pipelines, prompt templates, and metric code are available on request.

---

**Author:** Mithilesh Gungah  
**Degree:** MSc Data Science, Middlesex University London  
**Supervisor:** Dr. Giovanni Quattrone
