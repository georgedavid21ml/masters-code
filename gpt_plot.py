# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 17:34:17 2022

@author: George Smith
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Circle
import sys
import pandas as pd

df_95 = pd.read_csv("100-95-0_data.txt", sep='  ', lineterminator='\r')
data_95 = df_95.to_numpy()

df_95_ape = pd.read_csv("100-95-0.txt", sep='  ', lineterminator='\r')
data_95_ape = df_95_ape.to_numpy()

df_96 = pd.read_csv("100-96-0_data.txt", sep='  ', lineterminator='\r')
data_96 = df_96.to_numpy()

df_97 = pd.read_csv("100-97-0_data.txt", sep='  ', lineterminator='\r')
data_97 = df_97.to_numpy()

df_98 = pd.read_csv("100-98-0_data.txt", sep='  ', lineterminator='\r')
data_98 = df_98.to_numpy()

df_99 = pd.read_csv("100-99-0_data.txt", sep='  ', lineterminator='\r')
data_99 = df_99.to_numpy()


df_95_nps_100000 = pd.read_csv("100-95-0(nps=10e5).txt", sep='  ', lineterminator='\r')
data_95_nps_100000 = df_95_nps_100000.to_numpy()

df_95_nps_20000 = pd.read_csv("100-95-0(nps=2.10e4).txt", sep='  ', lineterminator='\r')
data_95_nps_20000 = df_95_nps_20000.to_numpy()

df_95_r_50 = pd.read_csv("100-95-0(r=50).txt", sep='  ', lineterminator='\r')
data_95_r_50 = df_95_r_50.to_numpy()

df_95_r_75 = pd.read_csv("100-95-0(r=75).txt", sep='  ', lineterminator='\r')
data_95_r_75 = df_95_r_75.to_numpy()

df_95_100Q = pd.read_csv("100-95-0(100xQ).txt", sep='  ', lineterminator='\r')
data_95_100Q = df_95_100Q.to_numpy()

df_95_500Q = pd.read_csv("100-95-0(500xQ).txt", sep='  ', lineterminator='\r')
data_95_500Q = df_95_500Q.to_numpy()

df_95_sc_off = pd.read_csv("100-95-0(field_only).txt", sep='  ', lineterminator='\r')
data_95_sc_off = df_95_sc_off.to_numpy()

df_97_50r = pd.read_csv("100-97-0(r=50).txt", sep='  ', lineterminator='\r')
data_97_50r = df_97_50r.to_numpy()

df_99_50r = pd.read_csv("100-99-0(r=50).txt", sep='  ', lineterminator='\r')
data_99_50r = df_99_50r.to_numpy()

df_wl_200 = pd.read_csv("100-95-0(wl=200).txt", sep='  ', lineterminator='\r')
data_wl_200 = df_wl_200.to_numpy()

df_wl_100 = pd.read_csv("100-95-0(wl=100).txt", sep='  ', lineterminator='\r')
data_wl_100 = df_wl_100.to_numpy()

df_chris_on = pd.read_csv("chris(sc=on).txt", sep='  ', lineterminator='\r')
data_chris_on = df_chris_on.to_numpy()

df_chris_off = pd.read_csv("chris(sc=off).txt", sep='  ', lineterminator='\r')
data_chris_off = df_chris_off.to_numpy()

df_sc_on = pd.read_csv("space_charge(on_1pC).txt", sep='  ', lineterminator='\r')
data_sc_on = df_sc_on.to_numpy()

df_sc_off = pd.read_csv("space_charge(off_1pC).txt", sep='  ', lineterminator='\r')
data_sc_off = df_sc_off.to_numpy()

df_sc_2doff = pd.read_csv("space_charge_2d(off_1pC).txt", sep='  ', lineterminator='\r')
data_sc_2doff = df_sc_2doff.to_numpy()

df_sc_2don = pd.read_csv("space_charge_2d(on_1pC).txt", sep='  ', lineterminator='\r')
data_sc_2don = df_sc_2don.to_numpy()

mm_fac = 10**3

