# Telecom Customer Churn Analysis & Prediction

---

## Project Goal

Develop a machine learning system to predict customer churn for a telecom company, uncover the main reasons for attrition, and provide actionable recommendations to retain high-value customers.  

The focus is on generating **business-driven insights** rather than only reporting numbers.

---

## Problem Context

Customer churn is a critical issue in the telecom sector, causing lost revenue and increased acquisition costs.  

This project addresses key questions:

- Which customers are most likely to leave?
- What behaviors or patterns drive churn?
- How can the company proactively retain at-risk customers?

---

## Dataset Overview

- Number of records: 7,043  
- Number of features: 21  
- Target variable: `Churn` (Yes/No)  
- Churn distribution: 26.5% Yes, 73.5% No  

Feature examples:

| Feature Type       | Examples |
|------------------|----------|
| Categorical       | Contract, PaymentMethod, InternetService, TechSupport, StreamingTV |
| Numerical         | Tenure, MonthlyCharges, TotalCharges |

Initial insights:

- Month-to-month contract customers churn more frequently.
- Shorter tenure is correlated with higher churn.
- High monthly charges with limited support increase churn risk.

---

## Data Preparation

Key preprocessing steps:

1. Handle missing values in `TotalCharges` and convert to numeric.  
2. Encode categorical features: binary to 0/1, multi-class with one-hot encoding.  
3. Remove non-predictive features like `customerID`.  
4. Split dataset: 80% train, 20% test.  
5. Address class imbalance with class weighting to improve churn recall.

---

## Modeling Approach

### Logistic Regression

- Pros: Simple and interpretable  
- Cons: Misses many churners (higher false negatives)  

| Metric           | Value |
|-----------------|-------|
| Accuracy         | 0.80  |
| Churn Recall     | 0.54  |

---

### XGBoost (Best Performing)

- Captures non-linear relationships and feature interactions.  
- Optimized for high recall to detect more churners.

| Metric           | Value |
|-----------------|-------|
| Accuracy         | 0.74  |
| Churn Recall     | 0.69  |
| F1-score         | 0.59  |

Top predictive features:

1. Contract type (month-to-month)  
2. Tenure  
3. MonthlyCharges  
4. Fiber optic InternetService  
5. TechSupport availability  

Business implication: Focus retention efforts on customers with **short-tenure, month-to-month contracts, and high monthly charges**.

---

## Business Recommendations

1. **Targeted Retention Campaigns**  
   - Offer personalized incentives to high-risk customers.  
   - Promote services like TechSupport and OnlineSecurity.

2. **Service Quality Improvements**  
   - Ensure fiber optic users receive reliable service.  
   - Provide proactive support for new customers (<12 months tenure).

3. **Contract Strategies**  
   - Encourage longer-term contracts with loyalty benefits.  
   - Offer early retention incentives to at-risk customers.

Expected outcomes:

- Reduced churn through early identification of high-risk customers.  
- Improved ROI on retention campaigns.  
- Increased customer lifetime value.

---

## Tech Stack

- Python (pandas, numpy, scikit-learn)  
- XGBoost  
- Matplotlib & Seaborn for visualizations  
- Jupyter Notebook for experimentation  

---

## Key Takeaways

- Predictive modeling allows the company to act proactively rather than reactively.  
- Contract type, tenure, and service usage are key indicators of churn.  
- XGBoost is effective at identifying at-risk customers with high recall.  
- Regular updates and monitoring keep the model accurate and relevant.

---

## Future Enhancements

- Include customer engagement metrics like support tickets and usage frequency.  
- Develop a real-time churn alert system.  
- Conduct A/B testing to measure the ROI of retention campaigns.
