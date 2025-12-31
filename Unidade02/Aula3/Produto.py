class Produto:

    def __init__(self, nome = '', marca = '', modelo = '', valor = '', quantidade = 0):
        self.nome = nome
        self.marca = marca
        self.modelo = modelo
        self.valor = valor
        self.quantidade = quantidade
    
    def vender(self, quantidade):
        if(quantidade > self.quantidade):
            print('*********************')
            print('Não há estoque suficiente.')
            print('Quantidade máxima:', self.quantidade)
            print('*********************')
        else:
            self.quantidade -= quantidade
    
    def comprar(self, quantidade):
        self.quantidade += quantidade


produto0 = Produto('Celular', 'Samsung', 'J13', 2000, 100)
produto0.comprar(10)
produto0.vender(100)

produto1 = Produto('Geladeira', 'Brastemp', 'BST9000', 5000, 50)

produto2 = Produto()

print(produto0.__dict__)
print(produto1.__dict__)
print(produto2.__dict__)
