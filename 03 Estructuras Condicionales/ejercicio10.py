# Solicita al usuario los datos
hemisferio = input("¿En qué hemisferio estás? (N/S): ").strip().upper()
mes = int(input("Ingresa el número del mes (1-12): "))
dia = int(input("Ingresa el día del mes: "))

if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"
else:
    estacion_norte = estacion_sur = "Fecha inválida"

if hemisferio == "N":
    print(f"Estás en el hemisferio norte. La estación es: {estacion_norte}")
elif hemisferio == "S":
    print(f"Estás en el hemisferio sur. La estación es: {estacion_sur}")
else:
    print("Hemisferio no reconocido. Por favor ingresa 'N' o 'S'.")