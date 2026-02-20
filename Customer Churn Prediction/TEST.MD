<h1 align="center">Customer Churn Prediction Engine</h1>
<h3 align="center">A business-aligned machine learning system for proactive customer retention</h3>

<p align="center">
  <img src="churn_rate.png" alt="Customer Churn Rate" width="500">
</p>

---

## 1. Problem Statement

Customer churn represents a **direct revenue risk** for subscription-based businesses.

This project focuses on identifying **customers most likely to churn** early enough to enable targeted, cost-effective retention strategies.

### Business Context
- Observed churn rate: **26.5%**
- Existing retention efforts are **untargeted and inefficient**
- Missing a churner is **more costly** than contacting a non-churner

### Objective
Build a **high-recall churn prediction model** that:
- Flags at-risk customers before churn occurs
- Prioritizes business impact over raw accuracy
- Produces interpretable insights to guide retention decisions

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
| Data challenges | Class imbalance, mixed data types |

### Key Observations
- `TotalCharges` stored as object → converted to numeric
- Moderate class imbalance required metric-aware evaluation
- Dataset size supports both interpretable and ensemble models

---

## 3. Methodology

A structured, production-style workflow was followed:

1. Data validation and preprocessing  
2. Exploratory Data Analysis (EDA)  
3. Feature engineering  
4. Baseline modeling  
5. Hyperparameter tuning  
6. Model benchmarking  
7. Business-driven model selection  

**Evaluation focus:** Recall, precision, and F1-score (not accuracy alone)

---

## Data Preparation & Feature Engineering

### Preprocessing
- Converted `TotalCharges` to numeric with missing-value handling
- Removed non-informative `customerID`
- Encoded categorical variables:
  - Binary features → 0/1
  - Multi-class features → One-Hot Encoding
- Train-test split: **80% / 20%**

### Feature Engineering
- Constructed full dummy-variable matrix
- Checked for outliers and multicollinearity
- Retained features capturing **contractual, behavioral, and service usage patterns**

---

## Exploratory Data Analysis (EDA)

EDA revealed **clear, actionable churn drivers**:

- Strong churn concentration among **month-to-month contracts**
- Short-tenure customers exhibit significantly higher churn
- Fiber optic users churn more when **support services are absent**
- Churners have **higher MonthlyCharges on average**
- Demographics alone are weak churn predictors

**Insight:**  
Churn is primarily driven by **service experience and contract structure**, not demographics.

---

## 4. Modeling Strategy

Models were trained and compared using a **consistent evaluation framework**.

Models were also evaluated using a fixed test set to ensure fair, apples-to-apples comparison.

### Models Evaluated
- Logistic Regression (baseline & tuned)
- Decision Tree (baseline & tuned)
- Random Forest (baseline & tuned)
- XGBoost

Hyperparameter tuning was performed using cross-validation where applicable.

---

## 5. Model Performance & Results

### Benchmark Comparison

| Metric | LR | Tuned LR | DT | Tuned DT | RF | Tuned RF | XGBoost |
|------|----|----------|----|----------|----|----------|---------|
| Accuracy | 0.80 | 0.79 | 0.72 | 0.78 | 0.78 | 0.79 | 0.74 |
| Precision (Churn) | 0.64 | 0.64 | 0.48 | **0.66** | 0.62 | 0.65 | 0.51 |
| Recall (Churn) | 0.54 | 0.51 | 0.49 | 0.40 | 0.49 | 0.50 | **0.69** |
| F1-score (Churn) | 0.58 | 0.57 | 0.48 | 0.50 | 0.55 | 0.56 | **0.59** |

---

## Final Model Selection

### Selected Model: **XGBoost**

**Rationale**
- Highest recall (**69%**) → minimizes missed churners
- Best overall F1-score
- Accepts lower precision to reduce costly false negatives
- Feature importance aligns with domain understanding

### Confusion Matrix (XGBoost)

| Actual \ Predicted | No Churn | Churn |
|------------------|----------|-------|
| No Churn         | 787      | 246   |
| Churn            | 116      | 258   |

---

## 6. Business Impact & Recommendations

### Key Drivers of Churn
1. Contract type (Month-to-month)
2. Tenure
3. MonthlyCharges
4. Fiber optic Internet service
5. TechSupport
6. OnlineSecurity

### Recommended Actions
- Target high-risk customers flagged by the model
- Incentivize contract upgrades for month-to-month users
- Bundle support services for fiber customers
- Monitor recall-precision trade-offs against retention ROI
- Retrain the model periodically with new customer data

---

## Technology Stack

- **Language:** Python 3.9  
- **Libraries:** XGBoost, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn  

---

## Future Work & Enhancements

While the current solution delivers strong business value, several extensions could further improve performance and production readiness:

### Advanced Feature Engineering
- Interaction features (e.g., tenure × contract type)
- Temporal behavior if historical data becomes available

### Model Enhancements
- Bayesian hyperparameter optimization
- Probability calibration
- Explainability using SHAP for stakeholder insights

### Production & Monitoring
- Package the pipeline into a deployable service
- Monitor data drift and performance decay
- Automate periodic retraining

### Business Integration
- A/B test retention strategies driven by predictions
- Measure uplift and campaign effectiveness
- Integrate with CRM and marketing automation tools

---

## Conclusion

This project demonstrates a **full, business-aligned churn prediction pipeline**, combining:
- Explanatory data analysis
- Feature engineering
- Model benchmarking
- Metric-driven decision-making

**Final Recommendation:**  
Deploy **XGBoost** to maximize churn detection and support proactive, cost-effective retention strategies.

---

## Code

[![View Code](https://img.shields.io/badge/View%20Code-6F42C1?style=for-the-badge&logo=github&logoColor=white)](./Telco_Customer_Churn_Prediction.ipynb)

---

## Contact

[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:mithileshgungah@gmail.com) &nbsp;&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mithilesh-gungah-331133215/)
