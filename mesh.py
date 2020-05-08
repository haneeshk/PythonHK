# Create the data.
from numpy import pi, sin, cos, mgrid
dphi, dtheta = pi/250.0, pi/250.0
[phi,theta] = mgrid[0:pi+dphi*1.5:dphi,0:2*pi+dtheta*1.5:dtheta]
m0 = 4; m1 = 3; m2 = 2; m3 = 3; m4 = 6; m5 = 2; m6 = 6; m7 = 4;
r = sin(m0*phi)**m1 + cos(m2*phi)**m3 + sin(m4*theta)**m5 + cos(m6*theta)**m7
x = r*sin(phi)*cos(theta)
y = r*cos(phi)
z = r*sin(phi)*sin(theta)
x
# View it.
from mayavi import mlab
s = mlab.mesh(x, y, z)
mlab.show()

import plotly.graph_objects as go

fig = go.Figure(data=[
    go.Mesh3d(
        x=[0, 1, 2, 0],
        y=[0, 0, 1, 2],
        z=[0, 2, 0, 1],
        colorbar_title='z',
        colorscale=[[0, 'gold'],
                    [0.5, 'mediumturquoise'],
                    [1, 'magenta']],
        # Intensity of each vertex, which will be interpolated and color-coded
        intensity=[0, 0.33, 0.66, 1],
        # i, j and k give the vertices of triangles
        # here we represent the 4 triangles of the tetrahedron surface
        i=[0, 0, 0, 1],
        j=[1, 2, 3, 2],
        k=[2, 3, 1, 3],
        name='y',
        showscale=True
    )
])

fig.show()


import numpy as np

import plotly.graph_objs as go

import numpy as np
import matplotlib.cm as cm
from scipy.spatial import Delaunay
n=12 # number of radii
h=1.0/(n-1)
r = np.linspace(h, 1.0, n)
theta= np.linspace(0, 2*np.pi, 36)

r,theta=np.meshgrid(r,theta)
r=r.flatten()
theta=theta.flatten()

#Convert polar coordinates to cartesian coordinates (x,y)
x=r*np.cos(theta)
y=r*np.sin(theta)
x=np.append(x, 0)#  a trick to include the center of the disk in the set of points. It was avoided
                 # initially when we defined r=np.linspace(h, 1.0, n)
y=np.append(y,0)
z = np.sin(-x*y)

points2D=np.vstack([x,y]).T
tri=Delaunay(points2D)


def tri_indices(simplices):
    #simplices is a numpy array defining the simplices of the triangularization
    #returns the lists of indices i, j, k

    return ([triplet[c] for triplet in simplices] for c in range(3))

def plotly_trisurf(x, y, z, simplices, colormap=cm.RdBu, plot_edges=None):
    #x, y, z are lists of coordinates of the triangle vertices
    #simplices are the simplices that define the triangularization;
    #simplices  is a numpy array of shape (no_triangles, 3)
    #insert here the  type check for input data

    points3D=np.vstack((x,y,z)).T
    tri_vertices=map(lambda index: points3D[index], simplices)# vertices of the surface triangles
    zmean=[np.mean(tri[:,2]) for tri in tri_vertices ]# mean values of z-coordinates of
                                                      #triangle vertices
    min_zmean=np.min(zmean)
    max_zmean=np.max(zmean)
    facecolor=[map_z2color(zz,  colormap, min_zmean, max_zmean) for zz in zmean]
    I,J,K=tri_indices(simplices)

    triangles=go.Mesh3d(x=x,
                     y=y,
                     z=z,
                     facecolor=facecolor,
                     i=I,
                     j=J,
                     k=K,
                     name=''
                    )

    if plot_edges is None:# the triangle sides are not plotted
        return [triangles]
    else:
        #define the lists Xe, Ye, Ze, of x, y, resp z coordinates of edge end points for each triangle
        #None separates data corresponding to two consecutive triangles
        lists_coord=[[[T[k%3][c] for k in range(4)]+[ None]   for T in tri_vertices]  for c in range(3)]
        Xe, Ye, Ze=[reduce(lambda x,y: x+y, lists_coord[k]) for k in range(3)]

        #define the lines to be plotted
        lines=go.Scatter3d(x=Xe,
                        y=Ye,
                        z=Ze,
                        mode='lines',
                        line=dict(color= 'rgb(50,50,50)', width=1.5)
               )
        return [triangles, lines]



def map_z2color(zval, colormap, vmin, vmax):
    #map the normalized value zval to a corresponding color in the colormap

    if vmin>vmax:
        raise ValueError('incorrect relation between vmin and vmax')
    t=(zval-vmin)/float((vmax-vmin))#normalize val
    R, G, B, alpha=colormap(t)
    return 'rgb('+'{:d}'.format(int(R*255+0.5))+','+'{:d}'.format(int(G*255+0.5))+\
           ','+'{:d}'.format(int(B*255+0.5))+')'


data2=plotly_trisurf(x,y,z, tri.simplices, colormap=cm.cubehelix, plot_edges=None)
fig2 = go.Figure(data=data2, layout=layout)
fig2['layout'].update(dict(title='Triangulated surface',
                          scene=dict(camera=dict(eye=dict(x=1.75,
                                                          y=-0.7,
                                                          z= 0.75)
                                                )
                                    )))

layout = go.Layout(
         title='Moebius band triangulation',
         width=800,
         height=800,
         scene=dict(
         xaxis=dict(axis),
         yaxis=dict(axis),
         zaxis=dict(axis),
        aspectratio=dict(
            x=1,
            y=1,
            z=0.5
        ),
        )
        )
py.iplot(fig2, filename='trisurf-cubehx')



from meshpy.tet import MeshInfo



import open3d as o3d
 print("Let's draw a cubic using o3d.geometry.LineSet.")
    points = [
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 1],
        [1, 0, 1],
        [0, 1, 1],
        [1, 1, 1],
    ]
    lines = [
        [0, 1],
        [0, 2],
        [1, 3],
        [2, 3],
        [4, 5],
        [4, 6],
        [5, 7],
        [6, 7],
        [0, 4],
        [1, 5],
        [2, 6],
        [3, 7],
    ]
    colors = [[1, 0, 0] for i in range(len(lines))]
points=o3d.utility.Vector3dVector(points)
lines=o3d.utility.Vector2iVector(lines)
line_set=o3d.geometry.LineSet(points,lines,)
line_set.colors = o3d.utility.Vector3dVector(colors)
o3d.visualization.draw_geometries([line_set])
