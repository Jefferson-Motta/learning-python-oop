# arquivos em Python
# Criando um arquivo e escrevendo dados nele

arquivo = open('pessoas.txt', 'w')

arquivo.write('Lucas\n')
arquivo.write('Ana\n')
arquivo.write('João\n')

arquivo.close()

# Lendo dados de um arquivo

with open('pessoas.txt', 'r+') as arquivoleitura:
    for linha in arquivoleitura:
        print(linha.strip())