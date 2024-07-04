**Time Series Forecasting**

Time Series Forecasting means analyzing and modeling time-series data to make future decisions. Some of the applications of Time Series Forecasting are weather forecasting, sales forecasting, business forecasting and stock price forecasting. ARIMA and SARIMA models are popular statistical techniques used for Time Series Forecasting.

**ARIMA vs SARIMA**

  * The ARIMA model is a forecasting tool for time series data that predicts future values based on past data by identifying and combining patterns like trends and noise. It uses differencing to make the data stationary, and applies autoregressive and moving average techniques to capture relationships over time.

  * The SARIMAX model is a type of time series forecasting tool that helps predict future data points by considering past patterns, seasonal trends, and external influences. It improves on basic models by factoring in things like holidays or special events that might affect the data.

In this project, Time Series Forecasting is done with ARIMA and SARIMA. We'll know which model is best for the dataset, after analysis. Here, I used Yahoo Finance API to collect Google stock price data.
