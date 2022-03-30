
import random
import math

#First Agent 
# Set up variables
y0=50
x0=50

# Random walk one stop
if random.random() < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
    
# 
if random.random() <0.5:
    x0 +=1
else:
    x0 -=1 

print(y0, x0)

# Random walk one stop 2
if random.random() < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
    
# 
if random.random() <0.5:
    x0 +=1
else:
    x0 -=1 

print(y0, x0)
      
#Second Agent 
# Set up variables
y1=50
x1=50

# Random walk one stop 
if random.random() < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1
    
# 
if random.random() <0.5:
    x1 +=1
else:
    x1 -=1 

print(y1, x1)

# Random walk one stop 2
if random.random() < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1
    
# 
if random.random() <0.5:
    x1 +=1
else:
    x1 -=1 

print(y1, x1)

#calc distance between points
y_diff = (y0 - y1)
y_diffsq = y_diff * y_diff
x_diff = (x0 - x1)
x_diffsq = x_diff * x_diff
sum = y_diffsq + x_diffsq
answer = sum**0.5
print(answer)


#create random starting point
y0=random.randint(0,100)
x0=random.randint(0,100)

#move y0 randomly 
if random.random() < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
    
#move xo randomly 
if random.random() <0.5:
    x0 +=1
else:
    x0 -=1 

print(y0, x0)

#Second Agent 
# Set up y1 and x1 to be a random starting point
y1=random.randint(0,100)
x1=random.randint(0,100)

#Move y1 randomly 
if random.random() < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1
    
#Move x1 randomly 
if random.random() <0.5:
    x1 +=1
else:
    x1 -=1 

print(y1, x1)

#Move y1 randomly
if random.random() < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1
    
#Move x1 randomly  
if random.random() <0.5:
    x1 +=1
else:
    x1 -=1 

print(y1, x1)

#calculate diff between points
y_diff = (y0 - y1)
y_diffsq = y_diff * y_diff
x_diff = (x0 - x1)
x_diffsq = x_diff * x_diff
sum = y_diffsq + x_diffsq
answer = sum**0.5
print(answer)