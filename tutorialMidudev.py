import os
os.system("cls")

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

#### LISTAS EN PYTHON ##########################
lista = [1, 2, 3, 4]
lista0 = ["manzanas", "peras", "moras", "mangos"] #Se separan por comillas y comas.
lista1 = [25, "manuel", True, 4587.3]
lista_vacia =[]
matrices = [[2, 4], [45, 85], [4621, 78]] #Se separa por comas

#metodo insert en una lista.
#se coloca un nuevo elemento en una pocicion de la lista sin reemplazar nada.

lista0.insert(2, "sandias")
#print(lista0)

lista2 = ["computadora", "Telefono", "mimadre"]
lista0.extend(lista2) #junta dos listas en una.
#print (lista0)

lista0.remove ("mimadre")
#print (lista0) #Remueve un item señalado en la lista. 

lista1.clear()#Limpia toda la lista 
#print(lista1) 

###  hay mas magia ##########3
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista [::2]) #Salta de 2 en 2, indices impares.
print (lista [::-1]) # muestra los valores de la lista en orden inverso. 
###  print (lista[desde : hasta : paso:])

#imprimir lista de listas. de elementos señalados.
print (matrices [1] [0]) 
#
#Forma de concatenar una lista 
#Esat es la forma menos eficeinte.
lista = lista + [10, 11, 12, 13, 14]
#print (lista)

#Esta es la forma mas eficiente. 
lista += [10, 11, 12, 13, 14]
print (lista)

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice
#### SOLUCIONES.
print (numeros [::-1])
numeros [0] = 50
numeros [4] = 10
print (numeros)

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

Sandwich =[]
#Sandwich.extend (pan + ingredientes + pan_abajo)
Sandwich += (pan + ingredientes + pan_abajo)
print(Sandwich)

# Ejercicio 4: Duplicando la lista
# Dada una lista:
lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

lista += [1, 2, 3]
print (lista)

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30
lista = [10, 20, 30, 40, 50]
print (lista [2:3])

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]
lista = [1, 2, 3, 4, 5, 6]
#lista[0] = 3
#lista[1] = 2
#lista[2] = 1
#print (lista)
print (lista [-4:-7:-1])
lista[:3] = [3, 2, 1]
print (lista)

print("la longitud de la lista es de: ", len(lista)) #imprime la longitud de la lista. 



