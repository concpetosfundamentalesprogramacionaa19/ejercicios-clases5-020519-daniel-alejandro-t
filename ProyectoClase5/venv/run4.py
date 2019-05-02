"""
	run4.py
	Autor: Daniel Tinizaray

	Deseamos obtener el costo de una carrera universitaria.
	El valor promedio de cada ciclo es de 1200 dolares.
	El valor promedio del seguro educativo por ciclo es de 100$. si la edad del estudiante es menor 0 igual a 20 caso contrario sera de 150$
	Si el estudiante Tiene una modalidad a distancia el numero de ciclos a seguir es de 10 caso contrario debera seguir 8 ciclos
	obtener la proyeccion del costo de la carrera de un estudiante
"""

# Entrada del usuario
edad = input("Inserte su edad \n")
edad = int(edad)        # Realiza un casting
modalidad = input("Introduzca su modalidad: \n")

# Declaracion e inicio de variables
numCiclos = 0
precioSeguroFinal = 0
precioMatriculaInicial = 1200
precioMatriculaFinal = 0

# Evaluamos edad
if (edad <= 20):
    seguro = 100
else:
    seguro = 150

# Evaluamos la modalidad
if modalidad == "Distancia":
    numCiclos = 10
    precioSeguroFinal = seguro * numCiclos
    #print(precioSeguroFinal)   print para testear
    precioMatriculaFianl = (precioMatriculaInicial * numCiclos) + precioSeguroFinal
    print("Debe ustudiar durante %d, en la modalidad %s con un costo aprox. de: %d$." % (numCiclos, modalidad, precioMatriculaFianl))
else:
    numCiclos = 8
    preicoSeguroFinal = seguro * numCiclos
    #print(precioSeguroFinal)   print para testear
    precioMatriculaFianl = (precioMatriculaInicial * numCiclos) + precioSeguroFinal
    print("Debe ustudiar durante %d, en la modalidad %s con un costo aprox. de: %d$." % (numCiclos, modalidad, precioMatriculaFianl))