import petsc4py, sys
petsc4py.init(sys.argv)
from  petsc4py import PETSc
m, n = 32, 32
hx=1.0/(m-1)
hy=1.0/(n-1)
A=PETSc.Mat()
# A.create(PETSc.COMM_WORLD)
A.create()
A.setSizes([m*n,m*n])
A.setFromOptions()
A.setType('aij')


A.setUp()
A[0,0]=diagv


diagv = 2.0/hx**2 + 2.0/hy**2
offdx = -1.0/hx**2
offdy = -1.0/hy**2
Istart
Iend
A.setre
Istart, Iend=A.getOwnershipRange()


for i in range(1,10):
    print(i)

for I in range(Istart, Iend):
    A[I,I] = diagv
    i = I//n # map row number to
    j = I - i*n # grid coordinates
    if i> 0 : J = I-n; A[I,J] = offdx
    if i< m-1: J = I+n; A[I,J] = offdx
    if j> 0 : J = I-1; A[I,J] = offdy
    if j< n-1: J = I+1; A[I,J] = offdy




A.assemblyBegin()
A.assemblyEnd()


A.getValues([0,1,2,3,5],[0,1,2,3,4,5])

A.getValues([1,2],[1,2])

A[0,0]
A[1,1]
A[1,100]
