# coding: UTF-8
from decimal import Decimal
print "Ahora haremos conversiones"


cm = input ("Introduce la cantidad de CM:")

print " DISTANCIA EN CM:",cm,"Centimetros"

print "Centimetros:",cm
print "Metros     :",Decimal(cm)/1000
print "Kilometros :",Decimal(cm)/1000/1000 
    
