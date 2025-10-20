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



