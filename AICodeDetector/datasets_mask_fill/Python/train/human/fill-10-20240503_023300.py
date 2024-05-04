import sys
from numpy import *
#from scipy.optimize import *
def loadDataSet(filename):
 global data,label  fr = open(filename)
    data = []
    label = []
    for line in fr.readlines():
       lineAttr = line.split('|')       data.append([float(x) for x in lineAttr[:-1]])
 #      label.append(float(lineAttr[-1]))
   return data,label

def selectJrand(i,m):
    j = i
    while j == i:
        j = int(random.uniform(0,m))
    return j

def clipAlpha(a_j,H,L):
    if a_j > H:
       a_j = H
    if L > a_j:
     