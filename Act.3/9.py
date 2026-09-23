texto = input("Introduce una palabra: ")

resultado = ""
contador = 1

for i in range(len(texto)):
    if i + 1 < len(texto) and texto[i] == texto[i + 1]:
        contador += 1
    else:
        resultado += texto[i] + str(contador)
        contador = 1

print(resultado)