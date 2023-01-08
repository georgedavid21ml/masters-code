# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 16:02:10 2022

@author: George Smith
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

r_length = 11
z_length = 11

step = 1

v_top = 1
v_bottom = 1
v_right = 2
v_left = 2

max_iter = 500

v_guess =1

colorinterpolation = 50
colourMap = plt.cm.jet

z, r = np.meshgrid(np.arange(0, z_length), np.arange(-r_length/2, r_length/2))

V1 = np.empty((z_length, r_length))

V1.fill(v_guess)

V1[(r_length-1):, :] = v_top
V1[:1, :] = v_bottom
V1[:, (z_length-1):] = v_right
V1[:, :1] = v_left

for iteration in range(0, max_iter):
    for i in range(1, z_length-1, step):
        for k in range(1, r_length-1, step):
            if (k == 5):
                V1[i, k]= V1[i-1,k]
            else:
                V1[i, k] = 0.25 * (V1[i+1][k] + V1[i-1][k] + V1[i][k+1] + V1[i][k-1]) + (V1[i, k+1]-V1[i,k-1])/(8*k)
            
plt.title("potential in 2d square")
plt.contourf(z, r, V1, colorinterpolation, cmap=colourMap)
plt.xlabel("z")
plt.ylabel("r")

# Set Colorbar
plt.colorbar()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(z, r, V1 ,cmap="plasma")
ax.set_xlabel("z")
ax.set_ylabel("r")
ax.set_zlabel("V")
ax.set_title("potential in 2d square")

plt.show()

print("")