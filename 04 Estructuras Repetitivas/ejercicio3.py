num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
suma = 0
if num1 < num2:
    for i in range(num1 + 1, num2):
        suma += i
else:
    for i in range(num2 + 1, num1):
        suma += i
print("La suma es:", suma)
