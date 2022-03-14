# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 10:38:25 2022

@author: gideo
"""
import random

class agent():
    def __init__(self, environment, ia):
        self.id = ia
        self.x = random.randint(0, len(environment)-1)
        self.y = random.randint(0,len(environment)-1)
        self.environment = environment
        self.store = 0
        print(self.x, self.y, len(environment))
    def __str__(self):        
        return "id = " + str(self.id) + ", x = " + str(self.x) + ", y = " + str(self.y)
    #make agents move randomly
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % len(self.environment)
        else:
            self.y = (self.y - 1) % len(self.environment)
            
        if random.random() < 0.5:
            self.x = (self.x + 1) % len(self.environment)
        else:
            self.x = (self.x - 1) % len(self.environment)
    #make agents eat environment data
    def eat(self): 
        if self.environment[self.y][self.x] > 10:
           self.environment[self.y][self.x] -= 10
           self.store += 10
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0 
        if self.store > 100:
            self.environment[self.y][self.x] += self.store
            self.store = 0
            

        


                
