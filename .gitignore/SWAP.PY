# coding : utf8
import time

print "VAMOS HA HACER UN SWAP!!!!!!"
print "el intercambio de cada mano durara 4 segundos"
mano_der=("movil")
mano_izq=("bocadillo")

mano_extra = mano_der
mano_der = mano_izq
mano_izq = mano_extra
time.sleep(4)
print "Que tengo en la mano? un",mano_der
time.sleep(4)
print "Y en la otra tengo un",mano_izq
