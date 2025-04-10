#Ejercicio N° 1
"""
for i in range (0,101):
    print(i)"""

#Ejercicio N° 2
"""
cont =int(0)
num = int(input("Ingrese un numero entero: "))

if num > 0:
    while num > 0:
       num = num //10
       cont = cont + 1
else:
    print("Ingrese un valor mayor a 0")  

print(cont) """

#Ejercicio N°3
"""
resultado = int(0)
num = int(input("Ingrese un primer valor "))
num1 = int(input("Ingrese un segundo valor "))

for i in range (num,num1):

    resultado = resultado + i
  
print(resultado) """

#Ejercicio N° 4
"""
resultado = int(0)
num = int(input("Ingrese un valor "))

while num != 0:
    resultado = resultado + num
    
    num = int(input("Ingrese un valor "))

print(resultado) """

# Ejercicio N° 5
"""
import random

aleatorio = [random.randint(0,9)]

while True:
    num = int(input("Elige un numero entreo el 0 y 9: "))

    if num == aleatorio:
        print("FELICIDADES HAS GANADO")
        break
    if  num < aleatorio:
        print("Elige un numer mas bajo")
        num = input("Elige un numero entreo el 0 y 9: ")
    else:

        print("Elige un numero mas alto")
        num = input("Elige un numero entre el 0 y 9: ")

    """
#Ejercicio N° 6 
"""
for i in range (100,0,-1):
    if i % 2 == 0:
        print(i)  """

#Ejercicio N° 7
"""
num = int(input("Elige un numero: "))
resultado = int(0)
for i in range(0,num):
    resultado = resultado + i

print(resultado) """

#Ejercicio N° 8
"""
cont = int(100)
contPar = int(0)
contImpar = int(0)
contNegativo = int(0)
contPositivo = int(0)
                   
for i in range(0,cont):

    num = int(input("Ingresa un numero: "))
    cont = cont - 1

    if num % 2 == 0:
     contPar = contPar + 1
    else:
     contImpar = contImpar + 1
    if num < 0:
     contNegativo = contNegativo + 1
    else:
        contPositivo = contPositivo + 1

print("Los numero Pares son: ",contPar)
print("Los numero Impares son: ",contImpar)
print("Los numero Negativos son: ",contNegativo)
print("Los numero Positivos son: ",contPositivo) """

#Ejercicio N° 9
"""
suma = int(0)
num = int(0)
media = int(0)
cont = int(100)

while cont > 0:
    num = int(input("Ingrese 100 numeros: "))
    cont = cont -1
    suma = suma + num
   
media = suma / 100   
    
print ("La media es de: ",media)   """
