nombre = input("Ingresa tu nombre: ")

print("Elige una opción: ")
print("1. Nombre en MAYÚSCULAS")
print("2. Nombre en minúsculas")
print("3. Nombre con la primera letra en mayúscula")
opcion = input("Ingresa 1, 2 o 3: ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción inválida. Ingresa 1, 2 o 3.")
