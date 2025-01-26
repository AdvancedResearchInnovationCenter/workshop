import h5py
import numpy as np
import tonic

h5 = h5py.File('/home/aric/neuromorphic_workshop/workshop.h5', 'r')
h5['events_data'][:, -1]

def arr_to_tonic(arr):
    out = np.zeros(len(arr), dtype=[('x', '<i2'), ('y', '<i2'), ('p', '?'), ('t', '<f8')])
    arr[:, 3] = arr[:, 3] * 1e6
    arr[:, 3] = arr[:, 3] - arr[0, 3]
    
    out['x'] = arr[:, 0].astype(np.int16)
    out['y'] = arr[:, 1].astype(np.int16)
    out['p'] = arr[:, 2].astype(bool)
    out['t'] = arr[:, 3].astype(np.float64)
    return out

events = arr_to_tonic(h5['events_data'][:])
    
print(events)

time_window = 50000
fps = 1e6 / time_window

print(fps, time_window)

transform = tonic.transforms.ToFrame(
    sensor_size=(346, 260, 2),
    time_window=time_window,
)

# events['p'] = [True]*len(events['p'])

frames = transform(events)

print(frames.shape)

# ani = tonic.utils.plot_animation(frames=frames[:, 1, :, :], fps=fps)

# ani.save("figs/animation.gif", writer='imagemagick', fps=fps)

#plot in 3d frames 0 and 1 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

slicer = tonic.slicers.SliceByTime(time_window=time_window)
sliced, _ = slicer.slice(events, 0)
sample = sliced[110]

fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

posi = sample[sample['p']]
nega = sample[~sample['p']]

# ax.scatter(posi['t'], posi['x'], posi['y'], c='r', marker='o', s=1, label='Positive', alpha=0.5)
# ax.scatter(nega['t'], nega['x'], nega['y'], c='b', marker='o', s=1, label='Negative', alpha=0.5)

# #no ticks
# ax.set_xticks([])
# ax.set_yticks([])
# ax.set_zticks([])

# ax.set_xlabel('Time')
# ax.set_ylabel('X')
# ax.set_zlabel('Y')

# ax.set_title('Events')

method = "count"


if method == "latest":
    img = np.zeros((346, 260))
    img[posi['x'], posi['y']] = 1
    img[nega['x'], nega['y']] = -1

    plt.imshow(img, cmap
    ='coolwarm')
elif method == "ToFrame":
    transform = tonic.transforms.ToFrame(
        sensor_size=(346, 260, 2),
        n_time_bins=1
    )
    frames = transform(sample)
    tonic.utils.plot_animation(frames)
elif method == "


print(img.shape)    

plt.show()