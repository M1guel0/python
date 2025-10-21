import os
os.system("cls")

### Añadir elementos a la lista. 
lista1 = ["a", "b", "c", "d", "e", "f"]
lista1.append ("Z") #inserta un elemeto al final de la lista.
print(lista1)

lista1.insert(1, "@") # Insertar un elemento en una posición indicada. 
print(lista1)

lista1.extend (["j", "ñ"]) #Agregar elementos al final de una lista.
print(lista1)

## Eliminar elementos de una lista .remove() y .pop()

lista1.remove("e") #elimina la primera aparicion del elemento de la lista.
print(lista1)

lista1.pop() #elimina el ultimo elemento de la lista y ademas te lo devuelve. 
print (lista1)
#####______________________________________________________#############

lista = lista1.pop(1) #Elimina el segundo elemento de la lista y lo devuelve @
print (lista) 
###Eliminar Rangos de elementos. del _ 
lista1 = [ 10, 11, 12, 13, 14, 15]
del lista1 [0:2]
print (lista1)
# METODO SORT()
print("Ordenar una lista modificando la original.")
numbers = [45511, 75158, 4863, 74123, 9856]
numbers.sort() #El metodo sort acomoda los numeros en orden de mayor a menor
print(numbers)

#LISTA ORDENDA COMO VARIABLE. 
# PARA ESTO SE USA SORTED() 
print("Crear una nueva lista ordenada con su varibale")
numbers = [45511, 75158, 4863, 74123, 9856]
numbers_Sorted = sorted(numbers) #Se crea la variable.
print (numbers_Sorted) #la lista ordenada se guarda como una variable que se puede usar. 

#Contar elementos en una lista.
#metodo count 
animals = ["gallo", "perro", "gato", "avestruz", "Elefante" ]
print (len(animals)) #muestra la longitud de la lista len()
print (animals.count ("gato")) #Cuantos "gato" hay en la lista. cuantas veces aparece 
#el elemento en la lista. 
print ("murcielago" in animals) #devuelve valores booleanos si un elemento esta o no en la lista. 

#################################################################################################################3
######################## EJERCICIOS DE PYTHON. ##################################################################

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

a = [1, 2, 3, 4, 5 ]
a.append(6)
a.insert(1, 10)
#print (a)
a[0] = 0
#print (a)

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

lista_a.extend (lista_b)
#print(lista_a)
lista_a.remove (1)
#print(lista_a)
lista = lista_a.pop(3)
#print(lista)
lista_b.clear ()
#print(lista_b)

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del (lista[2:5])
#print (lista)

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

lista = [5, 2, 8, 1, 9, 4, 2]
lista.sort()
print (lista)
print (lista.count(2))
print ( 7 in lista)

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

original = [1, 2, 3]
print (original)
copia_1 = original [:]
print(copia_1)
copia_2 = (original.copy())
print (copia_2)
Referencia = original
Referencia[0] = 10
print (Referencia)


# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.
cadenas = ["Manzana", "pera", "BANANA", "naranja"]
cadenas.sort(key=str.lower)
#cadenas.sort()
print (cadenas)
