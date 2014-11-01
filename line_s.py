import matplotlib.pyplot as plt
import numpy as np
import csv
import datetime as dt
import matplotlib.dates as mdates

csv_in = open('beleza.csv', 'rb')
myreader = csv.reader(csv_in)
bolas = []


maiorlvls = []
menorlvls = []
dates = []
for row in myreader:
        
	insc, data, dmed, dmax, hdmax,ramo,  = row
	bolas.append([str(insc), str(data), float(dmed), float(dmax)])

numcons =  len(set(tuple(x[0] for x in bolas)))
uniqueDates =   (set(tuple(x[1] for x in bolas)))

sortedDates = sorted(uniqueDates, key=lambda x: dt.datetime.strptime(x.rsplit(None, 1)[-1], '%Y-%m-%d'))
lendias = len(sortedDates)
#print sortedDates

for dia in xrange(0, 39):
	dates.append(bolas[1*dia][1])

#0 39 78
#0,1,2,3,4,5,6,7,8,9,10,11
#0,1,2,3,4

#cons 2 - 0,2,4,8
#cons 2 - 39,40,41,42
#cons 5 - 0,5,10,15
#cons 5 - 156, 157, 158
x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in sortedDates]
#(cons*39)+diacons
#cons 5 - 156, 157
#cons 0 - 0,1
datedBolas = []
print numcons
for cons in xrange(0, numcons):
	diacons = 0
	for dia in xrange(0, len(sortedDates)):
		
		try:	
			if str(bolas[(cons*39)+diacons][1]) != str(sortedDates[dia]):
				datedBolas.append([bolas[(cons*39)+diacons][0], str(sortedDates[dia]), float(0), float(0)])
				print str(cons) + " " + str(diacons) + " " + str(dia) + " IF " + str(sortedDates[dia])
			elif bolas[(cons*39)+diacons][0] != bolas[(cons*39)+2][0]:
				datedBolas.append([bolas[(cons*39)+diacons][0], str(sortedDates[dia]), float(0), float(0)])
				print str(cons) + " " + str(diacons) + " " + str(dia) + " EI " + str(sortedDates[dia]) + " " + bolas[(cons*39)+2][0]+ " " + bolas[(cons*39)+diacons][0]
			else:
				datedBolas.append(bolas[(cons*39)+diacons])
				print str(cons) + " " + str(diacons) + " " + str(dia) + " EL "+ str(sortedDates[dia])
				diacons = diacons + 1
				
		except: 
			datedBolas.append([bolas[(cons*39)+2][0], str(sortedDates[dia]), float(0), float(0)])
			print str(cons) + " " + str(diacons) + " " + str(dia) + " EX "+ str(sortedDates[dia])

plt.xlabel('Dias')
plt.ylabel('Fator de Carga')
#plt.ylim(-1, 7)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
#plt.plot(x,maiorlvls, label='maximo')
#plt.plot(x,menorlvls, label='minimo')

#print datedBolas
plt.rc('axes', color_cycle=['r', 'g', 'b', 'y'])
n=numcons+1
color=iter(plt.cm.rainbow(np.linspace(0,1,n)))

print numcons
for cons in xrange(0, numcons):
	c=next(color)
	print len(x)
	print len(tuple(x[2]/ x[3] if x[3] else 0 for x in datedBolas[(cons*lendias):(cons*lendias)+lendias]))
	plt.plot(x,    tuple(x[2]/ x[3] if x[3] else 0 for x in datedBolas[(cons*lendias):(cons*lendias)+lendias]), 'ro', label='Consumidor ' + str(cons) , c=c)
	plt.plot(x,    tuple(x[2]/ x[3] if x[3] else 0 for x in datedBolas[(cons*lendias):(cons*lendias)+lendias]), '--' , c=c)

plt.gcf().autofmt_xdate()
legend = plt.legend(loc='upper left', shadow=True, fontsize='small')
legend.get_frame().set_facecolor('#AAAACC')
plt.tick_params(axis='x', labelsize=8)
plt.show()





















