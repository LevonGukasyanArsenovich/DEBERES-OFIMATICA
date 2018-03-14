# coding: utf8
# Levon Gukasyan

# Inicializaciones
salir   = "N"
suma1   = 1
maximo  = 5 
suma    = 0

if maximo <= 0 :
	print "Error!"

while ( salir=="N" ):
	# Hago cosas
	if suma1%2==0:
		print suma1,
        if suma1 == maximo -2:
			print "+",
        
	# Incremento
        suma = suma + suma1
        suma1  = suma1 + 1
	# Activo indicador de salida si toca
	if ( suma1 > maximo): # Condición de salida
		salir = "S"
print "=", suma1
