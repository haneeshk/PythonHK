# from dolfin import *
# from fenics import *

import numpy as np
from scipy import constants
from numpy import log as log
from numpy import e as e
import matplotlib.pyplot as plt


from scitools.std import sqrt, pi, exp, linspace, plot, movie
import time

class   Bar:
        """This class creates a energy class for an elastic Bar"""



        def __init__(self, Diameter=1, PoissonRatio=0.2, YoungsModulus=1.23, Length=1):
            self.D=Diameter         # Diameter of the Beam
            self.nu=PoissonRatio    # Poisson's Ratio
            self.E=YoungsModulus    # Young's modulus
            self.L=Length           # Total Length

        def l(self, x):
            return np.sqrt(self.D **2 + x** 2)

        def strain(self, x,l=None):
             if l==None: l=self.l(x)
             L=self.L
             return log(l/L)


        def stress(self,x,l=None):
            if l==None: l=self.l(x)
            E=self.E
            ep=self.strain(x,l)
            return (x/l**2)*E*ep

        def energy(self, x):
            ep=self.strain(x)
            E=self.E
            return 0.5*E*ep**2




x= np.arange(-2,2,0.1)
B1=Bar(Length=np.sqrt(2))
B1strain=np.vectorize(B1.strain)
B1stress=np.vectorize(B1.stress)
B1energy=np.vectorize(B1.energy)

print(  "The parameters of "
        "\n \t Young's Modulus: \t{} "
        "\n \t Poisson's Ratio: \t{}"
        "\n \t Length: \t{}"
        "\n \t Diameter: \t{}".
        format(
        B1.E,
        B1.nu,
        B1.L,
        B1.D))


# B1strainVec=B1strain(x)
# B1stressVec=B1stress(x)
# B1energyVec=B1energy(x)
# plt.plot(x, B1strainVec)
# plt.plot(x, B1energyVec)
# plt.xlabel('$x_1$')
# plt.ylabel('$u_3$')
# plt.title('Deflection of a cantilever beam under self weight')
# plt.show()


def f(x,m,s):
    return (1.0/(sqrt(2*pi)*s))*exp(-0.5*((x-m)/s)**2)



m=0
s_min=0.2
s_max=2
x=linspace(m-3*s_max, m+3*s_max,10)
s_values =linspace(s_max, s_min, 3)
max_f=f(m,m,s_min)


#
plt.ion()
y=f(x,m, s_max)
print len(x), "\n", len(y)
print x, \
    "\n", \
      y
plt.plot(x,y)
plt.axis([x[0], x[-1], -0.1, max_f])
# plt.xlabel('x')
# plt.ylabel('f')
# counter=0
# # plt.figure()
# plt.show()
# for s in s_values:
#     y=f(x,m,s)
#     lines[0].set_ydata(y)
#     plt.draw()
#
#     # axis=[x[0], x[-1], -0.1, max_f],
#     #      xlabel='x', ylabel='f', legend='s=%4.2f' % s,
#     #      savefig='tmp%04d.png' % counter)
#     counter +=1
#     #time.sleep(0.2)