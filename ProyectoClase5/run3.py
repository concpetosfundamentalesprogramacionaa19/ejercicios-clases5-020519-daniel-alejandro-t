"""
	run2.py
	Autor: Daniel Tinizaray
"""

from MisVariables import *

# Condicional simple:

nota = input("Ingrese la nota 1: \n")
#nota2 = input("Ingrese nota 2: \n")

nota = int(nota)
#nota2 = int(nota2)

if nota >= 18:
	print("%s, su nota es: %d" % ("Sobresaliente", nota))
else:
	if nota >= 16 & nota < 18:
		print("%s, su nota es: %d" % ("Muy buena", nota))
	else:
		if nota >= 13 & nota < 16:
			print("%s, su nota es: %d" % ("Buena", nota))
		else:
print("%s, su nota es: %d" % ("Insuficiente", nota))