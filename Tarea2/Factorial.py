"""Calcuradora_factorial

Se intenta recibir un int y debe retornal el valor factorial
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
if NumEntrada < 0:
    print("Error de sintaxis")

#Se calcula el factorial del valor ingresado
else:
    RESULTADO=1
    for i in range(1,NumEntrada+1):
        RESULTADO *= i
    print(f"El factorial de {NumEntrada} equivale a {RESULTADO}")
