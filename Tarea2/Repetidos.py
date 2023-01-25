"""Eliminacion_de_repetidos

Este programa elimina los valores repetidos de una lista
"""

#Datos a cargar
Lista_repetida=[1, 2, 3, 3, 2, 4, 6]
#Lista_repetida=[3, 3, 3, 3, 3, 3, 3]

#Eliminacion de datos repetidos
Lista_limpia= set(Lista_repetida)

#Impresion de lista limpia
print(str(Lista_limpia))