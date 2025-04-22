# Eleccion a que desea convertir
seleccion = int(input("Si Desea convertir decimales a binarios presione 1, si desea convertir de binario a decimal presione 2: "))

#Bucle while para iniciar programa, si te equivocas en la selccion te vuelve a preguntar
while True:
    #Si seleccionas la opcion N° 1     
    if seleccion == 1:
        #Se muestra por pantalla:     
        num = int(input("Ingrese un numero mayor a 0 "))

        #Funcion para convertir decimal a binario
        def convertir_a_binario(num):
            #Bucle while para que se ingrese un numero positivo
            while True:

                if num > 0:               
                    binario = ''
                    while num >=1:
                        resultado = num % 2
                        binario = '{}'.format(resultado) + binario
                        num = num // 2
                    return binario
                      
                else:
                    #En el caso de no ingresar un numero positivo se le pedira que vuelva ingresar otro numero                      
                    num = int(input("Por favor ingrese un numero mayor al 0: "))
                
        #Se muestra por pantalla el resultado de la operacion            
        print(convertir_a_binario(num))
        break
                
    #La eleccion N° 2:   
    elif seleccion == 2:
        #Por pantalla nos pide que se ingrese un numero binario
        num1 = str(input("Ingresar numero binario: "))

        #Funcion para convertir de binario a decimal
        def binario_a_decimal():

            decimal = 0
            for i, bit in enumerate(num1):
            
                if bit == "1":
                    decimal += pow(2,len(num1) -1 - i)
            return decimal
        #Se muestra por pantalla el resultado de la operacion
        print(binario_a_decimal())
        break
    #Se le pedira que ingrese un numero valido en el caso que no hayas elegido ni la opcion N° 1 o N° 2.
    else:
        print("Ingrese un numero valido")
        seleccion = int(input("Si Desea convertir decimales a binarios presione 1, si desea convertir de binario a decimal presione 2: "))
