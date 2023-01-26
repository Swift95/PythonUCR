"""triangulo_de_numeros

Se crea un triangulo con numeros que llegan hasta el valor ingresado
"""

#Se recibe y valida que el input es un numero
while True:
    try:
        NumEntrada=int(input("digite un numero entero positivo:  "))
        break

    except ValueError:
        print("Este programa recibe unicamente numeros")
        continue

#Se valida si el numero es negativo   
if NumEntrada < 1:
    print("Error: El numero debe ser mayor a 0")
    
#Se concatenan los numeros para crear el triangulo
else:
    concatenado=""
    for i in range(1,NumEntrada+1):
        #concatenado += str(i)+" "
        concatenado= ''.join([concatenado, str(i)])
        print(concatenado)