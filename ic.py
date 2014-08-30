
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import matplotlib.animation as animation
import csv
from Tkinter import *
import tkMessageBox
from functools import partial


bolas = []
E1 = None
texts = [];

def showChart():
    numframes = 39
    numpoints = 2
    #np.random.random((numframes, numpoints))
    # list( csv.reader( open( r'bola1.csv' ) ) )   # [[0.1,0.1],[0.2,0.2],[0.3,0.3],[0.4,0.4],[0.5,0.5]]
    #bola2 = [[0.2,0.1],[0.3,0.2],[0.4,0.3],[0.5,0.4],[0.6,0.1]]
    
    #bolas = []

    global E1
    duration = E1.get()
    csv_in = open('bolas.csv', 'rb')
    myreader = csv.reader(csv_in)

    consumidores = 0
    maiordMax = 0


    for row in myreader:
        
        insc, data, dmed, dmax, hdmax,ramo,  = row
        if dmax > maiordMax:
            maiordMax = float(dmax)
        bolas.append([str(insc), str(data), float(dmed), float(dmax)])
 
    #for row in myreader:
    #    x, y = row
    #    bola1.append([float(x),float(y)])
 
    numcons =  len(set(tuple(x[0] for x in bolas)))
    numpoints = numcons

    #print bolasU;

    print numpoints
    dmed, dmax, c, s = np.random.random((4, numpoints))
    #y, e, c, s = np.random.random((4, numpoints))

    fig = plt.figure()
    plt.xlim(-0.5, 7.5)
    plt.ylim(-0.5, 7.5)
    plt.xlabel('dMed')
    plt.ylabel('dMax')
    
    scat = plt.scatter(dmed, dmax, c=c, s=s)
    
    ax=plt.gca()

    ani = animation.FuncAnimation(fig, update_plot, frames=xrange(numframes), interval=duration,
                                  fargs=(bolas, numpoints, numcons, maiordMax, scat, fig, ax))
    plt.show()

arrow = None



main()
