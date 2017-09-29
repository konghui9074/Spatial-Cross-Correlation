import csv, os
import numpy as np

os.chdir(r"C:\Users\Helen\Box Sync\Project_Uber & public transit NYC\Results\Spatial Cross-correlation\Test")

record=csv.reader(file('value1.csv','rb'))
firstline=True
value1=[]
for row in record:
    if firstline:
        firstline=False
        continue
    value1.append(map(float,row))
x=np.asarray(value1)
x=(x-np.mean(x))/np.std(x)

record=csv.reader(file('value2.csv','rb'))
firstline=True
value2=[]
for row in record:
    if firstline:
        firstline=False
        continue
    value2.append(map(float,row))
y=np.asarray(value2)
y=(y-np.mean(y))/np.std(y)

record=csv.reader(file('distance.csv','rb'))
distance=[]
for row in record:
    distance.append(map(float,row))
d=np.asarray(distance)

dx=1.0/d
dx[dx==float('inf')]=0
w=dx/np.sum(dx)

rc=np.dot(np.dot(x,w),np.transpose(y))
print rc
