import matplotlib.pyplot as plt
from pylab import rcParams
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import numpy as np

class plots():
    def __init__(self, data, window, threshold, ts_array, z_results):
        self.data = data
        self.window = window
        selff.threshold = threshold
        
    def plot_time_series(timeseries):
        timeseries.plot(figsize=(16,8))
        
    def plot_decomposition(timeseries):
        freq = ((24*60)//1)
        print("Freq is set to minute and model is additive")
        ts = seasonal_decompose(timeseries, model='additive', freq=freq)
        fig = plt.figure()
        fig = ts.plot()
        fig.set_size_inches(15,12)
        plt.title('Decomposition of time series')
        plt.show()

        
    def plot_rolling(timeseries, window, threshold=0.01):
        rollingmean = timeseries.rolling(window).mean()
        rollingstd = timeseries.rolling(window).std()
        
        fig = plt.figure(figsize=(12,8))
        orig = plt.plot(timeseries, label = 'Original Time series')
        mean = plt.plot(rollingmean, label = 'Rolling mean')
        std = plt.plot(rollingstd, label = 'Rolling stddev')
        plt.legend(loc='best')
        plt.title('Rolling mean and Standard deviation')
        plt.show()
        
    def plot_trend(timeseries):
        extract = seasonal_decompose(timeseries, freq =((24*60)//1))
        trend = extract.trend
        trend.plot(figsize=(16,8))
        plt.title('Trend')

    def plot_z_score(ts_array, z_results):
        fig, ax = plt.subplots(figsize=[18,16])
        ax = fig.add_subplot(2,1,1)
        ax.plot(ts_array[:])
        ax = fig.add_subplot(2,1,2, sharex=ax)
        ax.step(np.arange(1, len(ts_array)+1), z_results['signals'])
        plt.ylim(0, 1.5)
        plt.suptitle("Peak detection using Smoothed Z-score")

    def plot_results_all():
        fig = px.scatter(data, x='timestamp', y='dataset', color='is_spike')
        fig.update_layout(title='Anomaly events in each Time series')
        fig.show()

        