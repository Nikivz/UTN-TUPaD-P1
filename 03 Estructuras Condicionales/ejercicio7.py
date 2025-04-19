texto = input("Ingresa una frase o palabra: ")

if texto[-1].lower() in "aeiou":
    texto += "!"

print(texto)