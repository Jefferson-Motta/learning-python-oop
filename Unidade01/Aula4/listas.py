numeros = [10, 52, 13, 84, 15]
print("1->", [3])

numeros.append(50)
print("2->", numeros)

numeros.remove(50)
print("3->", numeros)

del numeros[3]
print("4->", numeros)

numeros = sorted((numeros))
print("5->", numeros)

for n in numeros:
    print(n)
    