#1. 95-99kV bunch length/size
"""
plt.plot(mm_fac*data_95[:, 3], mm_fac*data_95[:, 1], label="5KV")
#plt.plot(mm_fac*data_96[:, 3], mm_fac*data_96[:, 1], label="4KV")
plt.plot(mm_fac*data_97[:, 3], mm_fac*data_97[:, 1], label="3KV")
#plt.plot(mm_fac*data_98[:, 3], mm_fac*data_98[:, 1], label="2KV")
plt.plot(mm_fac*data_99[:, 3], mm_fac*data_99[:, 1], label="1KV")
plt.legend(title="1st anode voltage")
plt.xlabel("z(mm)")
plt.ylabel("dx(mm)")
plt.axvline(x=5, linestyle="--", color="black")
plt.xlim(0, 30)
plt.ylim(0, 0.7)
plt.title("trans-bunch size vs z")
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.show()

plt.plot(mm_fac*data_95[:, 3], mm_fac*data_95[:, 2], label="5KV")
#plt.plot(mm_fac*data_96[:, 3], mm_fac*data_96[:, 2], label="4KV")
plt.plot(mm_fac*data_97[:, 3],mm_fac* data_97[:, 2], label="3KV")
#plt.plot(mm_fac*data_98[:, 3], mm_fac*data_98[:, 2], label="2KV")
plt.plot(mm_fac*data_99[:, 3], mm_fac*data_99[:, 2], label="1KV")
plt.legend(title="1st anode voltage")
plt.xlabel("z(mm)")
plt.ylabel("dz(mm)")
plt.xlim(0, 30)
plt.title("long-bunch length vs z")
plt.show()
"""
#2.95-99 long/trans emittance
"""
plt.plot(data_95[:, 0], data_95[:, 5], label="5KV")
#plt.plot(mm_fac*data_96[:, 3], mm_fac*data_96[:, 2], label="4KV")
plt.plot(data_97[:, 0], data_97[:, 5], label="3KV")
#plt.plot(mm_fac*data_98[:, 3], mm_fac*data_98[:, 2], label="2KV")
plt.plot(data_99[:, 0], data_99[:, 5], label="1KV")
plt.legend(title="1st anode voltage")
plt.xlabel("time(s)")
plt.ylabel("longitudinal emittance(Js)")
plt.xlim(0, 4*10**-10)
plt.title("z-emi vs time")
plt.show()

plt.plot(data_95[:, 0], data_95[:, 4], label="5KV")
#plt.plot(mm_fac*data_96[:, 3], mm_fac*data_96[:, 2], label="4KV")
plt.plot(data_97[:, 0], data_97[:, 4], label="3KV")
#plt.plot(mm_fac*data_98[:, 3], mm_fac*data_98[:, 2], label="2KV")
plt.plot(data_99[:, 0], data_99[:, 4], label="1KV")
plt.legend(title="1st anode voltage")
plt.xlabel("time(s)")
plt.ylabel("transverse emittance(m.rad)")
plt.xlim(0, 4*10**-10)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
plt.title("x-emi vs time")
plt.show()
"""
#3. bunch length/size for 95kV for varying no of electrons
"""
plt.plot(mm_fac*data_95_nps_100000[:, 3], mm_fac*data_95_nps_100000[:, 1], label="100,000")
plt.plot(mm_fac*data_95[:, 3], mm_fac*data_95[:, 1], label="6242")
plt.xlabel("z(mm)")
plt.ylabel("dx(mm)")
plt.xlim(0, 30)
plt.ylim(0,0.3)
plt.title("trans-bunch size vs z")
plt.legend(title="no of electrons")
plt.show()

plt.plot(mm_fac*data_95_nps_100000[:, 3], mm_fac*data_95_nps_100000[:, 2], label="100,000")
plt.plot(mm_fac*data_95[:, 3], mm_fac*data_95[:, 2], label="6242")
plt.xlabel("z(mm)")
plt.ylabel("dz(mm)")
plt.xlim(0, 30)
plt.title("long-bunch size vs z")
plt.legend(title="no of electrons")
plt.show()
"""
#4. x/z emittance 95kv varying no of electrons
"""
plt.plot(data_95_nps_100000[:, 0], data_95_nps_100000[:, 5], label="100,000")
plt.plot(data_95[:, 0], data_95[:, 5], label ="6242")
plt.legend(title="no of electrons")
plt.xlabel("time(s)")
plt.ylabel("longitudinal emittance(Js)")
plt.xlim(0, 4*10**-10)
plt.ticklabel_format(style='sci', axis='y', scilimits=(-8, -8))
plt.title("z-emi vs time")
plt.show()

plt.plot(data_95_nps_100000[:, 0], data_95_nps_100000[:, 4], label="100,000")
plt.plot(data_95[:, 0], data_95[:, 4], label ="6242")
plt.legend(title="no of electrons")
plt.xlabel("time(s)")
plt.ylabel("transverse emittance(mrad)")
plt.xlim(0, 4*10**-10)
plt.ticklabel_format(style='sci', axis='y', scilimits=(-6, -6))
plt.title("x-emi vs time")
plt.show()
"""

