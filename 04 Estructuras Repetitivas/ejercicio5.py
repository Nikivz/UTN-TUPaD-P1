import random

numero_secreto = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1
    if intento < numero_secreto:
        print("Demasiado bajo")
    elif intento > numero_secreto:
        print("Demasiado alto")
    else:
        print(f"¡Correcto! Intentos: {intentos}")
        break
