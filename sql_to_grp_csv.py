import csv

_MAX_CONSUMIDORES_ = 0; #20
_GRUPO_ATV_ = "Resid" #"Beleza"


csv_in = open('ultimoSQL.csv', 'rb')
myreader = csv.reader(csv_in)

consumidores = 0

rep = open("report.txt", "w")

rep.write("Relatorio\n")
comp = False
lines = 0

with open('residencia.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
        )
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

        for row in myreader:
        
            

            cliente, date, ramo, tipo, medidor, cod, grandeza, valor,  = row

            

            adia = date.split()[0]
            #print hdmax + "   -   " + str(adia) + "   -   " + str(bdate)
            



            if cliente.isdigit() == False:
                continue

            
                

            if (cliente != consumidor) or (dia != adia):
                
                #31/05
				if consumidores > 0:
					dmed = round(soma / nhorarios,4)
					if dmed > dmax:
						print "ERROR"
						break
					print str(tipo) + " [] " + str(ramo) + " [] " + bdate.split()[0] + " [] " + str(dmed) + " [] " + str(dmax)
					spamwriter.writerow([consumidor, bdate.split()[0], dmed, dmax, hdmax,dramo])
					lines = lines + 1
					totalcli += soma
					rep.write("Dmed dia " + bdate.split()[0] + ":" + str(dmed) + "\n")
					rep.write("N de horarios dia " + bdate.split()[0] + " :" + str(nhorarios) + "\n")
				if _GRUPO_ATV_ is not None:
					if _GRUPO_ATV_ in ramo:
						foundgrupo = True

					else:
						if foundgrupo == True:
							break
						continue
                
				if (cliente != consumidor) and ndias != 39 and  consumidores > 0:
					while ndias != 39:
						comp = True
						spamwriter.writerow([consumidor, bdate.split()[0], dmed, dmax, hdmax,dramo])
						ndias += 1
						lines = lines + 1
					
				if (cliente != consumidor):
					if consumidores > 0:
						rep.write("N. de dias: " + str(ndias) + " Status: " + str(comp) + "\n")
						rep.write("Consumo Total: " + str(totalcli) + "\n")
                                
                        
					consumidores += 1
					if _MAX_CONSUMIDORES_ != 0 and consumidores >= _MAX_CONSUMIDORES_: break
					rep.write("\nConsumidor: " + cliente + "\n")
					ndias = 0
					totalcli = 0
					comp = False
                
				ndias += 1
				soma = 0
				dia = adia
				consumidor = cliente
				nhorarios = 0
				dmax = 0
				hdmax = None
				dramo = ramo
				
            bdate = date
            
            
            soma += float(valor)
            nhorarios += 1
            
            if float(valor) >= dmax:
                dmax = float(valor)
                hdmax = date
                
   
            

rep.write("\n\nTOTAIS: ")         
rep.write("\nN. de consumidores: " + str(consumidores))
rep.write("\nN. de linhas: " + str(lines))

rep.close()


            
            
            
