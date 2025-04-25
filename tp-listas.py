#Ejercicio N° 1
""""
lista = []
for i in range(0,100 + 1):
    if i % 4 == 0:
        lista.append(i)
print(lista) """

#Ejercicio N° 2
"""
lista = [32,"emiliano",'ñ',1.14,["maceta",455]]

print(lista[-2]) """

#Ejercicio N° 3
"""
listaVacia = []
print("Lista vacia: ",listaVacia)

listaVacia.append('Primer')
print("Primer elemento agregado ",listaVacia)

listaVacia.append('Segundo')
print("Segundo elemento agregado ",listaVacia)

listaVacia.append('Tercero')
print("Tercer elemento agregado ",listaVacia) """

#Ejercicio N° 4
"""
animales = ['perro','gato','conejo','pez']
print("Lista Original ",animales)

animales[1] = 'loro'
print("Se agrego el primer cambio ",animales)

animales[-1] = 'oso'

print("Se agrego el ultimo cambio ",animales) """

#Ejercicio N° 5
"""
numero = [8,15,3,22,7]

numero.remove(max(numero))

print(numero)

#Al ejecutar el programa se elimina el valor numerico de mas valor, 
# en el caso de poner "Min" se elimina el valor de menor valor """

#Ejercicio N° 6
"""
lista = []
for i in range (10,30 +1,5):
    lista.append(i)
print(lista[0:2]) """

#Ejercicio N° 7
"""
autos = ['sedan','polo','suran','gol']
print("Lista sin modificaciones: ",autos)

autos[1] = 'duna'
print("Lista con la primera modificacion ",autos)

autos[2] = 'amarok'
print("Lista con la segundo modificacion ",autos) """

#Ejercicio N° 8 

"""
lista = []

lista.append(2*5)
print("Lista con el primer valor agregado ",lista)

lista.append(2*10)
print("Lista con el segundo valor agregado ",lista)

lista.append(2*15)
print("Lista con el tercer valor agregado ",lista) """

#Ejercicio N° 9
""""
compras = [['pan','leche'],'arroz','fideos','salsa',['agua']]


compras[4].append('jugo')

print("Cambio en la lista del tercer cliente: ",compras)

compras[2] = 'tallarines'

print("Cambio Fides por tallarines: ",compras)

compras[0].remove('pan')

print("Eliminacion de: pan del primer cliente: ",compras) """

#Ejercicio N° 10

listaAnidada = []

listaAnidada.append(15)
listaAnidada.append(True)
listaAnidada.append([25.5])
listaAnidada[2].append(57.9)
listaAnidada[2].append(30.6)
listaAnidada.append(False)
print(listaAnidada)



               
    