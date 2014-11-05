#todos os grupos novos, media das medias, titulos(grupo, dias)

import sys

import matplotlib.patches as patches
import matplotlib.path as path
from numpy import arange
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
import numpy as np
import csv
import datetime as dt
import datetime
import matplotlib
import matplotlib.dates as mdates
from matplotlib.lines import Line2D
import matplotlib.ticker as ticker
class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BACK_LRED = '\033[101m' 
sume = 0
nb_plots_per_page = 4
grid_size = (nb_plots_per_page, 1)

###########################################################
grupo = str(sys.argv[1]).replace("grupo", "")
print "aaaaaaaaaaaa"+"\n".join(sys.argv[1])
useFC = True
mdiasme = 38
daysToRemove = [5,6]
removeFeriados = True
inserirFeriados = False
dateToRemove = ["2012-06-07"]
TresGraficos = False
CalcularErro = True
writeTable = True
###########################################################

csv_in = open(str(grupo)+'grp.csv', 'rb')
rep = open("table_report.txt", "a+")
myreader = csv.reader(csv_in)
bolas = []
maiordMax = 0
menordMax = 999999
week   = [ 
              'Segunda', 
              'Terca', 
              'Quarta', 
              'Quinta',  
              'Sexta', 
              'Sabado', 'Domingo']
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

#(cons*39)+diacons
#cons 5 - 156, 157
#cons 0 - 0,1
datedBolas = []
defaultval =-258
removeddays = 0
usedSortedDates = []

print numcons
for cons in xrange(0, numcons):
	diacons = 0
	for dia in xrange(0, len(sortedDates)):

		try:	#removeFeriados - inserirFeriados
			if bolas[(cons*mdiasme)+diacons][0] != bolas[(cons*mdiasme)+2][0]:
				if (datetime.datetime.strptime(sortedDates[dia], '%Y-%m-%d').weekday() in daysToRemove or 
					(sortedDates[dia] in dateToRemove and removeFeriados)):
					if inserirFeriados == True and (sortedDates[dia] in dateToRemove):
						datedBolas.append([bolas[(cons*mdiasme)+diacons][0], str(sortedDates[dia]), float(defaultval), float(defaultval)])
						if cons == 0: usedSortedDates.append(sortedDates[dia])
						print str(cons) + " " + str(diacons) + " " + str(dia) + " EI " + str(sortedDates[dia]) + " " + bolas[(cons*mdiasme)+2][0]+ " "
					#diacons = diacons + 1
					print  bcolors.WARNING + "removed " + sortedDates[dia] + bcolors.ENDC
					
					removeddays = removeddays + 1
				else:
			
					datedBolas.append([bolas[(cons*mdiasme)+diacons][0], str(sortedDates[dia]), float(defaultval), float(defaultval)])
					if cons == 0: usedSortedDates.append(sortedDates[dia])
					print str(cons) + " " + str(diacons) + " " + str(dia) + " EI " + str(sortedDates[dia]) + " " + bolas[(cons*mdiasme)+2][0]+ " " +bolas[(cons*mdiasme)+diacons][0]
			
			elif str(bolas[(cons*mdiasme)+diacons][1]) != str(sortedDates[dia]):
				if (datetime.datetime.strptime(sortedDates[dia], '%Y-%m-%d').weekday() in daysToRemove or 
					(sortedDates[dia] in dateToRemove and removeFeriados)):
					if inserirFeriados == True and (sortedDates[dia] in dateToRemove):
						if cons == 0: usedSortedDates.append(sortedDates[dia])
						datedBolas.append([bolas[(cons*mdiasme)+diacons][0], str(sortedDates[dia]), float(defaultval), float(defaultval)])
						print str(cons) + " " + str(diacons) + " " + str(dia) + " IF " + str(sortedDates[dia]) 						
					#diacons = diacons + 1
					removeddays = removeddays + 1
					print  bcolors.WARNING + "removed " + sortedDates[dia] + bcolors.ENDC
				else:
					if cons == 0: usedSortedDates.append(sortedDates[dia])
					datedBolas.append([bolas[(cons*mdiasme)+diacons][0], str(sortedDates[dia]), float(defaultval), float(defaultval)])
					print str(cons) + " " + str(diacons) + " " + str(dia) + " IF " + str(sortedDates[dia]) 
			else:
				if (datetime.datetime.strptime(sortedDates[dia], '%Y-%m-%d').weekday() in daysToRemove or 
					(sortedDates[dia] in dateToRemove and removeFeriados)):
					if inserirFeriados == True and (sortedDates[dia] in dateToRemove):
						if cons == 0: usedSortedDates.append(sortedDates[dia])
						datedBolas.append(bolas[(cons*mdiasme)+diacons])
						print str(cons) + " " + str(diacons) + " " + str(dia) + " EL "+ str(sortedDates[dia])
						diacons = diacons + 1
					removeddays = removeddays + 1
					diacons = diacons + 1

					print  bcolors.WARNING + "removed " + sortedDates[dia] + bcolors.ENDC
				else:
					if cons == 0: usedSortedDates.append(sortedDates[dia])
					datedBolas.append(bolas[(cons*mdiasme)+diacons])
					print str(cons) + " " + str(diacons) + " " + str(dia) + " EL "+ str(sortedDates[dia])
					diacons = diacons + 1
				
		except: 
			o = 9
			if (datetime.datetime.strptime(sortedDates[dia], '%Y-%m-%d').weekday() in daysToRemove or 
					(sortedDates[dia] in dateToRemove and removeFeriados)):
				if inserirFeriados == True and (sortedDates[dia] in dateToRemove):
					print "exp added " + sortedDates[dia]
					if cons == 0: usedSortedDates.append(sortedDates[dia])
					print str(cons) + "/" + str(numcons) + " " + str(diacons) + " " + str(dia) + " EX "+ str(sortedDates[dia])
					datedBolas.append([bolas[(cons*mdiasme)+2][0], str(sortedDates[dia]), float(defaultval), float(defaultval)])
				#diacons = diacons + 1
	
				print  bcolors.WARNING + "removed " + sortedDates[dia] + bcolors.ENDC
					
				removeddays = removeddays + 1
			else:
				print "exp added " + sortedDates[dia]
				if cons == 0: usedSortedDates.append(sortedDates[dia])
				print str(cons) + "/" + str(numcons) + " " + str(diacons) + " " + str(dia) + " EX "+ str(sortedDates[dia])
				datedBolas.append([bolas[(cons*mdiasme)+2][0], str(sortedDates[dia]), float(defaultval), float(defaultval)])

