# Customer Churn Prediction Engine
### A business-aligned machine learning system for proactive customer retention

<p align="center">
  <img src="churn_rate.png" alt="Customer Churn Rate" width="500">
</p>

---

## 1. Problem Statement

Customer churn represents a **direct and recurring revenue risk** for subscription-based businesses. Retaining an existing customer is typically far less costly than acquiring a new one, making early churn detection a critical business capability.

This project focuses on identifying **customers most likely to churn early enough** to enable **targeted, cost-effective retention strategies**, rather than relying on reactive or untargeted outreach.

### Business Context
- Observed churn rate: **26.5%**, indicating substantial revenue leakage
- Existing retention efforts are **broad and inefficient**
- Missing a churner (**false negative**) leads to irreversible revenue loss, while contacting a non-churner incurs relatively low cost

### Objective
Build a **cost-sensitive, recall-optimised churn prediction model** that:
- Proactively flags at-risk customers
- Explicitly minimises false negatives
- Aligns evaluation metrics with business costs
- Produces insights actionable by retention and marketing teams

---

## 2. Data Overview

### Dataset
- **Source:** IBM Telco Customer Churn Dataset  
- **Records:** 7,043 customers  
- **Features:** 21 variables covering demographics, services, contracts, and billing

| Aspect | Details |
|------|--------|
| Target variable | `Churn` (Yes / No) |
| Churn rate | 26.5% |
| Feature types | Categorical + numerical |
| Primary challenge | Class imbalance |

### Key Observations
- `TotalCharges` required numeric conversion and missing-value handling
- Moderate class imbalance required metric-aware evaluation
- Dataset scale supports both interpretable and ensemble models

---

## 3. Methodology

A structured, production-style workflow was followed to ensure **technical rigor and business alignment**:

1. Data validation and preprocessing  
2. Exploratory Data Analysis (EDA)  
3. Feature engineering  
4. Baseline modeling  
5. Cross-validated hyperparameter tuning  
6. Model benchmarking  
7. Business-driven model selection  

**Evaluation emphasis:** Recall, precision, and F1-score, rather than accuracy alone, to reflect asymmetric business costs.

---

## 4. Modeling Strategy

All models were trained and evaluated using a **consistent evaluation framework**, with comparisons made on a fixed **20% hold-out test set** to ensure fair benchmarking.

### Models Evaluated
- Logistic Regression (baseline & tuned)
- Decision Tree (baseline & tuned)
- Random Forest (baseline & tuned)
- XGBoost (baseline & tuned)

### Hyperparameter Tuning
- Performed via **cross-validated hyperparameter optimisation**
- Recall explicitly prioritised to reduce costly false negatives
- XGBoost enhanced using class-imbalance weighting and recall-focused tuning

---

## 5. Model Performance & Results

### Benchmark Comparison

| Metric | LR | Tuned LR | DT | Tuned DT | RF | Tuned RF | XGBoost | **Tuned XGBoost** |
|------|----|----------|----|----------|----|----------|---------|------------------|
| Accuracy | 0.80 | 0.79 | 0.72 | 0.78 | 0.78 | 0.79 | 0.74 | 0.73 |
| Precision (Churn) | 0.64 | 0.64 | 0.48 | **0.66** | 0.62 | 0.65 | 0.51 | 0.49 |
| Recall (Churn) | 0.54 | 0.51 | 0.49 | 0.40 | 0.49 | 0.50 | 0.69 | **0.82** |
| F1-score (Churn) | 0.58 | 0.57 | 0.48 | 0.50 | 0.55 | 0.56 | 0.59 | **0.62** |

---

## Final Model Selection

### Selected Model: **Tuned XGBoost**

**Rationale**
- Achieves the **highest churn recall (82%)**, capturing the majority of at-risk customers
- Delivers a **13 percentage-point absolute recall improvement** over baseline XGBoost
- Represents a **19% relative increase in recall**
- Reduces false negatives by approximately **42%**
- Accepts lower precision as a deliberate trade-off to minimise business risk

