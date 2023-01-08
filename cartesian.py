# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 15:02:51 2022
Week 1: mphys project: electron beam dynamics
for week1 code will attempt to 
1. solve Laplace's equation  in 2d cartesian for square box`
2. // for electrode postioned in centre of box
3. solve Laplace's equation in 2d polars f(r,z) (symmetry around theta)

@author: George Smith
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x_length = 10
y_length = 10

step = 1

v_top = 2
v_bottom = 2
v_right = 0
v_left = 0

max_iter = 500

v_guess =1

colorinterpolation = 50
colourMap = plt.cm.jet

X, Y = np.meshgrid(np.arange(0, x_length), np.arange(0, y_length))

V = np.empty((x_length, y_length))

V.fill(v_guess)

V[(y_length-1):, :] = v_top
V[:1, :] = v_bottom
V[:, (x_length-1):] = v_right
V[:, :1] = v_left

print("Please wait for a moment")
for iteration in range(0, max_iter):
    for i in range(1, x_length-1, step):
        for j in range(1, y_length-1, step):
            V[i, j] = 0.25 * (V[i+1][j] + V[i-1][j] + V[i][j+1] + V[i][j-1])



plt.title("potential in 2d square")
plt.contourf(X, Y, V, colorinterpolation, cmap=colourMap)
plt.xlabel("x(a.u.)")
plt.ylabel("y(a.u.)")

# Set Colorbar
plt.colorbar(label="<")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, V ,cmap="plasma")
ax.set_xlabel("x(a.u.)")
ax.set_ylabel("y(a.u.)")
ax.set_zlabel("V")
ax.set_title("potential in 2d square")

plt.show()

print("")