print tuple(x[1] for x in datedBolas)		

totais = [] #[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]
colors = [] #0,0,0,0,0,0

print lendias
sortedDates = usedSortedDates
print len(usedSortedDates)
lendias = len(usedSortedDates)

print sortedDates

x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in sortedDates]

for ih in xrange(0,numcons):
	totais.append([0,0])
	colors.append(0)

daycons = []
coday = []
coday1 = []
coday2 = []
for dia in xrange(0, lendias ):
	coday.append(0)
	coday1.append(0)
	coday2.append(0)


for cons in xrange(0, numcons):
	hoje = []
	for dia in xrange(0, lendias ):
		hoje.append(0)
	daycons.append(hoje)


for cons in xrange(0, numcons):
	maiordMaxA = 0
	for dia in xrange(0, lendias ):
		
		if datedBolas[(cons*lendias)+dia][3] != -258:
			maiordMaxA = maiordMaxA + datedBolas[(cons*lendias)+dia][3]
			coday[dia] = coday[dia] + 1
			print "Teste: OK"

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
defvaldiv = 3;
totDias1 = []
totDias2 = []
totDiasTod = []
totErro1 = []
totErro2 = []
numerr1 = 0
numerr2 = 0
tottotais = 0
for dia in xrange(0, lendias ):
	maiordMaxA = 0
	maiordMaxB = 0
	countA = 0
	countB = 0
	for cons in xrange(0, numcons):
		if datedBolas[(cons*lendias)+dia][3] != -258:
			
			if colors[cons] == 1:
				daycons[cons][dia]=1
				print "Estrato: 1 OK"
				if useFC == True:
					divnum = datedBolas[(cons*lendias)+dia][3]
				else:
					divnum = 1
				dksi = ( datedBolas[(cons*lendias)+dia][2] / divnum if divnum else defvaldiv)
				if dksi != defvaldiv:
					coday1[dia] = coday1[dia] + 1
					countA = countA + 1
					maiordMaxA = maiordMaxA + dksi
				
			else:
				daycons[cons][dia]=1
				print "Estrato: 2 OK"
				if useFC == True:
					divnum = datedBolas[(cons*lendias)+dia][3]
				else:
					divnum = 1
				dksi = ( datedBolas[(cons*lendias)+dia][2] / divnum if divnum else defvaldiv)
				if dksi != defvaldiv:
					coday2[dia] = coday2[dia] + 1
					countB = countB + 1
					maiordMaxB = maiordMaxB + dksi
	mediaUF = (maiordMaxA+maiordMaxB)/(countA+countB) if countA else 0
	
	tot1 = maiordMaxA/countA if countA else 0
	tot2 = maiordMaxB/countB if countB else 0
	totDiasTod.append(mediaUF)
	totDias1.append(tot1)
	totDias2.append(tot2)
	err1 = (tot1-mediaUF)/mediaUF if (tot1 != 0 and tot2 != 0) else defvaldiv
	err2 = (tot2-mediaUF)/mediaUF if (tot1 != 0 and tot2 != 0) else defvaldiv
	if err1 == defvaldiv: 
		err1 = 0
	else:
		numerr1 = numerr1 + 1

	if err2 == defvaldiv: 
		err2 = 0
	else:
		numerr2 = numerr2 + 1

	if err1 != defvaldiv or err2 != defvaldiv:
		tottotais = tottotais + 1
	totErro1.append(err1)
	totErro2.append(err2)
	

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

				if useFC == True:
					divnum = strMaior[dia::lendias][cons][3]
				else:
					divnum = 1

				dImx = strMaior[dia::lendias][cons][2]  /divnum if divnum else defvaldiv
				
				if dImx > 1 and dImx != defvaldiv:
					print " ERROR: " 
					print " DIMX: " + str(dImx) + " len dias: " + str(lendias) + "/" + str(dia) + "/" + str(cons)
					
				#print str(strMaior[dia::lendias][cons][2]) + " / " +str(strMaior[dia::lendias][cons][3])
				
				if dImx == defvaldiv:
					dImx = 1
				else:
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

				if useFC == True:
					divnum = strMenor[dia::lendias][cons][3]
				else:
					divnum = 1


				dImx = strMenor[dia::lendias][cons][2]  /divnum if divnum else defvaldiv
			
				#print str(strMenor[dia::lendias][cons][2]) + " / " +str(strMenor[dia::lendias][cons][3])
				

				if dImx > 1 and dImx != defvaldiv:
					print " ERROR: " 
					print " DIMX: " + str(dImx)
					
				#print str(strMaior[dia::lendias][cons][2]) + " / " +str(strMaior[dia::lendias][cons][3])
				
				if dImx == defvaldiv:
					dImx = 1
				else:
					if float(dImx) >= float(maiordMax):
						maiordMax = float(dImx)
					if float(dImx) <= float(menordMax):      
						menordMax = float(dImx)

				#if float(dImx) >= float(maiordMax):
				#	maiordMax = float(dImx)
				#if float(dImx) <= float(menordMax):      
				#	menordMax = float(dImx)
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

