# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 15:07:42 2022

@author: gideon
"""

import csv
import matplotlib
import matplotlib.animation
from copy import deepcopy
import drunkframework
import tkinter

NUM_DRUNKS = 25

def load_town(file):
    """
    Creates function to load environment data

    Parameters
    ----------
    file : str 
        name of file containing environment data.

    Returns
    ------- 
    drunk_town : list[list[int]]
        2d array of number representing environment.

    """
    drunk_town = []
    f = open(file, newline='')
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        drunk_town.append(rowlist)
    f.close() 
    return drunk_town

def plot_town(town):
    """
    Plot and show environemnt data 

    Parameters
    ----------
    town : list[list[int]]
        2d array of number representing environment.
        
    Returns
    -------
    None.

    """
    matplotlib.pyplot.ylim(0, len(town[0]))
    matplotlib.pyplot.xlim(0, len(town))
    matplotlib.pyplot.imshow(town)
    
def main():
    """
    main code for starting, updating and ending model

    """
    drunk_town = load_town("drunk.txt") 
    density_town = deepcopy(drunk_town) #create copy of town environment that becomes the denisty map
    fig,ax = matplotlib.pyplot.subplots() 
    
    drunks = []
    for i in range(NUM_DRUNKS):
        drunkman = drunkframework.person(150, 150, (i+1)*10, density_town) # create new person at pub with housenumber increasing by 10 each time
        drunks.append(drunkman)

    
    def update(framenumber):
        """
        updates model

        Parameters
        ----------
        framenumber : int

        Returns
        -------
        None.

        """
        drunkman = drunks[0]
        ax.clear()
        drunkman.move()
        drunkman.density()
        print(drunkman)
        plot_town(drunk_town)
        drunkman.show()
        if drunk_town[drunkman.y][drunkman.x] == drunkman.housenumber:
            drunks.pop(0)
            print (drunkman, "is home")
            
        
    def gen_function():   
        """
        create function to stop model when finished when all drunk people home

        """
        a = 0
        while len(drunks) > 0:
            yield a
            a = a + 1
        
    def start():
        """
        Function to begin running model and animation

        Returns
        -------
        None.

        """
        animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False, interval = 0)
        canvas.draw() 
        animation.save
        plot_town(density_town)
        drunkman.show()
        matplotlib.pyplot.show()
        
        #write file recording density of drunks passing each cell
        f2 = open('drunk_density.txt', 'w', newline='')
        writer = csv.writer(f2)
        for row in density_town: 
            writer.writerow(row)
        f2.close()
    
    #Create GUI
    root = tkinter.Tk()
    root.wm_title("Model")
    canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
    canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)    
    run_button = tkinter.Button(root, text = "Run", command = start)
    run_button.pack()
    root.mainloop() 
           
if __name__ == "__main__":
    main()
    
