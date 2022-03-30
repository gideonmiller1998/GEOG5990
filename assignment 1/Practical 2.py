# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Agent Based Modelling
import random
import operator
import matplotlib.pyplot


agents = []
num_of_agents = 10
num_of_interations = 100

#create random starting point y0 and x0 replaced into agents 
y0=random.randint(0,100)
x0=random.randint(0,100)
agents.append([y0,x0])


for i in range (num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])
       
for j in range (num_of_interations):    
    for i in range (num_of_agents):
        if random.random() <0.5:
            agents[i][0] = agents[i][0]+1
        else:
            agents[i][0] = agents[i][0]-1
        if random.random() <0.5:
             agents[i][1] = agents[i][1]+1
        else:
             agents[i][1] = agents[i][1]-1



#move y0 randomly 
if random.random() < 0.5:
    agents [0][0] =  agents [0][0] + 1
else:
    agents [0][0] =  agents [0][0] - 1
    
#move xo randomly 
if random.random() <0.5:
    agents[0][1] +=1
else:
    agents[0][1] -=1 

print( agents [0][0], agents[0][1])

#Second Agent 
# Set up y1 and x1 to be a random starting point
#y1=random.randint(0,100)
#x1=random.randint(0,100)
agents.append([random.randint(0,99),random.randint(0,99)])

#Move y1 randomly 
if random.random() < 0.5:
    agents[1][0] = agents [1][0] + 1
else:
    agents[1][0] = agents [1][0] - 1
    
#Move x1 randomly 
if random.random() <0.5:
    agents[1][1] +=1
else:
    agents[1][1] -=1 


#Move y1 randomly 
if random.random() < 0.5:
    agents[1][0] = agents [1][0] + 1
else:
    agents[1][0] = agents [1][0] - 1
    
#Move x1 randomly 
if random.random() <0.5:
    agents[1][1] +=1
else:
    agents[1][1] -=1 

print(agents)

#calculate pythagorian distance between yo, xo and y1, x1
answer = (((agents[0][1]-agents[1][1])**2) + ((agents[0][0] - agents[1][0])**2))**0.5
print(answer)

#using functions 
print(max(agents))

print(max(agents, key=operator.itemgetter(1)))

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
m = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(m[1],m[0], color='red')
matplotlib.pyplot.show()

