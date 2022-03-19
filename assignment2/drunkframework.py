# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 17:20:59 2022

@author: gideo
"""
import matplotlib

class person():
    def __init__(self, x, y):
        self.x = x 
        self.y = y
    def show(self):
        matplotlib.pyplot.scatter(self.x, self.y, color = "white")

