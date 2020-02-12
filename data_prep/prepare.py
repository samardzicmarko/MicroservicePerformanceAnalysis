import statsmodels
from statsmodels.tsa.stattools import adfuller
import pandas as pd

class clean_data:
    def __init__(self, significance=0.5):
        self.SignificanceLevel = significance
        self.pValue = None
        self.isStationary = None
        
    def ADF_Test(self, timeseries, printResults = True):
        
        adf = adfuller(timeseries, autolag='AIC')
        self.pValue = adf[1]
        
        if (self.pValue<self.SignificanceLevel):
            self.isStationary = True  
        else:
            self.isStationary = False
            
        dataResults = pd.Series(adf[0:4], index=['ADF Test Statistic', 'P-Value', 'Num. lags used', 'Num. Observation used'])
        
        for key, value in adf[4].items():
            dataResults['Critical Value (%s)'%key] = value
            
        print('Augmented Dickey-Fuller Test Results:')
        print(dataResults)

    def resample(timeseries):
        timeseries.copy()
        timeseries.index = pd.to_datetime(timeseries['datetime'])
        resampled = timeseries.resample('1Min').mean()
        resampled['stime'].fillna(resampled['stime'].mean(), inplace=True)
        return resampled
    
    def difference(timeseries):
        diff = timeseries.stime - timeseries.stime.shift(1)
        diff = diff.dropna(inplace=False)
        diff = pd.DataFrame(diff)
        return diff



    