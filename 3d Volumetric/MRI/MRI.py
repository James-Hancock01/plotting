import matplotlib.pyplot as plt 
from skimage import data
import DataIO as DataIO
import numpy as np
import time

def remove_keymap_conflicts(new_keys_set):
    for prop in plt.rcParams:
        if prop.startswith('keymap.'):
            keys = plt.rcParams[prop]
            remove_list = set(keys) & new_keys_set
            for key in remove_list:
                keys.remove(key)

class multi_slice_viewer:
    def __init__(self, ax, volume):
        remove_keymap_conflicts({'j', 'k', 'p'})
        self.ax = ax
        self.ax.volume = volume
        self.ax.index = volume.shape[0] // 2
        self.ax.imshow(volume[ax.index])
        fig.canvas.mpl_connect('key_press_event', self.process_key)

    def process_key(self, event):
        fig = event.canvas.figure
        # ax = fig.axes[0]
        if event.key == 'j':
            self.previous_slice()
        elif event.key == 'k':
            self.next_slice()
        elif event.key == "p":
            self.iterate_through_slices()
        fig.canvas.draw()

    def iterate_through_slices(self):
        print("iterating through slices")
        for i in range(0, self.ax.volume.shape[0]):
            self.next_slice()
            plt.pause(0.005)
            time.sleep(0.005)
        
    def previous_slice(self):
        volume = self.ax.volume
        self.ax.index = np.clip(self.ax.index - 1, 0, volume.shape[0] - 1)
        self.ax.images[0].set_array(volume[self.ax.index])

    def next_slice(self):
        volume = self.ax.volume
        self.ax.index = np.clip(self.ax.index + 1, 0, volume.shape[0] - 1)
        self.ax.images[0].set_array(volume[self.ax.index])

struct_arr = DataIO.getData()

fig, ax = plt.subplots()

slice_viewer = multi_slice_viewer(ax, struct_arr)


plt.show()