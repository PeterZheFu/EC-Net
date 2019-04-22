import pptk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (5, 5),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)


def openviewer(name):
    deviation = np.loadtxt(name)
    v_dev = pptk.viewer(deviation[:,0:3], deviation[:,3])
    print "This file has "
    print deviation.shape[0]
    v_dev.set(show_axis = False)
    v_dev.set(show_grid = False)
    #v_dev.set(bg_color = [1,1,1,1])
    v_dev.set(bg_color = [0,0,0,0])
    v_dev.set(point_size = 0.000001)
    v_dev.capture('points3D_p19_23k_203k_output_castle_deviation.png')
    v_dev.color_map('jet', scale=[0, 0.24])
    v_dev.set(show_axis = True)


# plot 3D point cloud
#deviation = np.loadtxt("points3D_p19_23k_203k_output_castle_deviation.xyz")
openviewer("points3D_p19_23k_203k_output_castle_deviation.xyz");

#deviation = np.loadtxt("castle_p30_colmap_point2mesh_distance.xyz")
openviewer("castle_p30_colmap_point2mesh_distance.xyz");

#deviation = np.loadtxt("points3D_p19_23k_input_castle_deviation.xyz")
#openviewer("castle_p19_points3D_output.xyz");

openviewer("castle_p30_points3D_colmap.xyz");

#v_dev = pptk.viewer(deviation[:,0:3], deviation[:,3])
#print deviation.shape

#print "This file has "
#print deviation.shape[0]

#print np.max(deviation, axis = 0)
#print np.min(deviation, axis = 0)

#print np.argmax(deviation, axis = 0)
#print np.argmin(deviation, axis = 0)

#v_dev.set(show_axis = False)
#v_dev.set(show_grid = False)
#v_dev.set(bg_color = [1,1,1,1])
#v_dev.set(bg_color = [0,0,0,0])
#v_dev.set(point_size = 0.000001)
#v_dev.capture('points3D_p19_23k_203k_output_castle_deviation.png')
#v_dev.color_map('jet', scale=[0, 0.24])
#v_dev.set(show_axis = True)

def openviewer(name):
    deviation = np.loadtxt(name)
    v_dev = pptk.viewer(deviation[:,0:3], deviation[:,3])
    print "This file has "
    print deviation.shape[0]
    v_dev.set(show_axis = False)
    v_dev.set(show_grid = False)
    #v_dev.set(bg_color = [1,1,1,1])
    v_dev.set(bg_color = [0,0,0,0])
    v_dev.set(point_size = 0.000001)
    v_dev.capture('points3D_p19_23k_203k_output_castle_deviation.png')
    v_dev.color_map('jet', scale=[0, 0.24])
    v_dev.set(show_axis = True)
#return;



