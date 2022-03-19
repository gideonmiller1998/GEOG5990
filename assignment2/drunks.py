# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 15:07:42 2022

@author: gideo
"""

import csv
import matplotlib
from copy import deepcopy
import drunkframework

def load_town(file):
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
    town = deepcopy(town)
    houses = list(range(10,260,10))
    num2cidx = {"0":0, "1":1}
    for house in houses:
        num2cidx[str(house)] = 2
    for i in range(len(town)):
        for j in range(len(town[i])):
            town[i][j] = num2cidx[str(int(town[i][j]))]

    matplotlib.pyplot.ylim(0, len(town[0]))
    matplotlib.pyplot.xlim(0, len(town))
    matplotlib.pyplot.imshow(town)

    
def main():
     drunk_town = load_town("drunk.txt") 
     plot_town(drunk_town)
     gideon = drunkframework.person(150, 150)
     gideon.show()
     matplotlib.pyplot.show()
     
     
if __name__ == "__main__":
    main()
    
