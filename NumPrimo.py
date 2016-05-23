# Ejercicio Libre
## Determinar si un numero es par o impar
print "Bienvenidos"

def par(num):
	if num % 2 == 0:
		print "El numero es Par"
	elif num%2 != 0:
		print "El numero es Impar"
		 
num = input("Ingrese Numero ->  ")

print par(num)
print "Fin del ejercicio"