unfilled_markers = [m for m, func in Line2D.markers.iteritems()
                    if func != 'nothing' and m not in Line2D.filled_markers]
unfilled_markers = sorted(unfilled_markers)[::-1]  

#mx = zip(axes, split_list(Line2D.filled_markers))

def nice_repr(text):
    return repr(text).lstrip('u')

print " len dias: " + str(lendias) 

#print maiorlvlsMa
plt.xlabel('Dias')
plt.ylabel('Fator de Carga')
print len(maiorlvlsMa)
print len(c)

plt.figure(1)#, figsize=(800.0, 500.0)
#plt.figure.tight_layout()


ax4 = plt.subplot2grid(grid_size, (sume % nb_plots_per_page, 0))
#ax4= plt.subplot(4,1,sume)
#axV = ax.twinx()
hhd = []
hhd.extend(maiorlvlsMa)
hhd.extend(maiorlvlsMe)
maiorlld =  max(hhd)
maiorlld = maiorlld + maiorlld*0.10
sume = sume+1

#matplotlib.rc('font', size=3)
#plt.ylim(0, maiorlld )
dias_remov = "";
for dise in xrange(0,6):
	if dise not in daysToRemove:
		dias_remov = dias_remov + " " + week[dise]

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

#plt.title(dias_remov + '\nGrupo:' + str(grupo) + " Num. Consumidores: " + str(numcons) + '\n Maior Estrato N.:'+str(len(strMaior)/lendias) )
figtext(.5,.95,'Grupo:' + str(grupo), fontsize=14, ha='center')
figtext(.5,.93,"NG: " + str(numcons),ha='center',fontsize=10 )
figtext(.5,.91,'Uteis Estrato 1 - Consumidores de Grande Porte ',fontsize=10,ha='center')# NE 1:'+str(len(strMaior)/lendias)
ax4.set_ylabel('FC')
#plt.plot(c,maiorlvlsMa, label='Maximo', marker='.', color="#FF0000" )
#plt.plot(c,totDias1, label='Media E.1', marker='+', color="#000000" )
#plt.plot(c,totDiasTod , label='Media Geral', marker='.', color="#5B913C", linewidth=0.5)
width=0.2
ax4.bar(c, coday1, alpha=0.2)

