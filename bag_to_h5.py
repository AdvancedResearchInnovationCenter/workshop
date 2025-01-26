import rosbag
import numpy as np
import h5py

# Path to rosbag
bag = rosbag.Bag('w.bag')

events = []

for topic, msg, t in bag.read_messages(topics=['/dvs/events']):
    for current_event in msg.events:
        t_sec = current_event.ts.secs + (current_event.ts.nsecs/1e9) # Seconds
        event_tmp = [int(current_event.x), int(current_event.y), int(current_event.polarity), t_sec]
        events.append(event_tmp)

events_array = np.array(events)

# Save directory of h5 data sequence
h5f = h5py.File('workshop1.h5', 'w')
h5f.create_dataset('events_data', data=events_array)
h5f.close()

print('Success')
