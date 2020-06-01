import ROOT
import numpy as np
import sympy as sym
from sympy import init_printing

s1 = "tempo"
s2 = "space"
print(s1)
print(s2)

s3 = s1[:-4] 
s4 = s1[-3]
s5 = s1[-1:]
s6 = s3 + s4 + s5
print(s6)

s7 = s2[:-4] 
s8 = s2[-3]
s9= s2[-1:]
s10 = s7 + s8 + s9
print(s10)
