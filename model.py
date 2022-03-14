# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 12:08:27 2022

@author: gideo
"""
import matplotlib
import matplotlib.animation
matplotlib.use('TkAgg') 
import random 
import time
import agentframework
import csv    
import tkinter
import requests
import bs4
import os

start = time.process_time()

#import x and y coordinates from web page 
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
#print(td_ys)
#print(td_xs) 


def run(): 
    """
    create function to run animation of agents

    Returns
    -------
    None.

    """
    global num_of_agents, num_of_iterations, agents, neighbourhood, carry_on
    num_of_agents = int(agent_entry.get())
    num_of_iterations = int(iteration_entry.get())
    neighbourhood = 20
    agents = []
    carry_on = True

    #assign coordinates from web page to x and y and appends to agents list
    for i in range(num_of_agents):
        if (len(td_ys) > i):
            y = int(td_ys[i].text) * 3
            x = int(td_xs[i].text) * 3
        else:
            y = None
            x = None
        agents.append(agentframework.agent(environment, agents, y, x, i)) 
        
    for agent in agents:
        print(agent)
    
    #create animation of agents moving and saves as GIF
    #writer = matplotlib.animation.PillowWriter(fps=5)
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw() 
    #animation.save("agents_animation.gif", writer = writer)
    

def gen_function():
    """
    yields an icrementing number until number of iteration exceeded or carry on is false


    Yields
    ------
    a : int
        next iteration number.

    """
    global carry_on
    a = 0
    while (a < num_of_iterations) and carry_on :
        yield a	
        a = a + 1
    
#create Graphical User Interface
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#add menu bar to GUI
menu_bar = tkinter.Menu(root) 
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="File", menu=model_menu)
model_menu.add_command(label="Quit", command=root.destroy)

#add option to change number of agents to GUI
agent_label = tkinter.Label(root, text = "Number of Agents")
agent_label.pack()
agent_entry = tkinter.Entry(root)
agent_entry.pack()

#add option to change number of iteration to GUI
iteration_label = tkinter.Label(root, text = "Number of Iterations")
iteration_label.pack()
iteration_entry = tkinter.Entry(root)
iteration_entry.pack()

#add option to change stopping condition to GUI
stopping_label = tkinter.Label(root, text = "Stop model when random number (between 0 and 1) less than")
stopping_label.pack()
stopping_entry = tkinter.Entry(root)
stopping_entry.pack()

run_button = tkinter.Button(root, text = "Run", command = run)
run_button.pack()

#import environment data
environment = []
f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
f.close() 


def update(frame_number):    # make model update
    """
    Updates model at each iteration
    
    Parameters
    ----------
    frame_number: int
        current iteration number
    
    """

    global carry_on
    fig.clear()   
    random.shuffle(agents) #shuffles order of agents
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        #print(agents[i])
        
    if random.random()<float(stopping_entry.get()): 
        carry_on = False
        print("stopping condition after", frame_number, "iterations")
        
    for agent in agents:
        print(agent)

    #plot coordinates in environment
    matplotlib.pyplot.ylim(0, len(environment[0]))
    matplotlib.pyplot.xlim(0, len(environment))
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color = "white")
matplotlib.pyplot.show()

#write out new environment file
f2 = open('environmentout.txt', 'w', newline='')
writer = csv.writer(f2)
for row in environment:
    writer.writerow(row)
f2.close()

#calculate total amount stored by each agent
total_store = 0
for agent in agents:
      total_store = total_store + agent.store
#print (total_store)

# #create new file and append total stored by agents
f3 = open('totalstore.txt', 'a', newline='')
f3.write(str(total_store) + os.linesep)
f3.close()

root.mainloop() 

end = time.process_time()
print("time = " + str(end - start))
