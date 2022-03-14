# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 12:08:27 2022

@author: gideo
"""

import matplotlib
import random 
import time
import itertools
import agentframework
import csv    
import os

#start = time.process_time()

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
num_of_iterations = 100
neighbourhood = 20
agents = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


#creates list on random coordintaes 
for i in range(num_of_agents):
    agents.append(agentframework.agent(environment, i, agents))
for agent in agents:
    print(agent)

carry_on = True

def update(frame_number):    
    fig.clear()   
    global carry_on
#agents move then eat environment and sick up environemnt if eat over 100
    random.shuffle(agents) #shuffles order of agents
   # for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        print(agents[i])
        
    if random.random()<0.1:
        carry_on = False
        print("stopping condition")
        # for agent in agents:
        #      print(agent)

    # plot coordinates in environment
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
#matplotlib.pyplot.show()

#find distance between agents and max/min
# all_distances = []       
# for pair in itertools.combinations(agents, 2): #stops testing agents against themselves
#     distance = pair[0].distance_between(pair[1])
#     all_distances.append(distance) 
   # print(distance)
#print("max distance =", max(all_distances))
#print("min distance =", min(all_distances))

#write out environment file
# f2 = open('environmentout.txt', 'w', newline='')
# writer = csv.writer(f2)
# for row in environment:
#         writer.writerow(row)
# f2.close()

#total amount stored by each agent
# total_store = 0
# for agent in agents:
#     total_store = total_store + agent.store
# #print (total_store)
# #create new file append total stored by agents
# f3 = open('totalstore.txt', 'a', newline='')
# f3.write(str(total_store) + os.linesep)
# f3.close()

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

matplotlib.pyplot.show()

#end = time.process_time()
#print("time = " + str(end - start))



