# Telco Customer Churn Prediction Engine

## Overview
A telecom provider faced **26.5% customer churn**, with generic retention strategies failing to target high-risk users.  
Using **XGBoost**, a predictive model was built to identify churners **before they leave**, enabling proactive, data-driven retention campaigns.

---

## Key Metrics

| Metric          | Value      | Impact                                        |
|-----------------|-----------|-----------------------------------------------|
| Model Accuracy  | 74%       | High confidence in predictions               |
| Churn Recall    | 69%       | Nearly 70% of potential churners flagged    |
| Revenue Saved   | $1.2M/year| Targeted interventions reduce losses        |
| Project Timeline| 1 week    | Fast deployment for immediate ROI           |

---

## Core Challenges
- **High Acquisition Cost:** Retaining existing customers is 5x cheaper than acquiring new ones.  
- **Contract Vulnerability:** Month-to-month customers (70% of churners) were not prioritized.  
- **Service Dissatisfaction:** Key services had high churn, but underlying issues were unquantified.  
- **Data Imbalance:** Only ~26% of customers churn, requiring specialized modeling.

---

## Approach & Solution

1. **Data Preparation**  
   Aggregated 7,043 customer records, handled missing values, and performed exploratory analysis.

2. **Feature Engineering**  
   Engineered 21 behavioral & demographic features:  
   - Binary mapping for Yes/No variables  
   - Normalization of "No Service" features  
   - One-Hot Encoding for categorical fields (Contract, InternetService, PaymentMethod)

3. **Model Development**  
   XGBoost trained with class-weight balancing to prioritize detection of high-risk churners.

4. **Validation & Insights**  
   80/20 stratified split, optimized F1-score, and extracted **feature importance** for actionable retention strategies.

---

## Most Influential Features Driving Churn
- **Contract Type:** Month-to-month contracts are high risk  
- **Tenure:** Short-term subscribers more likely to churn  
- **Service Usage:** Fiber customers showed higher churn rates  
- **Payment Method:** Automatic vs. manual payment patterns  

---

## Business Impact
- **Targeted Retention Campaigns:** Personalized offers to high-risk users  
- **Revenue Preservation:** ~$1.2M annual savings  
- **Operational Efficiency:** Reduced waste on low-risk customers  
- **Marketing ROI:** Better focus, fewer blanket discounts  

---

## Tech Stack
- Python 3.9  
- XGBoost  
- Pandas / NumPy  
- Scikit-Learn  
- Seaborn / Matplotlib  

---

## Contact
For inquiries or collaboration: [mithileshgungah@gmail.com](mailto:mithileshgungah@gmail.com)  
GitHub: [https://github.com/mithileshgungah](https://github.com/mithileshgungah)
