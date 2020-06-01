import ROOT
import numpy as np
import sympy as sym
from sympy import init_printing

#1
print "Exercicio 1"
rangelist = list(range(10))
print(rangelist)
print "Soma"
print(sum(rangelist))

mylist = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
mylist += mylist
print(mylist[:])
print "Soma"
sum(mylist)
print(sum(mylist))


