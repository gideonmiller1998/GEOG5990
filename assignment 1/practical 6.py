# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 12:08:27 2022

@author: gideo
"""

import random
import matplotlib.pyplot 
import time
import itertools
import agentframework
import csv    
import os

start = time.process_time()
#create function for distance between points
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2))**0.5

#import environment data
environment = []
f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
#plot environment data
#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show() 
f.close() 


num_of_agents = 10
num_of_iterations = 1000
agents = []

#creates list on random coordintaes to length specified in num of agents
for i in range(num_of_agents):
    agents.append(agentframework.agent(environment, i))
for agent in agents:
    print(agent)

#random move agents
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
for agent in agents:
    print(agent)
    
#agents eat environment
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        
#plot coordinates in environment
matplotlib.pyplot.ylim(0, len(environment))
matplotlib.pyplot.xlim(0, len(environment))
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
#matplotlib.pyplot.show()

#find distance between agents and max/min
all_distances = []       
for pair in itertools.combinations(agents, 2):
    #stops testing agents against themselves
    distance = distance_between(pair[0], pair[1])
    all_distances.append(distance) 
    #print(distance)
#print(max(all_distances))
#print(min(all_distances))

#write out environment file
f2 = open('environmentout.txt', 'w', newline='')
writer = csv.writer(f2)
for row in environment:
        writer.writerow(row)
f2.close()

#total amount stored by each agent
total_store = 0
for agent in agents:
    total_store = total_store + agent.store
print (total_store)
#create new file append total stored by agents
f3 = open('totalstore.txt', 'a', newline='')
f3.write(str(total_store) + os.linesep)
f3.close()


end = time.process_time()
#print("time = " + str(end - start))



