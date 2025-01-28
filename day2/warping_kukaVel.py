import numpy as np
import h5py
import time
import cv2
import warnings
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")

h5f = h5py.File('/home/aric/neuromorphic_workshop/salah.h5', 'r')

events = h5f['events_data'][:]
print(events.shape)
h5f.close()
events[:,3] = (events[:,3] - events[0,3])

events = events[events[:,0] > 150, :]
events = events[events[:,0] < 490, :]
events = events[events[:,1] > 130, :]
events = events[events[:,1] < 350, :]

W = 640
H = 480

camera_matrix = np.array([[998.26179644, 0.0, 328.43880897], [0.0, 997.00199357, 236.79904821], [0.0, 0.0, 1.0]])
dist_coeffs = np.array([-2.45446920e-01, -1.62643150e+00, -2.52514776e-03, -1.80453681e-04, 1.21369322e+01])

z = 0.09
f = camera_matrix[0,0]
v_actual = 0.1
u_dot = - (f / z) * v_actual

events_buffer = 10000
t_sample = 1/500.0
t_sim = events[-1,-1] - events[0,-1]
ti = 0.0
time_array = np.linspace(ti, t_sim, num=int((t_sim-ti)/t_sample))

# fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
# out = cv2.VideoWriter('kuka_0.5spd_high_aperture_warp_low..avi', fourcc, 3.0, (640, 480))

for j in range(len(time_array)-1):
    t_visualize = time_array[j]
    time_window_events_initial = np.where(events[:,3] > t_visualize)
    events_array = events[time_window_events_initial[0][0:events_buffer],:]
    t_ref = events_array[-1,-1]
    warped_image = np.zeros((H, W))
    for i in range(len(events_array)):
        warped_event_x = events_array[i,0] + u_dot * (t_ref - events_array[i,-1])
        warped_event_y = events_array[i,1]
        if int(warped_event_x) < W-150 and int(warped_event_x) > 150 and int(warped_event_y) < H-130 and int(warped_event_y) > 130:
            warped_image[int(warped_event_y), int(warped_event_x)] = warped_image[int(warped_event_y), int(warped_event_x)] + 1
    norm_warp = warped_image / np.max(warped_image)
    iwe_vector = warped_image.reshape((H*W))
    norm_warp = np.array(255*norm_warp, np.uint8)
    norm_warp = cv2.cvtColor(norm_warp, cv2.COLOR_GRAY2BGR)
    norm_warp = cv2.putText(norm_warp, 'Time ='+str(round(time_array[j],2)), (10,450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1, cv2.LINE_AA)
    # out.write(norm_warp)
    cv2.imshow('Warped Events', norm_warp)
    cv2.imwrite('/home/aric/neuromorphic_workshop/exclude/salah/'+str(j)+'.png', norm_warp)
    cv2.waitKey(1)

# out.release()
cv2.destroyAllWindows()