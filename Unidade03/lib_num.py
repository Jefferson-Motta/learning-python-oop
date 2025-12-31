import numpy as np

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0
for n in numeros:
    soma += n
media = soma / len(numeros)
array_numeros = np.array(numeros)
print("Média na mão:", media)

media = np.mean(array_numeros)
print("Média com NumPy:", media)