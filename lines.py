import matplotlib.pyplot as plt
import numpy as np
import csv
import datetime as dt
import matplotlib.dates as mdates
from matplotlib.lines import Line2D

csv_in = open('celulose.csv', 'rb')
myreader = csv.reader(csv_in)
bolas = []
maiordMax = 0
menordMax = 999999

maiorlvls = []
menorlvls = []
dates = []
for row in myreader:
        
        insc, data, dmed, dmax, hdmax,ramo,  = row
        #if dmax > maiordMax:
        #    maiordMax = float(dmax)
        bolas.append([str(insc), str(data), float(dmed), float(dmax)])

numcons =  len(set(tuple(x[0] for x in bolas)))


print numcons






for dia in xrange(0, 39):

    for cons in xrange(0, numcons):
        try:
            print str(dia) + " - " + str(cons)
            dImx = bolas[dia::39][cons][2]/bolas[dia::39][cons][3] if bolas[dia::39][cons][3] else 0
            #dImx = bolas[cons*dia][2]
            #print dImx
        
            print bolas[dia::39][cons]
        
            if dImx >= maiordMax:
                    maiordMax = dImx
                    print str(bolas[dia::39][cons][2]) + "/" + str(bolas[dia::39][cons][3]) + "=" + str(dImx)
            if dImx <= menordMax:
                    print str(bolas[dia::39][cons][2]) + "/" + str(bolas[dia::39][cons][3]) + "=" + str(dImx)            
                    menordMax = dImx
        except: 
                continue
            
    dates.append(bolas[1*dia][1])
    maiorlvls.append(maiordMax)
    menorlvls.append(menordMax)
    print str(maiordMax) + " " + str(menordMax)
    #print bolas[1*dia][1]
    maiordMax = 0
    menordMax = 999999



#x = np.arange(len(maiorlvls))

x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in dates]

#plt.plot_date(x, maiorlvls, fmt="bo", tz=None, xdate=True)
#splt.plot_date(x, menorlvls, fmt="bo", tz=None, xdate=True)

#plt.show()


marker_style = dict(linestyle=':', color='cornflowerblue', markersize=10)
# Filter out filled markers and marker settings that do nothing.
unfilled_markers = [m for m, func in Line2D.markers.iteritems()
                    if func != 'nothing' and m not in Line2D.filled_markers]
unfilled_markers = sorted(unfilled_markers)[::-1]  # Reverse-sort for pretty

#mx = zip(axes, split_list(Line2D.filled_markers))

def nice_repr(text):
    return repr(text).lstrip('u')

plt.xlabel('Dias')
plt.ylabel('Fator de Carga')
#plt.ylim(-1, 7)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(x,maiorlvls, 'ro', label='maximo',marker='<', color="#FF0000" )
plt.plot(x,menorlvls , 'ro', label='minimo',marker='<', color="#0000FF")
plt.gcf().autofmt_xdate()
legend = plt.legend(loc='upper left', shadow=True, fontsize='x-large')
legend.get_frame().set_facecolor('#AAAACC')
plt.show()





















