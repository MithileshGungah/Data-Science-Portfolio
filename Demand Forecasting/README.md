# Daily Sales Forecasting Under Volatile Demand

## Business Problem
Accurate short-term demand forecasting is critical for retail operations. Over-forecasting leads to excess inventory, higher holding costs, and waste, while under-forecasting results in stockouts, lost revenue, and poor customer experience. These risks are amplified in environments with high volatility, irregular demand spikes, and strong calendar effects.

This project develops and evaluates forecasting models designed to deliver reliable 7-day sales forecasts that materially outperform simple baselines under realistic operational conditions.

---

## Objective
The primary objective is to identify forecasting approaches that balance:
- short-term accuracy
- robustness to volatility and demand spikes
- interpretability for operational decision-making

Rather than optimizing for perfect prediction of rare extremes, the focus is on stable and dependable forecasts suitable for inventory planning, staffing, and near-term operational execution.

---

## Forecast Horizon
A 7-day forecast horizon is used throughout the project, aligning with common business planning cycles such as:
- weekly inventory replenishment
- workforce scheduling
- short-term budgeting and performance tracking
- promotion monitoring

---

## Data Overview
- Granularity: daily aggregated sales  
- Coverage: approximately four years  
- Characteristics:
  - strong calendar-driven seasonality
  - frequent irregular demand spikes
  - end-of-year and holiday-related effects
  - high variance dominating absolute error metrics  

Missing dates were explicitly handled to construct a continuous daily time series, ensuring valid time-series modeling and leakage-free evaluation.

---

## Exploratory Data Analysis
Exploratory analysis revealed several consistent patterns:
- a clear long-term upward growth trend
- pronounced monthly seasonality, with early-year dips and late-year peaks
- recurring intra-year transitions, including post-winter rebounds and late-year surges
- demand persistence across adjacent periods rather than isolated, random spikes

Weekly aggregation was evaluated but excluded from final reporting, as it did not reveal stable calendar-aligned patterns beyond what was already captured by daily and monthly views.

---

## Forecasting Models Evaluated
The following approaches were implemented and compared under a unified evaluation framework:

### Baselines
- Naive
- Seasonal Naive (7-day)

### Statistical Models
- ARIMA
- SARIMA

### Decomposition-Based
- Prophet

### Feature-Based Machine Learning
- Random Forest
- XGBoost

### Deep Learning
- LSTM (benchmarking only)

All models were trained and evaluated using identical data splits, feature construction, and forecast horizons to ensure fair comparison.

---

## Feature Engineering
For supervised models, features were constructed using historical information only to prevent leakage:
- lagged demand features (lag_1, lag_7, lag_14)
- rolling statistics capturing recent demand level and volatility
- calendar features (month, day of week)

---

## Evaluation Methodology
Models were evaluated using rolling-origin backtesting with strict time-based splits and a fixed 7-day forecast horizon.

Evaluation metrics included:
- MAE for average error magnitude
- RMSE to emphasize large forecast errors
- WMAPE for volume-weighted relative performance

RMSE was used as the primary ranking metric due to its sensitivity to large forecast misses, which are most costly in volatile demand environments.

---

## Key Results
- XGBoost consistently achieved the strongest performance, delivering the lowest MAE, RMSE, and WMAPE across rolling evaluation windows.
- RMSE was reduced by approximately 25–31 percent relative to naive and seasonal naive baselines.
- Prophet and SARIMA formed a strong second tier, confirming the value of explicit trend and seasonality modeling.
- Naive baselines and LSTM underperformed, highlighting the limitations of rigid repetition assumptions and sequence-based deep learning in spike-driven daily data.
- Absolute errors remained elevated across all models due to rare but extreme demand spikes, making relative performance improvements the most meaningful indicator of model quality.

---

## Forecast Behavior and Interpretability
Final-fold diagnostics and a 7-day forward forecast demonstrate:
- stable short-term predictions with controlled variability
- limited overreaction to isolated spikes
- behavior consistent with known calendar effects, including end-of-year uplift, early-year slowdowns, and post-holiday normalization

This balance supports operational reliability rather than aggressive extrapolation of rare extremes.

---

## Model Explainability
SHAP analysis was used to interpret the final XGBoost model. Key findings include:
- calendar month as the dominant driver, confirming strong monthly seasonality observed in EDA
- strong influence of weekly and bi-weekly lag features, capturing short-term momentum
- meaningful contribution from rolling demand statistics
- comparatively weak day-of-week effects, explaining the limited value of rigid weekly seasonal assumptions

The alignment between EDA insights and SHAP attribution confirms that the model learned meaningful and interpretable demand structure.

---

## Business Impact
This analysis demonstrates that feature-based gradient boosting models can materially reduce large forecast errors under volatile demand conditions. The resulting forecasts support:
- improved inventory allocation
- more reliable staffing decisions
- risk-aware short-term operational planning

By prioritizing stability and interpretability, the approach reflects how forecasting models are evaluated and deployed in real business environments.

---

## Limitations and Future Work

- Incorporate explicit holiday and promotion indicators to better capture event-driven demand spikes.
- Produce prediction intervals to support uncertainty-aware planning and risk management.
- Explore direct multi-step forecasting approaches to reduce recursive error accumulation.
- Extend the framework to hierarchical forecasting across regions, categories, or customer segments.
- Deploy the solution as a scheduled forecasting pipeline or lightweight API for operational use.

## Takeaway

For short-term daily sales forecasting under volatile demand, feature-based gradient boosting provides the strongest balance of robustness, adaptability, and interpretability. Classical seasonal models remain effective benchmarks, while increased model complexity alone does not guarantee improved forecasting performance.

--- 

## Technology Stack
- **Language:** Python 3.12  
- **Libraries:** Pandas, NumPy, Scikit-learn, XGBoost, Statsmodels, Prophet, SHAP, Matplotlib, Plotly, TensorFlow

---

## Code

[![View Code]()

---

## Contact

[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:mithileshgungah@gmail.com) &nbsp;&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mithilesh-gungah-331133215/)
