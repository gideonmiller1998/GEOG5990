# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 17:20:59 2022

@author: gideo
"""
import matplotlib
import random

class person():
    def __init__(self, y, x, housenumber, town):
        """
        

        Parameters
        ----------
        y : TYPE
            DESCRIPTION.
        x : TYPE
            DESCRIPTION.
        housenumber : TYPE
            DESCRIPTION.
        town : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        self.y = y
        self.x = x
        self.housenumber = housenumber
        self.town = town
    
    def __str__(self):       
        """
        

        Returns
        -------
        str
            DESCRIPTION.

        """
        return f"housenumber = {self.housenumber}, x = {self.x}, y = {self.y}"
    
    def move(self):
        """
        

        Returns
        -------
        None.

        """
        if random.random() < 0.5:
            self.y = (self.y + 5) % 300
        else:
            self.y = (self.y - 5) % 300
                
        if random.random() < 0.5:
            self.x = (self.x + 5) % 300
        else:
            self.x = (self.x - 5) % 300

    def density(self):
        """
        

        Returns
        -------
        None.

        """
        self.town[self.y][self.x] += 1 
            
               
    def show(self):
        """
        

        Returns
        -------
        None.

        """
        matplotlib.pyplot.scatter(self.x, self.y, color = "white")
        


