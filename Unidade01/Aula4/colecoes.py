#conjuntos
conjunto = set ([4, 7, 2, 3, 0, 8])
print("Conjunto", conjunto)

#tupla
tupla = (3, 2, 4, 6, 0)
print(tupla)


pessoas = {'nome': 'Orion', 'telefone': '(61)99467-3898', 'endereço': 'ABC'}
print(pessoas['telefone'])

pessoas = [
    {'nome': 'Orion', 'telefone': '(61)99467-3898', 'endereço': 'ABC'},
    {'nome': 'Orion', 'telefone': '(61)99467-3898', 'endereço': 'ABC'},
    {'nome': 'Orion', 'telefone': '(61)99467-3898', 'endereço': 'ABC'},
    {'nome': 'Orion', 'telefone': '(61)99467-3898', 'endereço': 'ABC'},
    {'nome': 'Orion', 'telefone': '(61)99467-3898', 'endereço': 'ABC'},
    {'nome': 'Orion', 'telefone': '(61)99467-3898', 'endereço': 'ABC'},
]

print(pessoas[2]['endereço'])