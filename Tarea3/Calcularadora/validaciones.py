"""Validacion de entrada de usuario"""

def entrada(texto_entrada):
    while True:
        input_usuario= input(f"{texto_entrada} \n")
        if input_usuario == "":
            return input_usuario
        try:
            int_input= int(input_usuario)
            return int_input

        except ValueError:
            print("Este programa recibe unicamente numeros \n")
            continue
