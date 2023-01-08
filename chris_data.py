# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 17:37:48 2022

@author: George Smith
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Circle
import sys
import pandas as pd

df = pd.read_csv("100-100-95kV_GPT_map.txt", sep='\t', lineterminator='\r')
chris_data = df.to_numpy()

delta =10**-3*(7.5*10**-5)
python_data =np.array([-1.2822,	
                       -1.25694,	
                       -1.26823,	
                       -1.32162,	
                       -1.41057,	
                       -1.52857,	
                       -1.67046,	
                       -1.83109,	
                       -2.00462,	
                       -2.18506,	
                       -2.36721,	
                       -2.54706,	
                       -2.72176,	
                       -2.88925,	
                       -3.04798,	
                       -3.19675,	
                       -3.33467,	
                       -3.46119,	
                       -3.57606,	
                       -3.67935,	
                       -3.77139,	
                       -3.85272,	
                       -3.92402,	
                       -3.98608,	
                       -4.03971,	
                       -4.08572,	
                       -4.12492,	
                       -4.15803,	
                       -4.18576,	
                       -4.20872,	
                       -4.22747,	
                       -4.24253,	
                       -4.25433,	
                       -4.26327,	
                       -4.26969,	
                       -4.27389,	
                       -4.27616,	
                       -4.27672,	
                       -4.27578,	
                       -4.27354,	
                       -4.27018,	
                       -4.26585,	
                       -4.2607,
                       -4.25488,	
                       -4.24854,	
                       -4.24181,	
                       -4.23482,	
                       -4.22774,	
                       -4.22069,	
                       -4.21384,	
                       -4.20731,	
                       -4.20126,	
                       -4.19582,	
                       -4.19112,	
                       -4.18727,	
                       -4.18437,	
                       -4.18249,	
                       -4.18181])

plt.plot(np.linspace(0, 29, len(chris_data[704:1000, 3])), (10**-6)*chris_data[704:1000, 3])
#plt.plot(np.linspace(0, 29, len(python_data)), python_data)
plt.title("Python central axial field")
plt.xlabel("z(mm)")
plt.ylabel("V(MV/m")
plt.legend(framealpha = 1 ,title =" cat:-100kV \n 1st ano:-95kV \n 2nd ano:0V ", loc="upper right")
plt.show()



