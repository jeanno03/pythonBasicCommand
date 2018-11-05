oName = "Jacques"
oName02 = "Paul"

oChiffre = 10
oChiffre02 = "10"

print(oName + ":")
print("salut")

print(oName02 + ":")
print("salut")

print(oName + ":")
print("tu vas bien?")

print(oName02 + ":")
print("oui")

print(oName+str(oChiffre))
print(oChiffre+int(oChiffre02))

if oChiffre==int(oChiffre02) :
	print("réussite")
else:
	print("echec")

if oChiffre<int(oChiffre02) :
	print("réussite")
else:
	print("echec")

if oChiffre<int(oChiffre02) :
	print("réussite")
elif oChiffre>int(oChiffre02):
	print("réussite 02")
elif oChiffre==int(oChiffre02):
	print("réussite 03")

oAge = int(input("Quel age avez-vous? "))
print(oAge)

if oAge>=18:
	print("bravo vous êtes majeur")
elif oAge <18:
	print("vous etes mineur")

for i in range(0,20):
	print(i)

for i in range(20):
	print(i)

for n in oName:
	print(n)



print("longueur de oName : " + str(len(oName)))

for n in oName:
	print(n)

for n in oName:
	print(oName[0])

for i in range(0,len(oName)):
	print(oName[i])

for i in range(0,len(oName)):
	print(str(i) + " : " +oName[i])

oInput=""

while oInput !="o":
	oInput = input ("Voulez vous quitter le programme ? o/n")
print("Bravo vous avez quitté le programme")	

while not oInput =="oui":
	oInput = input ("Voulez vous quitter le programme ? oui")
print("Bravo vous avez quitté le programme")	

oNameList=["Pierre","Paul","Jacques"]
oNombreList=[2,5,9]

for item in oNameList:
	print(item)
print("je récupère le 1er item de oNameList, puis son 1er caractère")
print(oNameList[0][0])

oNameList.append("Marie")

print(oNameList)

oNameList.insert(0,"Sam")

print(oNameList)

oNameList.remove("Pierre")

print(oNameList)

oNameList.pop()
print("retire le dernier élément")
print(oNameList)


oNameList.reverse()
print("inverse les éléments")
print(oNameList)

oNameList.sort()
print("trier les éléments")
print(oNameList)