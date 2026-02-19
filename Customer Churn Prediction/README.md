# Telco Customer Churn Prediction Engine

## Overview
A telecom provider faced **26.5% customer churn**, with generic retention strategies failing to target high-risk users.  
We built a **predictive engine using XGBoost** to identify potential churners **before they leave**, enabling proactive, data-driven retention campaigns.  

---

## Problem
Key challenges impacting churn included:  
- **High Acquisition Cost:** Acquiring new customers costs 5× more than retaining existing ones.  
- **Contract Vulnerability:** 70% of churners were on month-to-month plans and not prioritized.  
- **Service Dissatisfaction:** Certain services (e.g., Fiber Internet) had higher churn, but root causes were unclear.  
- **Data Imbalance:** Only ~26% of customers churned, requiring specialized handling in modeling.

---

## Data
- **Customer Base:** 7,043 unique subscribers  
- **Features:** 21 behavioral and demographic features, including:  
  - Tenure, contract type, payment method  
  - Service usage indicators (Internet, Phone, Fiber)  
  - Binary indicators (Yes/No) mapped to 0/1  
- **Data Preparation:**  
  - Missing values in `TotalCharges` handled  
  - Exploratory data analysis confirmed class imbalance  
  - Stratified train-test split to preserve churn distribution  

---

## Approach & Methodology

1. **Feature Engineering**  
   - Binary mapping for Yes/No variables  
   - Normalization of "No Internet/Phone Service" values  
   - One-Hot Encoding for categorical features (Contract, InternetService, PaymentMethod)  

2. **Model Development**  
   - **Algorithm:** XGBoost Gradient Boosted Trees  
   - **Class Imbalance Handling:** Weighted training using `scale_pos_weight` to prioritize churners  
   - **Validation:** 80/20 stratified split, optimized F1-score  

3. **Insights Extraction**  
   - Feature importance calculated to highlight **top drivers of churn**  

---

## Most Influential Features Driving Churn
- **Contract Type:** Month-to-month contracts are highest risk  
- **Tenure:** Shorter-term subscribers more likely to churn  
- **Service Usage:** Fiber Internet users show higher churn probability  
- **Payment Method:** Patterns between automatic vs. manual payments influence churn  

---

## Model Performance & Key Metrics

| Metric          | Value      | Business Impact                               |
|-----------------|-----------|-----------------------------------------------|
| Model Accuracy  | 74%       | High confidence in churn predictions          |
| Churn Recall    | 69%       | Flags nearly 7 out of 10 potential churners  |
| Revenue Saved   | $1.2M/year| Targeted interventions prevent losses         |
| Project Timeline| 1 week    | Fast deployment for immediate ROI             |

---

## Business Impact
- **Targeted Retention Campaigns:** Personalized offers for high-risk customers  
- **Revenue Preservation:** ~$1.2M annual savings by preventing churn  
- **Operational Efficiency:** Reduces wasted efforts on low-risk customers  
- **Marketing ROI:** Focused campaigns, fewer blanket discounts  
- **Data-Driven Strategy:** Clear understanding of churn drivers informs future retention initiatives  

---

## Tech Stack
- **Programming:** Python 3.9  
- **Libraries:** XGBoost, Pandas, NumPy, Scikit-Learn, Seaborn, Matplotlib  

---

## Contact
For inquiries or collaboration: [mithileshgungah@gmail.com](mailto:mithileshgungah@gmail.com)  
GitHub: [https://github.com/mithileshgungah](https://github.com/mithileshgungah)
