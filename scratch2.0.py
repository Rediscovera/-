import urllib
import urllib.request
import sys
import numpy as np

target_url="http://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data"
data=urllib.request.urlopen(target_url)
xlist=[]
labels=[]
for line in data:
    row=line.strip().decode().split(",")
    xlist.append(row)
nrow=len(xlist)
ncol=len(xlist[1])

type2= [0] * 3
colCounts=[]

col=3
colData=[]
for row in xlist:
    colData.append(float(row[col]))

colArray=np.array(colData)
colMean=np.mean(colArray)
colsd=np.std(colArray)

print(str(colMean)+'\t\t'+str(colsd)+'\n')

ntiles=4

percentBdry=[]

for i in range(ntiles+1):
    percentBdry.append(np.percentile(colArray, i*(100)/ntiles))

print("\n Boundaries for 4 Equal %s \n" % percentBdry + '\n')

ntiles=10

percentBdry = []

for i in range(ntiles + 1):
    percentBdry.append(np.percentile(colArray, i * (100) / ntiles))

print("\n Boundaries for 10 Equal %s \n" % percentBdry + '\n')

col=60
colData=[]
for row in xlist:
    colData.append(row[col])

unique=set(colData)
print("the unique label values %s " % unique + '\n')

catDict = dict(zip(list(unique), range(len(unique))))

catCount = [0]*2

for elt in colData:
    catCount[catDict[elt]]+=1
print("\nCounts for each value of Categporical Label %s\n" % list(unique))
print(catCount)