# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 10:38:25 2022

@author: gideo
"""
import random

class agent():
    
    def __init__(self, environment, agents, y, x, ia):
        """
        

        Parameters
        ----------
        environment : List[List[int]]
            2d array of number representing environment.
        agents : List[agent]
            List of all agents.
        y : Int
            y coordinate of agent.
        x : Int
            x coordinate of agent.
        ia : integer
            ID of the agents
            

        Returns
        -------
        None.

        """
        self.id = ia
        
        self.x = x
        if (x == None):
            self.x = random.randint(0,300)
        else:
            self.x = x 
            
        self.y = y
        if (y == None):
            self.y = random.randint(0,300)
        else:
            self.y = y
            
        self.environment = environment
        
        self.agents = agents
        
        self.store = 0
            
    
    def __str__(self): 
        """
        give each agent an id and shows x and y coordinate

        """
        return "id = " + str(self.id) + ", x = " + str(self.x) + ", y = " + str(self.y) + ", store = " + str(self.store)
    

    def move(self):
        """
        make each agent move randomly

        Returns
        -------
        None.

        """
        if random.random() < 0.5:
            self.y = (self.y + 1) % len(self.environment)
        else:
            self.y = (self.y - 1) % len(self.environment)
            
        if random.random() < 0.5:
            self.x = (self.x + 1) % len(self.environment)
        else:
            self.x = (self.x - 1) % len(self.environment)
            
    
    def eat(self): 
        """
        Make agents eat environment data and then deposit environemnt data if store exceeds 100.

        Returns
        -------
        None.

        """
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


    def share_with_neighbours(self, neighbourhood):
        """
        agents share store with other agents in neighbourhood

        Parameters
        ----------
        neighbourhood : number
            area surrounding agent.

        Returns
        -------
        None.

        """
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                #print("sharing " + str(dist) + " " + str(ave))
                
    def distance_between(self, agent):
        """
        calculate distances between agents

        Parameters
        ----------
        agent : agent
            agent comparing against.

        Returns
        -------
        number
            distance between two agents.

        """
        return (((self.x - self.x)**2) + ((self.y - self.y)**2))**0.5
    


        


                
