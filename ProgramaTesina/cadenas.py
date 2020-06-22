f = open('cadena1.nwk','r')
g = open('cadena2.nwk','r')

cadena_newick1 = f.read()
cadena_newick2 = g.read()


Distancia_total = 0

parentesis_a = []
hojas = []
izquierdo = []
derecho = []
hojas_izquierdo = []

parentesis_a2 = []
hojas2 = []
izquierdo2 = []
derecho2 = []
hojas_izquierdo2 = []

for x in range(0,len(cadena_newick1)): #Recorrer la cadena Newick.

	if cadena_newick1[x] =='(': #Agregar los paréntesis que abren a la pila.
		parentesis_a.append(cadena_newick1[x]) 

	elif cadena_newick1[x]!='(' and cadena_newick1[x]!=')' and cadena_newick1[x]!= ',' and cadena_newick1[x]!=' ':#Agregar las hojasa la pila.
		hojas.append(cadena_newick1[x])

	elif cadena_newick1[x]==')':#Sacar los paréntesis de la pila, si hay un paréntesis que cierra.
		parentesis_a.pop()

	elif len(parentesis_a)==1:#Validar que sea el último paréntesis
		for y in range(0,x):
			izquierdo.append(cadena_newick1[y])
		for y in range(x,len(cadena_newick1)):
			derecho.append(cadena_newick1[y])

#Recorrido arbol 2

for x in range(0,len(cadena_newick2)): #Recorrer la cadena Newick.

	if cadena_newick2[x] =='(': #Agregar los paréntesis que abren a la pila.
		parentesis_a2.append(cadena_newick2[x]) 

	elif cadena_newick2[x]!='(' and cadena_newick2[x]!=')' and cadena_newick2[x]!= ',' and cadena_newick2[x]!=' ':#Agregar las hojas2 a la pila.
		hojas2.append(cadena_newick2[x])

	elif cadena_newick2[x]==')':#Sacar los paréntesis de la pila, si hay un paréntesis que cierra.
		parentesis_a2.pop()

	elif len(parentesis_a2)==1:#Validar que sea el último paréntesis
		for y in range(0,x):
			izquierdo2.append(cadena_newick2[y])
		for y in range(x,len(cadena_newick2)):
			derecho2.append(cadena_newick2[y])

izquierdo.pop(0)
izquierdo2.pop(0)
derecho.pop(0)
derecho.pop(len(derecho)-1)
derecho2.pop(0)
derecho2.pop(len(derecho2)-1)


for x in izquierdo:
	if x!='(' and x!=')' and x!=',' and x!=' ':
		hojas_izquierdo.append(x)

for x in izquierdo2:
	if x!='(' and x!=')' and x!=',' and x!=' ':
		hojas_izquierdo2.append(x)

for x in hojas_izquierdo:
	for y in hojas_izquierdo2:
		if x == y:
			Distancia_total = Distancia_total + 1

for x in hojas_izquierdo2:
	for y in hojas_izquierdo:
		if x == y:
			Distancia_total = Distancia_total + 1












print("Pila de paréntesis abiertos 1")
print(parentesis_a)
print("-----------------------------------")
print("Pila de hojas 1")
print(hojas)
print("-----------------------------------")
print("Arbol izquierdo 1")
print(izquierdo)
print("Arbol derecho")
print(derecho)
print("Hojas del arbol Izquierdo")
print(hojas_izquierdo)

print("Pila de paréntesis abiertos 2")
print(parentesis_a2)
print("-----------------------------------")
print("Pila de hojas 2")
print(hojas2)
print("-----------------------------------")
print("Arbol izquierdo 2")
print(izquierdo2)
print("Arbol derecho2")
print(derecho2)
print("Hojas del arbol Izquierdo2")
print(hojas_izquierdo2)
print("La Distancia_total es:")
print(Distancia_total)

Pausa = input()

f.close()
g.close()


