# coding : utf8
# LEVON GUKASYAN
print "NO SE PERMITEN NUMEROS REPETIDOS!"
A = input("dime un numero=")
B = input("dime un numero=")
C = input("dime un numero=")
if (A==B and A==C) or (B==A and B==C) or (C==A and C==B):
	print "error 2 numeros" 
if A > B and A > C:
	print A,"Es mayor que",B,"y",C 
	print B,"Y",C,"SON MENORES QUE",A 

elif B > A and B > C :
	print B,"Es mayor que",A,"y",C 
	print A,"Y",C,"SON MENORES QUE",B 
	
	
elif C > A and C > B :
	print C,"Es mayor que",A,"y",B 
	print A,"Y",B,"SON MENORES QUE",A
	 
else:
	print "No se permiten valores Iguales"
	
