# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 15:02:51 2022
Week 1: mphys project: electron beam dynamics
for week1 code will attempt to 
1. solve Laplace's equation  in 2d cartesian for square box
2. // for electrode postioned in centre of box
3. solve Laplace's equation in 2d polars f(r,z) (symmetry around theta)

@author: George Smith
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x_length = 100
y_length = 100
z_length = 46
r = 46
c_x = x_length // 2
c_y = y_length // 2


step = 1

v_top = 1
v_bottom = 1
v_right = 2
v_left = 2

max_iter = 2000

v_guess = 100

colorinterpolation = 50
colourMap = plt.cm.jet

X, Y, Z= np.meshgrid(np.arange(0, x_length), np.arange(0, y_length), np.arange(0, y_length))

V2 = np.empty((x_length, y_length, z_length))

V2.fill(0)

def dist(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            
def make_circle(array, cx, cy, r, value):
    x_node = []
    y_node = []
    for x in range(cx - r, cx + r):
        for y in range(cy - r, cy + r):
            if dist(cx, cy, x, y) <= r:
                array[x, y] = value
                x_node.append(x)
                y_node.append(y)
            else:
                array[x,y] =0
    nodes = np.array([x_node, y_node])
    return nodes
             
        
for k in range(0, z_length, step):
    test = V2[:, :, k]
    if k == (z_length-1):
        nodes = make_circle(test, c_x, c_y, r, 2)
    
    else:
        make_circle(test, c_x, c_y, r, 1)



for iteration in range(0, max_iter):
    if (iteration % 100 )==0:
        print(100*iteration/max_iter, "%")
    for x in range(1, x_length-1):
        for y in range(1, y_length-1):
            for z in range(1, z_length-1):
                if (V2[x, y, z] == 0):
                    pass
                else:
                    V2[x, y, z]= 1/6 * (V2[x+1][y][z] + V2[x][y+1][z] + V2[x][y][z+1] + V2[x-1][y][z]\
                                        +V2[x][y-1][z] + V2[x][y][z-1])

data_2 = np.array([1,
1.00765,
1.01539,
1.02327,
1.03135,
1.03969,
1.04835,
1.05739,
1.06686,
1.07682,
1.08733,
1.09843,
1.11018,
1.12262,
1.13581,
1.1498,
1.16462,
1.18032,
1.19692,
1.21448,
1.23302,
1.25255,
1.27312,
1.29473,
1.31739,
1.34112,
1.36591,
1.39177,
1.41869,
1.44664,
1.47561,
1.50557,
1.53648,
1.56832,
1.60102,
1.63455,
1.66884,
1.70383,
1.73945,
1.77563,
1.8123,
1.84937,
1.88676,
1.92439,
1.96216,
2
])

v_central = V2[50, 50, :]
plt.plot(np.linspace(0, z_length, z_length), v_central, label ="cartesian", linestyle="--")
plt.plot(np.linspace(0, 46, 46), data_2, label="2d polar")
plt.legend(title="model")
plt.title("central potential of cylinder")
plt.xlabel("z")
plt.ylabel("voltage")
plt.show()