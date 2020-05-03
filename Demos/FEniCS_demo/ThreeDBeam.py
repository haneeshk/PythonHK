"""
Created on Sat Nov 19 20:03:15 2016

@author: Haneesh
"""

import numpy as np
from fenics import *
from dolfin import *

from SDomains import *

# Geometry and Material Parameters
from MatGeoProp import W, Length
from MatGeoProp import nx, ny, nz, tol
from MatGeoProp import rho, g







# Create mesh and define function space
mesh = BoxMesh(Point(0, 0, 0), Point(Length, W, W), nx, ny, nz)
V = VectorFunctionSpace(mesh, 'P', 2)

# Define boundary condition
from MatGeoProp import tol
def clamped_boundary(x, on_boundary):
    return on_boundary and x[0] < tol


bc = DirichletBC(V, Constant((0, 0, 0)), clamped_boundary)




#Define function spaces
u = TrialFunction(V)
v = TestFunction(V)



# Define Variational Problem
from MatGeoProp import lambda_, mu
d = u.geometric_dimension()  # space dimension
def epsilon(u):
    return 0.5 * (nabla_grad(u) + nabla_grad(u).T)


def sigma(u):
    return lambda_ * nabla_div(u) * Identity(d) + 2 * mu * epsilon(u)

f = Constant((0, 0, rho * g))
T = Constant((0, 0, 0))

a = inner(sigma(u), epsilon(v)) * dx
L = dot(f, v) * dx + dot(T, v) * ds

# Compute solution
u = Function(V)
problem = LinearVariationalProblem(a, L, u, bc)
solver = LinearVariationalSolver(problem)
solver.parameters["linear_solver"] = "cg"
solver.solve()  # solve(a==L,u,bc)



# Save solution in VTK format

File('Displacement_Field.xml') << u




#f = Expression('100*exp(-100*(x[0]*x[0] + x[1]*x[1]))')