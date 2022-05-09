# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 17:20:59 2022

@author: gideon
"""
import matplotlib
import random

class person():
    def __init__(self, y, x, housenumber, town):
        """
        

        Parameters
        ----------
        y : Int
            y coordinate of drunk.
        x : Int
            x coordinate of drunk.
        housenumber : Int
            House number of drunk.
        town : List[List[int]]
            2d array of number representing environment.

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
        
        give each drunk a house number and shows x and y coordinate

        """
        return f"housenumber = {self.housenumber}, x = {self.x}, y = {self.y}"
    
    def move(self):
        """
        Make each drunk move randomly

        Returns
        -------
        None.

        """
        if random.random() < 0.5:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300
                
        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300

    def density(self):
        """
        record number of times each cell is landed on

        Returns
        -------
        None.

        """
        self.town[self.y][self.x] += 1 
            
               
    def show(self):
        """
        
        plot drunk

        Returns
        -------
        None.

        """
        matplotlib.pyplot.scatter(self.x, self.y, color = "white")
        


