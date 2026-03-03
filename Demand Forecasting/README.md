# Short-Term Sales Forecasting Under Volatile Demand

## Overview

This project builds a production-aware short-term sales forecasting framework for a highly volatile daily retail demand series. Using approximately four years of historical transaction data aggregated into a continuous daily time series, multiple statistical, machine learning, and deep learning models were benchmarked under strict rolling-origin backtesting with a fixed 7-day forecast horizon.

The objective was not to maximise complexity, but to identify a model that delivers stable, operationally reliable forecasts under spike-driven demand conditions.

---

## Key Result

**XGBoost delivered the strongest overall performance**, achieving approximately **25 to 31 percent reduction in RMSE relative to naive baselines**.

This improvement directly enhances short-term planning reliability in volatile demand environments where large forecast misses drive disproportionate operational cost.

---

## Why This Matters

Daily retail demand in this dataset exhibits:

- Strong monthly and weekly seasonality  
- Heavy-tailed, spike-driven fluctuations  
- Nonlinear demand dynamics  
- Irregular high-impact transactions  

In such settings, forecast robustness and sensitivity to extreme deviations matter more than purely average error reduction.

---

## Methodology Highlights

- Continuous daily time series construction with strict temporal integrity  
- Leakage-free feature engineering using lagged and rolling statistics  
- Rolling-origin cross-validation with fixed 7-day recursive forecasting  
- Unified evaluation across all models  
- Metrics aligned with operational risk: MAE, RMSE, and WMAPE  
- Explicit trade-off analysis between interpretability and predictive performance  

---

## Models Benchmarked

- Naive and seasonal naive baselines  
- ARIMA and SARIMA  
- Prophet  
- Random Forest  
- XGBoost  
- LSTM  

Classical seasonal models performed strongly but were less adaptive to irregular spikes. Deep sequence modelling did not outperform tree-based boosting under recursive multi-step evaluation and moderate data volume.

---

## Interpretability and Governance

To ensure transparent model selection:

- SHAP was applied to the final XGBoost model  
- Month-level seasonality and weekly lag effects emerged as dominant drivers  
- Rolling demand statistics stabilised predictions under volatility  

This confirms that predictive strength was driven by meaningful temporal structure rather than noise.

---

## Business Impact

A 25 to 31 percent reduction in RMSE translates into:

- Lower stockout risk during demand surges  
- Reduced overstock exposure during pullbacks  
- Improved short-term inventory alignment  
- Greater operational stability under volatility  

Forecast improvements are most valuable during high-variance periods where large misses are costly.

---

## Core Takeaways

- Model effectiveness depends on alignment with demand structure, not complexity alone  
- Boosted tree ensembles can outperform deep sequence models in moderate-sized retail datasets  
- Rolling-origin validation is essential for realistic deployment simulation  
- Interpretability tools such as SHAP enable high-capacity models to meet governance standards  

---

## Technology Stack
- **Language:** Python 3.12  
- **Libraries:** Pandas, NumPy, Scikit-learn, Statsmodels, Prophet, XGBoost, TensorFlow, SHAP, Matplotlib, Seaborn

---

## Code

[![View Notebook](https://img.shields.io/badge/View%20Notebook-6F42C1?style=for-the-badge&logo=github&logoColor=white)](./Telco_Customer_Churn_Prediction.ipynb)

---

## Contact

[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:mithileshgungah@gmail.com) &nbsp;&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mithilesh-gungah-331133215/)
