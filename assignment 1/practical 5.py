# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 12:08:27 2022

@author: gideo
"""

import random
import operator
import matplotlib.pyplot 
import time
import itertools
import agentframework


start = time.process_time()
#create function for distance between points
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []

#creates list on random coordintaes to length specified in num of agents
for i in range(num_of_agents):
    agents.append(agentframework.agent())

#random walk one step first set of coordinates
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()

#plot all 10 coordinates
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

#find distance between agents and max/min
all_distances = []
for agents_row_a in agents:
    for agents_row_b in agents:
        #stops testing agents against themselves
        if agents_row_b != agents_row_a:
            distance = distance_between(agents_row_a, agents_row_b)
            all_distances.append(distance)   
print(max(all_distances))
print(min(all_distances))
    
    
end = time.process_time()
print("time = " + str(end - start))


