import petsc4py, sys
petsc4py.init(sys.argv)
from  petsc4py import PETSc
m, n = 32, 32
hx=1.0/(m-1)
hy=1.0/(n-1)
A=PETSc.Mat()
A.create(PETSc.COMM_WORLD)
A.setSizes([m*n,m*n])
A.setType('aij')



diagv = 2.0/hx**2 + 2.0/hy**2
offdx = -1.0/hx**2
offdy = -1.0/hy**2


Istart, Iend=A.getOwnershipRange()
