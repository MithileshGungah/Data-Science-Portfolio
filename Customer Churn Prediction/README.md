# Customer Churn Prediction Engine  
### A Business-Aligned Machine Learning System for Proactive Customer Retention

<p align="center">
  <img src="churn_rate.png" alt="Customer Churn Rate" width="500">
</p>

---

## Executive Summary

This project develops a cost-sensitive customer churn prediction system designed to support proactive, revenue-preserving retention strategies in subscription-based businesses.

Using the IBM Telco dataset (7,043 customers; 26.6% churn rate), churn prediction is reframed as a **business optimisation problem** - where the cost of missing a churner (false negative) materially exceeds the cost of contacting a retained customer. Model evaluation is therefore driven by **recall**, not raw accuracy.

A structured, production-style workflow was implemented, benchmarking Logistic Regression, Decision Tree, Random Forest, and XGBoost under consistent cross-validated evaluation. Through recall-focused hyperparameter tuning, **Tuned XGBoost** was selected as the final model.

### Key Outcomes
- Recall improved from **69% → 82%** (+12.8pp)
- False negatives reduced by **~42%**
- Precision deliberately traded for recall to align with asymmetric business costs
- Equivalent to **~£150k recoverable lifetime value per 10,000 customers** (conservative retention assumptions)

### Business Value
The system enables a shift from reactive churn response to proactive, targeted retention, allowing organisations to:
- Intervene before revenue is lost  
- Allocate retention spend more efficiently  
- Reduce recurring revenue leakage at scale  

This project demonstrates how metric selection, model tuning, and evaluation design directly influence financial outcomes.

---

## 1. Problem Statement

Customer churn represents a direct and recurring revenue risk in subscription-based businesses. Retaining existing customers is typically more cost-effective than acquisition, making early churn detection strategically critical.

This project focuses on identifying at-risk customers early enough to enable targeted, cost-effective intervention - reframing churn detection as a cost-sensitive decision system rather than a pure classification task.

### Business Context
- Churn rate: **26.6%**
- Retention efforts are broad and inefficient
- Missing a churner leads to irreversible revenue loss
- Contacting a non-churner incurs relatively low cost

### Objective

Build a high-recall churn prediction model that:

- Minimises false negatives (revenue-critical errors)
- Accepts controlled increases in false positives
- Aligns evaluation metrics with business cost asymmetry
- Produces insights actionable by retention teams

---

## 2. Data Overview

### Dataset
- **Source:** IBM Telco Customer Churn Dataset  
- **Records:** 7,043 customers  
- **Features:** 21 demographic, service, contract, and billing variables  

| Aspect | Details |
|--------|--------|
| Target | `Churn` |
| Churn Rate | 26.6% |
| Feature Types | Categorical + Numerical |
| Primary Challenge | Class imbalance |

### Data Considerations
- `TotalCharges` required numeric conversion and missing value handling
- Class imbalance required recall-aware evaluation
- Dataset size supports both interpretable and ensemble models

---

## 3. Methodology

A structured workflow ensured technical rigor and business alignment:

1. Data validation and preprocessing  
2. Exploratory Data Analysis  
3. Feature engineering  
4. Baseline modeling  
5. Cross-validated hyperparameter tuning  
6. Model benchmarking  
7. Business-driven model selection  

Because churn prevention involves asymmetric cost risk, model evaluation prioritised **recall, precision, and F1-score**, rather than accuracy.

---

## 4. Modeling Strategy

All models were evaluated on a fixed **20% hold-out test set** under consistent metrics.

### Models Evaluated
- Logistic Regression (baseline & tuned)
- Decision Tree (baseline & tuned)
- Random Forest (baseline & tuned)
- XGBoost (baseline & tuned)

### Tuning Strategy
- Cross-validated hyperparameter optimisation
- Recall explicitly prioritised
- Class imbalance handled via weighting
- Trade-offs evaluated via confusion matrix comparison

---

## 5. Model Performance

