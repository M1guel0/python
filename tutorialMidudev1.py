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
print (a)
a[0] = 0
print (a)

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

lista_a.extend (lista_b)
lista_a.remove (1)
lista_a.pop(3)
lista_a.clear ()
