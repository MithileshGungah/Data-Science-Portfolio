# Customer Churn Prediction Engine
### A business-aligned machine learning system for proactive customer retention

<p align="center">
  <img src="churn_rate.png" alt="Customer Churn Rate" width="500">
</p>

---

## Executive Summary (For Recruiters & Hiring Managers)

This project builds a cost-sensitive customer churn prediction engine designed to support proactive, revenue-preserving retention strategies in subscription-based businesses.

Using a telecom dataset of 7,043 customers with a 26.5% churn rate, the system reframes churn prediction as a business optimisation problem, where the cost of missing a churner (false negative) far outweighs the cost of contacting a loyal customer. Model evaluation and selection are therefore driven by recall, not raw accuracy.

A structured, production-style machine learning workflow was implemented, benchmarking four model families (Logistic Regression, Decision Tree, Random Forest, XGBoost) under consistent cross-validated evaluation. Through recall-focused hyperparameter tuning, a Tuned XGBoost model was selected as the final solution.

### Key outcomes
- Churn recall improved from 69% to 82 percent
- False negatives reduced by approximately 42 percent
- Precision was deliberately traded for recall to align predictions with real business costs
- Model outputs translate directly into actionable retention strategies
- Equivalent to ~£150k in recoverable lifetime value per 10,000 customers under conservative retention assumptions

### Business value
The system enables a shift from reactive churn response to targeted, data-driven retention, allowing organisations to:
- intervene earlier in the customer lifecycle
- allocate retention spend more efficiently
- reduce recurring revenue leakage at scale

This project demonstrates how metric choice, model selection, and evaluation design can materially affect business outcomes, and why churn prediction must be treated as a cost-sensitive decision system rather than a leaderboard optimisation task.

---

## 1. Problem Statement

Customer churn represents a **direct and recurring revenue risk** for subscription-based businesses. Retaining an existing customer is typically far less costly than acquiring a new one, making early churn detection a critical business capability.

This project focuses on identifying **customers most likely to churn early enough** to enable **targeted, cost-effective retention strategies**, rather than relying on reactive or untargeted outreach.

### Business Context
- Observed churn rate: **26.5%**, indicating substantial revenue leakage  
- Existing retention efforts are **broad and inefficient**  
- Missing a churner (**false negative**) leads to irreversible revenue loss, while contacting a non-churner incurs relatively low cost  

### Objective

Because the cost of missing a churner is significantly higher than the cost of contacting a non-churner, this is an inherently **cost-sensitive classification problem**.

The primary objective is therefore to build a **high-recall churn prediction model** that:
- Proactively flags at-risk customers before churn occurs  
- **Minimises false negatives**, which represent irreversible revenue loss  
- Accepts a controlled increase in false positives as a deliberate and cost-effective trade-off 
- Aligns evaluation metrics with real business costs rather than raw accuracy  
- Produces insights actionable by retention and marketing teams

---

## 2. Data Overview

### Dataset
- **Source:** IBM Telco Customer Churn Dataset  
- **Records:** 7,043 customers  
- **Features:** 21 variables spanning demographics, services, contracts, and billing  

| Aspect | Details |
|------|--------|
| Target variable | `Churn` (Yes / No) |
| Churn rate | 26.5% |
| Feature types | Categorical + numerical |
| Primary challenge | Class imbalance |

### Key Observations
- `TotalCharges` required numeric conversion and missing-value handling  
- Moderate class imbalance required metric-aware evaluation  
- Dataset scale supports both interpretable linear models and ensemble methods  

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

Because churn prevention carries **asymmetric business costs**, model evaluation focused on **recall, precision, and F1-score**, rather than accuracy alone. Recall was prioritised to minimise false negatives, ensuring that the majority of at-risk customers were identified for potential retention intervention.

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

**Primary metric:** Recall (Churn), reflecting the higher cost of false negatives in churn prevention.

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

