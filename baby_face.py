import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt

class kid:
    def __init__(self, age, name, gender):
        self.age = age
        self.name = name
        self.gender = gender
        plt.ion()
        return
    
    def print(self):
        print(f"My name is {self.name}.")
        print(f"I am a {self.gender}.")
        print(f"I am {self.age} years old.")
        return
    
    def plot(self, position_x, position_y, dist=10):
        figure, ax = plt.subplots(figsize=(10, 8))
        self.fig = figure
        self.ax = ax
        plt.ion()
        plt.plot([position_x-dist, position_x+dist], [position_y, position_y], 'mo', ms=35)
        plt.plot([position_x], [position_y-10], 'r^', ms=30)
        plt.plot([position_x-4, position_x-2, position_x+2, position_x+4], [position_y-15, position_y-20, position_y-20, position_y-15], 'g', linewidth=5)
        plt.plot([position_x-15, position_x+15], [position_y+5, position_y+5], 'w', ms=0)
        self.position_x = position_x
        self.position_y = position_y
        self.dist=dist
        figure.canvas.draw()
        figure.canvas.flush_events()
        return

    def forward(self):
        print(f"if you draw me out, I'll walk forward. hahahahaha...")
        return
    
    def replot_eyes(self, position_x, position_y, dist=10, eye_color='m', eye_size=35):
        ax = self.ax
        figure = self.fig
        plt.ion()
        plt.plot([position_x-dist, position_x+dist], [position_y, position_y], f'{eye_color}o', ms=eye_size)
        figure.canvas.draw()
        figure.canvas.flush_events()
        return
    
    def move(self, dist=9):
        position_x = self.position_x
        position_y = self.position_y
        original_dist = self.dist
        self.replot_eyes(position_x, position_y, dist=original_dist, eye_color='w', eye_size=36)
        self.replot_eyes(position_x, position_y, dist=dist, eye_color='m')
        self.dist = dist
        return
    
    def continous_move(self, start_dist, end_dist):
        if end_dist >= start_dist:
            for idx in range(start_dist, end_dist+1):
                self.move(idx)
                time.sleep(1)
        else:
            for idx in range(start_dist, end_dist-1, -1):
                self.move(idx)
                time.sleep(1)
        return

