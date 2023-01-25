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
print("Estudiante: %s" % (Diccionario_Notas["class"]["student"]["name"]))
print("Notas:")
for materia, nota in Diccionario_Notas["class"]["student"]["marks"].items():
    print("  {0}: {1}".format(materia,nota))
    
