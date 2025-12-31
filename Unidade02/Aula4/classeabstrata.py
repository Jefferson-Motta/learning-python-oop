from abc import ABC, abstractmethod

class Imovel(ABC):
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

    @abstractmethod
    def aluguelSugerido(self):
        pass

class ImovelResidencial(Imovel):
    def __init__(self, nome, uf, valor, endereco ='', area =''):
        super().__init__(nome, uf, valor, endereco, area)
        self.quartos = 0
        self.piscinas = False

    def aluguelSugerido(self):
        return self.valor * 0.01


class ImovelComercial(Imovel):

    def aluguelSugerido(self):
        return self.valor * 0.015


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
            case _: print('Algodão') # Usar _ para o caso default

class Fazenda(Imovel, ImovelRural):

   def __init__(self, nome, uf, valor, hectares='', curral='', produtiva=True, endereco='', area=''):
        Imovel.__init__(self, nome, uf, valor, endereco, area)
        ImovelRural.__init__(self, hectares, curral, produtiva)

   def aluguelSugerido(self):
        return self.valor * 0.025

casa = ImovelResidencial('Minha Casa', 'GO', 300000)
casa.detalhar()
print(casa.aluguelSugerido())


clinica = ImovelComercial('Clinica x ', 'SP', 800000 )
clinica.detalhar()
print(clinica.aluguelSugerido())