#Ejercicio N° 1

#Crear funcion
"""
def imprimir_hola_mundo():
    return print("Hola mundo")

#Programa Principal, llamar a la funcion
#Mostrar funcion

imprimir_hola_mundo()  """

#Ejercicio N° 2
"""
#Crear funcion

def saludar_usuario():
    return print(f"Hola {usuario}")
    
#Programa Principal, pedir nombre al usuario

usuario = input("Ingrese su nombre ")

#Mostrar saludo
saludar_usuario() """

#Ejercicio N° 3
"""
#Crear funcion

def informacion_personal():
    
    return print(f"Soy {nombre} {apellido} tengo {edad} y vivo en {residencia}")

#Pantalla principal,pedir datos al usuario

nombre = input("Ingrese su nombre ")
apellido = input("Ingrese su apellido ")
edad =int(input("Ingrese su edad "))
residencia = input("Ingrese donde vive ")

#Mostrar datos
informacion_personal() """

#Ejercicio N° 4
"""
import math

#Funcion calcular area del circulo

def calcular_area_circulo(radio):

    return math.pi* math.pow(radio,2)

#Calcular perimetro del circulo

def perimetro_de_circulo(radio):

    return (2*math.pi) * radio

#Programa principal

radio = float(input("Ingrese el radio "))
area = calcular_area_circulo(radio)
perimetro = perimetro_de_circulo(radio)

#Mostrar por pantalla el resultado
print(f"El area del circulo es {area} y el perimetro es {perimetro}") """

#Ejercicio N° 5
"""
#Crear funcion
def segundo_a_horas(segundos):

    return segundos // 3600

#Pedir al usuario los segundos
segundos = int(input("Ingrese los segundos "))

#Mostrar por pantalla
print(segundo_a_horas(segundos)) """

#Ejercicio N° 6
"""
#Crear funcion
def calcular_tablas(numero):

    for i in range (1,10 + 1):
        
        resultado = numero*i
        print(resultado)
    

#Pantalla Principal
numero = int(input("Ingrese un numero "))

#Mostrar por pantalla 
print(calcular_tablas(numero)) """


#Ejercicio N° 7
"""
#Crear Funcion
def operaciones_basicas(a,b):

    r1 = a+b
    r2 = a-b
    r3 = a*b

    if a > 0 and b > 0:
        r4 = a//b
           
    else:
    
        return r1,r2,r3,print("No se puede dividir por 0,Intente nuevamente con otro numero")

    return  r1,r2,r3,r4

#Pantalla Principal
a = int(input("Ingrese un primer numero "))
b = int(input("Ingrese un segundo numero "))

#Mostrar Resultado
print(operaciones_basicas(a,b)) """

#Ejercicio N° 8
"""
import math

#Crear Funcion
def calcular_imc(peso,altura):

    imc = peso // (math.pow(altura,2))

    return imc


#Pantalla Principal
#Ingresar Datos

peso = float(input("Ingresa tu peso "))
altura = float(input("Ingrese su altura "))

#Mostrar por pantalla
print(calcular_imc(peso,altura)) """

#Ejercicio N° 9 
"""
#Importar libreria para la fraccion
from fractions import Fraction

#Crear Funcion
def celcius_a_fahrenheit(celcius):

    return (celcius * Fraction(9,5)) + 32
    
#Pantalla principal
#Pedir datos al usuario
celcius = float (input("Ingrese los grados en celcius "))

#Mostrar resultado
print(celcius_a_fahrenheit(celcius)) """


#Ejercicio N° 10

#Crear Funcion

def calcular_promedio(a,b,c):
    return (a + b + c) / 3

#Pantalla principal
#Pedir datos al usuario
a = float(input("Ingrese el primer numero "))
b = float(input("Ingrese el segundo numero "))
c = float(input("Ingrese el tercer numero "))

#Mostrar por pantalla los resultados
print(calcular_promedio(a,b,c))