#5. bunch length/size varying radius 50,75,100
"""
plt.plot(mm_fac*data_95_r_50[:, 3], mm_fac*data_95_r_50[:, 1], label="50")
plt.plot(mm_fac*data_95_r_75[:, 3], mm_fac*data_95_r_75[:, 1], label="75")
plt.plot(mm_fac*data_95[:, 3], mm_fac*data_95[:, 1], label="100")
plt.xlabel("z(mm)")
plt.ylabel("dx(mm)")
plt.xlim(0, 30)
plt.ylim(0, 0.3)
plt.title("trans-bunch size vs z")
plt.legend(title="radius(um)")
plt.show()

plt.plot(mm_fac*data_95_r_50[:, 3], mm_fac*data_95_r_50[:, 2], label="50")
plt.plot(mm_fac*data_95_r_75[:, 3], mm_fac*data_95_r_75[:, 2], label="75")
plt.plot(mm_fac*data_95[:, 3], mm_fac*data_95[:, 2], label="100")
plt.xlabel("z(mm)")
plt.ylabel("dz(mm)")
plt.xlim(0, 30)
plt.title("long-bunch size vs z")
plt.legend(title="radius(um)")
plt.show()
"""
# x/z emittance 95kV varying radius 50,75,100
"""
plt.plot(data_95_r_50[:, 0], data_95_r_50[:, 5], label="50")
plt.plot(data_95_r_75[:, 0], data_95_r_75[:, 5], label="75")
plt.plot(data_95[:, 0], data_95[:, 5], label ="100")
plt.legend(title="radius(um)")
plt.xlabel("time(s)")
plt.ylabel("longitudinal emittance(Js)")
plt.xlim(0, 4*10**-10)
plt.ticklabel_format(style='sci', axis='y', scilimits=(-8, -8))
plt.title("z-emi vs time")
plt.show()

plt.plot(data_95_r_50[:, 0], data_95_r_50[:, 4], label="50")
plt.plot(data_95_r_75[:, 0], data_95_r_75[:, 4], label="75")
plt.plot(data_95[:, 0], data_95[:, 4], label ="100")
plt.legend(title="radius(um)")
plt.xlabel("time(s)")
plt.ylabel("transverse emittance(mrad)")
plt.xlim(0, 4*10**-10)
plt.ticklabel_format(style='sci', axis='y', scilimits=(-6, -6))
plt.title("x-emi vs time")
plt.show()
"""

