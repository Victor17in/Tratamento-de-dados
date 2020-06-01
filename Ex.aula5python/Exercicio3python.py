import ROOT
import numpy as np
import sympy as sym
from sympy import init_printing

#3
print "Exercicio 3"
mylist2 = (11, 22, 33, 44, 55, 66)
print(mylist2[:])
print(mylist2[3:5])
mylist3 = mylist2[3:5]
mylist3 += mylist2
print(mylist3[:])
