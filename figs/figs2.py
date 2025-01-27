#%%
import h5py
import numpy as np
import tonic

h5 = h5py.File('/home/aric/neuromorphic_workshop/workshop.h5', 'r')

events = h5['events_data'][:]
print(events.shape)

def arr_to_tonic(arr): #we will cover tonic later. For now just know that it is a format for storing events that is more memory efficient.
    out = np.zeros(len(arr), dtype=[('x', '<i2'), ('y', '<i2'), ('p', '?'), ('t', '<f8')])
    arr[:, 3] = arr[:, 3] * 1e6
    arr[:, 3] = arr[:, 3] - arr[0, 3]
    
    out['x'] = arr[:, 0].astype(np.int16)
    out['y'] = arr[:, 1].astype(np.int16)
    out['p'] = arr[:, 2].astype(bool)
    out['t'] = arr[:, 3].astype(np.float64)
    return out

events = arr_to_tonic(events)

import matplotlib.pyplot as plt
ts0 = events[0]['t']
ts1 = events[-1]['t']

print("Time span: ", (ts1 - ts0) / 1e6, "seconds")

#30 ms windows
breaks = np.arange(ts0, ts1, 30e3)
print("Number of 30 ms windows: ", len(breaks) - 1)

breaks_idx = np.searchsorted(events['t'], breaks)
counts = np.diff(breaks_idx)


sample = events[breaks_idx[120]:breaks_idx[121]]
#3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(sample['t'], sample['x'], sample['y'], c=sample['p'], s=1, cmap='coolwarm')
ax.set_xlabel('Time (us)')
ax.set_ylabel('X')
ax.set_zlabel('Y')

plt.show()
#%%

frame = tonic.transforms.ToFrame(sensor_size=(346, 260, 2), time_window=30e3)(sample)
print(frame[0, :, :].shape)
frame = np.concatenate([np.zeros((1, 260, 346)), frame[0, :, :]], axis=0)
fig, ax = plt.subplots(1, 1)
frame = frame.transpose(1,2, 0)
ax.imshow(frame)
plt.show()
# %%

frame_single = np.sum(frame, axis=2)
fig, ax = plt.subplots(1, 1)
ax.imshow(frame_single, cmap='gray')
# %%


voxel = tonic.transforms.ToVoxelGrid(sensor_size=(346, 260, 2), n_time_bins=4)(sample)
print(voxel.shape)

fig, axes = plt.subplots(2, 2, figsize=(5, 5), sharex=True, sharey=True)

for i in range(4):
    ax = axes.flatten()[i]
    print(voxel[i, 0 :, :].shape)
    ax.imshow(voxel[i, 0 :, :][0], cmap='gray')
    ax.set_title(f"Time bin {i+1}")



# %%
