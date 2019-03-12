import pandas as pd
from pandas import DataFrame
from math import exp
from pylab import *
import matplotlib.pyplot as plot

target_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"

wine = pd.read_csv(target_url, header=0, sep=";")

summary = wine.describe()
wineNormalized = wine
ncols = len(wineNormalized.columns)
nrows = len(wine.index)

for i in range(ncols):
    mean = summary.iat[1, i]
    sd = summary.iat[2, i]
    wineNormalized.iloc[:, i] = ( wineNormalized.iloc[:, i] - mean) / sd

nDataCol = len(wine.columns) - 1
for i in range(nrows):
    dataRow = wineNormalized.iloc[i, 1:nDataCol]
    normTarget = wineNormalized.iat[i, nDataCol]
    labelColor = 1.0 / (1.0 + exp(-normTarget))
    dataRow.plot(color=plot.cm.RdYlBu(labelColor), alpha=0.5)

plot.xlabel("Attribute Index")
plot.ylabel("Quartile Ranges - Normalized")
plot.show()
