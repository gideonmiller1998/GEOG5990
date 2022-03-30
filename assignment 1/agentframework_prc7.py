# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 10:38:25 2022

@author: gideo
"""
import random

class agent():
    def __init__(self, environment, ia, agents):
        self.id = ia
        self.x = random.randint(0, len(environment)-1)
        self.y = random.randint(0, len(environment)-1)
        self.environment = environment
        self.agents = agents
        self.store = 0
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
        #make agents sick up if eat over 100
        if self.store > 100:
            self.environment[self.y][self.x] += self.store
            self.store = 0        
#make agents share whatvthey eat with other agents if within theire neighbourhood
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                #print("sharing " + str(dist) + " " + str(ave))
     #calculate distance between agents  
    def distance_between(self, agent):
        return (((self.x - self.x)**2) + ((self.y - self.y)**2))**0.5

        


                
