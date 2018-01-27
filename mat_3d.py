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

# os.chdir('c:/Users/jeyabala1/Documents/Python Scripts/CN1_mart200')
fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# for file in sorted(glob.glob('*.txt')):
#     plt.clf()
# #     file_name1 = file.split('_')[1]
#     filename = file.split('.')[0]
    # y_array = []
    # y_array.append(dist)
    # for i, y1 in enumerate(y_array):
    #     x, z = np.loadtxt(file, skiprows=0, usecols= (0, 1) , unpack=True)
    #     y = []
    #     for i in range(len(x)):
    #         y.append(float(y1)*5)
    #     ax.plot_wireframe(x, y, z)
    #     # for x, y in zip(x1, y2):
    #     #     plt.annotate('{}'.format(x), xy=(x, y))
    # with open(str(filename) + '_' +'out'+'.txt', "w+") as outfile:
    #     with open(file, "r+") as infile:
    #         lines = infile.readlines()
    #         data = []
    #         for line in lines[1:361]:
    #             linecounts = [x for x in line.rstrip('\n').split(' ') if x != '']
    #             twotheta = float(linecounts[4])
    #             data.append(twotheta)

    #         for i, line in enumerate(data):
    #             if i < 180:
    #                 theta1 = (data[i]+ data[i+180])/4
    #                 if math.isnan(theta1):
    #                     continue
    #                 else:
    #                     outfile.write(('%.10s\t%.10s\n' %(i, theta1)))
with open('outlier_90.dat', 'w+') as outfile:
    x1, y1 = np.loadtxt('outlier_90.txt',skiprows=0, usecols=(0, 1), unpack=True)
    # Removing outlier data
    outlier = (~is_outlier.is_outlier(y1, 0.70))
    # xj = xi[outlier1]
    # outlier = (~is_outlier.is_outlier(xj))
    x = x1[outlier]
    y = y1[outlier]
    for x1, y1 in zip(x, y):
        outfile.write(str(x1) + '\n')
    #     plt.annotate('{}'.format(x), xy=(x, y))
    plt.plot(x, y, 'o',  color="blue", label='center')
    plt.ylabel('2theta')
    plt.xlabel('distance')
    plt.show()
    # plt.savefig(str(file) + '_' + 'out' + '.png', dpi=100)
