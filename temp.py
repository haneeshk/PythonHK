import numpy.distutils.system_info as sysinfo
sysinfo.get_info('blas')

np.show_config()

import numpy as np
from matplotlib import pyplot as plt
x=np.arange(-10,10,0.1)
y_list=list(map(np.sin, x))
y=np.array(y_list)

x

plt.plot(x,y,'ro')

#%%

from only import only
only.TableForm(only.only("^d.*",dir(C)))

import sys
sys.path
from only.only import


TableForm(dir())

# %%
import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(y=list(y)))
fig.add_trace(go.Scatter(y=list(x)))
fig.update_layout(title = 'Hello Figure')
fig.show()


# %%

import sympy
sympy.init_printing(use_latex=True)
import scipy
dir(sympy)
x=sympy.symbols('x')
sympy.diff(sympy.sin(x**2),x)
sympy.series(sympy.sin(x**2),x,0,5)


#%%
from IPython.display import display

display(x)


from only.only import *
TableForm(dir())

class a:
    __init__(self)