#if TresGraficos == False:
#	plt.plot(c,totDiasTod, label='media -', marker='x', color="#000055")
#	plt.plot(c,totDias2, label='media <', marker='.', color="#000000" )

	
#plt.plot(c,menorlvlsMa , label='Minimo', marker='x', color="#0000FF")
plt.gcf().autofmt_xdate()
plt.tick_params(axis='x', labelsize=8)

legend = plt.legend(loc='upper left', shadow=True, fontsize='xx-small')
#legend.get_frame().set_facecolor('#AAAACC')
plt.tick_params(axis='x',which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='off')
#ax224 = ax4.twinx()
#ax224.bar(c, coday1, alpha=0.2)

  

ax24 = plt.subplot2grid(grid_size, (sume % nb_plots_per_page, 0))
#ax24 = plt.subplot(4,1,sume+1)
#plt.ylim(0, maiorlld )
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
#plt.title('Menor Estrato N.:' + str(len(strMenor)/lendias))
figtext(.5,.725,'Uteis Estrato 2 - Consumidores de Pequeno Porte', fontsize=10, ha='center')
#figtext(.5,.70,'NE 2.:' + str(len(strMenor)/lendias) ,ha='center',fontsize=8 )
#plt.plot(c,maiorlvlsMe, label='Maximo', marker='.', color="#FF0000" )
#plt.plot(c,totDias2, label='Media E.2', marker='+', color="#000000" )
ax24.bar(c, coday2, alpha=0.2)
width=0.2
sume = sume+1
#plt.plot(c,totDias1 , label='media E.1', marker='.', color="#FFE4B5" , linewidth=0.5 )
#plt.plot(c,totDiasTod , label='Media Geral', marker='.', color="#5B913C", linewidth=0.5)
#plt.plot(c,menorlvlsMe , label='Minimo', marker='x', color="#0000FF")
ax24.set_ylabel('FC')
#plt.gcf().autofmt_xdate()
plt.tick_params(axis='x', labelsize=4)
plt.xticks( rotation='vertical')
#legend = plt.legend(loc='upper left', shadow=True, fontsize='xx-small')
#for tick in plt.gca().xaxis.iter_ticks():
    #tick[0].label2On = True
    #tick[0].label1On = False
    #tick[0].label2.set_rotation('vertical')
#legend.get_frame().set_facecolor('#AAAACC')
#ax224 = ax24.twinx()



###########################################################
grupo = str(sys.argv[1]).replace("grupo", "")
print "aaaaaaaaaaaa"+"\n".join(sys.argv[1])
useFC = True
mdiasme = 38
daysToRemove = [0,1,2,3,4]
removeFeriados = False
inserirFeriados = True
dateToRemove = ["2012-06-07"]
TresGraficos = False
CalcularErro = True
writeTable = True
###########################################################

csv_in = open(str(grupo)+'grp.csv', 'rb')
rep = open("table_report.txt", "a+")
myreader = csv.reader(csv_in)
bolas = []
maiordMax = 0
menordMax = 999999
week   = [ 
              'Segunda', 
              'Terca', 
              'Quarta', 
              'Quinta',  
              'Sexta', 
              'Sabado', 'Domingo']
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

#(cons*39)+diacons
#cons 5 - 156, 157
#cons 0 - 0,1
datedBolas = []
defaultval =-258
removeddays = 0
usedSortedDates = []

