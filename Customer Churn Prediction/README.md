# Customer Churn Prediction Engine

A business-aligned machine learning system for proactive customer retention

<p align="center">
  <img src="churn_rate.png" alt="Customer Churn Rate" width="500">
</p>

---

## Overview

The goal of this project is to **identify customers at risk of leaving** using the Telco dataset and provide **actionable insights** for retention strategies. By detecting high-risk users, the company can save revenue, optimize marketing spend, and improve customer lifetime value.

---

## Problem Context

- Current churn rate: **26.5%**, indicating significant customer attrition.  
- Key challenges identified:
  - Month-to-month customers are most vulnerable.  
  - Dissatisfaction in Fiber, TechSupport, and OnlineSecurity services.  
  - Generic retention campaigns do not focus on high-risk customers.  
  - Dataset is imbalanced (~27% churners), requiring careful evaluation using precision, recall, and F1-score metrics.  

**Objective:** Build a predictive solution to flag potential churners and support targeted interventions.

---

## Dataset Details

**Source:** [IBM Telco Customer Churn Dataset](https://github.com/IBM/telco-customer-churn-on-icp4d/tree/master/data)  
**Total records:** 7,043 customers  
**Features:** 21 (demographics, contract, service usage, and payment info)  

**Quick Snapshot:**

| Metric               | Value              |
|---------------------|------------------|
| Total customers      | 7,043             |
| Churners             | 26.5%             |
| Non-churners         | 73.5%             |
| Categorical features | 16                |
| Numerical features   | 3                 |
| Missing values       | `TotalCharges` fixed |
| Class Imbalance      | Only ~26.5% churners |

---

## Data Preparation & Feature Engineering

### Preprocessing Highlights

- Converted `TotalCharges` from object → float; handled missing values.  
- Encoded categorical variables:
  - Binary → 0/1 (Yes/No)  
  - Multi-class → One-Hot Encoding (Contract, PaymentMethod, InternetService)  
- Removed non-predictive `customerID`.  
- Split dataset: **80% train / 20% test**.  
- Optional: Scaling numeric features (XGBoost not sensitive), SMOTE/class weighting considered for imbalance.

### Feature Engineering

- Dummy variables created for categorical features.  
- Checked for outliers → none significant.  
- Prepared data for modeling to capture behavioral and demographic patterns.  

---

## Predictive Modeling

Two models were evaluated: **Logistic Regression** and **XGBoost**.

### Logistic Regression

| Metric               | Result |
|---------------------|--------|
| Accuracy             | 0.80   |
| Precision (Churn)    | 0.64   |
| Recall (Churn)       | 0.54   |
| F1-score (Churn)     | 0.58   |

**Observation:**  
- Good overall accuracy and highly interpretable.  
- High false negatives → misses some churners.  

### XGBoost

| Metric               | Result |
|---------------------|--------|
| Accuracy             | 0.74   |
| Precision (Churn)    | 0.51   |
| Recall (Churn)       | 0.69   |
| F1-score (Churn)     | 0.59   |

**Confusion Matrix (XGBoost)**

| Actual \ Predicted | No Churn (0) | Churn (1) |
|------------------|--------------|-----------|
| No Churn (0)     | 782          | 251       |
| Churn (1)        | 115          | 259       |

**Top Drivers of Churn**

1. Contract type (Month-to-month)  
2. Tenure  
3. MonthlyCharges  
4. Fiber optic InternetService  
5. TechSupport  
6. OnlineSecurity  
7. OnlineBackup  
8. StreamingTV  
9. DeviceProtection  
10. PaymentMethod  

**Key Takeaways:**  
- XGBoost identifies more churners (higher recall), ideal for retention campaigns.  
- Slight drop in precision → some non-churners may be targeted.  
- Feature importance aligns with business intuition for actionable strategies.  

---

## Business Strategy Recommendations

1. **Prioritize High-Risk Segments:**  
   - Month-to-month contracts, short tenure (<12 months), high MonthlyCharges, Fiber users.  
2. **Retention Programs:**  
   - Personalized discounts, loyalty rewards, service bundles.  
   - Upsell TechSupport and OnlineSecurity packages.  
3. **Service Enhancement:**  
   - Improve fiber-optic service quality and technical support responsiveness.  
4. **Monitoring & Optimization:**  
   - Track campaign effectiveness; retrain models quarterly with fresh data.  

**Expected Outcomes:**  
- Minimize missed churners → maximize ROI of campaigns.  
- Optimize marketing and operational efficiency.  
- Increase customer lifetime value through targeted interventions.  

---

## Technology Stack

- **Programming Language:** Python 3.9  
- **Libraries:** XGBoost, Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn  

---

## Conclusion

The project successfully flags high-risk customers and uncovers major churn drivers.  
**Recommendation:** Use XGBoost for predictive retention efforts. Combining analytics with actionable business strategies enables the company to reduce churn, save revenue, and focus resources efficiently.

---

## Contact

- Email: [mithileshgungah@gmail.com](mailto:mithileshgungah@gmail.com)  
- GitHub: [https://github.com/mithileshgungah](https://github.com/mithileshgungah)
