# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 13:35:01 2017

@author: jeyabala1
"""
 
#!/usr/bin/python3.4.3

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy as np
from pylab import *
import glob
import os

# #f, (ax1,ax2,ax3,ax4) = plt.subplots(1,2,3,4, sharex=True)
# ax1 = plt.subplot2grid((6,1),(0,0), rowspan=2, colspan=1)
# ax2 = plt.subplot2grid((6,1),(3,0), rowspan=2, colspan=1)
# plt.figure(figsize=(12,9), dpi=75)

# subplot(2,1,1)
# x, y, y1 = np.loadtxt('Z:/Bureau/Zeb/CoupTrail/81_2d10x10ht/therm.test', skiprows=1, usecols= (0, 1, 2) , unpack=True)
# plt.plot(x,y, color="blue", linewidth=1.5, linestyle="-", label='center')
# plt.plot(x,y1, color="red", linewidth=1.5, linestyle="-", label='surface')
# plt.xlabel('Time, sec')
# plt.ylabel('Temperature,C')
# plt.title('Cooling Curve & Internal Stress Evolution')
# plt.legend()

# subplot(2,1,2)
# x2, y2 = np.loadtxt('mecaphase.test', skiprows=1, usecols= (0, 3) , unpack=True)
# x3, y3 = np.loadtxt('mecaphase.test', skiprows=1, usecols= (0, 9) , unpack=True)
# plt.plot(x2,y2, color="blue", linewidth=1.5, linestyle="-", label='center')
# plt.plot(x3,y3, color="red", linewidth=1.5, linestyle="-", label='surface')
# # plt.xlim(0.0,60.0)
# plt.xlabel('Time, sec')
# plt.ylabel('axial stress, MPa')
# plt.legend()
# with open('sortie.txt','r+').read() 
# node = data.split('_')[0]
os.chdir('c:/Users/jeyabala1/Documents/Python Scripts/CN1_Aus220')
for file in sorted(glob.glob('*.txt')):
    plt.clf()
    filename = file.split('.')[0]
    plt.figure(figsize=(8,6), dpi=75)
    x1, y1 = loadtxt(filename, skiprows=1, usecols=(0, 4), unpack=True)
    plt.plot(x1, y1, 'o',  color="blue", label='center')
    plt.xlabel('distance, microns')
    plt.ylabel('Stress')
    plt.title('Carburising')
    plt.legend()
    plt.savefig('cn1_stress', dpi=69, format='png')
    plt.show()

# Reading data for fitting
# (xi, yi) = loadtxt('test.dat', skiprows=1, usecols=(0, 1), unpack=True)

# # Removing outlier data
# outlier = (is_outlier(yi))
# x = xi[outlier]
# y = yi[outlier]

# pylab.plot(x, y, 'o', x, line)
# pylab.show()

