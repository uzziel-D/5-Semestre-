numeros = [2, 7, 11, 15]
objetivo = 9

for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        if numeros[i] + numeros[j] == objetivo:
            print(numeros[i], numeros[j])