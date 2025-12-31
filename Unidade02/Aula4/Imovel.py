class Imovel:
    def __init__(self, nome, uf, valor, endereco = '', area = ''):
        self.nome = nome
        self.uf = uf
        self.valor = valor
        self.endereco = endereco
        self.area = area
    
    def detalhar(self):
        print(self.__dict__)
    
    def calcularImposto(self):
        return self.valor * 0.02

class ImovelResidencial(Imovel):
    ...

class ImovelComercual(Imovel):
    ...

class ImovelRural:
    def __init__(self, hectares = '', curral = '', produtiva = True):
        self.hectares = hectares
        self.curral = curral
        self.produtiva = produtiva

    def MesdePlantacao(self, mes):
        match int(mes):
            case 1: print('Milho')
            case 2: print('Feijão')
            case 3: print('Soja')
            case other: print('Algodão')

class Fazenda(Imovel, ImovelRural):
   ...


fazenda = Fazenda('Fazenda Modelo', 'GO', 1500000) 
fazenda.detalhar() 
print(fazenda.calcularImposto())
fazenda.MesdePlantacao(7)

casa = ImovelResidencial('Minha Casa', 'GO','19000')  
#casa.detalhar()

clinica = ImovelComercual('Clinica x ', 'SP','30000')  
#clinica.detalhar()



'''imovel = Imovel('Solar do Cerrado', 'DF',5000)
imovel.endereco = 'ABC'
imovel.area = '2000'
imovel.detalhar()'''