import numpy
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt
import urllib.request
from sklearn.metrics import roc_curve, auc

target_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data"
data = urllib.request.urlopen(target_url)
xlist = []
labels = []

for line in data:
    row = line.strip().decode().split(",")
    if row[-1] == 'M':
        labels.append(1.0)
    else:
        labels.append(0.0)
    row.pop()
    floatRow = [float(num) for num in row]
    xlist.append(floatRow)

indices = range(len(xlist)) #样本个数
xListTest = [xlist[i] for i in indices if i%3 == 0]
xListTrain = [xlist[i] for i in indices if i%3 != 0]
labelsTest = [labels[i] for i in indices if i%3 == 0]
labelsTrain = [labels[i] for i in indices if i%3 != 0]

xTrain = numpy.array(xListTrain)
xTest = numpy.array(xListTest)
# 标签是固定的  不会改变
yTrain = numpy.array(labelsTrain)
yTest = numpy.array(labelsTest)

alphaList = [0.1**i for i in range(-3, 6)]

aucList = []
for alph in alphaList:
    rocksVMinesRidgeModel = linear_model.Ridge(alpha=alph)
    rocksVMinesRidgeModel.fit(xTrain, yTrain)
    fpr, tpr, thresholds = roc_curve(yTest, rocksVMinesRidgeModel.predict(xTest))
    roc_auc = auc(fpr, tpr)
    aucList.append(roc_auc)

for i in range(len(aucList)):
    print(aucList[i], alphaList[i])

x = range(-3, 6)
plt.plot(x, aucList, 'k')
plt.figure()

indexBest = aucList.index(max(aucList))
alph = alphaList[indexBest]
rocksVMinesRidgeModel = linear_model.Ridge(alpha=alph)
rocksVMinesRidgeModel.fit(xTrain, yTrain)

plt.scatter(rocksVMinesRidgeModel.predict(xTest), yTest, s=100, alpha=0.25)
plt.show()