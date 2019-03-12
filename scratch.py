import urllib
import urllib.request
import sys

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
for col in range(ncol):
    for row in xlist:
        try:
            a = float(row[col])
            if isinstance(a,float):
                type2[0]+=1
        except ValueError:
            if len(row[col])>0:
                type2[1]+=1
            else:
                type2[2]+=1
    colCounts.append(type2)
    type2= [0] * 3
print("dddddddd")
iCol=0
for types in colCounts:
    print(str(iCol)+'\t\t'+str(types[0])+'\t\t'+str(types[1])+'\t\t'+str(types[2])+'\n')
    iCol+=1
