
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
    colors = [0,0,0,0,0,0]
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

    
    #bolasCres = sorted(bolas, key=lambda a_entry: a_entry[3]) 
    #print bolasCres[1::36];

    if numcons > 3:
        bolasLow = []
        bolasHigh = []
        
        for cons in xrange(1, numcons+1):
            maiordMaxA = 0
            for dia in xrange(0, 39):
                #print bolas[cons*dia][3]
                if bolas[cons*dia][3] >= maiordMax:
                   maiordMaxA = bolas[cons*dia][3]
                    
           #print str(maiordMaxA) + " " + str(maiordMax)
          
            if maiordMaxA >= (maiordMax):
                for dia in xrange(0, 39):
                    #bolasHigh.append(bolas[cons*dia])
                    #print "maior " + str(bolas[cons*dia])
                    colors[cons-1] = 1;
            else:
                for dia in xrange(0, 39):
                    #bolasLow.append(bolas[cons*dia])
                    #print "menor " + str(bolas[cons*dia])
                    colors[cons-1] = 5;

        
    #for cons in xrange((numcons/2), (numcons)+1):
    #    colors[cons-1] = 5;

   


    #print bolasU;

    print numpoints
    dmed, dmax, c, s = np.random.random((4, numpoints))
    #y, e, c, s = np.random.random((4, numpoints))

    fig = plt.figure()
    plt.xlim(-0.5, 18.5)
    plt.ylim(-0.5, 18.5)
    plt.xlabel('dMed')
    plt.ylabel('dMax')
    color_data = np.random.random((numframes, numpoints)) * 10
    #print color_data


    #print colors;

    scat = plt.scatter(dmed, dmax, c=colors, s=s)
    
    ax=plt.gca()

    ani = animation.FuncAnimation(fig, update_plot, frames=xrange(numframes), interval=duration,
                                  fargs=(bolas, color_data, numpoints, numcons, maiordMax, scat, fig, ax))
    plt.show()

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
