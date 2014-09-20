import csv

_MAX_CONSUMIDORES_ = 0; #20




botauto = 1

rowsd = 0

rep = open("report.txt", "w")

rep.write("Relatorio\n")
comp = False
lines = 0


for consumidores in xrange(0, botauto):
	csv_in = open('novosg.csv', 'rb')
	myreader = csv.reader(csv_in)
	with open(str(consumidores)+'AAgrp.csv', 'wb') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		foundgrupo = False
		soma = 0
		dia = ""
		consumidor = ""
		nhorarios = 0
		dmed = 0
		dmax = 0
		hdmax = ""
		ndias = 0
		totalcli = 0;
		adia = None
		bdate = None
		dramo = ""
		
		cachelist = []

		for row in myreader:
			dmax = 0
			dmed = 0
			grupo, nomecli, cod, data, medicao,  = row
			rowsd += 1
			#if rowsd > 500:
			#	break

			if len(cachelist) > 0 and cod != cachelist[0][0]:
				if len(cachelist) >= 38:
					for x in cachelist:
						spamwriter.writerow(x)
				#else:
				print "Running: " + str(consumidores) + " Medicoes: " + str(len(cachelist))
				cachelist = []
				cachecli = ""


			canal1  = medicao.split("canal1|1|")[1].split("canal2|3|")[0].split("|");
			if len(canal1) < 96:
				print len(canal1)
			#canal2  = medicao.split("canal2|3|")[1].split("canal3|5|")[0].split("|");
			#canal3  = medicao.split("canal3|5|")[1].split("|");

			for x in canal1:
				if len(x) > 0:
					dmed = dmed + float(x)
					if float(x) >= dmax:
						dmax = float(x)

			dmed = round(dmed / len(canal1),4)
			cachelist.append([cod, data.split()[0], dmed, dmax,grupo])
