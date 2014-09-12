import csv

_MAX_CONSUMIDORES_ = 0; #20
_GRUPO_ATV_ = "Resid" #"Beleza"


csv_in = open('ultimoSQL.csv', 'rb')
myreader = csv.reader(csv_in)

consumidores = 0

rep = open("report.txt", "w")

rep.write("Relatorio\n")


with open('residencial.csv', 'wb') as csvfile:
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


            
            
            
