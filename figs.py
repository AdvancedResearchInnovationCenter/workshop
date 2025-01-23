
import tonic

nmnist = tonic.datasets.DVSGesture("figs/", train=False)
events, label = nmnist[10]

time_window = 33000
fps = 1e6 / time_window

print(fps, time_window)

transform = tonic.transforms.ToFrame(
    sensor_size=nmnist.sensor_size,
    time_window=time_window,
)

events['p'] = [True]*len(events['p'])

frames = transform(events)

print(frames.shape)

ani = tonic.utils.plot_animation(frames=frames[:, 1, :, :], fps=fps)

ani.save("figs/animation.gif", writer='imagemagick', fps=fps)