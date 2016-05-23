#Desarrolle un programa que permita ingresar dos arreglos
#uno numerico y otro alfabetico, ornearlos, e imprimir mayor o menor 
#para cada caso
print "Bienvenidos"

arreglonum = []
arregloalfa = []
resp = raw_input(" Desea ingresar valores S/N?  ")
while resp == "s":	
	dato = raw_input(" Por favor, Ingrese Palabras o Numeros ->  ")
	if dato.isdigit():
		arreglonum.append(dato)
	if dato.isalpha():
		arregloalfa.append(dato)
	resp= raw_input (" Agregar otro? ")

print "Ordenando arreglos.....\n"
arreglonum.sort()
arregloalfa.sort()

if len(arreglonum) > len(arregloalfa):
	print "El arreglo mayor es el Numerico, y contiene"+str(len(arreglonum))+" elementos.\n"
else:
	print "El arreglo mayor es el Alfabetico, y contiene "+str(len(arregloalfa))+" elementos.\n"	

print "A continuacion los arreglos."
print "Numerico"
print (arreglonum)
print "Alfabetico"
print (arregloalfa)
