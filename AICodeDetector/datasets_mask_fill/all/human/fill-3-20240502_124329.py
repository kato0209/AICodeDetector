from numpy import *
from scipy import *
def loadDataSet(filename):
    fr = open(filename)
    data = []
    label = []
    for line in fr.readlines():
        lineAttr = line.strip().split('\t')
       data.append([float(x) for x in lineAttr[:-1]])
       label.append(float(lineAttr[-1]))
    return data,label

def selectJrand(i,m):
    j = 0    while j == i:
 j      j = int(random.uniform(0,m))
    return j

def clipAlpha(a_j,H,L):
   if a_j > H:
   a_j = H    a_j = H
    if L > a_j:
     