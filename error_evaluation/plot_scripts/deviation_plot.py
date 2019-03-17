from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import random

import argparse
parser = argparse.ArgumentParser("simple_example")
parser.add_argument("file_path", help="a file with four columns: x, y, z, deviation error", type=str)
args = parser.parse_args()
print(args.file_path)

import numpy as np
matrix = np.loadtxt(args.file_path)#, usecols=range(6))

fig = pyplot.figure()
ax = Axes3D(fig)

sequence_containing_x_vals = matrix[:,0]
sequence_containing_y_vals = matrix[:,1]
sequence_containing_z_vals = matrix[:,2]
#sequence_containing_deviation_vals = matrix[:,3]


ax.scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals)
pyplot.show()
