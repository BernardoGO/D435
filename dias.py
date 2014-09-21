
bolea = True
#bool(daycons[0][x]) & bool(daycons[1][x]) & bool(daycons[2][x]) & bool(daycons[3][x]
#for 


#xd = tuple(1 if (bolea = (bolea and daycons[y][x] for y in xrange(0, numcons))) else 0 for x in xrange(0, lendias))


cango = False
xd = []

for x in xrange(0, lendias):
	bolle = 0
	for y in xrange(0, numcons):
		bolle = bolle + daycons[y][x]
	xd.append(bolle)

mm = max(xd)
cc = [i for i, j in enumerate(xd) if j == mm]
notasmax = mm
maxindex = -1
maiornuml = [0,0]
passit = False

while cango is False:

	

	consdiamax = []

	for x in xrange(0, numcons):
		if daycons[x][cc[0]] == 1:
			consdiamax.append(x)

	print len(coday1)
	print len(coday2)
	print len(c)
	for i in daycons: print i

	diastodos = []
	for x in xrange(0, lendias):
		bolle = True
		for y in consdiamax:
			bolle = bolle and daycons[y][x]
		diastodos.append(bolle)

	if diastodos >= maiornuml[0]:
		maiornuml = [diastodos, maxindex]

	if sum(diastodos) > 10 or passit:
		cango = True
	else:
		#notasmax.append(mm)
		#print xd
		if maxindex - 1 < len(xd)*-1:
			passit = True
			mm = maiornuml[1]
			continue

		maxindex = maxindex - 1
		print maxindex
		print len(xd)*-1
		mm = sorted(xd)[maxindex]

	

#numinscr - dmed - dmax - dia

#print bcolors.BACK_LRED + str(xd) + bcolors.ENDC
csvres = []
for y in xrange(0,len(diastodos)):
	for x in consdiamax:
		if diastodos[y] == 1:
			csvres.append(datedBolas[(x*lendias)+y])

with open(str(grupo)+'MedGrp.csv', 'wb') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=',')
	for x in csvres:
		spamwriter.writerow(x)
print bcolors.BACK_LRED + str(diastodos) + bcolors.ENDC

print consdiamax
plt.show()
