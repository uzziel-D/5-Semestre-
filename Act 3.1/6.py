texto = input("Introduzca una palabra: ")

c = 0

for letra in texto:
    if letra in "aeiou":
        c += 1

print(c)