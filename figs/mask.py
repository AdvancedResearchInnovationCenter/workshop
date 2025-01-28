import h5py
import numpy as np
import matplotlib.pyplot as plt

events = h5py.File('/home/aric/neuromorphic_workshop/workshop.h5', 'r')
events_data = events['events_data'][10000:-10000]