### Confusion Matrix Comparison

#### Baseline XGBoost

| Actual \ Predicted | No Churn | Churn |
|------------------|----------|-------|
| No Churn         | 787      | 246   |
| Churn            | 116      | 258   |

#### Tuned XGBoost (Recall-Focused)

| Actual \ Predicted | No Churn | Churn |
|------------------|----------|-------|
| No Churn         | 720      | 313   |
| Churn            | 68       | 306   |

**Key Difference:**  
Hyperparameter tuning significantly reduces **false negatives** (from **116 → 68**, ~42% reduction), at the cost of increased false positives — a deliberate and appropriate trade-off for churn prediction.

---

## 6. Business Impact

The churn prediction model enables a shift from **reactive churn response** to **proactive, data-driven retention**, allowing the business to intervene before revenue is lost.

### Key Drivers of Churn

Model interpretation highlights the following primary churn drivers:

1. **Contract Type (Month-to-Month)**  
   Customers on month-to-month contracts exhibit significantly higher churn risk due to lower switching barriers.

2. **Customer Tenure**  
   Churn is most pronounced among new and short-tenure customers, indicating onboarding and early experience gaps.

3. **Monthly Charges**  
   Higher monthly charges are associated with churn when perceived value does not match cost.

4. **Fiber Optic Internet Service**  
   Fiber customers show elevated churn, particularly when support services are absent.

5. **Technical Support**  
   Lack of TechSupport strongly correlates with churn, highlighting the importance of post-sale service quality.

6. **Online Security Services**  
   Customers without OnlineSecurity are more likely to churn, suggesting unmet expectations around reliability and protection.

---

### Recommended Business Actions

Based on these insights, the following actions are recommended:

- Proactively target high-risk customers flagged by the model before churn occurs  
- Incentivise contract upgrades for month-to-month customers through discounts or bundles  
- Strengthen onboarding and engagement for low-tenure customers  
- Bundle support and security services for fiber customers to improve perceived value  
- Prioritise retention spend based on predicted churn risk and customer value  
- Monitor recall–precision trade-offs to balance campaign cost and ROI  
- Retrain the model periodically to adapt to evolving customer behaviour  

---

### Business Value Delivered

By aligning model optimisation with business costs, the solution:
- Reduces missed churners and associated revenue leakage  
- Enables more efficient allocation of retention resources  
- Supports data-driven decision-making across marketing and customer success teams  
- Provides a scalable framework for ongoing churn management  

---

## 7. Future Enhancements

### Modeling Improvements
- Bayesian hyperparameter optimisation
- Probability calibration for cost-based thresholding
- Explicit cost-sensitive loss functions

### Explainability & Trust
- SHAP-based feature attribution for stakeholder transparency
- Customer-level explanations to support targeted interventions

### Production & Monitoring
- Deploy as batch or real-time scoring service
- Monitor data drift and performance decay
- Automate periodic retraining pipelines

### Business Integration
- A/B test retention strategies driven by predictions
- Measure uplift and campaign effectiveness
- Integrate with CRM and marketing automation platforms

---

## Conclusion

This project demonstrates a **business-aligned churn prediction system** that combines:
- Insight-driven EDA
- Cost-sensitive modeling
- Rigorous benchmarking
- Metric-driven decision-making

By prioritising recall over raw accuracy, the final solution aligns predictive performance with **real financial impact**.

**Final Recommendation:**  
Deploy **Tuned XGBoost** to maximise churn detection and support proactive, cost-effective retention strategies.

---

## Technology Stack
- **Language:** Python 3.12  
- **Libraries:** XGBoost, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn

---

## Code
[View Notebook](./Telco_Customer_Churn_Prediction.ipynb)

---

## Contact
- **Email:** mithileshgungah@gmail.com  
- **LinkedIn:** https://www.linkedin.com/in/mithilesh-gungah-331133215/
