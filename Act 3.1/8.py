texto = input("Introduce una frase: ")
palabras = texto.split()
larga = max(palabras, key=len)
print(larga)