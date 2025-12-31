# criando um arquivo csv

import csv

carros = [
    {'Vw', 'Gol', '2020'},
    {'Fiat', 'Uno', '2021'},
    {'Ford', 'Ka', '2022'},
]

with open('carros.csv', 'w',newline='') as arquivo_csv:
    fileCSV = csv.writer(arquivo_csv, delimiter=';')
    
    fileCSV.writerow(['Marca', 'Modelo', 'Ano'])
    fileCSV.writerows(carros)