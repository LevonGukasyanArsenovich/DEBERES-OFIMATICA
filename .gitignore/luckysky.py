# coding: utf8
import os
from decimal import Decimal
os.system('clear')
print "https://www.queelvueloteacompañe.estroll "  
print """   
       | **    BIENVENIDO A   ** |
       |Luck Sky Vueling Airlines| """
       
print "\n"
print "--PRECIO DEL BILLETE: 500$"

print "--Es usted trabajador? O del LADO OSCURO?"
#PREGUNTA SI ES TRABAJADOR O NO , O SI ES DEL LADO OSCURO
trabajador = raw_input("--s/n/lo:")

trabajador = trabajador.upper()

os.system('clear') 
if trabajador =="S" : 
	print """
	   ******Bienvenido empleado******"""
	# AQUI PREGUNTA EL CARGO DE TRABAJADOR QUE TIENE
	print """
	                       | 1-AZAFATA DE HALCÓN MILENARIO
	Usted que cargo tiene? | 2-HAN SOLO PILOTO
	                       | 3-CHEWBACCA,  4-CARGA MALETAS"""
	                       
	 
	cargo = input("--1,2,3 o 4:")
	print "--Usted tiene PROMO LEIA?"# PREGUNTA SI TIENE PROMO LEIA 
	desc  = raw_input ("--s/n:")
	desc  = desc.upper()
	os.system('clear') 
	
	if cargo == 1 and desc == "S": 
		print "--Azafata De Halcon Milenario tiene un 45% desc."
		print "--PRECIO TOTAL:",Decimal(500-(500*45/100)),"$"
		print "GRACIAS POR SU VISITA"
	if cargo == 1 and desc == "N":
		print "--Azafata De Halcon Milenario tiene un 10% desc." 
		print "--PRECIO TOTAL:",Decimal(500-(500*10/100)),"$"
		print "GRACIAS POR SU VISITA"
	if cargo == 2 and desc == "S": 
		print "--HAN SOLO PILOTO tiene un 95% desc."
		print "--PRECIO TOTAL:",Decimal(500-(500*95/100)),"$"
		print "GRACIAS POR SU VISITA"
	if cargo == 2 and desc == "N":
		print "--HAN SOLO PILOTO tiene un 60% desc." 
		print "--PRECIO TOTAL:",Decimal(500-(500*60/100)),"$"
		print "GRACIAS POR SU VISITA"
	if cargo == 3 and desc == "S": 
		print "--HAN SOLO PILOTO tiene un 95% desc."
		print "--PRECIO TOTAL:",Decimal(500-(500*95/100)),"$"
		print "GRACIAS POR SU VISITA"
	if cargo == 3 and desc == "N":
		print "--HAN SOLO PILOTO tiene un 60% desc." 
		print "--PRECIO TOTAL:",Decimal(500-(500*60/100)),"$"
		print "GRACIAS POR SU VISITA"
	if (cargo == 4 or cargo == 5) and desc == "S": 
		print "--Los CHEWBACCAS Y los Carga maletas teneis un 40% desc."
		print "--PRECIO TOTAL:",Decimal(500-(500*40/100)),"$"
		print "GRACIAS POR SU VISITA"
	if (cargo == 4 or cargo == 5) and desc == "N":
		print "--Los CHEWBACCAS Y los Carga maletas teneis un 5% desc." 
		print "--PRECIO TOTAL:",Decimal(500-(500*5/100)),"$"
		print "GRACIAS POR SU VISITA"
	print "GRACIAS POR SU VISITA"
		
elif  trabajador == "N" :
	print "--De acuerdo"
	os.system('clear')
#AQUI PREGUNTA LA EDAD DEL CLIENTE
	edad = input("--Introduzca su edad: ")
	 
	if edad <0 :
		print "EDAD MAL INTRODUCIDA"
	if edad >=0 and edad <=3 :
		print "El billete es GRATIS"
		print "GRACIAS POR SU VISITA"
	if edad >3 and edad <=10 : 
		print "--DESCUENTO EWOK 80%"
		print "--PRECIO TOTAL",Decimal(500-(500*80/100)),"$"
		print "GRACIAS POR SU VISITA"
	if 	edad >10 and edad <=16 : 
		print "--DESCUENTO PADAWAN 15%"
		print "--PRECIO TOTAL",Decimal(500-(500*15/100)),"$"
		print "GRACIAS POR SU VISITA"
	if 	edad >16 and edad <=60 : 
		print "--JEDI NORMAL Usted no tiene descuento"
		print "--PRECIO TOTAL: 500$"
		print "GRACIAS POR SU VISITA"
	if 	edad >60 : 
		print "--DESCUENTO YODA(40%)"
		print "--PRECIO TOTAL",Decimal(500-(500*40/100)),"$"
		print "GRACIAS POR SU VISITA"
		
		
elif trabajador == "LO" :#SI ES DEL LADO OSCURO LE PREGUNTA SI ES LORD SITH O DARTH VADER
	print """   
		| **    BIENVENIDO AL   ** |
		|        LADO OSCURO       | """
		
	print """
	                          | 1-LORD SITH
	Usted que targeta tiene?  | 2-DARTH VADER"""
	
	cargo2 = input("--1/2:")     
	print "--Usted tiene PROMO LEIA?"# PREGUNTA SI TIENE PROMO LEIA 
	desc2  = raw_input ("--s/n:")
	desc2 = desc2.upper()
	
	if cargo2 == 1 and desc2 =="S" :
		print "--LORD SITH TIENE UN DESCUENTO DEL 45%"
		print "--PRECIO TOTAL",Decimal(500-(500*45/100)),"$"
		print "GRACIAS POR SU VISITA"
	if cargo2 == 1 and desc2 =="N" :
		print "--LORD SITH TIENE UN DESCUENTO DEL 10%"
		print "--PRECIO TOTAL",Decimal(500-(500*10/100)),"$"
		print "GRACIAS POR SU VISITA"
	if cargo2 == 2 and desc2 =="S" :
		print "--DARTH VADER TIENE UN DESCUENTO DEL 65%"
		print "--PRECIO TOTAL",Decimal(500-(500*65/100)),"$"
		print "GRACIAS POR SU VISITA"
	if cargo2 == 2 and desc2 =="N" :
		print "--DARTH VADER TIENE UN DESCUENTO DEL 20%"
		print "--PRECIO TOTAL",Decimal(500-(500*20/100)),"$"
		print "GRACIAS POR SU VISITA"
	
else:
	print "Error"
