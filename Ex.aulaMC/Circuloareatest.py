import ROOT
import numpy as np
import sympy as sym
from sympy import init_printing
import random

n=1000000
j=0
v=0
listx=[]
for i in range(n):
  x=random.uniform(0,1)
  listx.append(x)
#print listx
listy=[]
for i in range(n):
  y=random.uniform(0,1)
  listy.append(y)
#print listy
for x,y in zip(listx,listy):
  if x*x+y*y <= 1: #Para r=1
    j= j+1
  else:
    v= v+1
print "Numero total de tentativas:"
print n
print "Numero de hits no circulo:"
print j
print "Numero de hits fora do circulo:"
print v
print "Area do circulo:"
print (4*j)/float(n)
print "Area do circulo aproximado:"
o=(4*j)/float(n)
print ("%.2f" % o)



