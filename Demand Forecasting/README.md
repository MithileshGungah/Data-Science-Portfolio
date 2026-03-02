# Daily Sales Forecasting Under Volatile Demand

## Project Overview
This project evaluates multiple forecasting approaches for daily sales prediction in a highly volatile, spike-driven demand environment. The objective is to identify models that deliver reliable short-term forecasts that materially outperform simple baselines under realistic operational constraints.

The analysis focuses on a **7-day ahead forecasting horizon**, aligning with common planning cycles for inventory management, staffing, and short-term operational decision making.

---

## Business Context
Daily sales forecasting is inherently challenging due to irregular demand spikes, strong calendar effects, and short-term volatility. Large forecast errors during these periods can lead to overstocking, stockouts, or inefficient resource allocation.

Rather than optimizing for perfect accuracy, this project emphasizes:
- Robustness to large deviations  
- Relative improvement over naive benchmarks  
- Forecast stability and interpretability  

These priorities reflect how forecasting models are evaluated and deployed in real business environments.

---

## Data and Key Characteristics
- Daily aggregated sales time series  
- Strong weekly recurrence and calendar seasonality  
- Frequent irregular demand spikes  
- End-of-year and holiday-driven effects  
- High variance that dominates absolute error metrics  

Missing dates were explicitly handled to construct a **continuous daily time series**, ensuring valid time-series modeling and leakage-free evaluation.

---

## Modeling Approaches Evaluated
The following models were implemented and compared under a unified evaluation framework:

- Naive and Seasonal Naive (7-day)
- ARIMA and SARIMA
- Prophet
- Random Forest (feature-based)
- XGBoost (feature-based)
- LSTM (sequence model)

All models were evaluated using the same data splits, feature construction, and forecast horizon to ensure fair and consistent comparison.

---

## Evaluation Methodology
- Rolling-origin backtesting with strict time-based splits  
- Fixed 7-day forecast horizon  
- Evaluation metrics:
  - MAE (average error magnitude)
  - RMSE (sensitivity to large forecast errors)
  - WMAPE (volume-weighted relative error)

**RMSE** was used as the primary ranking metric due to its emphasis on large forecast misses, which are most costly in volatile demand settings.

---

## Key Results
- **XGBoost consistently delivered the strongest performance**, achieving the lowest MAE, RMSE, and WMAPE across rolling folds.
- RMSE was reduced by approximately **25–31%** relative to naive and seasonal naive baselines.
- **Prophet and SARIMA** formed a strong second tier, confirming the value of explicitly modeling trend and seasonality in daily demand data.
- **Naive baselines and LSTM** underperformed, highlighting the limitations of rigid repetition assumptions and sequence-based deep learning in spike-driven daily data.
- Absolute errors remained elevated across all models due to rare but extreme demand spikes, making **relative performance differences** the most meaningful indicator of model quality.

---

## Forecast Behavior and Interpretability
Final-fold visualizations and a 7-day forward forecast show:
- Stable short-term forecasts with controlled variability  
- Difficulty predicting sharp, isolated demand spikes across all models  
- Calendar-consistent behavior, including end-of-year uplift, holiday-related dips, and post-holiday normalization  

This behavior supports **operational reliability** over aggressive extrapolation of rare peaks.

---

## Model Explainability
SHAP analysis was used to interpret the final XGBoost model. Predictions are driven primarily by:
- Month-level seasonality  
- Weekly and bi-weekly lag structure  
- Recent rolling demand level and volatility  

Day-of-week effects were present but comparatively weaker, explaining why models relying mainly on fixed weekly repetition (e.g., seasonal naive) performed poorly.

---

## Business Impact
The analysis demonstrates that feature-based forecasting models can **materially reduce large forecast errors** under realistic conditions. Stable and interpretable forecasts support improved planning decisions related to inventory, staffing, and short-term operations in volatile demand environments.

---

## Future Work
Potential extensions include:
- More systematic hyperparameter tuning for top-performing models (XGBoost, Prophet, SARIMA)
- Incorporation of explicit holiday and promotion indicators
- Probabilistic forecasting and prediction intervals for uncertainty estimation
- Direct multi-step forecasting strategies to reduce recursive error accumulation
- Segmented forecasting by region, category, or customer segment

---

## Takeaway
Feature-based gradient boosting provides the most reliable balance of adaptability, robustness, and interpretability for short-term daily sales forecasting in volatile environments. Classical seasonal models remain strong benchmarks, while increased model complexity does not inherently guarantee improved performance.
