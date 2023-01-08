# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 17:29:22 2022

@author: George Smith
"""

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
import time


start = time.time()

grid_size = 100

r_length = 10
z_length = 49


step = 0.2

v_top = 0
v_right = 0
v_left = 0

cat_1 =2
ano_1 =2
ano_2 =2
hvs =2
grid =2
plate = 2

max_iter = 2000


v_guess =-100

colorinterpolation = 50
colourMap = plt.cm.jet

z, r = np.meshgrid(np.arange(0, z_length, step), \
                   np.arange(0, r_length , step))

    
grid_r = int(r_length/step)
grid_z = int(z_length/step)
    
V1 = np.empty((int(r_length/step), int(z_length/step)))

V1.fill(v_guess)


V1[(grid_r-1):, :] = v_top
V1[:, (grid_z-1):] = v_right
V1[:, :1] = v_left


"""
location by 2d array

loc = [[z_start, z_end], [r_start, r_end]]
extend the size in z to mitigate boundary errors(z'= z + 20)
"""
cat_1_loc =[[20, 20], [0, 0.275]]
ano_1_loc =[[3.825+20,3.925+20],[0.9, 3.8]]
ano_2_loc =[[28.725+20,29.25 + 20],[2.55, 10]]
hvs_loc = [[5.6+20, 6.35+20],[1.575,6]]
grid_loc =[[20,20],[0.5, 2.6]]
plate_loc = [[0.3+20, 2.35+20], [4.575, 4.575+4.625]]








V1[round(cat_1_loc[1][0]*grid_r/r_length):round(cat_1_loc[1][1]*grid_r/r_length)+1, \
   round(cat_1_loc[0][0]*grid_z/z_length):round(cat_1_loc[0][1]*grid_z/z_length)+1] = cat_1

V1[round(ano_1_loc[1][0]*grid_r/r_length):round(ano_1_loc[1][1]*grid_r/r_length), \
   round(ano_1_loc[0][0]*grid_z/z_length):round((ano_1_loc[0][1]*grid_z/z_length))+1] = ano_1
    
V1[round(ano_2_loc[1][0]*grid_r/r_length):round(ano_2_loc[1][1]*grid_r/r_length), \
   round(ano_2_loc[0][0]*grid_z/z_length)-1:round((ano_2_loc[0][1]*grid_z/z_length))] = ano_2
    
V1[round(hvs_loc[1][0]*grid_r/r_length):round(hvs_loc[1][1]*grid_r/r_length), \
   round(hvs_loc[0][0]*grid_z/z_length):round((hvs_loc[0][1]*grid_z/z_length))] = hvs

V1[round(grid_loc[1][0]*grid_r/r_length)+1:round(grid_loc[1][1]*grid_r/r_length), \
   round(grid_loc[0][0]*grid_z/z_length):round((grid_loc[0][1]*grid_z/z_length))+1] = grid

#V1[round(plate_loc[1][0]*grid_size/r_length):round(plate_loc[1][1]*grid_size/r_length), \
  # round(plate_loc[0][0]*grid_size/z_length):round((plate_loc[0][1]*grid_size/z_length))] = plate


def electrode_nodes(array):
    i_nodes = []
    k_nodes = []    
    for i in range(0, grid_r-1, 1):
        for k in range(0, grid_z-1, 1):
            if (array[i][k] == 2):
                i_nodes.append(i)
                k_nodes.append(k)
    nodes = np.array(list(zip(i_nodes, k_nodes)))
    return nodes
                
nodes = electrode_nodes(V1)



#electrode values with their locations
#location formula node = x*grid/X where x is either r or z and X is the radius and axial length

cat_1 = -100
ano_1 = -95
ano_2 =0
hvs = -100
grid =-100
plate = -100

V1[round(cat_1_loc[1][0]*grid_r/r_length):round(cat_1_loc[1][1]*grid_r/r_length)+1, \
   round(cat_1_loc[0][0]*grid_z/z_length):round(cat_1_loc[0][1]*grid_z/z_length)+1] = cat_1

V1[round(ano_1_loc[1][0]*grid_r/r_length):round(ano_1_loc[1][1]*grid_r/r_length), \
   round(ano_1_loc[0][0]*grid_z/z_length):round((ano_1_loc[0][1]*grid_z/z_length))+1] = ano_1
    
V1[round(ano_2_loc[1][0]*grid_r/r_length):round(ano_2_loc[1][1]*grid_r/r_length), \
   round(ano_2_loc[0][0]*grid_z/z_length)-1:round((ano_2_loc[0][1]*grid_z/z_length))] = ano_2
    
V1[round(hvs_loc[1][0]*grid_r/r_length):round(hvs_loc[1][1]*grid_r/r_length), \
   round(hvs_loc[0][0]*grid_z/z_length):round((hvs_loc[0][1]*grid_z/z_length))] = hvs

V1[round(grid_loc[1][0]*grid_r/r_length)+1:round(grid_loc[1][1]*grid_r/r_length), \
   round(grid_loc[0][0]*grid_z/z_length):round((grid_loc[0][1]*grid_z/z_length))+1] = grid


#V1[round(plate_loc[1][0]*grid_size/r_length):round(plate_loc[1][1]*grid_size/r_length), \
 #  round(plate_loc[0][0]*grid_size/z_length):round((plate_loc[0][1]*grid_size/z_length))] = plate





for iteration in range(0, max_iter):
    if(iteration % 100) == 0:    
        print(100*iteration/max_iter, "%")
    for i in range(1, grid_z-1, 1):
        for k in range (0, grid_r-1, 1):
            if [k,i] in nodes.tolist():
                pass
            else:
                if (k==0):
                    V1[0, i]= 1/6*(V1[0, i+1] + V1[0, i-1]) + 2/3*V1[1, i]
                else:
                    V1[k, i] = 0.25 * (V1[k][i+1] + V1[k][i-1] + V1[k+1][i] + V1[k-1][i])\
                        + (step/(8*k))*(V1[k+1, i]-V1[k-1, i])

end = time.time()


def gradient_func(array, dimension):
#f(x)' = lim(step->0) (f(x+step)-f(x))/step
#where f(x) is our potential
    h = dimension/ (grid_size-1)
    grad = np.empty(len(array))
    for i in range(0, len(array)- 1, 1):
        grad[i] = (array[i+1]-array[i])/h
    
    return grad

E_field = np.gradient(V1) 
E_r = -1*E_field[0]/(step)
E_z = -1*E_field[1]/(step)


E_r[0,:] = 0
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

fac_1 = 10**-3
fac_2 = 10**6

data = np.empty((1, 4))
for i in range(101, len(z), 1):
    for k in range(0, 49, 1):
        new_row = [fac_1*r[k, i], fac_1*(z[k, i]-z[0, 101]), fac_2*E_r[k, i], fac_2*E_z[k, i]]
        data = np.vstack((data, new_row))
        
np.savetxt("100-97-0(2).txt", data, delimiter='\t')





#e_z_test =-1* gradient_func(V1[0, :], z_length)

#average = np.mean(e_z_test[61:])

    
plt.scatter(np.linspace(0, 29, len(E_z[0, 101:])), E_z[0, 101:])
plt.xlabel("z")
plt.ylabel("E_z")
plt.title("E_z vs z (python model)")

print("")
