print('hola mundo')
# esto es un coemnatrio. #
'''
esto es un comentario largo
de varias lienas

'''
Texto = ("""hola comestan todos 
         osea q con este metodo pueo escribir texto
         en varias lineas de codigo como 
         un texto largo""")
print(Texto)
h = 2
y = 5
c = 7 
resultado = (h + y) * c
print(resultado)

# numeros enteros con int. 

cantidad = 100

#numeros flotantes. (numeros decimales. float)
precio = 9.99
altura = 1.75

#cadenas de texto. 
nombre = "miguel angel"
mensaje = 'con comillas cortas'
#caracteres especiales. 
mensaje1 = 'Hola, soy un programador de \'Python\''
#print (mensaje1)
mensaje2 = "El curso se llama \"Python desde cero\""
#print(mensaje2)

#booleanos. son valores de verdadero o falso. 
EsmayordeEdad = True
Tiene_descuento = False

#a = b = c = 12

# arritmetica valores.

a = 10
b = 3

suma = a + b  # 13
resta = a - b    # 7
multiplicacion = a * b    # 30
division = a / b   # 3.333333333
división_entera = a // b   # 3
modulo = a % b   # 1
exponenciacion = a ** b   # 1000

print(suma)
print(resta)
print(multiplicacion)
print(division)
print(división_entera)
print(modulo)
print(exponenciacion)

#operadores de comparación. 
igual = a == b   # False
diferente = a != b   # True
mayor_que = a > b   # True
menor_que = a < b   # False
mayor_o_igual = a >= b   # True
menor_o_igual = a <= b   # False

print(igual, diferente,mayor_que, menor_que, mayor_que, menor_o_igual)
 
#operadores lógicos. 
resultado_and = (a > 5) and (b < 5)   # True
resultado_or = (a > 15) or (b < 5)   # True
resultado_not = not (a > 5)   # False

resultado_and1 = (a < 5) and (b < 5 ) #false
resultado_or1 = (a > 15) or (b < 2) # false
print(resultado_and1, resultado_or1)

#ESTRUCTURAS DE CONTROL. 
#estructuras condicionales. 
#operadores if y if-else.
edad = 19
if edad >= 18: 
    print("eres mayor de edad")

edad = 15
if edad >= 18:
   print ("Eres mayor de edad.")

else:
   print ("eres menor de edad.")
#operador condicional if-elif.else. 
calificacion = int (input("Ingresa la calificación: "))
if calificacion >= 90:
   print ("Excelente")
elif calificacion >= 80:
   print ("Muy bueno")
elif calificacion >= 70:
   print ("Bueno")
else:
   print ("Necesita mejorar")

#bucles/loops 
#bucle for. 
frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print(fruta) #sale los valores de "frutas" como una lista una debajo de otra. 

for x in "melocoton": # sale la palabra dividida m-e-l-o-c-o-t-o-n como una lista, una debajo de otra. 
   print(x)

print("Numeros del 1 al 5 con exponencia de 2 con bucle for")
for numero in range (0,7): # en esta linea el range(0,7) utiliza los numeros del 0 al 6, es decir no usa el numero despues de la coma. 
 
   print(numero** 2)
   
   #bucle while 
contador = 0
while contador < 5: #While junto con condición, contador tiene q ser menor a 5

    print(contador)
    contador += 1 
#bucle while con break. 
contador = 0
while (True): # el bucle while se ejecuta indefinidamente con la condición True. 

    print(contador)
    contador += 1 # cuando aparece un +=1 es para incrementar en 1 el valor del contador, por lo cual si es 0 pasa a 1 y luego a 2 hasta q la condición sea falsa o un break.  

    if contador == 5:
        break
####____________________________________________________###################
print ("usando while con rango de numero")   

rango_denumeros1 = 5
while 10 >= rango_denumeros1:
   print (rango_denumeros1)
   rango_denumeros1 += 1

print("numero par ")
numero_par = 0
while numero_par %2 ==0:
   numero_par +=1
   print (numero_par)
   
print ("numero par con for y if ")
for par in range (0, 10):
   if par%2 ==0:
      print (par)
 
#par = 10 % 2
#print (par)
par = 1
if par % 2 ==0:
   print("es par")
else:
   print ("es impar ")


   

#bucle for con continue. 
for i in range(10): #comienza el bucle for, range(10) toma los valores del 0 al 9, 

    if i % 2 == 0: #condición if donde el numero i del range() sea divisible en 2 y el resto sea 0, numero par. 
        continue # omite la iteracción y pasa a la siguiente, si i es par, la instrucción print(i) se omite. 
    print(i) # se imprimi solo numeros impares, debido a q se omitieron los pares con "continue" 

#bucle for con pass. 
for i in range (10):
 pass

# LISTAS DE DATOS. 
Carros = ["renault", "kia", "mazda"]
print (Carros [1])
Carros.append ("mercedez")
print(Carros)
Carros.insert (0, "honda")
print(Carros)
Carros.remove("kia")
print(Carros)
carros_eliminados = Carros.pop (2)
print(Carros)
print(carros_eliminados)
Carros.sort()
print(Carros)
Carros.reverse()
print(Carros)

#LISTA DE COMPRESIÓN. 
NUMEROS = range(1,11) #lista de NUMEROS  que van desde el 1 al 10
cuadrados = [x **2 for x in NUMEROS] # compresion de lista, toma cada numero x de la lista NUMEROS y lo eleva al cuadrado. 
print(cuadrados) #imprime la lista al calcular la variable x al cudrado **2 

#Diccionarios   
''' el diccionario es una estructura de datos mutable y no ordenada, almacena pares de clave - valor. Con llaves {} 
se separan por comas "," '''
persona = {"nombre":"Juan","edad": 25,"Ciudad":"Bogotá"}
print (persona["nombre"])
print (persona["edad"])
print (persona["Ciudad"])
#Metodos de diccionario. 
''' '''
print (persona.keys()) #imprime las claves.
print (persona.values()) #imprime los valores.
print (persona.items()) #imprime tanto las claves con sus valores.

persona.update ({"profesión":"ingeniero"})
print (persona)

#Conjuntos SET. 

numeros = set ([1,2,3,4,5])
Conjunto1 = {1,2,3}
Conjunto2 = {3,4,5}

Union = Conjunto1 | Conjunto2
print (Union)
Intersección = Conjunto1 & Conjunto2  
print (Intersección)
Diferencia = Conjunto1 - Conjunto2
print (Diferencia)
Diferencia_Simetrica = Conjunto1 ^ Conjunto2
print (Diferencia_Simetrica)

#Metodos de conjuntos. 
frutas = {"manzana", "banana", "naranja"}

frutas.add("pera") #agrega un elemento al conjunto 
print(frutas)  # Imprime {"manzana", "banana", "naranja", "pera"}

frutas.remove("banana") #elimina un elemento, si no existe genera un error 
print(frutas)  # Imprime {"manzana", "naranja", "pera"}

frutas.discard("uva") #elimina un elemento, si no existe no pasa nada 
print(frutas)  # Imprime {"manzana", "naranja", "pera"}

frutas.add("sandia")
#frutas.clear() # elimina todos los elemenentos del conjunto 
print(frutas)  # Imprime set()

def multiplicar (a,b):
   return a*b
Resultado = multiplicar (5,3) + multiplicar (2,4)
print (Resultado)

pregunta2 = 5*3*2*4
print (pregunta2)

numero1 = int(input ("Escribe un nuemero: "))
if numero1 %2==0:
   print ("El numero es par")
else:
   print ("El numero ", numero1, "Es impar")  

              