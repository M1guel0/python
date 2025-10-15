import os
os.system("clear")

#INPUT EN PYTHON 
print ("Hola como te llamas??")
#nombre = input()
#print (nombre)

print ("Que edad tienes??")
#edad = input()
#print (edad)

#nombre = input ("Hola como te llamas??\n") #Salto de linea cuando. sin el \n se escribe en la misma linea de comando 
#print (nombre)

#edad = int(input ("Qué edad tienes ??\n"))
#print (edad)

##tIPADO DINAMICO, ES DECIR SE PEUEDEN CAMBIAR LOS TIPOS DE VARIABLES, SI PRIMERO ERA UNA CADENA SE PUEDE CAMBAIR A ENTERO U OTRO.

name = "miguel"
print (type(name)) #tipo de dato cadena string

name = 45
print (type(name)) #tipo de dato int cambió el tipo de datos.

# EL F-STRING Literal de cadena de formato. 
#print(f"hola me llamo {nombre}, tengo {edad + 5} años" )

#nombres de variables 
"""Una manera de asignar nombres a las variables de la manera correcta"""
Por_ejemplo_esta_es_una_variable = "ok, manera snake"
porejemplo = "ok 'todojunto'"
PorEjemploVariable = "Mayuscula en cada palabra"
POR_EJEMPLO_vARIABLE = "SANKE EN MAYUSCULA"
AGUAPANELA = 45.788
#print(AGUAPANELA)

#### LISTAS EN PYTHON 
lista = [1, 2, 3, 4]
lista0 = ["manzanas", "peras", "moras", "mangos"] #Se separan por comillas y comas.
lista1 = [25, "manuel", True, 4587.3]
lista_vacia =[]
matrices = [[2, 4], [45, 85], [4621, 78]] #Se separa por comas

#metodo insert en una lista.
#se coloca un nuevo elemento en una pocicion de la lista sin reemplazar nada.

lista0.insert(2, "sandias")
print(lista0)

