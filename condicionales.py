#Ejercicio 1
"""edad = int(input("Ingrese tu edad "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")"""

#Ejercicio 2

"""nota = int(input("Ingrese la nota del alumno "))

if nota >= 6:
    print("Aprobaste la materia")
else:
    print("Desaprobaste")"""

#Ejercicio 3 

"""num = int(input("Ingrese un numero "))

if num % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor ingrese un numero par")"""

#Ejercicio 4

""" edad = int(input("Ingrese su edad "))

if edad <= 12:
    print("Eres un NIÑO de", edad, " años")
elif edad >= 12 and edad < 18:
    print("Eres un ADOLESCENTE de",edad, " años")
elif edad >= 18 and edad < 30:
    print("Eres un ADULTO/A JOVEN de ",edad," años")
else:
    print("Eres un ADULTO/A de ",edad," años") """

#Ejercicio 5
"""
contraseña = input("Ingrese una contraseña de entre 8 y 14 caracteres ")

if len(contraseña)>= 8 and len(contraseña)<= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor ingrese una contraseña de entre 8 y 14 caracteres") """

#Ejercicio 6
"""
from statistics import mode,median, mean
import random

num_aleatorio = [random.randint (1, 100) for i in range (50)]

print(num_aleatorio)
print()

if mean(num_aleatorio) > median(num_aleatorio) > mode(num_aleatorio):
    print("Es de sesgo positivo")
elif mean(num_aleatorio)< median(num_aleatorio) < mode(num_aleatorio):
    print("Es de sego negativo")
else:
    print("No hay sesgo") """

#Ejercicio 7
"""
cadena = input("Ingrese una frase ")

if cadena[-1] == 'a' or cadena[-1] == 'e':
    print(cadena,"!")

elif cadena[-1] == 'i' or cadena[-1] == 'o':
    print(cadena, "!")
elif cadena[-1] == 'u':
    print(cadena,"!")
else:
    print(cadena) """

#Ejercicio 8
"""
nombre = input("Ingrese su nombre ")
print("Opcion 1: Nombre en Mayusculas")
print("Opcion 2: Nombre en Minusculas")
print ("Opcion 3: La primera letra en Mayuscula")
opcion= int(input("Elija una de las opciones: 1,2,3: "))

if opcion == 1:
   resultado = nombre.upper()
   print(resultado)

elif opcion == 2:
    resultado = nombre.lower()
    print(resultado)
elif opcion == 3:
    resultado = nombre.title()
    print(resultado)
else: 
    print("Elija una opcion correcta") """

#Ejercicio 9
"""
terremoto = int(input("Segun la escala de Ritchter, describa la magnitud de su terremoto: "))

if terremoto < 3:
    print("EL terremoto es Muy Leve (Imperceptible)")
elif terremoto >= 3 and terremoto < 4:
    print("El terremoto es Leve (Ligeramente perceptible)")
elif terremoto >= 4 and terremoto < 5:
    print("El terremoto es Moderado (Sentido por personas, pero generalmente no causa daños)")
elif terremoto >= 5 and terremoto < 6:
    print("El terremoto es Fuerte (Puede causar daños en estructuras debiles)")
elif terremoto >= 6 and terremoto < 7:
    print("El terremoto es Muy fuerte (Puede causar daños significativos)")
elif terremoto >= 7:
    print("El terremoto es Extremo (Puede causar grandes daños a gran escala)")

else:
    print("El numero esta fuera de la escala") """

# Ejercicio 10 

hemisferio = input("Ingrese el hemisferio en que se encuentra ")
dia = int(input("Ingrese el dia en que se encuentre "))
mes = input("Ingrese el mes en que se encuentra ")

if hemisferio == "norte" and ((dia >= 21 and mes == "Diciembre") or(mes == "enero" or mes == "febrero")):
    print("Estamos en invierno")
elif hemisferio == "norte" and dia <= 20 and mes == "marzo":
    print("Estamos en invierno")

elif hemisferio == "sur" and ((dia >= 21 and mes == "Diciembre") or (mes == "enero" or mes == "febrero")) :
    print("Estamos en verano")
elif hemisferio == "sur" and dia <= 20 and mes == "marzo":
    print("Estamos en verano")
else:
    pass


if hemisferio == "norte" and ((dia >= 21 and mes == "marzo") or(mes == "abril" or mes == "mayo")):
    print("Estamos en privamera")
elif hemisferio == "norte" and dia <= 20 and mes == "junio":
    print("Estamos en primavera")

elif hemisferio == "sur" and ((dia >= 21 and mes == "marzo") or (mes == "abril" or mes == "mayo")) :
    print("Estamos en otoño")
elif hemisferio == "sur" and dia <= 20 and mes == "junio":
    print("Estamos en otoño")
else:
    pass



if hemisferio == "norte" and ((dia >= 21 and mes == "junio") or(mes == "julio" or mes == "agosto")):
    print("Estamos en verano")
elif hemisferio == "norte" and dia <= 20 and mes == "septiembre":
    print("Estamos en verano")

elif hemisferio == "sur" and ((dia >= 21 and mes == "junio") or (mes == "julio" or mes == "agosto")) :
    print("Estamos en invierno")
elif hemisferio == "sur" and dia <= 20 and mes == "septiembre":
    print("Estamos en invierno")
else:
    pass



if hemisferio == "norte" and ((dia >= 21 and mes == "septiembre") or(mes == "octubre" or mes == "noviembre")):
    print("Estamos en otoño")
elif hemisferio == "norte" and dia <= 20 and mes == "diciembre":
    print("Estamos en otoño")

elif hemisferio == "sur" and ((dia >= 21 and mes == "septiembre") or (mes == "octubre" or mes == "noviembre")) :
    print("Estamos en primavera")
elif hemisferio == "sur" and dia <= 20 and mes == "diciembre":
    print("Estamos en primavera")
else:
    pass

