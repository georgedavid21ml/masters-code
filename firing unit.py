# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 13:09:47 2022

@author: George Smith

firing unit has folllwing dimesnions:
radius = 10mm
axial length(z) = 28mm

cathode(s) at:
1. r=0, z=0

andode(s) at:
1. r=1-4, z=3
2. r=3-10, z=28

high voltage shield:
r=2-6, z=5

grid:
r=1, z=0
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


grid_size = 60

r_length = 10
z_length = 30

step_r = 1
step_z = 1

v_top = 100
v_bottom = 0
v_right = 0
v_left = 0

cat_1 =2
ano_1 =2
ano_2 =2
hvs =2
grid =2

max_iter = 500

v_guess =1

colorinterpolation = 50
colourMap = plt.cm.jet

r, z = np.meshgrid(np.linspace(0, z_length -1, grid_size), \
                   np.linspace(0, (r_length-1) , grid_size))

V1 = np.empty((grid_size, grid_size))

V1.fill(v_guess)
"""
V1[(r_length-18):, :] = v_top
#V1[:1, :] = v_bottom
V1[:, (z_length-1):] = v_right
V1[:, :1] = v_left

V1[0, 0] = cat_1
V1[1:4, 3] = ano_1
V1[3:10, 27] = ano_2
V1[2:6, 5] = hvs
V1[1, 0] = grid

def electrode_nodes(array, step):
    i_nodes = []
    k_nodes = []    
    for i in range(0, r_length, step):
        for k in range(0, z_length, step):
            if (array[i][k] == 2):
                i_nodes.append(i)
                k_nodes.append(k)
    nodes = np.array(list(zip(i_nodes, k_nodes)))
    return nodes
                
nodes = electrode_nodes(V1, 1)


cat_1 =0
ano_1 =5
ano_2 =10
hvs =2
grid =0

V1[0, 0] = cat_1
V1[1:4, 3] = ano_1
V1[3:10, 27] = ano_2
V1[2:6, 5] = hvs
V1[1, 0] = grid
"""
for iteration in range(0, max_iter):
    for i in range(1, z_length-1, step_z):
        for k in range (0, r_length-18, step_r):
                if (k==0):
                    V1[0, i]= 1/6*(V1[0, i+1] + V1[0, i-1] + 4*V1[1, i])
                else:
                    V1[k, i] = 0.25 * (V1[k][i+1] + V1[k][i-1] + V1[k+1][i] + V1[k-1][i])\
                        + (1/(8*k))*(V1[k+1, i]-V1[k-1, i])




E_field = np.gradient(V1) 
E_r = -1*E_field[0]
E_z = -1*E_field[1]
   

#heat map
plt.title("potential of firing unit")
plt.contourf(z, r, V1, colorinterpolation, cmap=colourMap)
plt.xlabel("r")
plt.ylabel("z")

# Set Colorbar
plt.colorbar()


#3d plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(z, r, V1 ,cmap="plasma")
ax.set_xlabel("r")
ax.set_ylabel("z")
ax.set_zlabel("V")
ax.set_title("potential of firing unit")





plt.show()


print("")