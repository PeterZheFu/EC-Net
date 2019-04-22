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

# plot 3D point cloud
deviation = np.loadtxt("points3D_p19_23k_203k_output_castle_deviation.xyz")


v_dev = pptk.viewer(deviation[:,0:3], deviation[:,3])
#print deviation.shape

print deviation.shape[0]

print np.max(deviation, axis = 0)
print np.min(deviation, axis = 0)

print np.argmax(deviation, axis = 0)
print np.argmin(deviation, axis = 0)

v_dev.set(show_axis = False)
v_dev.set(show_grid = False)
#v_dev.set(bg_color = [1,1,1,1])
v_dev.set(bg_color = [0,0,0,0])
v_dev.set(point_size = 0.000001)
v_dev.capture('points3D_p19_23k_203k_output_castle_deviation.png')
v_dev.color_map('jet', scale=[0, 0.24])
v_dev.set(show_axis = True)
