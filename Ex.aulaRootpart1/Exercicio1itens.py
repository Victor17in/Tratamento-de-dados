import ROOT
import numpy as np
import sympy as sym
from sympy import init_printing
def funcvar(x): 
	return np.sin(2*x)/x
print(funcvar(1))
x = sym.Symbol('x')

print(sym.diff(sym.sin(2*x)/x, x))
#Avaliar em x=1
def funcvar1(x):
	return sym.cos(2*x)*2/x - sym.sin(2*x)/x**2
print(funcvar1(1))

eq1 = sym.diff(sym.sin(2*x)/x, x)
sym.solve(eq1,1)
print(sym.solve(eq1,1))

print(sym.diff(sym.sin(2*x)/x, x, 2)) #devirada segunda
print(sym.diff(sym.sin(2*x)/x, x, 3)) #derivada terceira

sym.integrate(sym.sin(2*x)/x, x)
print(sym.integrate(sym.sin(2*x)/x, x))
print(sym.integrate(sym.sin(2*x)/x, (x, 0, 3))) #integral definida



