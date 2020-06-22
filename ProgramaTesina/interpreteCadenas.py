f = open ('cadena1.nwk','r')
g = open ('cadena2.nwk','r')

cadena_newick1 = f.read()
cadena_newick2 = g.read()

sepA = cadena_newick2.split("(")
sepB = cadena_newick2.split("(")

pilaA=[]
pilaB=[]

for x in sepA:
	pilaA.append(x)
for x in sepB:
	pilaB.append(x)

print(pilaA)
print(pilaB)

Pausa = input()

f.close()
g.close()