print numcons
for cons in xrange(0, numcons):
	diacons = 0
	for dia in xrange(0, len(sortedDates)):

		try:	#removeFeriados - inserirFeriados
			if bolas[(cons*mdiasme)+diacons][0] != bolas[(cons*mdiasme)+2][0]:
				if (datetime.datetime.strptime(sortedDates[dia], '%Y-%m-%d').weekday() in daysToRemove or 
					(sortedDates[dia] in dateToRemove and removeFeriados)):
					if inserirFeriados == True and (sortedDates[dia] in dateToRemove):
						datedBolas.append([bolas[(cons*mdiasme)+diacons][0], str(sortedDates[dia]), float(defaultval), float(defaultval)])
						if cons == 0: usedSortedDates.append(sortedDates[dia])
						print str(cons) + " " + str(diacons) + " " + str(dia) + " EI " + str(sortedDates[dia]) + " " + bolas[(cons*mdiasme)+2][0]+ " "
					#diacons = diacons + 1
					print  bcolors.WARNING + "removed " + sortedDates[dia] + bcolors.ENDC
					
					removeddays = removeddays + 1
				else:
			
					datedBolas.append([bolas[(cons*mdiasme)+diacons][0], str(sortedDates[dia]), float(defaultval), float(defaultval)])
					if cons == 0: usedSortedDates.append(sortedDates[dia])
					print str(cons) + " " + str(diacons) + " " + str(dia) + " EI " + str(sortedDates[dia]) + " " + bolas[(cons*mdiasme)+2][0]+ " " +bolas[(cons*mdiasme)+diacons][0]
			
			elif str(bolas[(cons*mdiasme)+diacons][1]) != str(sortedDates[dia]):
				if (datetime.datetime.strptime(sortedDates[dia], '%Y-%m-%d').weekday() in daysToRemove or 
					(sortedDates[dia] in dateToRemove and removeFeriados)):
					if inserirFeriados == True and (sortedDates[dia] in dateToRemove):
						if cons == 0: usedSortedDates.append(sortedDates[dia])
						datedBolas.append([bolas[(cons*mdiasme)+diacons][0], str(sortedDates[dia]), float(defaultval), float(defaultval)])
						print str(cons) + " " + str(diacons) + " " + str(dia) + " IF " + str(sortedDates[dia]) 						
					#diacons = diacons + 1
					removeddays = removeddays + 1
					print  bcolors.WARNING + "removed " + sortedDates[dia] + bcolors.ENDC
				else:
					if cons == 0: usedSortedDates.append(sortedDates[dia])
					datedBolas.append([bolas[(cons*mdiasme)+diacons][0], str(sortedDates[dia]), float(defaultval), float(defaultval)])
					print str(cons) + " " + str(diacons) + " " + str(dia) + " IF " + str(sortedDates[dia]) 
			else:
				if (datetime.datetime.strptime(sortedDates[dia], '%Y-%m-%d').weekday() in daysToRemove or 
					(sortedDates[dia] in dateToRemove and removeFeriados)):
					if inserirFeriados == True and (sortedDates[dia] in dateToRemove):
						if cons == 0: usedSortedDates.append(sortedDates[dia])
						datedBolas.append(bolas[(cons*mdiasme)+diacons])
						print str(cons) + " " + str(diacons) + " " + str(dia) + " EL "+ str(sortedDates[dia])
						diacons = diacons + 1
					removeddays = removeddays + 1
					diacons = diacons + 1

					print  bcolors.WARNING + "removed " + sortedDates[dia] + bcolors.ENDC
				else:
					if cons == 0: usedSortedDates.append(sortedDates[dia])
					datedBolas.append(bolas[(cons*mdiasme)+diacons])
					print str(cons) + " " + str(diacons) + " " + str(dia) + " EL "+ str(sortedDates[dia])
					diacons = diacons + 1
				
		except: 
			o = 9
			if (datetime.datetime.strptime(sortedDates[dia], '%Y-%m-%d').weekday() in daysToRemove or 
					(sortedDates[dia] in dateToRemove and removeFeriados)):
				if inserirFeriados == True and (sortedDates[dia] in dateToRemove):
					print "exp added " + sortedDates[dia]
					if cons == 0: usedSortedDates.append(sortedDates[dia])
					print str(cons) + "/" + str(numcons) + " " + str(diacons) + " " + str(dia) + " EX "+ str(sortedDates[dia])
					datedBolas.append([bolas[(cons*mdiasme)+2][0], str(sortedDates[dia]), float(defaultval), float(defaultval)])
				#diacons = diacons + 1
	
				print  bcolors.WARNING + "removed " + sortedDates[dia] + bcolors.ENDC
					
				removeddays = removeddays + 1
			else:
				print "exp added " + sortedDates[dia]
				if cons == 0: usedSortedDates.append(sortedDates[dia])
				print str(cons) + "/" + str(numcons) + " " + str(diacons) + " " + str(dia) + " EX "+ str(sortedDates[dia])
				datedBolas.append([bolas[(cons*mdiasme)+2][0], str(sortedDates[dia]), float(defaultval), float(defaultval)])

