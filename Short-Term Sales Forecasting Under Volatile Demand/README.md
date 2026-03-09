# Short-Term Sales Forecasting Under Volatile Demand

<p align="center">
  <img src="demand_forecasting.png" alt="Short-Term Sales Forecasting Under Volatile Demand" width="500">
</p>

## Overview

This project develops a **production-oriented short-term sales forecasting framework** for a highly volatile daily retail demand series.

Approximately **four years of historical transaction data** were aggregated into a continuous daily time series and used to benchmark **eight forecasting models** spanning classical statistics, lagged-feature-based machine learning models, and deep learning approaches:

- Naive baseline  
- Seasonal Naive  
- ARIMA  
- SARIMA  
- Prophet  
- Random Forest  
- XGBoost  
- LSTM  

All models were evaluated using **strict rolling-origin backtesting with a fixed 7-day forecast horizon**, replicating how forecasts would perform in real operational deployment.

The **7-day forecasting window** aligns with weekly retail planning cycles, including **inventory replenishment, staffing allocation, and promotional planning**, while still providing sufficient forward visibility under volatile demand conditions.

Rather than maximising model complexity, the objective was to identify a forecasting approach capable of delivering **stable, operationally reliable predictions under spike-driven demand dynamics**.

---

## Key Results

**XGBoost delivered the strongest overall performance under rolling-origin evaluation**, outperforming both classical statistical models and deep learning approaches.

Relative to baseline methods, the final model achieved:

- **24.9% reduction in RMSE vs Naive baseline**
- **30.9% reduction in RMSE vs Seasonal Naive**
- **46.5% reduction in systematic under-forecast bias**

These improvements indicate that the model not only reduced average forecast error but also **significantly improved demand calibration during volatile demand spikes**, where large forecast misses can drive disproportionate operational costs.

---

## Seasonal Demand Signal

Exploratory analysis revealed **strong recurring monthly demand patterns**, with repeated peaks during specific months and a clear surge toward year-end.

<p align="center">
  <img src="seasonality_pattern.png" width="1000">
</p>

These seasonal patterns informed the feature engineering strategy. Calendar-based variables such as **month** and **day-of-week**, along with lagged demand and rolling demand statistics, were incorporated into the modelling pipeline.

Model explainability using **SHAP** confirmed that **month was the most influential feature in the final XGBoost model**, demonstrating that the model successfully captured the seasonal demand structure observed during exploratory analysis.

---

## Why This Matters

Daily retail demand in this dataset exhibits several characteristics that make forecasting challenging:

- Strong **weekly and monthly seasonality**
- **Heavy-tailed demand spikes**
- **Nonlinear demand dynamics**
- Irregular **high-impact transactions**

In such environments, forecasting models must be able to **adapt to nonlinear patterns and extreme deviations**, rather than simply minimising average error.

Improving forecast calibration during volatile demand periods is often more operationally valuable than small gains in average accuracy.

---

## Methodology Highlights

To ensure realistic evaluation and production relevance, the modelling framework included:

- Construction of a **continuous daily time series with strict temporal integrity**
- **Leakage-free feature engineering** using lagged demand and rolling statistics
- **Rolling-origin cross-validation** with recursive 7-day forecasting
- Unified evaluation across all candidate models
- Metrics aligned with operational risk: **MAE, RMSE, and WMAPE**
- Explicit comparison of **interpretability vs predictive performance**

This setup closely simulates how forecasting models behave when deployed in real-world retail planning environments.

---

## Models Benchmarked

Eight forecasting models were evaluated to compare different modelling paradigms.

| Model Type | Model | Key Strength |
|------|------|------|
| Baseline | Naive | Simple persistence benchmark |
| Baseline | Seasonal Naive | Captures weekly seasonality |
| Statistical | ARIMA | Classical autoregressive modelling |
| Statistical | SARIMA | Seasonal time-series modelling |
| Hybrid | Prophet | Additive trend + seasonality modelling |
| Machine Learning | Random Forest | Nonlinear feature interactions |
| Machine Learning | **XGBoost** | Boosted tree ensembles |
| Deep Learning | LSTM | Sequential neural modelling |

Classical seasonal models performed strongly but were less adaptive to irregular spikes, while deep sequence modelling did not outperform tree-based boosting under recursive multi-step forecasting and moderate data volume.

---

## Interpretability and Governance

To ensure transparency in model selection and feature influence:

- **SHAP** was applied to the final XGBoost model
- **Month-level seasonality** and **weekly lag features** emerged as dominant drivers
- Rolling demand statistics improved stability during volatile demand periods

This confirms that predictive improvements were driven by **meaningful temporal structure rather than noise or overfitting**.

---

## Business Impact

A **24–31% reduction in RMSE** combined with a **46% reduction in systematic under-forecast bias** translates into tangible operational improvements in retail demand planning.

Potential benefits include:

- Reduced **stockout risk during demand surges**
- Lower **overstock exposure during demand slowdowns**
- Improved **short-term inventory alignment**
- More reliable **weekly replenishment and staffing decisions**

Forecast accuracy improvements are particularly valuable during **high-volatility periods**, where large forecast misses can create disproportionate operational costs.

---

## Core Takeaways

- Forecasting performance depends on **alignment with demand structure**, not model complexity alone  
- **Boosted tree ensembles can outperform deep learning** in moderate-sized retail time-series datasets  
- **Rolling-origin validation is essential** for realistic deployment simulation  
- Interpretability tools such as **SHAP enable high-capacity models to remain transparent and auditable**

---

## Technology Stack

**Language**

- Python 3.12

**Libraries**

- Pandas  
- NumPy  
- Scikit-learn  
- Statsmodels  
- Prophet  
- XGBoost  
- TensorFlow  
- SHAP  
- Matplotlib  
- Seaborn  

---

## Code

[![View Notebook](https://img.shields.io/badge/View%20Notebook-6F42C1?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MithileshGungah/Data-Science-Portfolio/blob/948dcb489612b0cd27feffb8f150d81daf39960e/Short-Term%20Sales%20Forecasting%20Under%20Volatile%20Demand/Short_Term_Sales_Forecasting.ipynb)

---

## Contact

[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:mithileshgungah@gmail.com) &nbsp;&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mithilesh-gungah-331133215/)
