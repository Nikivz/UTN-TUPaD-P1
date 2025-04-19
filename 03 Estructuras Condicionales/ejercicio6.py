import random
from statistics import mean, median, multimode

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
modas = multimode(numeros_aleatorios)

print("Números aleatorios:", numeros_aleatorios)
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda(s): {modas}")

if len(modas) == 1:
    moda = modas[0]
    if media > mediana > moda:
        print("Sesgo positivo")
    elif media < mediana < moda:
        print("Sesgo negativo")
    elif media == mediana == moda:
        print("Sin sesgo")
    else:
        print("No se puede determinar un sesgo claro")
else:
    print("No se puede determinar el sesgo porque no hay una única moda")