# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
import operator
import matplotlib.pyplot

num_of_agents = 10
num_of_interations = 100
agents = []


#create random agents
for i in range (num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

#move agents      
for j in range (num_of_interations):    
    for i in range (num_of_agents):
        if random.random() <0.5:
            agents[i][0] = (agents[i][0]+1) % 100
        else:
            agents[i][0] = (agents[i][0]-1) % 100
            
        if random.random() <0.5:
             agents[i][1] = (agents[i][1]+1) % 100
        else:
             agents[i][1] = (agents[i][1]-1) % 100

'''
#calculate distances
answer = (((agents[0][1]-agents[1][1])**2) + ((agents[0][0] - agents[1][0])**2))**0.5
print(answer)
'''
#plot agents
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range (num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()
