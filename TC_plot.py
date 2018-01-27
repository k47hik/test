import glob
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.chdir('Z:')
for file in sorted(glob.glob('*.exp')):
    filename = file.split('.')[0]

    with open(filename + '.dat', 'w+') as outfile:
            with open(file, "r+") as infile:
                for i, line in enumerate(infile):
                    if i == 20 or line.startswith('   '):
                        outfile.write(line)
    plt.clf()
    x, y = np.loadtxt(filename + '.dat', skiprows=1, usecols=(0, 1), unpack=True)
    plt.plot(x, y, 'o',  color="blue", label='center')
    plt.xlabel('heat')
    plt.ylabel('temp')
    plt.savefig(filename + '.png', dpi=100)
