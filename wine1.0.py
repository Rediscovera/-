import pandas as pd
from pandas import DataFrame
from math import exp
from pylab import *
import matplotlib.pyplot as plot

target_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data"

glass = pd.read_csv(target_url, header=None, prefix="V")
glass.columns = {'ID', 'RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe', 'Type'}

summary = glass.describe()
print(summary)

ncol1 = len(glass.columns)

glassNormalized = glass.iloc[:, 1:ncol1]
ncol2 = len(glassNormalized.columns)
summary2 = glassNormalized.describe()

for i in range(ncol2):
    mean = summary2.iloc[1, i]
    sd = summary2.iloc[2, i]
    glassNormalized.iloc[:, i] = (glassNormalized.iloc[:, i] - mean) / sd

array = glassNormalized.values
plot.boxplot(array)
plot.show()


