import sys
import numpy as np
import scipy.stats as stats
import pylab
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot
from random import uniform
from math import exp

target_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"

abalone = pd.read_csv(target_url, header=None, prefix="V")
abalone.columns = ['Sex', 'Length', 'Diameter', 'Height', 'Whole wt', 'Shucked wt',
                   'Viscera wt', 'Shell wt', 'Rings']

summary = abalone.describe()

minRings = summary.iloc[3, 7]
maxRings = summary.iloc[7, 7]
nrows = len(abalone.index)

plot.subplot(121)
for i in range(nrows):
    dataRow = abalone.iloc[i, 1:8]
    labelColor = (abalone.iloc[i, 8] - minRings) / (maxRings - minRings)
    dataRow.plot(color=plot.cm.RdYlBu(labelColor), alpha=0.5)

plot.xlabel("Attribute Index")
plot.ylabel("Quartile Ranges")

meanRings = summary.iloc[1, 7]
sdRings = summary.iloc[1, 7]
plot.subplot(122)
for i in range(nrows):
    dataRow = abalone.iloc[i, 1:8]
    normTarget = (abalone.iat[i, 8] - meanRings) / sdRings
    labelColor = 1.0 / (1.0 + exp(-normTarget))
    dataRow.plot(color=plot.cm.RdYlBu(labelColor), alpha=0.5)
plot.xlabel("Attribute Index")
plot.ylabel("Quartile Ranges")

plot.show()

# dataRow2 = rocksVMines.iloc[1, 0:60]
# dataRow3 = rocksVMines.iloc[2, 0:60]
# dataRow21 = rocksVMines.iloc[20, 0:60]
#
# mean2 = 0.0; mean3 = 0.0; mean21 = 0.0
# numElt = len(dataRow2)
# for i in range(numElt):
#     mean2 += dataRow2[i]/numElt
#     mean3 += dataRow3[i]/numElt
#     mean21 += dataRow21[i]/numElt
#
# var2 = 0.0; var3 = 0.0; var21 = 0.0
# for i in range(numElt):
#     var2 += (dataRow2[i] - mean2) * (dataRow2[i] - mean2)
#     var3 += (dataRow3[i] - mean3) * (dataRow3[i] - mean3)
#     var21 += (dataRow21[i] - mean21) * (dataRow21[i] - mean21)
#
# corr23 = 0.0; corr221 = 0.0
# print()
# for i in range(numElt):
#     corr23 += (dataRow2[i] - mean2) * (dataRow3[i] - mean3) / sqrt(var2 * var3)
#
#     corr221 += (dataRow2[i] - mean2) * (dataRow21[i] - mean21) / sqrt(var2 * var21)
#
# print("Correlation between attribute 2&3\n")
# print(corr23)
# print('\n')
#
# print("Correlation between attribute 2&21\n")
# print(corr221)


# target = []
# for i in range(208):
#     if rocksVMines.iat[i, 60] == "M":
#         target.append(1.0)
#     else:
#         target.append(0.0)
#
# plot.subplot(121)
# dataRow = rocksVMines.iloc[0:208, 35]
# plot.scatter(dataRow, target)
# plot.xlabel("Attribute Value")
# plot.ylabel("Target Value")
#
#
# target = []
# for i in range(208):
#     if rocksVMines.iat[i, 60] == "M":
#         target.append(1.0 + uniform(-0.1, 0.1))
#
#     else:
#         target.append(0.0 + uniform(-0.1, 0.1))

# plot.subplot(122)
# dataRow = rocksVMines.iloc[0:208, 35]
# plot.scatter(dataRow, target, alpha=0.5, s=120)
# plot.xlabel("Attribute Value")
# plot.ylabel("Target Value")
# plot.show()


# dataRow2 = rocksVMines.iloc[1, 0:60]
# dataRow3 = rocksVMines.iloc[2, 0:60]
# dataRow21 = rocksVMines.iloc[20, 0:60]

# plot.subplot(211)
# plot.scatter(dataRow2, dataRow3)
# plot.xlabel("2nd Attribute")
# plot.ylabel("3rd Attribute")
#
#
#
# plot.subplot(212)
# plot.scatter(dataRow2, dataRow21)
# plot.xlabel("2nd Attribute")
# plot.ylabel("21st Attribute")
# plot.show()

# for i in range(208):
#     if rocksVMines.iat[i, 60] == "M":
#         pcolor = "red"
#     else:
#         pcolor = "blue"
#
#     dataRow = rocksVMines.iloc[i, 0:60]
#     dataRow.plot(color=pcolor)
#
# plot.xlabel("Attribute Index")
# plot.ylabel("Attribute Values")
# plot.show()


# data=urllib.request.urlopen(target_url)
# xlist=[]
# labels=[]
#
# for line in data:
#     row=line.strip().decode().split(",")
#     xlist.append(row)
#
# nrow=len(xlist)
# ncol=len(xlist[1])
#
# type2= [0] * 3
# colCounts=[]
#
# col=3
# colData=[]
# for row in xlist:
#     colData.append(float(row[col]))
#
# stats.probplot(colData, dist="norm", plot=pylab)
# pylab.show()

#
# colArray=np.array(colData)
# colMean=np.mean(colArray)
# colsd=np.std(colArray)
#
# print(str(colMean)+'\t\t'+str(colsd)+'\n')
#
# ntiles=4
#
# percentBdry=[]
#
# for i in range(ntiles+1):
#     percentBdry.append(np.percentile(colArray, i*(100)/ntiles))
#
# print("\n Boundaries for 4 Equal %s \n" % percentBdry + '\n')
#
# ntiles=10
#
# percentBdry = []
#
# for i in range(ntiles + 1):
#     percentBdry.append(np.percentile(colArray, i * (100) / ntiles))
#
# print("\n Boundaries for 10 Equal %s \n" % percentBdry + '\n')
#
# col=60
# colData=[]
# for row in xlist:
#     colData.append(row[col])
#
# unique=set(colData)
# print("the unique label values %s " % unique + '\n')
#
# catDict = dict(zip(list(unique), range(len(unique))))
#
# catCount = [0]*2
#
# for elt in colData:
#     catCount[catDict[elt]]+=1
# print("\nCounts for each value of Categporical Label %s\n" % list(unique))
# print(catCount)