#x/z size length varying charge
"""
plt.plot(mm_fac*data_95[:, 3], mm_fac*data_95[:, 1], label="1e-15")
plt.plot(mm_fac*data_95_100Q[:, 3], mm_fac*data_95_100Q[:, 1], label="1e-13")
plt.plot(mm_fac*data_95_500Q[:, 3], mm_fac*data_95_500Q[:, 1], label="5e-13")
plt.xlabel("z(mm)")
plt.ylabel("dx(mm)")
plt.xlim(0, 30)
plt.ylim(0, 0.3)
plt.title("trans-bunch size vs z")
plt.legend(title="charge C")
plt.show()

plt.plot(mm_fac*data_95[:, 3], mm_fac*data_95[:, 2], label="1e-15")
plt.plot(mm_fac*data_95_100Q[:, 3], mm_fac*data_95_100Q[:, 2], label="1e-13")
plt.plot(mm_fac*data_95_500Q[:, 3], mm_fac*data_95_500Q[:, 2], label="5e-13")
plt.xlabel("z(mm)")
plt.ylabel("dz(mm)")
plt.xlim(0, 30)
plt.title("long-bunch size vs z")
plt.legend(title="charge C")
plt.show()
"""
#x/z emittance varying charge
"""
plt.plot(data_95[:, 0], data_95[:, 5], label ="1e-15")
plt.plot(data_95_100Q[:, 0], data_95_100Q[:, 5], label="1e-13")
plt.plot(data_95_500Q[:, 0], data_95_500Q[:, 5], label="5e-13")
plt.legend(title="charge C")
plt.xlabel("time(s)")
plt.ylabel("longitudinal emittance(Js)")
plt.xlim(0, 3.9*10**-10)
plt.ticklabel_format(style='sci', axis='y', scilimits=(-8, -8))
plt.title("z-emi vs time")
plt.show()

plt.plot(data_95[:, 0], data_95[:, 4], label ="1e-15")
plt.plot(data_95_100Q[:, 0], data_95_100Q[:, 4], label="1e-13")
plt.plot(data_95_500Q[:, 0], data_95_500Q[:, 4], label="5e-13")
plt.legend(title="charge C")
plt.xlabel("time(s)")
plt.ylabel("transverse emittance(mrad)")
plt.xlim(0, 4*10**-10)
plt.ticklabel_format(style='sci', axis='y', scilimits=(-6, -6))
plt.title("x-emi vs time")
plt.show()
"""
#x/z sizes varying space charge
"""
plt.plot(mm_fac*data_95[:, 3], mm_fac*data_95[:, 1], label="on")
plt.plot(mm_fac*data_95_sc_off[:, 3], mm_fac*data_95_sc_off[:, 1],'.',label="off")
plt.xlabel("z(mm)")
plt.ylabel("dx(mm)")
plt.xlim(0, 30)
plt.ylim(0, 0.3)
plt.title("trans-bunch size vs z")
plt.legend(title="space charge effects")
plt.show()

plt.plot(mm_fac*data_95[:, 3], mm_fac*data_95[:, 2], label="on")
plt.plot(mm_fac*data_95_sc_off[:, 3], mm_fac*data_95_sc_off[:, 2], '.',label="off")
plt.xlabel("z(mm)")
plt.ylabel("dz(mm)")
plt.xlim(0, 30)
plt.title("long-bunch size vs z")
plt.legend(title="space charge effects")
plt.show()
"""
# x/z emittance varying space charge
"""
plt.plot(data_95[:, 0], data_95[:, 5], label ="on")
plt.plot(data_95_sc_off[:, 0], data_95_sc_off[:, 5], '.', label="off", )
plt.legend(title="space charge effects")
plt.xlabel("time(s)")
plt.ylabel("longitudinal emittance(Js)")
plt.xlim(0, 3.9*10**-10)
plt.ticklabel_format(style='sci', axis='y', scilimits=(-8, -8))
plt.title("z-emi vs time")
plt.show()

plt.plot(data_95[:, 0], data_95[:, 4], label ="on")
plt.plot(data_95_sc_off[:, 0], data_95_sc_off[:, 4], '.' ,label="off")
plt.legend(title="space charge effects")
plt.xlabel("time(s)")
plt.ylabel("transverse emittance(mrad)")
plt.xlim(0, 4*10**-10)
plt.ticklabel_format(style='sci', axis='y', scilimits=(-6, -6))
plt.title("x-emi vs time")
plt.show()
"""
# varying 1st anode at r=50 x/z sizes

plt.plot(mm_fac*data_95_r_50[:, 3], mm_fac*data_95_r_50[:, 1], label="5KV")
plt.plot(mm_fac*data_97_50r[:, 3], mm_fac*data_97_50r[:, 1], label="3KV")
plt.plot(mm_fac*data_99_50r[:, 3], mm_fac*data_99_50r[:, 1], label="1KV")
plt.xlabel("z(mm)")
plt.ylabel("dx(mm)")
plt.xlim(0, 30)
plt.ylim(0, 0.25)
plt.title("trans-bunch size vs z(r=50)")
plt.legend(title="1st anode voltage")
plt.show()

plt.plot(mm_fac*data_95_r_50[:, 3], mm_fac*data_95_r_50[:, 2], label="5KV")
plt.plot(mm_fac*data_97_50r[:, 3], mm_fac*data_97_50r[:, 2], label="3KV")
plt.plot(mm_fac*data_99_50r[:, 3], mm_fac*data_99_50r[:, 2], label="1KV")
plt.xlabel("z(mm)")
plt.ylabel("dz(mm)")
plt.xlim(0, 30)
plt.title("long-bunch size vs z(r=50)")
plt.legend(title="1st anode voltage")
plt.show()

