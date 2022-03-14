# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 15:54:01 2022

@author: gideo
"""

import random
import operator
import matplotlib.pyplot
import time


start = time.process_time()
#create function for distance between points
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100

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
