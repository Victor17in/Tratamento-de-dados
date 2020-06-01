import ROOT
import numpy as np
import sympy as sym
from sympy import init_printing

x = sym.Symbol('x')
y = sym.Symbol('y')
x = input("Comprimento ")
y = input("Largura ")
print "A perimetro e:"
print(x*y)