print tuple(x[1] for x in datedBolas)		

totais = [] #[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]
colors = [] #0,0,0,0,0,0

print lendias
sortedDates = usedSortedDates
print len(usedSortedDates)
lendias = len(usedSortedDates)

print sortedDates

x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in sortedDates]

for ih in xrange(0,numcons):
	totais.append([0,0])
	colors.append(0)

daycons = []
coday = []
coday1 = []
coday2 = []
for dia in xrange(0, lendias ):
	coday.append(0)
	coday1.append(0)
	coday2.append(0)


for cons in xrange(0, numcons):
	hoje = []
	for dia in xrange(0, lendias ):
		hoje.append(0)
	daycons.append(hoje)


for cons in xrange(0, numcons):
	maiordMaxA = 0
	for dia in xrange(0, lendias ):
		
		if datedBolas[(cons*lendias)+dia][3] != -258:
			maiordMaxA = maiordMaxA + datedBolas[(cons*lendias)+dia][3]
			coday[dia] = coday[dia] + 1
			print "Teste: OK"

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
defvaldiv = 3;
totDias1 = []
totDias2 = []
totDiasTod = []
totErro1 = []
totErro2 = []
numerr1 = 0
numerr2 = 0
tottotais = 0
for dia in xrange(0, lendias ):
	maiordMaxA = 0
	maiordMaxB = 0
	countA = 0
	countB = 0
	for cons in xrange(0, numcons):
		if datedBolas[(cons*lendias)+dia][3] != -258:
			
			if colors[cons] == 1:
				daycons[cons][dia]=1
				print "Estrato: 1 OK"
				if useFC == True:
					divnum = datedBolas[(cons*lendias)+dia][3]
				else:
					divnum = 1
				dksi = ( datedBolas[(cons*lendias)+dia][2] / divnum if divnum else defvaldiv)
				if dksi != defvaldiv:
					coday1[dia] = coday1[dia] + 1
					countA = countA + 1
					maiordMaxA = maiordMaxA + dksi
				
			else:
				daycons[cons][dia]=1
				print "Estrato: 2 OK"
				if useFC == True:
					divnum = datedBolas[(cons*lendias)+dia][3]
				else:
					divnum = 1
				dksi = ( datedBolas[(cons*lendias)+dia][2] / divnum if divnum else defvaldiv)
				if dksi != defvaldiv:
					coday2[dia] = coday2[dia] + 1
					countB = countB + 1
					maiordMaxB = maiordMaxB + dksi
	mediaUF = (maiordMaxA+maiordMaxB)/(countA+countB) if countA else 0
	
	tot1 = maiordMaxA/countA if countA else 0
	tot2 = maiordMaxB/countB if countB else 0
	totDiasTod.append(mediaUF)
	totDias1.append(tot1)
	totDias2.append(tot2)
	err1 = (tot1-mediaUF)/mediaUF if (tot1 != 0 and tot2 != 0) else defvaldiv
	err2 = (tot2-mediaUF)/mediaUF if (tot1 != 0 and tot2 != 0) else defvaldiv
	if err1 == defvaldiv: 
		err1 = 0
	else:
		numerr1 = numerr1 + 1

	if err2 == defvaldiv: 
		err2 = 0
	else:
		numerr2 = numerr2 + 1

	if err1 != defvaldiv or err2 != defvaldiv:
		tottotais = tottotais + 1
	totErro1.append(err1)
	totErro2.append(err2)
	

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

				if useFC == True:
					divnum = strMaior[dia::lendias][cons][3]
				else:
					divnum = 1

				dImx = strMaior[dia::lendias][cons][2]  /divnum if divnum else defvaldiv
				
				if dImx > 1 and dImx != defvaldiv:
					print " ERROR: " 
					print " DIMX: " + str(dImx) + " len dias: " + str(lendias) + "/" + str(dia) + "/" + str(cons)
					
				#print str(strMaior[dia::lendias][cons][2]) + " / " +str(strMaior[dia::lendias][cons][3])
				
				if dImx == defvaldiv:
					dImx = 1
				else:
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

				if useFC == True:
					divnum = strMenor[dia::lendias][cons][3]
				else:
					divnum = 1


				dImx = strMenor[dia::lendias][cons][2]  /divnum if divnum else defvaldiv
			
				#print str(strMenor[dia::lendias][cons][2]) + " / " +str(strMenor[dia::lendias][cons][3])
				

				if dImx > 1 and dImx != defvaldiv:
					print " ERROR: " 
					print " DIMX: " + str(dImx)
					
				#print str(strMaior[dia::lendias][cons][2]) + " / " +str(strMaior[dia::lendias][cons][3])
				
				if dImx == defvaldiv:
					dImx = 1
				else:
					if float(dImx) >= float(maiordMax):
						maiordMax = float(dImx)
					if float(dImx) <= float(menordMax):      
						menordMax = float(dImx)

				#if float(dImx) >= float(maiordMax):
				#	maiordMax = float(dImx)
				#if float(dImx) <= float(menordMax):      
				#	menordMax = float(dImx)
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

