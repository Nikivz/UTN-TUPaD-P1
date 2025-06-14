numero = int(input("Ingrese un número entero: "))
numero_invertido = 0
n = abs(numero)
while n > 0:
    digito = n % 10
    numero_invertido = numero_invertido * 10 + digito
    n //= 10

if numero < 0:
    numero_invertido = -numero_invertido

print("Número invertido:", numero_invertido)
