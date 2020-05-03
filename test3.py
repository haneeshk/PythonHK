# %%codecell
import initHK
import sys
import os
print(os.pardir)
from os.path import dirname
os.pardir
print(dirname("test3.ipynb"))
sys.path.append(os.pardir+"/startup")
import initHK
sys.path
# %%codecell

x=2+2
y=3
del(x)
print(y)

# %%markdown

This is $x^2$

# %%timeit

ans=(sin*ov*cos)(pi/2)
print(ans)
