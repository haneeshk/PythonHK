# %%codecell

import sys
import os
from os.path import dirname
sys.path.append(os.getcwd()+"/startup")
# from initHK import at, ov, to;
from IPython.display import display as Echo
# from numpy import *
from initHK import *
print(sin*at*pi)


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


# %%codecell

a=2.0;
b=a;
b=3.0;
print(a)


from functional_notations import _f,
