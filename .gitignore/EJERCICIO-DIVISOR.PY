# coding : utf8
#levon gukasyan
print "DIVISOR DE NUMEROS"

dividendo =input("Escriba el dividendo: ")
divisor =input("Escriba el divisor: ")

if (dividendo % divisor) == 0:
	print "Division exacta====COCIENTE:",dividendo / divisor,
elif divisor == 0:
	print "No se puede dividir este numero"
else:
	print " Division no exacta====COCIENTE:", dividendo / divisor, "Residu:", dividendo%divisor
	
