import os
os.system("cls")

#bucle while 
#con una sola y simple condición.
print ("bucle While")
contador = 0
while contador <= 5:
    print (contador) #miesntras la condicion contador < 5 se cumpla. Se hace lo de la linea de abajo, se imprime. 
    contador += 1 #Es importante para evitar un bucle infinito.

#while True:
    #print("hola") #Esta es una demostracion de bucle infinito. 

contador1 = 0
print ("bucle while con break ")
while True:
  print(contador1)
  contador1 +=1
  if contador1 == 10:
     break
print ("segundo ejejmplo")

contador2 = 0
while contador2 <= 100:
   contador2 += 1
   print(contador2)
   
   if contador2 % 5 == 0:
      print(f"el numero {contador2} es multiplo de 5")
      break
