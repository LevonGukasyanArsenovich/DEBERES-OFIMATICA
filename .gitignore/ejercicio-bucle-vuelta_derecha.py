# coding: utf8
# Levon Gukasyan
# 15/03/2018
import time 

salir      = "N"
suma       = 1

while ( salir=="N" ):
	time.sleep(0.2)
	# Hago cosas
	if suma%8==1 or suma%8==2 :
		print suma ,"-> arriba"
	if suma%8==3 or suma%8==4 :
		print suma , "-> derecha"
	if suma%8==5 or suma%8==6 :
		print suma , "-> abajo"
	if suma%8==7 or suma%8==0 :
		print suma ,"-> izquierda"

	# Incremento
	suma = suma + 1 

	# Activo indicador de salida si toca
	if (suma >8): # Condición de salida
		time.sleep(0.2)
		salir = "S"
print "-*Se acabo la vuelta*-"

print "--------------------------------------"

print "MODO BORRACHO"
print "--------------"

salir      = "N"
suma       = 1

while ( salir=="N" ):
	time.sleep(0.2)
	
	# Hago cosas
	if suma%8==3 or suma%8==5 :
		print suma ,"-> arriba"
	if suma%8==4 or suma%8==2 :
		print suma , "-> derecha"
	if suma%8==1 or suma%8==6 :
		print suma , "-> abajo"
	if suma%8==0 or suma%8==7:
		print suma ,"-> izquierda"
	

	# Incremento
	suma = suma + 1 
    
	# Activo indicador de salida si toca
	if (suma >8): # Condición de salida
		time.sleep(0.2)
		salir = "S"
print "-*Te paro la poli amigo*-"