unfilled_markers = [m for m, func in Line2D.markers.iteritems()
                    if func != 'nothing' and m not in Line2D.filled_markers]
unfilled_markers = sorted(unfilled_markers)[::-1]  

#mx = zip(axes, split_list(Line2D.filled_markers))

def nice_repr(text):
    return repr(text).lstrip('u')

print " len dias: " + str(lendias) 

#print maiorlvlsMa
plt.xlabel('Dias')
plt.ylabel('Fator de Carga')
print len(maiorlvlsMa)
print len(c)

#plt.figure(1)#, figsize=(800.0, 500.0)
#plt.figure.tight_layout()



ax = plt.subplot2grid(grid_size, (sume % nb_plots_per_page, 0))
#ax= plt.subplot(4,1,sume)
#axV = ax.twinx()
hhd = []
hhd.extend(maiorlvlsMa)
hhd.extend(maiorlvlsMe)
maiorlld =  max(hhd)
maiorlld = maiorlld + maiorlld*0.10
sume = sume+1

#matplotlib.rc('font', size=3)
#plt.ylim(0, maiorlld )
dias_remov = "";
for dise in xrange(0,6):
	if dise not in daysToRemove:
		dias_remov = dias_remov + " " + week[dise]

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

#plt.title(dias_remov + '\nGrupo:' + str(grupo) + " Num. Consumidores: " + str(numcons) + '\n Maior Estrato N.:'+str(len(strMaior)/lendias) )
#figtext(.5,.95,'Dias Uteis Grupo:' + str(grupo), fontsize=14, ha='center')
#figtext(.5,.93,"NG: " + str(numcons),ha='center',fontsize=10 )
#figtext(.5,.91,'Estrato 1 - Consumidores de Grande Porte  NE 1:'+str(len(strMaior)/lendias),fontsize=10,ha='center')
figtext(.5,.54,'Nao Uteis Estrato 1 - Consumidores de Grande Porte', fontsize=10, ha='center')
ax.set_ylabel('FC')
#plt.plot(c,maiorlvlsMa, label='Maximo', marker='.', color="#FF0000" )
#plt.plot(c,totDias1, label='Media E.1', marker='+', color="#000000" )
#plt.plot(c,totDiasTod , label='Media Geral', marker='.', color="#5B913C", linewidth=0.5)
width=0.2




	
#plt.plot(c,menorlvlsMa , label='Minimo', marker='x', color="#0000FF")
plt.gcf().autofmt_xdate()
plt.tick_params(axis='x', labelsize=8)

legend = plt.legend(loc='upper left', shadow=True, fontsize='xx-small')
#legend.get_frame().set_facecolor('#AAAACC')
plt.tick_params(axis='x',which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='off')
#ax22 = ax.twinx()
ax.bar(c, coday1, alpha=0.2)

