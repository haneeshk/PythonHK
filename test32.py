import numpy as np
x=np.arange(-np.pi,np.pi,0.01)
from matplotlib import pyplot as plt
plt.plot(x,np.sin(x),'--w');



# Black plotting
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from jupyterthemes import jtplot
jtplot.style(theme='monokai', context='notebook', ticks=True, grid=False)

%%
