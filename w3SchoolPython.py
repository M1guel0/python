x = "increible." 
#Ejemplo de variable global 
def myfunc ():
    print ("Python es ", x) #la variable fuera de la funcion se puede usar. 
myfunc()

"""Una variable dentro de una función es local, podemos hacer que la variable 
Sea global usando el termino "global"
"""

def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)


x = 'awesome'
def myfunc():
  #global x
  x = 'fantastic'
myfunc()
print('Python is ' + x)

txt = "Hello world"
print (txt.strip())
#####--------------------------------------------------###############
#LISTAS EN PYTHON. 
""" SEU USAN PARA ALMACENRA VARIOS ELEMENTOS EN UNA SOLA VARIABLE."""
mi_lista = ["manzana", "platano", "pera"]
print (mi_lista)
print(len(mi_lista))

lista1 = ["abc", 34, True, 40, "masculino"]# la lsita puede tener diferentes tipos de valores como cadena, entero y booleano. 

Thislist = list (("manzana", "platano", "pera"))
print (Thislist)
print (Thislist[1]) #imprime platano.
print (len(Thislist))#imprime la cantidad de elementos de la lista. 
print (type(Thislist))# Imprime el tipo de los elementos de la lista. 

"""la indexacion de una lista, se adquiere un elemento seleccionado respecto a su posición. 
0 Es el priemro de izquierda a derecha. Con valores negativos de derecha a izquierda -1 es el ultimo.  """

print(Thislist[-1]) #imprime pera
#Rango de la indexación de una lista. 

Thislist = ["apple", "Banana", "Cherry", "orange", "kiwi", "melon", "mango"]
print(Thislist[1:3]) #imprime desde la pocicion 1 hasta el 2, el 3 no lo cuenta.
print(Thislist[:3]) # Vacio entonces empieza desde el zero hasta la pocicion 2.
print(Thislist[2:]) # Empieza desde la pocicion 2 hasta el final de la lista
print(Thislist[-1:-4]) # Imprime en blanco por que el rango no empieza desde la ultima pocicion. 
print(Thislist[-4:-1]) #imprime desde la pocicion -4 (De Derecha a izquierda) hasta el -2, el -1 no cuenta. 

#########_____________________________###############
#REVISA SI UN ELEMENTO ESTA EN LA LISTA.
Thislist = ["apple", "Banana", "Cherry", "orange", "kiwi", "melon", "mango"]
if "apple" in Thislist:
   print("Si \"apple\" esta en la lista")
#####_________________________________________##############
#CAMBIAR LOS ELEMENTOS DE UNA LISTA.
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) # sE CAMBIA EL VALOR DE banana a blackcurrant.
#Se cambia un rango de valores.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"] #Pocicion 1 y 2 a cambiar. 
print(thislist)
 
Thislist = ["manzana", "plátano", "cereza"]
Thislist[1:2] = ["grosella negra", "sandía"] # Reemplaza la pocicion 1 con dos elementos. aumenta la cantidad de elementos de la lista.
print(Thislist) 

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"] #Reemplaza las pociciones 1 y 2 por un solo elemento. 
print(thislist)

###INSERTAR ELEMENTOS A UNA LISTA
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "mango")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert (2, "sandia")
print(thislist)

mi_lista = ["apple", "banana", "cherry"]
mi_lista1= ["grosella negra", "sandía"]
mi_lista.extend(mi_lista1) #El metodo extend. extiende una lista con otra colocandola al final. 
print(mi_lista)

######__________________________________################
#RECORRE UNA LISTA.
Thislist = ["grosella negra", "sandía"]
for x in Thislist:
   print(x)

Thislist = ["grosella negra", "sandía"]
for x in range(len(Thislist)):
   print(Thislist)

estalista = []