### Benchmark Comparison

| Metric | LR | Tuned LR | DT | Tuned DT | RF | Tuned RF | XGBoost | **Tuned XGBoost** |
|--------|----|----------|----|----------|----|----------|---------|------------------|
| Accuracy | 0.80 | 0.79 | 0.72 | 0.78 | 0.78 | 0.79 | 0.74 | 0.73 |
| Precision (Churn) | 0.64 | 0.64 | 0.48 | **0.66** | 0.62 | 0.65 | 0.51 | 0.49 |
| Recall (Churn) | 0.54 | 0.51 | 0.49 | 0.40 | 0.49 | 0.50 | 0.69 | **0.82** |
| F1-score (Churn) | 0.58 | 0.57 | 0.48 | 0.50 | 0.55 | 0.56 | 0.59 | **0.62** |

**Primary metric:** Recall (Churn)

---

## Final Model Selection

### Selected Model: Tuned XGBoost

**Rationale**
- Highest churn recall (**82%**)
- +12.8pp absolute recall improvement
- ~42% reduction in false negatives
- Precision trade-off accepted to minimise revenue risk

### Confusion Matrix Comparison

**Baseline XGBoost**

| Actual \ Predicted | No Churn | Churn |
|-------------------|----------|-------|
| No Churn          | 787      | 246   |
| Churn             | 116      | 258   |

**Tuned XGBoost**

| Actual \ Predicted | No Churn | Churn |
|-------------------|----------|-------|
| No Churn          | 720      | 313   |
| Churn             | 68       | 306   |

False negatives reduced from 116 → 68.

---

## 6. Business Impact

### Quantified Financial Impact (Scaled Projection)

Scaling recall uplift to a cohort of 10,000 customers:

- 10,000 × 26.6% churn × 12.8pp recall uplift ≈ **341 additional churners identified**
- Forward-looking revenue per churner ≈ **£1,464** (tenure differential × monthly revenue)
- Revenue exposure identified ≈ **~£500k per 10,000 customers**
- Assuming 30% retention success → **~£150k recoverable revenue**

These projections use transparent, conservative assumptions and represent scalable financial exposure rather than guaranteed realised revenue.

---

By prioritising recall, the model shifts retention strategy from reactive to proactive - reducing revenue-critical missed churners while accepting manageable outreach cost increases.

---

### Key Drivers of Churn
- Month-to-month contracts
- Low tenure
- Higher monthly charges
- Fiber plans without support services
- Lack of technical support or online security

---

### Recommended Business Actions

**Contract & Pricing**
- Incentivise contract upgrades
- Target high-value churn-risk customers

**Onboarding & Engagement**
- Prioritise low-tenure outreach
- Improve early lifecycle engagement

**Service Optimisation**
- Bundle support services with fiber plans
- Proactively engage support-lacking customers

**Operational Monitoring**
- Track campaign ROI
- Retrain model periodically
- Monitor recall–precision balance

---

## 7. Future Enhancements
- Threshold optimisation using cost curves
- Probability calibration
- SHAP-based explainability
- A/B testing of retention interventions
- Uplift modelling for targeted ROI optimisation

---

## Conclusion

This project demonstrates a business-aligned churn prediction system integrating:

- Structured ML workflow
- Cost-sensitive evaluation
- Transparent financial translation
- Actionable retention strategy

Optimising for recall rather than accuracy ensures alignment between predictive performance and financial impact.

**Final Recommendation:** Deploy Tuned XGBoost with recall-focused thresholding to support proactive churn prevention.

---

## Technology Stack
- **Language:** Python 3.12  
- **Libraries:** XGBoost, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn  

---

## Code

[![View Notebook](https://img.shields.io/badge/View%20Notebook-6F42C1?style=for-the-badge&logo=github&logoColor=white)](./Telco_Customer_Churn_Prediction.ipynb)

---

## Contact

[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:mithileshgungah@gmail.com) &nbsp;&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mithilesh-gungah-331133215/)