if TresGraficos == True:
	#0,21
	ax1 = plt.subplot(4,1,sume)
	if CalcularErro == False:
		plt.ylim(0, maiorlld )
	else:
		oir = 32
		#plt.ylim(-0.9, 0.9 )
	plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
	plt.gca().xaxis.set_major_locator(mdates.DayLocator())
	#ax1.set_yticks((-0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9))
	ax1.set_ylabel('ERFC')
	print numerr1
	print numerr2
	print tottotais
	figtext(.5,.655,'Erro Relativo de FC sem Divisao em Estratos', fontsize=9, ha='center')
	figtext(.5,.64,'ERM 1:' + str(round((sum(totErro1) )/(numerr1),4)) + ' ERM 2:' + str(round((sum(totErro2) )/(numerr2),4))    + ' FCM:' + str(round(sum(totDiasTod)/tottotais,4)) ,ha='center',fontsize=6 )
#	figtext(.5,.91,'Estrato 1 - Consumidores de Grande Porte  N.:'+str(len(strMaior)/lendias),fontsize=10,ha='center')
	#plt.title('Medias Erro Medio 1: ' + str(round((sum(totErro1) )/(numerr1),4)) +  ' Erro Medio 2: ' + str(round((sum(totErro2) )/(numerr2),4)) + 'FC Medio: ' + str(round(sum(totDiasTod)/tottotais,4) ))

		

	

	
	sume = sume + 1
	plt.gcf().autofmt_xdate()
	plt.tick_params(axis='x', labelsize=3)
	plt.tick_params(axis='y', labelsize=6)
	
	#plt.yticks(np.arange(0.9, 0.9, 0.1))
	legend = plt.legend(loc='upper left', shadow=True, fontsize='xx-small')
	legend.get_frame().set_facecolor('#AAAACC')
  

ax2 = plt.subplot2grid(grid_size, (sume % nb_plots_per_page, 0))
#ax2 = plt.subplot(4,1,sume)
#plt.ylim(0, maiorlld )
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
#plt.title('Menor Estrato N.:' + str(len(strMenor)/lendias))
#figtext(.5,.385,'Estrato 2 - Consumidores de Pequeno Porte', fontsize=10, ha='center')
#figtext(.5,.37,'NE 2.:' + str(len(strMenor)/lendias) ,ha='center',fontsize=8 )
figtext(.5,.36,'Nao Uteis Estrato 2 - Consumidores de Pequeno Porte', fontsize=10, ha='center')
#plt.plot(c,maiorlvlsMe, label='Maximo', marker='.', color="#FF0000" )
#plt.plot(c,totDias2, label='Media E.2', marker='+', color="#000000" )
width=0.2
ax2.bar(c, coday2, alpha=0.2)
#plt.plot(c,totDias1 , label='media E.1', marker='.', color="#FFE4B5" , linewidth=0.5 )
#plt.plot(c,totDiasTod , label='Media Geral', marker='.', color="#5B913C", linewidth=0.5)
#plt.plot(c,menorlvlsMe , label='Minimo', marker='x', color="#0000FF")
ax2.set_ylabel('FC')
#plt.gcf().autofmt_xdate()
plt.tick_params(axis='x', labelsize=4)
plt.xticks( rotation='vertical')
legend = plt.legend(loc='upper left', shadow=True, fontsize='xx-small')
#for tick in plt.gca().xaxis.iter_ticks():
    #tick[0].label2On = True
    #tick[0].label1On = False
    #tick[0].label2.set_rotation('vertical')
#legend.get_frame().set_facecolor('#AAAACC')
#ax221 = ax2.twinx()





print bcolors.BACK_LRED + " OK! " + bcolors.ENDC

subplots_adjust(bottom=0.20)
#plt.savefig(str(grupo)+'grp.pdf', bbox_inches=None, pad_inches=0.1, frameon=None)

if writeTable == True:
	rep.write(str(grupo) + "|" + str(numcons)+ "|" +  str(round(sum(totDiasTod)/tottotais,4) ) + "|" + str(round((sum(totErro1) )/(numerr1),4)) + "|" + str(round((sum(totErro2) )/(numerr2),4)) +   "\n")
print coday1
print coday2

print bcolors.BACK_LRED + str("OK") + bcolors.ENDC
plt.axis('equal')
plt.show()





















