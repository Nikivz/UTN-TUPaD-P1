suma = 0
cantidad = 100

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i+1}: "))
    suma += numero

media = suma / cantidad
print("La media es:", media)
