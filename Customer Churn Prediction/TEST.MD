# Customer Churn Prediction Engine

<p align="center">
  <img src="churn.jpg" alt="Customer Churn Analysis" width="400">
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

### Quick Snapshot

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
- Considered scaling, SMOTE, and class weighting for imbalance handling.

### Feature Engineering

- Dummy variables created for categorical features.  
- Outlier analysis performed → no significant anomalies detected.  
- Final dataset prepared to capture behavioral and contractual churn patterns.

---

## Exploratory Data Analysis (EDA)

EDA was conducted to understand churn drivers and guide modeling decisions.

**Key insights:**
- Strong churn concentration among **month-to-month contracts**  
- Higher churn for customers with **short tenure**  
- Elevated churn among **fiber optic users**, especially without TechSupport or OnlineSecurity  
- Churners exhibit **higher MonthlyCharges on average**  
- No strong multicollinearity detected  

EDA confirmed churn is primarily driven by **behavioral and service-related factors** rather than demographics alone.

---

## Predictive Modeling

A structured modeling pipeline was followed, progressing from baseline models to tuned models and final benchmarking.  
All models were evaluated on the **same test set** using churn-focused metrics.

### Models Evaluated

- Logistic Regression  
- Tuned Logistic Regression  
- Decision Tree  
- Tuned Decision Tree  
- Random Forest  
- Tuned Random Forest  
- XGBoost  

---

## Model Benchmarking Results

The table below summarizes the **final evaluation metrics** for all baseline and tuned models.

| Metric | Logistic Regression | Tuned LR | Decision Tree | Tuned DT | Random Forest | Tuned RF | XGBoost |
|------|---------------------|----------|---------------|----------|---------------|----------|---------|
| Accuracy | 0.80 | 0.79 | 0.72 | 0.78 | 0.78 | 0.79 | 0.74 |
| Precision (Churn) | 0.64 | 0.64 | 0.48 | **0.66** | 0.62 | 0.65 | 0.51 |
| Recall (Churn) | 0.54 | 0.51 | 0.49 | 0.40 | 0.49 | 0.50 | **0.69** |
| F1-score (Churn) | 0.58 | 0.57 | 0.48 | 0.50 | 0.55 | 0.56 | **0.59** |

---

## Key Benchmarking Insights

- **Logistic Regression**
  - Highest overall accuracy.
  - Highly interpretable.
  - Lower recall → misses many churners.

- **Tuned Logistic Regression**
  - Similar performance to baseline.
  - Regularization did not materially improve churn detection.

- **Decision Tree**
  - Weakest overall performer.
  - Tuning improved precision but reduced recall.
  - High overfitting risk.

- **Random Forest**
  - Robust and balanced.
  - Tuned RF achieved strong precision with moderate recall.
  - Still misses a significant proportion of churners.

- **XGBoost**
  - **Highest recall for churners (0.69)**.
  - Best F1-score among all models.
  - Lower precision accepted to minimize missed churn cases.

---

## Final Model Selection Rationale

XGBoost was selected as the final model because:

- Missed churners are **more costly** than false positives  
- It identifies the **largest proportion of at-risk customers**  
- Recall was prioritized over accuracy due to business impact  
- Feature importance aligns with domain knowledge  

This makes XGBoost the **most business-aligned model**, despite slightly lower precision.

---

## Final Model Evaluation

### Confusion Matrix (XGBoost)

| Actual \ Predicted | No Churn (0) | Churn (1) |
|------------------|--------------|-----------|
| No Churn (0)     | 782          | 251       |
| Churn (1)        | 115          | 259       |

- Successfully identifies **69% of churners**
- Accepts some false positives to maximize churn detection

---

## Top Drivers of Churn

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

---

## Business Strategy Recommendations

1. **Recall-Driven Targeting**
   - Focus on customers flagged as high risk by XGBoost.
2. **High-Risk Segments**
   - Month-to-month contracts  
   - Short tenure customers  
   - High MonthlyCharges  
   - Fiber users without support services  
3. **Retention Actions**
   - Personalized discounts and loyalty rewards  
   - TechSupport and OnlineSecurity bundles  
4. **Monitoring & Optimization**
   - Periodic retraining with new data  
   - Track precision–recall trade-offs against campaign ROI  

---

## Technology Stack

- **Programming Language:** Python 3.9  
- **Libraries:** XGBoost, Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn  

---

## Conclusion

This project demonstrates a **complete, benchmark-driven churn modeling pipeline**, from EDA and feature engineering to tuned model comparison and business-aligned selection.

**Final Recommendation:** Deploy **XGBoost** to maximize churn detection and support targeted, cost-effective retention strategies.

---

## Contact

- Email: [mithileshgungah@gmail.com](mailto:mithileshgungah@gmail.com)  
- GitHub: [https://github.com/mithileshgungah](https://github.com/mithileshgungah)
