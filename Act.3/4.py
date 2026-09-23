texto = input("Introduzca una palabra: ")

if texto == texto[::-1]:
    print("Es palíndromo")
else:
    print("No es palíndromo")