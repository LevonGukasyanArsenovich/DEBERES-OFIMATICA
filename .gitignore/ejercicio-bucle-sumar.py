# coding: utf8
# Levon Gukasyan

# Inicializaciones
salir  = "N"
suma   = 0
maximo = input ("Digame numero:") 
suma1  = 0

if maximo <= 0 :
	print "Error 404"

while ( salir=="N" ):
	if suma%2==0 :
		print suma
	# Incremento
	suma = suma + suma1
	suma = suma + 1
	# Activo indicador de salida si toca
	if ( suma > maximo): # Condición de salida
		print suma
		salir = "S"
