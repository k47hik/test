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
import is_outlier

os.chdir('TiC_180_4')
fig = plt.figure()

for file in sorted(glob.glob('*.dat')):
    filename = file.split('.')[0]
    plt.figure(figsize=(8,6), dpi=75)
    xi, yi = loadtxt(file, skiprows=1, usecols=(0, 1), unpack=True)
    # for x, y in zip(xi, yi):
    #     plt.annotate('{}'.format(x), xy=(x, y))
    # Removing outlier data
    outlier = (~is_outlier.is_outlier(yi))
    x = xi[outlier]
    y = yi[outlier]
    plt.plot(xi, yi, 'o',  color="blue", label='center')
    plt.xlabel('azi')
    plt.ylabel('position')
    plt.savefig(filename + '_' + 'psi' + '.png', dpi=100)
