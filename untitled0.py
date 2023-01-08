"""
Created on Thu Oct 13 13:09:47 2022

@author: George Smith

firing unit has folllwing dimesnions:
radius = 10mm
axial length(z) = 28mm

cathode(s) at:
1. r=0, z=0

andode(s) at:
1. r=0.9-3.8, z=3.35-3.45
2. r=2.55-31.75, z=28.25-28.775

high voltage shield:
1. r=1.575-2.675, z=5.125-5.875
2. r=1.575-29.35, z=6.225-6.975

grid:
r=0.5-2.6, z=-0.475-0.025
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Circle
import sys


grid_size = 150

r_length = 23.125
z_length = 23.125

step_r = 1
step_z = 1

v_top = 0
v_right = 100
v_left = 0

cat_1 =2
ano_1 =2
ano_2 =2
hvs =2
grid =2

max_iter = 10000

v_guess =30

colorinterpolation = 50
colourMap = plt.cm.jet

z, r = np.meshgrid(np.linspace(0, z_length, grid_size), \
                   np.linspace(0, (r_length) , grid_size))

V1 = np.empty((grid_size, grid_size))

V1.fill(v_guess)


V1[(grid_size-1):, :] = v_top
V1[:, (grid_size-1):] = v_right
V1[:, :1] = v_left


"""
location by 2d array

loc = [[z_start, z_end], [r_start, r_end]]
"""




for iteration in range(0, max_iter):
    for i in range(1, grid_size-1, step_z):
        for k in range (0, grid_size-1, step_r):
            if (k==0):
                   V1[0, i]= 1/6*(V1[0, i+1] + V1[0, i-1]) + 2/3*V1[1, i]
            else:
                V1[k, i] = 0.25 * (V1[k][i+1] + V1[k][i-1] + V1[k+1][i] + V1[k-1][i])\
                        + (1/(8*k))*(V1[k+1, i]-V1[k-1, i])


def gradient_func(array, dimension):
#f(x)' = lim(step->0) (f(x+step)-f(x))/step
#where f(x) is our potential
    h = dimension/ (grid_size-1)
    grad = np.empty(len(array))
    for i in range(0, len(array)-1, 1):
        grad[i] = (array[i+1]-array[i])/h
        
    
    return grad

E_field = np.gradient(V1) 
E_r = -1*E_field[0]
E_z = -1*E_field[1]
   
"""
#heat map
plt.title("potential of firing unit")
plt.contourf(r, z, V1, colorinterpolation, cmap=colourMap)
plt.xlabel("r")
plt.ylabel("z")

# Set Colorbar
plt.colorbar()


#3d plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(r, z, V1 ,cmap="plasma")
ax.set_xlabel("r")
ax.set_ylabel("z")
ax.set_zlabel("V")
ax.set_title("potential of firing unit")


fig_2 = plt.figure()
ax_2 = fig_2.add_subplot(111)

color = 2 * np.log(np.hypot(E_r, E_z))
ax_2.streamplot(z, r, E_z, E_r, color=color, linewidth=1, cmap=plt.cm.inferno,
              density=2, arrowstyle='->', arrowsize=1)

ax_2.set_title("Electric field")
ax_2.set_xlabel("z")
ax_2.set_ylabel("r")


plt.show()
"""


e_z_test =-1* gradient_func(V1[0, :], z_length)

print(np.mean(e_z_test[:grid_size-2]))

plt.scatter(z[0, :grid_size-2], e_z_test[:grid_size-2])
plt.xlabel("z")
plt.ylabel("E_z")
plt.title("E_z vs z (python model)")

print("")
"""
for i in range(0, len(r), 1):
    for k in range(0, len(z), 1):
        new_row = [r[i, k], z[i, k], E_r[i, k], E_z[i, k]]
        data = np.vstack((data, new_row))
        
np.savetxt("field_map.txt", data)
"""