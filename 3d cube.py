# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 12:03:40 2022

@author: George Smith
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


x_length = 11
y_length = 11
z_length = 11

step = 1

v_front = 0
v_back = 0
v_right = 0
v_left = 0
v_top = 2
v_bottom = 2

max_iter = 500

v_guess =0

colorinterpolation = 50
colourMap = plt.cm.jet

X, Y, Z = np.meshgrid(np.arange(0, x_length), np.arange(0, y_length), np.arange(0, z_length))

V = np.empty((x_length, y_length, z_length))

V.fill(v_guess)

#v_front and v_back at V[x, y, 0] and V[x, y, z_length]
V[:, :, :1] = v_front
V[:, :, (z_length-1)] = v_back

#v_left and v_right at V[0, y, z] and V[x_length, y, z]
V[:1, :, :] = v_left
V[(x_length-1), :, :] = v_right

#v_bottom and v_top at V[x, 0, z] and V[x, y_length, z]
V[:, :1, :] = v_bottom
V[:, (y_length-1), :] = v_top


test = V

for iteration in range(0, max_iter):
    for x in range(1, x_length-1):
        for y in range(1, y_length-1):
            for z in range(1, z_length-1):
                V[x, y, z]= 1/6 * (V[x+1][y][z] + V[x][y+1][z] + V[x][y][z+1] + V[x-1][y][z]\
                                   +V[x][y-1][z] + V[x][y][z-1])
         
                    
                    
V_xy = V[:, :, 5]
                    
plt.title("potential in 3d cube xy-plane(z=5)")
plt.contourf(Y[:,:, 5], X[:,:,5], V_xy, colorinterpolation, cmap=colourMap)
plt.xlabel("x")
plt.ylabel("y")

# Set Colorbar
plt.colorbar()
plt.show()