#varying 1st anode r=50 x/z emittance
"""
plt.plot(data_95_r_50[:, 0], data_95_r_50[:, 5], label ="5KV")
plt.plot(data_97_50r[:, 0], data_97_50r[:, 5], label="3KV", )
plt.plot(data_99_50r[:, 0], data_99_50r[:, 5], label="1KV", )
plt.legend(title="1st anode voltage")
plt.xlabel("time(s)")
plt.ylabel("longitudinal emittance(Js)")
plt.xlim(0, 3.9*10**-10)
plt.ticklabel_format(style='sci', axis='y', scilimits=(-8, -8))
plt.title("z-emi vs time(r=50)")
plt.show()

plt.plot(data_95_r_50[:, 0], data_95_r_50[:, 4], label ="5KV")
plt.plot(data_97_50r[:, 0], data_97_50r[:, 4], label="3KV")
plt.plot(data_99_50r[:, 0], data_99_50r[:, 4], label="1KV")
plt.legend(title="1st anode voltage")
plt.xlabel("time(s)")
plt.ylabel("transverse emittance(mrad)")
plt.xlim(0, 4*10**-10)
plt.ticklabel_format(style='sci', axis='y', scilimits=(-6, -6))
plt.title("x-emi vs time(r=50)")
plt.show()
"""
#x/z size varying wavelength
"""
plt.plot(mm_fac*data_95[:, 3], mm_fac*data_95[:, 1], label="400")
plt.plot(mm_fac*data_wl_200[:, 3], mm_fac*data_wl_200[:, 1], label="200")
plt.plot(mm_fac*data_wl_100[:, 3], mm_fac*data_wl_100[:, 1], label="100")
plt.xlabel("z(mm)")
plt.ylabel("dx(mm)")
plt.xlim(0, 30)
plt.ylim(0, 0.25)
plt.title("trans-bunch size vs z")
plt.legend(title="wavelength nm")
plt.show()

plt.plot(mm_fac*data_95[:, 3], mm_fac*data_95[:, 2], label="400")
plt.plot(mm_fac*data_wl_200[:, 3], mm_fac*data_wl_200[:, 2], label="200")
plt.plot(mm_fac*data_wl_100[:, 3], mm_fac*data_wl_100[:, 2], label="100")
plt.xlabel("z(mm)")
plt.ylabel("dz(mm)")
plt.xlim(0, 30)
plt.title("long-bunch size vs z")
plt.legend(title="wavelength nm")
plt.show()
"""
#x/z emi varying wavelength
"""
plt.plot(data_95[:, 0], data_95[:, 5], label ="400")
plt.plot(data_wl_200[:, 0], data_wl_200[:, 5], label="200", )
plt.plot(data_wl_100[:, 0], data_wl_100[:, 5], label="100", )
plt.legend(title="wavelength nm")
plt.xlabel("time(s)")
plt.ylabel("longitudinal emittance(Js)")
plt.xlim(0, 3.9*10**-10)
plt.ticklabel_format(style='sci', axis='y', scilimits=(-8, -8))
plt.title("z-emi vs time")
plt.show()

plt.plot(data_95[:, 0], data_95[:, 4], label ="400")
plt.plot(data_wl_200[:, 0], data_wl_200[:, 4], label="200")
plt.plot(data_wl_100[:, 0], data_wl_100[:, 4], label="100")
plt.legend(title="wavelength nm")
plt.xlabel("time(s)")
plt.ylabel("transverse emittance(mrad)")
plt.xlim(0, 4*10**-10)
plt.ticklabel_format(style='sci', axis='y', scilimits=(-6, -6))
plt.title("x-emi vs time")
plt.show()
"""

#chris data \w sc =on/off
"""
plt.plot(mm_fac*data_chris_on[:, 3], mm_fac*data_chris_on[:, 1], label="on")
plt.plot(mm_fac*data_chris_off[:, 3], mm_fac*data_chris_off[:, 1], label="off")
plt.xlabel("z(mm)")
plt.ylabel("dx(mm)")
plt.xlim(0, 30)
plt.title("trans-bunch size vs z")
plt.legend(title="space charge")
plt.show()

plt.plot(mm_fac*data_chris_on[:, 3], mm_fac*data_chris_on[:, 2], label="on")
plt.plot(mm_fac*data_chris_off[:, 3], mm_fac*data_chris_off[:, 2], label="off")
plt.xlabel("z(mm)")
plt.ylabel("dz(mm)")
plt.xlim(0, 30)
plt.title("long-bunch size vs z")
plt.legend(title="space charge")
plt.show()
"""

