# coding : utf8
import os

print """
     ####################################
     ##      Ejercicio multiples       ##
     ####################################         
     ##  comparador-multiplos.py       ##             PyshXS
     #################################### """


numero1=input("Digame un numero: ")
numero2=input("Digame un numero: ")

os.system('cls')
if numero1<=0 or numero2<=0:
	print "No se puede,son negativos o no son multiples"
elif numero1%numero2==0 and numero1>numero2 :
		print numero1,"es mayor y multiple que",numero2
elif numero1%numero2==0 and numero1==numero2 :
		print numero1,"son iguales y multiples que",numero2
elif numero2%numero1==0 and numero2>numero1 :
		print numero2,"es mayor y multiple que",numero1
elif numero2%numero1==0 and numeroz==numero1 :
		print numero2,"son igauales y multiples que",numero1
else:
	print numero1,"y",numero2,"no son multiples"
