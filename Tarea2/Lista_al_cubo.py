"""Lista_al_Cubo

Se eleva al cubo los valores de una lista especifica
"""
#Se crea la lista de numeros a elevar
Lista_inicial=[1,3,5,8,9]

#Se crea la lista que almacenara los numeros elevados
Lista_final=[]

#Se elevan los numero de la lista inicial y se almacenan en la lista final
for valor in Lista_inicial:
    Lista_final.append(valor**3)

#Se imprime el producto final
print(Lista_final)