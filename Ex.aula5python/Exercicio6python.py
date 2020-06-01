import ROOT
import numpy as np
import sympy as sym
from sympy import init_printing

print "A primeira temos a conversao de Celsius para Fahrenheit e depois o oposto:"
x = sym.Symbol('x')
y = sym.Symbol('y')
x = input("Temperatura em Celsius: ")

print "Em Fahrenheit:"
print(1.8*x+32)

y = input("Temperatura em Fahrenheit: ")
print "Em Celsius:"
print((5*y-160)/9)
