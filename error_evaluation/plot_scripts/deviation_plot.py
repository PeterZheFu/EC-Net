from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import random

import argparse

import pptk
import numpy as np

parser = argparse.ArgumentParser("simple_example")
parser.add_argument("file_path1", help="a file with four columns: x, y, z, deviation error", type=str)
parser.add_argument("file_path2", help="a file with four columns: x, y, z, deviation error", type=str)
args = parser.parse_args()

matrix1 = np.loadtxt(args.file_path1)#, usecols=range(6))
matrix2 = np.loadtxt(args.file_path2)

fig = pyplot.figure()
ax = Axes3D(fig)


v = pptk.viewer(matrix1[:,0:3])

v.set(show_axis = True)

#attr_color = pptk.rand(1)       # 1 random scalar
#v.attributes(attr_color)
v.color_map([[1, 1, 1]])