#x/z sizes varyign sc and charge
"""
plt.plot(mm_fac*data_sc_on[:, 3], mm_fac*data_sc_on[:, 1], label="on:1pC")
plt.plot(mm_fac*data_sc_off[:, 3], mm_fac*data_sc_off[:, 1], label="off:1pC")
#plt.plot(mm_fac*data_95[:, 3], mm_fac*data_95[:, 1], label="on:1fC")
#plt.plot(mm_fac*data_95_sc_off[:, 3], mm_fac*data_95_sc_off[:, 1],'.',label="off:1fC")
plt.xlabel("z(mm)")
plt.ylabel("dx(mm)")
plt.xlim(0, 30)
plt.ylim(0, 0.4)
plt.title("trans-bunch size vs z")
plt.legend(title="space charge:Q")
plt.show()

plt.plot(mm_fac*data_sc_on[:, 3], mm_fac*data_sc_on[:, 2], label="on:1pC")
plt.plot(mm_fac*data_sc_off[:, 3], mm_fac*data_sc_off[:, 2], label="off:1pC")
#plt.plot(mm_fac*data_95[:, 3], mm_fac*data_95[:, 2], label="on:1fC")
#plt.plot(mm_fac*data_95_sc_off[:, 3], mm_fac*data_95_sc_off[:, 2],'.',label="off:1fC")
plt.xlabel("z(mm)")
plt.ylabel("dz(mm)")
plt.xlim(0, 30)
plt.title("long-bunch size vs z")
plt.legend(title="space charge:Q")
plt.show()
"""
#z/x size 2d cirlce algorithm
"""
plt.plot(mm_fac*data_sc_2don[:, 3], mm_fac*data_sc_2don[:, 1], label="on:1pC")
plt.plot(mm_fac*data_sc_2doff[:, 3], mm_fac*data_sc_2doff[:, 1], label="off:1pC")
#plt.plot(mm_fac*data_95[:, 3], mm_fac*data_95[:, 1], label="on:1fC")
#plt.plot(mm_fac*data_95_sc_off[:, 3], mm_fac*data_95_sc_off[:, 1],'.',label="off:1fC")
plt.xlabel("z(mm)")
plt.ylabel("dx(mm)")
plt.xlim(0, 30)
plt.ylim(0, 0.4)
plt.title("trans-bunch size vs z")
plt.legend(title="space charge:Q")
plt.show()

plt.plot(mm_fac*data_sc_2don[:, 3], mm_fac*data_sc_2don[:, 2], label="on:1pC")
plt.plot(mm_fac*data_sc_2doff[:, 3], mm_fac*data_sc_2doff[:, 2], label="off:1pC")
#plt.plot(mm_fac*data_95[:, 3], mm_fac*data_95[:, 2], label="on:1fC")
#plt.plot(mm_fac*data_95_sc_off[:, 3], mm_fac*data_95_sc_off[:, 2],'.',label="off:1fC")
plt.xlabel("z(mm)")
plt.ylabel("dz(mm)")
plt.xlim(0, 30)
plt.title("long-bunch size vs z")
plt.legend(title="space charge:Q")
plt.show()
"""
"""
plt.plot(mm_fac*data_sc_2don[:, 3], mm_fac*data_sc_2don[:, 1], label="on:1pC")
plt.plot(mm_fac*data_sc_2doff[:, 3], mm_fac*data_sc_2doff[:, 1], label="off:1pC")
#plt.plot(mm_fac*data_95[:, 3], mm_fac*data_95[:, 1], label="on:1fC")
#plt.plot(mm_fac*data_95_sc_off[:, 3], mm_fac*data_95_sc_off[:, 1],'.',label="off:1fC")
plt.xlabel("z(mm)")
plt.ylabel("dx(mm)")
plt.xlim(0, 30)
plt.ylim(0, 0.4)
plt.title("trans-bunch size vs z")
plt.legend(title="space charge:Q")
plt.show()

plt.plot(mm_fac*data_sc_2don[:, 3], mm_fac*data_sc_2don[:, 2], label="on:1pC")
plt.plot(mm_fac*data_sc_2doff[:, 3], mm_fac*data_sc_2doff[:, 2], label="off:1pC")
#plt.plot(mm_fac*data_95[:, 3], mm_fac*data_95[:, 2], label="on:1fC")
#plt.plot(mm_fac*data_95_sc_off[:, 3], mm_fac*data_95_sc_off[:, 2],'.',label="off:1fC")
plt.xlabel("z(mm)")
plt.ylabel("dz(mm)")
plt.xlim(0, 30)
plt.title("long-bunch size vs z")
plt.legend(title="space charge:Q")
plt.show()
"""