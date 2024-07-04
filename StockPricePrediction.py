#Stockprice prediction - Yahoo Finance API - yfinance
import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.tsa.arima.model import ARIMA
import statsmodels.api as sm
import warnings

#stockprice data - Google
today = date.today()
d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days = 365)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2

data = yf.download('GOOG', 
                   start = start_date, end = end_date, 
                   progress = False)
data["Date"] = data.index
data = data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
data.reset_index(drop = True, inplace = True)
print(data.tail())

#Date & Close columns - enough
data = data[["Date", "Close"]]
print(data.head())

#Visualize close price of Google
plt.plot(data["Date"], data["Close"])

# from graph, it is clear that the dataset is not stationary; it is seasonal.
# so, we have to use seasonal decomposition method, 
# split the time series data into 4 different parts, for better understanding of time series data
result = seasonal_decompose(data["Close"], 
                            model = 'multiplicative', period = 24)
fig = plt.figure()
fig = result.plot()
fig.set_size_inches(15, 10)
# our data is seasonal; so we need to use SARIMA;
# for that, we need p,q,d values - found using autocorrelation plot
# d - 0 or 1; 1 for seasonal

#p
pd.plotting.autocorrelation_plot(data["Close"])
# p = 5; curve moving down after 5th line of first boundary

#q
plot_pacf(data["Close"], lags = 100)
#q = 2; only 2 points far away from all points

#ARIMA Model
p, d, q = 5, 1, 2
model = ARIMA(data["Close"], order = (p, d, q))
fitted = model.fit()
print(fitted.summary())
#predicted values will be wrong, since the data is seasonal; 
# ARIMA model will never perform well on seasonal time series data; so we use SARIMA


#SARIMA Model
model=sm.tsa.statespace.SARIMAX(data['Close'], order=(p, d, q),
                                seasonal_order=(p, d, q, 12))
model=model.fit()
print(model.summary())

# Future stock price prediction using SARIMA model
predictions = model.predict(len(data), len(data)+15)
print(predictions)