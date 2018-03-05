# coding: utf8
salir  = "N"
numero = 2010 

while ( salir=="N" ):
	# Hago cosas
	print "informe año:",numero

	# Incremento
	numero = numero +1
	# Activo indicador de salida si toca
	if ( numero >2016): # Condición de salida
    	    salir = "S"
