# %%codecell

import sys
import os
from os.path import dirname
sys.path.append(os.getcwd()+"/startup")
import initHK;
from IPython.display import display as Echo
from numpy import *


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
