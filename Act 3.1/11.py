numeros = [0, 1, 0, 3, 12]

resultado = []

for numero in numeros:
    if numero != 0:
        resultado.append(numero)

for numero in numeros:
    if numero == 0:
        resultado.append(numero)

print(resultado)