"""Notas_de_Clase

Este prograba imprime las notas que un estudiante obtuvo en cada materia apartir de un diccionario
"""
#Datos a cargar
Diccionario_Notas= {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80,
                "math": 90
            },
        }
    }
}

#Impresion de datos seleccionado
notas=[]
for materia, nota in Diccionario_Notas["class"]["student"]["marks"].items():
    notas.append(nota)

promedio= sum(notas)/len(notas)
print("{0}: {1}".format(Diccionario_Notas["class"]["student"]["name"],promedio))