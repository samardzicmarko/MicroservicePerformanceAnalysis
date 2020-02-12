import numpy as np
import pandas as pd

class get_signals():
    def __init__(self, array, lag, threshold, influence):
        self.y = list(array)
        self.length = len(self.y)
        self.lag = lag
        self.threshold = threshold
        self.influence = influence
        self.signals = np.zeros(len(y))
        self.filteredY = np.array(y)
        self.avgFilter = np.zeros(len(y))
        self.stdFilter = np.zeros(len(y))
        avgFilter[self.lag - 1] = np.mean(self.y[0:self.lag])
        stdFilter[self.lag - 1] = np.std(self.y[0:self.lag])
        
    def detect_spikes(y, lag, threshold, influence):
        signals = np.zeros(len(y))
        filteredY = np.array(y)
        avgFilter = np.zeros(len(y))
        stdFilter = np.zeros(len(y))
        avgFilter[lag - 1] = np.mean(y[0:lag])
        stdFilter[lag - 1] = np.std(y[0:lag])
        for i in range(lag, len(y) - 1):
            if abs(y[i] - avgFilter[i-1]) > threshold * stdFilter [i-1]:
                if y[i] > avgFilter[i-1]:
                    signals[i] = 1
                else:
                    signals[i] = -1

                filteredY[i] = influence * y[i] + (1 - influence) * filteredY[i-1]
                avgFilter[i] = np.mean(filteredY[(i-lag):i])
                stdFilter[i] = np.std(filteredY[(i-lag):i])
            else:
                signals[i] = 0
                filteredY[i] = y[i]
                avgFilter[i] = np.mean(filteredY[(i-lag):i])
                stdFilter[i] = np.std(filteredY[(i-lag):i])
                

        return dict(signals = np.asarray(signals),
                    avgFilter = np.asarray(avgFilter),
                    stdFilter = np.asarray(stdFilter))



        


