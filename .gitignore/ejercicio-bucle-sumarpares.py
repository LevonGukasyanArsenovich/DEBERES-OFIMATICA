# coding: utf8
# Levon Gukasyan

# Inicializaciones
salir  = "N"
suma   = 1
maximo = input ("Digame numero:") 
suma1  = 0

if maximo <= 0 :
	print "Error 404"

while ( salir=="N" ):
	# Hago cosas
	print suma

	# Incremento
	suma1 = suma + suma1
	suma  = suma + 1
	# Activo indicador de salida si toca
	if ( suma > maximo): # Condición de salida
		print suma1
		salir = "S"
