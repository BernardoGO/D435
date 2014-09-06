
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
    csv_in = open('celulose.csv', 'rb')
    myreader = csv.reader(csv_in)

    consumidores = 0
    maiordMax = 0


    for row in myreader:
        
        insc, data, dmed, dmax, hdmax,ramo,  = row
        if float(dmax) > maiordMax:
            maiordMax = float(dmax)
        bolas.append([str(insc), str(data), float(dmed), float(dmax)])
 
    #for row in myreader:
    #    x, y = row
    #    bola1.append([float(x),float(y)])
 
    numcons =  len(set(tuple(x[0] for x in bolas)))
    numpoints = numcons
    consumidores = 0
    #maiordMax = 0
    bolasCres = [1,1,1,1,1,1]
    totais = [] #[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]
    colors = [] #0,0,0,0,0,0
    
    for ih in xrange(0,numcons):
        totais.append([0,0])
        colors.append(0)
    

    bolasCres = sorted(bolas, key=lambda a_entry: a_entry[3]) 
    print bolasCres[len(bolasCres) - 10:len(bolasCres)-1];

    return



arrow = None

def update_plot(i, bolas, color_data, numpoints, numcons, maiordMax, scat, fig, ax):
    #scat.set_array(data[i])
       # [ 300 * abs(x)**1.5 + 100 for x in bola1[i]] 

    global texts
    global arrow

    #csv_in = open('bola1.csv', 'rb')
    #myreader = csv.reader(csv_in)
    #global bola1 
    #bola1 = []
    #for row in myreader:
    #    x, y = row
    #    bola1.append([float(x),float(y)])

    #print bola1;
    #0 39 78
    #1 40 79
    
    values = tuple( (x*39)+i    for x in xrange(0, 6))

    #scat.set_offsets([bola1[i][:2], bola2[i][:2]])
    #print values
    xy = tuple([x[2], x[3]] for x in bolas)
    ids = tuple(x[0] for x in bolas)
    
    #print xy[i::39];
    #for line in xy[i::39]: print line 
    #print i
    #print xy[i::39]

    scat.set_offsets(xy[i::39])
    #scat._sizes = [300 * abs(bola1[i][1])**1.5 + 100,   300 * abs(bola2[i][1])**1.5 + 100]
    #scat._sizes = (tuple(300 * abs(1)**1.5 + 100 for x in bolas))
    sizes = tuple([ (2000 * abs(x[2]/(x[3]) if x[3] else 0 )) ] for x in bolas)
    scat._sizes = sizes
    #scat.set_array(color_data[i])
    #print color_data[i]
    sizes2 = tuple([ str((2000 * abs(x[2]/(x[3]) if x[3] else 0 ))) + " " + x[1] ] for x in bolas[i::39])
    #for line in sizes2: print line 
    #print texts
    #for yu in texts:
    #    plt.gcf().texts.remove(yu)
    
    ax.set_title(bolas[i][1] + "  Quadro: " + str(i))
    #fig.suptitle(bolas[i][1], fontsize=14, fontweight='bold')
    #for x in values:
    #    texts.append(plt.annotate(ids[x], xy=xy[x]))
        #arrow2 = matplotlib.text.Annotation(ids[x], xy=xy[x]) 
        #ax.add_artist(arrow2)
        #texts.append(ax) 
        #arrow2.remove() 
    
    #print ax.patches
    


    return scat,


def main():
  
    top = Tk()
    global E1
    
    L1 = Label(top, text="intervalos")
    L1.pack( side = LEFT)

    E1 = Entry(top, bd =5)
    E1.pack(side = LEFT)

 
    B = Button(top, text ="mostrar", command = showChart)
    B.pack()

    top.mainloop()
    




main()
