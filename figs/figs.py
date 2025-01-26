
import tonic

nmnist = tonic.datasets.DVSGesture("figs/", train=False)
events, label = nmnist[10]

time_window = 100000
fps = 1e6 / time_window

print(fps, time_window)

transform = tonic.transforms.ToFrame(
    sensor_size=nmnist.sensor_size,
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
print(sliced)
sample = sliced[10]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

posi = sample[sample['p']]
nega = sample[~sample['p']]

ax.scatter(posi['t'], posi['x'], posi['y'], c='r', marker='o', s=1, label='Positive')
ax.scatter(nega['t'], nega['x'], nega['y'], c='b', marker='o', s=1, label='Negative')

#no ticks
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

ax.set_xlabel('Time')
ax.set_ylabel('X')
ax.set_zlabel('Y')

ax.set_title('Events')

#legend
ax.legend()

plt.show()