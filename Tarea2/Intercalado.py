"""Intercalador_de_strings

Este programa intercala letras de strings con la misma longitud
"""
#Se reciben los 2 valores de entrada y se valida que tengan la misma longitud 
while True:
    String1=str(input("Ingrese el primer string:  "))
    String2=str(input("Ingrese el primer string:  "))
    
    
    if len(String1)==len(String2):
        break        
    else:
        print("Ambos strings deben tener la misma longitud")  
        continue

#Se intercalan las letras de los strings
concatenado=""
for i in range(len(String1)):
    concatenado += String1[i]+String2[i]

#Se imprime el resultado
print(concatenado)

