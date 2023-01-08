# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 13:09:47 2022

@author: George Smith
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


r_length = 46
z_length = 46

step_r = 1
step_z = 1

v_top = 0
v_bottom = 0
v_right = 2
v_left = 1

max_iter = 3000

v_guess =1

colorinterpolation = 50
colourMap = plt.cm.jet

z, r = np.meshgrid(np.linspace(0, r_length -1, r_length), \
                   np.linspace(0, (z_length-1) , z_length))

V1 = np.empty((r_length, z_length))

V1.fill(v_guess)

V1[:, (r_length-1)] = v_right
#V1[:1, :] = v_bottom
#V1[(z_length-1):, :] = v_right
V1[:1, 0] = v_left


for iteration in range(0, max_iter):
    for i in range(1, z_length-1, step_z):
        for k in range (0, r_length-1, step_r):
            if (k==0):
                V1[0, i]= 1/6*(V1[0, i+1] + V1[0, i-1] + 4*V1[1, i])
            else:
                V1[k, i] = 0.25 * (V1[k][i+1] + V1[k][i-1] + V1[k+1][i] + V1[k-1][i])\
                    + (1/(8*k))*(V1[k+1, i]-V1[k-1, i])




E_field = np.gradient(V1) 
E_r = -1*E_field[0]
E_z = -1*E_field[1]
   
"""
#heat map
plt.title("potential in 2d cylindrical coords")
plt.contourf(z, r, V1, colorinterpolation, cmap=colourMap)
plt.xlabel("z(a.u.)")
plt.ylabel("r(a.u.)")
#plt.yticks(np.arange(0, 20, 5))
# Set Colorbar
plt.colorbar()


#3d plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(r, z, V1 ,cmap="plasma")
ax.set_xlabel("r(a.u.)")
ax.set_ylabel("z(a.u.)")
ax.set_zlabel("V")
ax.set_title("potential in 2d cylindrical coords")
"""
"""

fig_2 = plt.figure()
ax_2 = fig_2.add_subplot(111)

color = 2 * np.log(np.hypot(E_r, E_z))
ax_2.streamplot(z, r, E_z, E_r, color=color, linewidth=1, cmap=plt.cm.inferno,
              density=2, arrowstyle='->', arrowsize=1.5)

ax_2.set_title("Electric field")
ax_2.set_xlabel("z")
ax_2.set_ylabel("r")


"""
centre = V1[0,:]
plt.plot(z[0,:], centre)


plt.show()



print("")