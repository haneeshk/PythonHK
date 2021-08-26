
# %%

import sys

import numpy as np
sys.path.append(r'/Users/haneeshkesari/Downloads/cmake_example/cmake-build-debug/')
from pythonppDemo import *
import plotly.express as px
import plotly.graph_objects as go

# Add data


# Create and style traces



x=np.array(LinSpace(0,2,10));
x
# %%
def plot(xi,yi):
    import pandas as pd
    df = pd.DataFrame(dict(
    x1 =x,
    x2 = yi))

    return px.line(df,x="x1",y="x2")

# %%

fig=plot(x,np.cos(10*x)*np.sin(x));
fig.show()

 # %%

x0=np.array(LinSpace(-10,10,10))
y0=np.sin(x0)
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=x0, y=y0, name='High 2014',
                         line=dict(color='firebrick', width=1,dash="dashdot")))




fig1.show()
import matplotlib.pyplot as plt
plt.plot(x0, y0)