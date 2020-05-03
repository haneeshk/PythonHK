# This defines the material properties and
# geometry of a 3D elastic beam


# material Elastic properties
mu= 1         # shear modulus
beta = 1.25
lambda_ = beta
E=mu*(3*lambda_+2*mu)/(lambda_+mu)  # Young's modulus
nu=lambda_/(2*(lambda_+mu))
Estar=E*(1-nu)/((1+nu)*(1-2*nu))    # Wenqiang's derivation


#Other material properties
rho= 1         # density


# geometry parameters
Length= 1.23/2      # Length of the beam
W= 0.1       #  Width of the beam
delta = W/Length
gamma = 0.4 * delta**2
g = gamma

# Mesh parameters
nx=100  # number of elements in the x-direction
ny=30   # number of elements in the y-direction
nz=30   # number of elements in the z-direction
tol = 1e-14