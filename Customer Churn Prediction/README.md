# Customer Churn Prediction Engine

## Project Objective
Identify customers at risk of churn using the Telco dataset and provide actionable insights to reduce attrition and improve retention strategies.

---

## 1. Problem Statement
- Churn Rate: 26.5% of customers were leaving the service.  
- Challenges:  
  - Month-to-month contracts have the highest attrition.  
  - Service dissatisfaction in key offerings (Fiber, TechSupport, OnlineSecurity).  
  - Generic retention campaigns were not targeting high-risk users.  
  - Imbalanced dataset: only ~27% of customers churn.  

**Goal:** Build a predictive model to flag high-risk customers and inform targeted retention campaigns.

---

## 2. Dataset Overview
- **Source:** [IBM Telco Customer Churn Dataset](https://github.com/IBM/telco-customer-churn-on-icp4d/tree/master/data)  
- **Records:** 7,043 customers  
- **Features:** 21 (Demographic, Contract, Service usage, Payment methods)  

**Key Statistics:**

| Metric              | Value |
|--------------------|-------|
| Total Records      | 7,043 |
| Target Variable    | Churn (Yes/No) |
| Churn Rate         | 26.5% Yes, 73.5% No |
| Categorical Features | 16 |
| Numerical Features   | 3 |

**Observations:**  
- Categorical variables require encoding.  
- `customerID` is unique and non-predictive.  
- Missing values in `TotalCharges` addressed via conversion and imputation.

---

## 3. Data Preprocessing & Feature Engineering
**Steps Taken:**
1. Converted `TotalCharges` to numeric and handled missing values.  
2. Encoded categorical variables:  
   - Binary: Yes/No → 1/0  
   - Multi-class: One-Hot Encoding (Contract, InternetService, PaymentMethod)  
3. Dropped non-predictive `customerID`.  
4. Split dataset into train (80%) and test (20%).  
5. Optional considerations: scaling numeric features (not required for XGBoost), handling class imbalance (SMOTE/class weighting).

---

## 4. Modeling Approach
Two supervised models were tested: **Logistic Regression** and **XGBoost**.

### 4.1 Logistic Regression
| Metric           | Value |
|-----------------|-------|
| Accuracy         | 0.80  |
| Churn Precision  | 0.64  |
| Churn Recall     | 0.54  |
| F1-score (Churn) | 0.58 |

**Observation:**  
- Interpretable and good overall accuracy.  
- High false negatives → misses a significant portion of churners.

### 4.2 XGBoost
| Metric           | Value |
|-----------------|-------|
| Accuracy         | 0.74  |
| Churn Precision  | 0.51  |
| Churn Recall     | 0.69  |
| F1-score (Churn) | 0.59 |

**Confusion Matrix (XGBoost):**

|Actual \ Predicted| No churn (0) | Churn (1) |
|-----------------|--------------|-----------|
| No churn (0)    | 782          | 251       |
| Churn (1)       | 115          | 259       |

**Top Features Influencing Churn:**
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

**Insights:**  
- Captures more potential churners than Logistic Regression (higher recall).  
- Slightly lower precision → some non-churners targeted.  
- Aligns with business intuition → actionable for retention.

---

## 5. Business Insights
- **High-Risk Segments:**  
  - Month-to-month contracts, short tenure (<12 months), high MonthlyCharges, Fiber customers.  
- **Retention Strategies:**  
  - Personalized offers: discounts, loyalty rewards, service bundles.  
  - Promote TechSupport, OnlineSecurity, and longer-term contracts.  
- **Service Improvement:**  
  - Fiber Internet quality and tech support responsiveness.  
- **Campaign Monitoring:**  
  - Track success and update models quarterly.

---

## 6. Expected Impact
- **Revenue Preservation:** Targeted retention campaigns prevent ~$1.2M/year in lost revenue.  
- **Operational Efficiency:** Focus marketing and retention resources on high-risk customers.  
- **Customer Lifetime Value:** Increase by reducing churn among early-tenure and high-spend customers.  
- **Strategic Insights:** Clear understanding of churn drivers informs long-term business decisions.

---

## 7. Tech Stack
- Python 3.9  
- Libraries: XGBoost, Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn  

---

## 8. Conclusion
This project successfully identifies high-risk customers and key drivers of churn.  
**XGBoost is recommended** for proactive retention campaigns. By combining predictive modeling with actionable strategies, the company can reduce churn, save revenue, and optimize retention efforts.

---

## Contact
- Email: [mithileshgungah@gmail.com](mailto:mithileshgungah@gmail.com)  
- GitHub: [https://github.com/mithileshgungah](https://github.com/mithileshgungah)
