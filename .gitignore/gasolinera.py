# coding : utf8
# Levon Gukasyan
# Fecha de creacion 19/02/2018
import time
print """               
         *******************************************
         $$$$$$  BIENVENIDO A LA GASOLINERA   $$$$$$
         ******************************************* """
# AGREGAMOS LAS VARIABLES CON SU PRECIO         
supernormal     = 1.5
superturbo      = 1.55
sinplomonormal  = 1.6
sinplomosabor   = 1.65
dieselnormal    = 1.7
dieselfast      = 1.75
naranplo = sinplomonormal+sinplomosabor
time.sleep(3)

saludar  = raw_input("Quiere ver nuestra tabla de precios? ")

if (saludar=="SI" or saludar=="si") or (saludar=="Si" or saludar=="sI") :
	print """
----|supernormal     = 1.5	        OFERTAS ESPECIALES!!
----|superturbo      = 1.55         
----|sinplomonormal  = 1.6     LLENE SU DESPOSITO AL MEJOR PRECIO!!
----|sinplomosabor   = 1.65
----|dieselnormal    = 1.7
----|dieselfast      = 1.75
----|naranplo        = sinplomonormal (incluido sabor naranja)"""
else : 
	print "Lo sentimos que tenga un buen dia!"
time.sleep(5)
gasolina =raw_input("Que tipo de gasolina quiere? ")
litros   =input("Cuantos litros? ")

if gasolina=="supernormal" or gasolina=="SUPERGASOLINA" : 
    print "Importe:",supernormal*litros,"$"
    
elif gasolina=="superturbo" or gasolina=="SUPERTURBO" : 
    print "Importe:",superturbo*litros,"$"
    
elif gasolina=="dieselnormal" or gasolina=="DIESELNORMAL" : 
    print "Importe:",dieselnormal*litros,"$"
    
elif gasolina=="dieselfast" or gasolina=="DIESELFAST" : 
    print "Importe:",dieselfast*litros,"$" 
    
elif gasolina=="sinplomonormal" or gasolina=="SINPLOMONORMAL" : 
    print "Importe:",sinplomonormal*litros,"$"
     
elif gasolina=="naranplo" or gasolina=="NARANPLO":
	print "Importe:",naranplo*litros,"$"
	
else :
	print "no se puede hacer"