| Actual \\ Predicted | No Churn | Churn |
|------------------|----------|-------|
| No Churn         | 787      | 246   |
| Churn            | 116      | 258   |

#### Tuned XGBoost (Recall-Focused)

| Actual \\ Predicted | No Churn | Churn |
|------------------|----------|-------|
| No Churn         | 720      | 313   |
| Churn            | 68       | 306   |

**Key Difference:**  
Hyperparameter tuning reduces **false negatives from 116 to 68 (~42%)**, at the cost of increased false positives - an appropriate trade-off for churn prevention.

---

## 6. Business Impact

### Quantified Financial Impact (Scaled Projection)

To translate recall uplift into projected financial exposure, results were scaled to a cohort of 10,000 customers:

- 10,000 × 26.6% churn × 12.8pp recall improvement ≈ **341 additional churners identified**
- Estimated forward-looking revenue per churner ≈ **£1,464** (derived from tenure differential × average monthly revenue)
- Total revenue exposure identified ≈ **£500k per 10,000 customers**
- Assuming 30% retention effectiveness → **~£150k realistically recoverable revenue**

These projections are based on transparent and conservative assumptions and represent scalable financial exposure rather than guaranteed realised revenue.

---

The churn prediction model enables a shift from **reactive churn response** to **proactive, data-driven retention**, allowing the business to intervene **before revenue is lost**.

By prioritising recall, the model ensures that the majority of at-risk customers are identified, even if this requires additional outreach.

---

### Key Drivers of Churn

Model interpretation shows churn is primarily driven by **contract structure, service experience, and early customer lifecycle factors**, rather than demographics:

1. **Contract Type (Month-to-Month)**  
   High churn due to low switching barriers and weak long-term commitment  

2. **Customer Tenure**  
   Elevated churn among new and short-tenure customers  

3. **Monthly Charges**  
   Higher charges increase churn when perceived value is low  

4. **Fiber Optic Internet Service**  
   Higher churn, especially when support services are absent  

5. **Technical Support & Online Security**  
   Lack of post-sale support strongly correlates with churn  

---

### Recommended Business Actions

Actions are grouped by **business lever** to support ownership and execution:

#### Contract & Pricing Strategy
- Incentivise contract upgrades for month-to-month customers  
- Offer targeted discounts to high-risk, high-value customers  

#### Customer Onboarding & Early Engagement
- Prioritise outreach for low-tenure customers  
- Strengthen onboarding to reduce early dissatisfaction  

#### Service & Support Optimisation
- Bundle TechSupport and OnlineSecurity with fiber plans  
- Proactively engage fiber customers lacking support services  

#### Retention Campaign Execution
- Allocate retention spend based on predicted churn risk  
- Monitor recall-precision trade-offs against campaign ROI  

#### Model Operations
- Retrain the model periodically with updated customer data  
- Track performance to ensure sustained business impact  

---

### Business Value Delivered

By aligning model optimisation with real business costs, the solution:
- Reduces missed churners and associated revenue leakage  
- Enables more efficient retention spend  
- Supports data-driven decisions across marketing and customer success  
- Provides a scalable framework for ongoing churn management  

---

## 7. Future Enhancements

- Explore advanced techniques (e.g., SMOTE) to further address class imbalance and improve churn detection 
- Enhance feature engineering to capture complex customer behavior  
- Improve explainability using SHAP or LIME  
- Calibrate probabilities for cost-based decision thresholds  
- Evaluate retention strategies via A/B testing and uplift measurement  

---

## Conclusion

This project demonstrates a **business-aligned churn prediction system** combining:
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

[![View Notebook](https://img.shields.io/badge/View%20Notebook-6F42C1?style=for-the-badge&logo=github&logoColor=white)](./Telco_Customer_Churn_Prediction.ipynb)

---

## Contact

[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:mithileshgungah@gmail.com) &nbsp;&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mithilesh-gungah-331133215/)
