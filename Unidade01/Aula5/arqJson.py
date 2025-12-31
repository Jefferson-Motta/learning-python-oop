# criando um arquivo JSON

import json
pessoas = [
    { 'nome': 'Lucas', 'telefone': '123456789', 'endereco': 'Rua A' },
    { 'nome': 'Ana', 'telefone': '987654321', 'endereco': 'Rua B' },
    { 'nome': 'João', 'telefone': '456789123', 'endereco': 'Rua C' }  
]

with open('pessoas.json', 'w') as arquivo_json:
    json.dump(pessoas, arquivo_json, indent=4)

