# coding : utf8
# Levon Gukasyan
from math import pi

print """CIRCULO Y TRIANGULO"""

FIGURA = raw_input("Escriba t o c:")
FIGURA = FIGURA.upper()

if FIGURA=="T":
	BASE   = input("Esciba la base:    ")
	ALTURA = input("Escriba la altura: ")
	
	if BASE >=0 and ALTURA >=0 or BASE==ALTURA :
		print "Un triangulo de base",BASE,"y",ALTURA,"""Tienen una area de""",BASE*ALTURA/2
		
	else :
		print "No se pueden NEGATIVOS"		

elif FIGURA =="C":
    RADIO=input("Escriba el radio:")
    if RADIO >=0 :
	    print "Un circulo de radio:",RADIO,"""
		tine una area de :""",2*pi*RADIO
    else :
        print "No se puede negativos" 

else :
	print "Error escriba t o c"
