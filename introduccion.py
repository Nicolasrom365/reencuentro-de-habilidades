import random

def jugar_juego():
    continuar = 1
    while continuar == 1:
        print("Bienvenido/a a Destreza de Habilidades de Bendy Play")
        print("Elija la dificultad del juego: 1=Fácil, 2=Medio, 3=Difícil")
        dificultad = int(input("Digite el número de dificultad: "))

        if dificultad == 1:
            cant_digitos = 3
        elif dificultad == 2:
            cant_digitos = 4
        elif dificultad == 3:
            cant_digitos = 5
        else:
            print("Opción de dificultad no válida. Elige 1, 2 o 3.")
            continue

        digitos = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        codigo = ''

        for i in range(cant_digitos):
            elegido = random.choice(digitos)
            while elegido in codigo:
                elegido = random.choice(digitos)
            codigo += elegido

        print("Tiene que adivinar un código de", cant_digitos, "dígitos distintos")
        propuesta = input("¿Qué código propones?: ")

        intentos = 1

        while propuesta != codigo:
            intentos += 1
            aciertos = 0
            coincidencias = 0
            for i in range(cant_digitos):
                if propuesta[i] == codigo[i]:
                    aciertos += 1
                elif propuesta[i] in codigo:
                    coincidencias += 1
            print("Tu propuesta (", propuesta, ") tiene", aciertos, "Aciertos y", coincidencias, "coincidencias")
            propuesta = input("Propón otro código: ")

        print("¡FELICIDADES! Adivinaste el código en", intentos, "intentos")

    print("Gracias por jugar.")
