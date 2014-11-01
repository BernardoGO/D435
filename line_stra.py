import matplotlib.pyplot as plt
import numpy as np
import csv
import datetime as dt
import matplotlib.dates as mdates
from matplotlib.lines import Line2D

csv_in = open('beleza.csv', 'rb')
myreader = csv.reader(csv_in)
bolas = []
maiordMax = 0
menordMax = 999999

maiorlvlsMe = []
menorlvlsMe = []
maiorlvlsMa = []
menorlvlsMa = []
#dates = []
for row in myreader:
        
	insc, data, dmed, dmax, hdmax,ramo,  = row
	bolas.append([str(insc), str(data), float(dmed), float(dmax)])

numcons =  len(set(tuple(x[0] for x in bolas)))
uniqueDates =   (set(tuple(x[1] for x in bolas)))

sortedDates = sorted(uniqueDates, key=lambda x: dt.datetime.strptime(x.rsplit(None, 1)[-1], '%Y-%m-%d'))
lendias = len(sortedDates)
#print sortedDates

#for dia in xrange(0, 39):
#	dates.append(bolas[1*dia][1])

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
defaultval =-258
print numcons
for cons in xrange(0, numcons):
	diacons = 0
	for dia in xrange(0, len(sortedDates)):
		
		try:	
			if bolas[(cons*39)+diacons][0] != bolas[(cons*39)+2][0]:
				datedBolas.append([bolas[(cons*39)+diacons][0], str(sortedDates[dia]), float(defaultval), float(defaultval)])
				print str(cons) + " " + str(diacons) + " " + str(dia) + " EI " + str(sortedDates[dia]) + " " + bolas[(cons*39)+2][0]+ " " +bolas[(cons*39)+diacons][0]
			
			elif str(bolas[(cons*39)+diacons][1]) != str(sortedDates[dia]):
				datedBolas.append([bolas[(cons*39)+diacons][0], str(sortedDates[dia]), float(defaultval), float(defaultval)])
				print str(cons) + " " + str(diacons) + " " + str(dia) + " IF " + str(sortedDates[dia]) 
			else:
				datedBolas.append(bolas[(cons*39)+diacons])
				print str(cons) + " " + str(diacons) + " " + str(dia) + " EL "+ str(sortedDates[dia])
				diacons = diacons + 1
				
		except: 
			print str(cons) + " " + str(diacons) + " " + str(dia) + " EX "+ str(sortedDates[dia])
			datedBolas.append([bolas[(cons*39)+2][0], str(sortedDates[dia]), float(defaultval), float(defaultval)])
			

totais = [] #[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]
colors = [] #0,0,0,0,0,0

for ih in xrange(0,numcons):
	totais.append([0,0])
	colors.append(0)

for cons in xrange(0, numcons):
	maiordMaxA = 0
	for dia in xrange(0, lendias):
		if datedBolas[(cons*lendias)+dia][3] != -258:
			maiordMaxA = maiordMaxA + datedBolas[(cons*lendias)+dia][3]

		totais[cons][1] = maiordMaxA
		totais[cons][0] = cons

totaisCres = sorted(totais, key=lambda a_entry: a_entry[1]) 
print totaisCres
for cons in xrange((numcons/2), (numcons)):
	colors[totaisCres[cons][0]] = 1;

strMaior = []
strMenor = []

for cons in xrange((numcons/2), (numcons)):
	colors[totaisCres[cons][0]] = 1;

print colors

for cons in xrange(0, numcons):
	if colors[cons] == 1:
		strMaior.extend(datedBolas[(cons*lendias):(cons*lendias)+lendias])
	else:
		strMenor.extend(datedBolas[(cons*lendias):(cons*lendias)+lendias])

print strMaior

#70
#0 70 140
#1 71 141
print " start " + str(len(strMaior))
for dia in xrange(0, lendias):
	for cons in xrange(0, (numcons)):
		try:
			#print " try" + str((cons*lendias)+dia) 
			#print " ts" + strMaior[cons][dia][3]
			if strMaior[(cons*lendias)+dia][3] != -258:
				dImx = strMaior[dia::lendias][cons][2]  /strMaior[dia::lendias][cons][3] if strMaior[dia::lendias][cons][3] else 0
				if dImx > 1:
					print " ERROR: " 
					print " DIMX: " + str(dImx)
				print str(strMaior[dia::lendias][cons][2]) + " / " +str(strMaior[dia::lendias][cons][3])
				
				if float(dImx) >= float(maiordMax):
					maiordMax = float(dImx)
				if float(dImx) <= float(menordMax):      
					menordMax = float(dImx)
			else:
				y = 3
				
		except: 
			continue

	maiorlvlsMa.append(maiordMax)
	if menordMax == 999999: 
		menordMax = 0
	menorlvlsMa.append(menordMax)

	maiordMax = 0
	menordMax = 999999

for dia in xrange(0, lendias):
	for cons in xrange(0, (numcons)):
		try:
			#print " try" + str((cons*lendias)+dia) 
			#print " ts" + strMaior[cons][dia][3]
			if strMenor[(cons*lendias)+dia][3] != -258:
				dImx = strMenor[dia::lendias][cons][2]  /strMenor[dia::lendias][cons][3] if strMenor[dia::lendias][cons][3] else 0
				if dImx > 1:
					print " ERROR: " 
					print " DIMX: " + str(dImx)
				print str(strMenor[dia::lendias][cons][2]) + " / " +str(strMenor[dia::lendias][cons][3])
				
				if float(dImx) >= float(maiordMax):
					maiordMax = float(dImx)
				if float(dImx) <= float(menordMax):      
					menordMax = float(dImx)
			else:
				y = 3
				
		except: 
			continue

	maiorlvlsMe.append(maiordMax)
	if menordMax == 999999: 
		menordMax = 0
	menorlvlsMe.append(menordMax)

	maiordMax = 0
	menordMax = 999999




c = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in sortedDates]

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
print maiorlvlsMa
plt.xlabel('Dias')
plt.ylabel('Fator de Carga')
 
#plt.ylim(0, 1)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(c,maiorlvlsMa, label='maximo', marker='>', color="#FF0000" )
plt.plot(c,menorlvlsMa , label='minimo', marker='>', color="#0000FF")

plt.plot(c,maiorlvlsMe, label='maximo', marker='<', color="#FF0000" )
plt.plot(c,menorlvlsMe , label='minimo', marker='<', color="#0000FF")
plt.gcf().autofmt_xdate()
plt.tick_params(axis='x', labelsize=8)
legend = plt.legend(loc='upper left', shadow=True, fontsize='x-large')
legend.get_frame().set_facecolor('#AAAACC')

plt.show()






















