# Customer Churn Prediction Engine  
### A Business-Aligned Machine Learning System for Proactive Customer Retention

<p align="center">
  <img src="churn_rate.png" alt="Customer Churn Rate" width="500">
</p>

---

# Executive Summary

This project develops a **customer churn prediction system** designed to support proactive retention strategies in subscription-based businesses.

Using the **IBM Telco Customer Churn dataset (7,032 customers after cleaning; 26.6% churn rate)**, churn prediction is reframed as a **business optimisation problem**, where the cost of missing a churner (false negative) is significantly higher than contacting a customer who would not churn.

For this reason, model evaluation prioritises **recall**, rather than overall accuracy.

Multiple machine learning models were benchmarked under a consistent evaluation framework. After recall-focused hyperparameter tuning, **Tuned XGBoost** was selected as the final model.

---

### Model Deployment

The final Tuned XGBoost model was deployed as an interactive Streamlit web application that enables on-demand and batch churn predictions, along with an estimated revenue impact for retention decisions.

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live%20Application-ff4b4b)](https://mg-churn.streamlit.app)

---

## Key Outcomes

- **Recall improved from 0.54 → 0.87**
- **False negatives reduced from 171 → 49**
- High recall achieved while maintaining competitive overall model performance
- Financial projection estimates **~£381k recoverable revenue per 10,000 customers**

---

## Business Value

The system enables organisations to shift from **reactive churn management** to **proactive customer retention**, allowing them to:

- Detect churn risk earlier
- Intervene before revenue is lost
- Target retention campaigns more efficiently
- Reduce recurring revenue leakage

The project demonstrates how **metric selection, model tuning, and evaluation design directly influence financial outcomes**.

---

# 1. Problem Statement

Customer churn represents a major revenue risk in subscription-based businesses. Retaining existing customers is typically more cost-effective than acquiring new ones, making early churn detection strategically critical.

This project frames churn prediction as a **cost-sensitive decision problem**, where:

- Missing a churner leads to revenue loss
- Contacting a non-churner incurs relatively low cost

### Objective

Develop a machine learning model that:

- **Maximises recall** to detect as many churners as possible
- Minimises **false negatives** (missed churners)
- Accepts controlled increases in false positives
- Produces insights actionable for retention strategies

---

# 2. Data Overview

### Dataset

- **Source:** IBM Telco Customer Churn Dataset  
- **Records:** 7,043 customers (7,032 after cleaning)  
- **Features:** 21 demographic, contract, service, and billing attributes  

| Aspect | Details |
|------|------|
| Target Variable | `Churn` |
| Churn Rate | 26.6% |
| Feature Types | Numerical + Categorical |
| Key Challenge | Class imbalance |

### Data Preparation

Key preprocessing steps included:

- Converting **TotalCharges** to numeric format
- Handling missing values
- Feature engineering (e.g., `AvgMonthlySpend`, tenure indicators)
- Encoding categorical variables
- Train/test split with **stratified sampling**

---

# 3. Methodology

The project follows a structured machine learning workflow:

1. Data validation and preprocessing  
2. Exploratory data analysis  
3. Feature engineering  
4. Baseline model training  
5. Hyperparameter tuning  
6. Model benchmarking  
7. Business-driven model selection  

Because churn prevention involves **asymmetric cost risk**, model evaluation prioritised:

- **Recall**
- Precision
- F1-score

rather than raw accuracy.

---

# 4. Modeling Strategy

Models were evaluated using a **20% hold-out test set**.

### Models Evaluated

- Logistic Regression (baseline & tuned)
- Decision Tree (baseline & tuned)
- Random Forest (baseline & tuned)
- XGBoost (baseline & tuned)

### Hyperparameter Tuning

Models were tuned using **cross-validation**, with adjustments to:

- model complexity
- learning rates
- sampling parameters
- class imbalance handling

---

# 5. Model Performance

## Benchmark Comparison

| Model | Accuracy | Precision | Recall | F1 |
|------|------|------|------|------|
| LR Baseline | 0.77 | 0.54 | 0.82 | 0.65 |
| LR Tuned | 0.77 | 0.55 | 0.82 | 0.66 |
| DT Baseline | 0.73 | 0.50 | 0.49 | 0.50 |
| DT Tuned | 0.75 | 0.52 | 0.80 | 0.63 |
| RF Baseline | 0.80 | 0.66 | 0.52 | 0.58 |
| RF Tuned | 0.78 | 0.57 | 0.78 | 0.66 |
| XGB Baseline | 0.81 | 0.68 | 0.54 | 0.60 |
| **XGB Tuned** | **0.73** | **0.49** | **0.87** | **0.63** |

**Primary evaluation metric:** Recall

---

# 6. Final Model Selection

### Selected Model: Tuned XGBoost

Although **Logistic Regression** achieved a slightly higher Average Precision (**0.68**) in the Precision-Recall analysis, the **tuned XGBoost model** was selected because the primary objective of this project is to **maximise recall** and identify as many churners as possible.

With **recall = 0.87**, the model identifies the largest proportion of customers likely to churn.

---

## Confusion Matrix (Tuned XGBoost)

| Actual \ Predicted | No Churn | Churn |
|-------------------|----------|-------|
| No Churn | 696 | 337 |
| Churn | 49 | 325 |

Key interpretation:

- **325 churners correctly detected**
- Only **49 churners missed**
- Higher false positives accepted to minimise missed churners

In churn prediction, **missing a churner typically carries greater business cost** than contacting a customer who may not churn.

---

# 7. Financial Impact

### Revenue Impact Projection

Scaling model performance to **10,000 customers**:

- Additional churners identified: **~867**
- Estimated future revenue per churner: **~£1,464**
- Revenue exposure identified: **~£1.27M**
- Assuming **30% retention success** → **~£381k recoverable revenue**

These projections use simplified assumptions and represent **potential revenue exposure**, not guaranteed realised revenue.

---

# 8. Key Drivers of Churn

SHAP analysis highlights the main factors influencing churn risk:

- Month-to-month contracts
- Short customer tenure
- Higher monthly charges
- Fiber optic internet plans
- Electronic check payment method
- Lack of add-on services (TechSupport, OnlineSecurity)

These insights support targeted retention strategies.

---

# 9. Limitations

Several limitations should be acknowledged:

- Dataset size is relatively small (~7k customers)
- Behavioural usage data is not included
- Financial projections rely on simplified assumptions
- Default classification threshold (0.5) was used

In practice, organisations would optimise thresholds based on **retention campaign cost and customer lifetime value**.

---

# 10. Future Work

Potential extensions include:

- Threshold optimisation for cost-sensitive deployment
- Advanced imbalance handling (e.g., SMOTE)
- Time-series customer behaviour modelling
- Customer-level explainability with SHAP
- Model deployment with monitoring and retraining pipelines

---

# Conclusion

This project demonstrates how a **business-aligned machine learning workflow** can transform churn prediction into a practical decision-support tool.

By prioritising **recall**, the model identifies significantly more at-risk customers, enabling proactive retention interventions and reducing revenue loss.

The final **Tuned XGBoost model** provides the strongest balance between predictive performance and business impact.

---

# Technology Stack

- Python  
- XGBoost  
- Scikit-learn  
- Pandas / NumPy  
- Matplotlib / Seaborn  

---

# Code

[![View Notebook](https://img.shields.io/badge/View%20Notebook-6F42C1?style=for-the-badge&logo=github&logoColor=white)](./Telco_Customer_Churn_Prediction.ipynb)

---

# Contact

[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:mithileshgungah@gmail.com) &nbsp;&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mithilesh-gungah-331133215/)
