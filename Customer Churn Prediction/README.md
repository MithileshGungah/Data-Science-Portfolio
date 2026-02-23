# Customer Churn Prediction Engine
### A business-aligned machine learning system for proactive customer retention

<p align="center">
  <img src="churn_rate.png" alt="Customer Churn Rate" width="500">
</p>

---

## 1. Problem Statement

Customer churn represents a **direct and measurable revenue risk** for subscription-based businesses.

This project focuses on identifying **customers most likely to churn** early enough to enable **targeted, cost-effective retention strategies**, rather than broad and inefficient outreach.

### Business Context
- Observed churn rate: **26.5%**
- Existing retention efforts are **untargeted and inefficient**
- Missing a churner (**false negative**) is significantly **more costly** than contacting a non-churner

### Objective
Build a **cost-sensitive, high-recall churn prediction model** that:
- Proactively flags at-risk customers
- Explicitly minimizes false negatives
- Prioritizes business impact over raw accuracy
- Produces insights actionable by retention teams

---

## 2. Data Overview

### Dataset
- **Source:** IBM Telco Customer Churn Dataset  
- **Records:** 7,043 customers  
- **Features:** 21 (demographics, services, contracts, billing)

| Aspect | Details |
|------|--------|
| Target variable | `Churn` (Yes / No) |
| Churn rate | 26.5% |
| Feature types | Categorical + numerical |
| Key challenge | Class imbalance |

### Key Observations
- `TotalCharges` required numeric conversion and missing-value handling
- Moderate class imbalance necessitated recall-focused evaluation
- Dataset scale supports both interpretable and ensemble models

---

## 3. Methodology

A structured, production-style workflow was followed:

1. Data validation and preprocessing  
2. Exploratory Data Analysis (EDA)  
3. Feature engineering  
4. Baseline modeling  
5. **Cross-validated hyperparameter tuning**  
6. Model benchmarking  
7. **Business-driven model selection**

**Evaluation emphasis:** Recall, precision, and F1-score (not accuracy alone)

---

## 4. Modeling Strategy

Models were trained and evaluated using a **consistent framework**, with all comparisons made on a fixed **20% hold-out test set**.

### Models Evaluated
- Logistic Regression (baseline & tuned)
- Decision Tree (baseline & tuned)
- Random Forest (baseline & tuned)
- XGBoost (baseline & tuned)

### Hyperparameter Tuning
- Performed via **cross-validated hyperparameter optimisation**
- Recall prioritised to minimise costly false negatives
- XGBoost additionally tuned using class imbalance weighting and recall-focused configurations

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

## 6. Final Model Selection

### Selected Model: **Tuned XGBoost**

**Rationale**
- Highest churn recall (**82%**), capturing the majority of at-risk customers
- **13 percentage-point absolute recall improvement** over baseline XGBoost
- **19% relative increase in recall**
- **~42% reduction in false negatives**, directly reducing missed churners
- Lower precision accepted as a deliberate trade-off to reduce business risk

### Confusion Matrix (Tuned XGBoost)

| Actual \\ Predicted | No Churn | Churn |
|------------------|----------|-------|
| No Churn         | 723      | 310   |
| Churn            | 67       | 307   |

---

## 7. Business Impact

### Key Outcomes
- **Designed an end-to-end, cost-sensitive churn prediction pipeline** on a 7,043-customer telecom dataset with 21 features, optimising recall to minimise false negatives under a 26.5% churn rate  
- **Benchmarked and tuned four model families** (Logistic Regression, Decision Tree, Random Forest, and XGBoost) via cross-validated hyperparameter optimisation, selecting XGBoost for superior churn recall  
- **Improved churn recall from 69% to 82% through targeted XGBoost tuning**, delivering a 13 percentage-point absolute gain and a 19% relative increase, while reducing false negatives by approximately 42% on a 20% hold-out test set  

### Practical Implications
- Earlier identification of at-risk customers
- More efficient allocation of retention spend
- Reduced revenue leakage from missed churners

---

## 8. Future Enhancements

- Bayesian hyperparameter optimisation
- Probability calibration for campaign thresholding
- SHAP-based explainability for stakeholder transparency
- Deployment with monitoring, drift detection, and automated retraining

---

## Conclusion

This project demonstrates a **business-aligned churn prediction system**, combining:
- Insight-driven EDA
- Cost-sensitive modeling
- Rigorous benchmarking
- Metric-driven decision-making

By explicitly prioritising recall, the final solution aligns predictive performance with **real financial impact**.

**Final Recommendation:**  
Deploy **Tuned XGBoost** to maximise churn detection and support proactive, cost-effective retention strategies.

---

## Technology Stack
- **Language:** Python 3.12  
- **Libraries:** XGBoost, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn

---

## Code
[![View Code](https://img.shields.io/badge/View%20Code-6F42C1?style=for-the-badge&logo=github&logoColor=white)](./Telco_Customer_Churn_Prediction.ipynb)

---

## Contact
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:mithileshgungah@gmail.com) &nbsp;&nbsp; [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mithilesh-gungah-331133215/)
