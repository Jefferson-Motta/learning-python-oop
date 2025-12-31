from abc import ABC, abstractmethod

class Imovel(ABC):
    def __init__(self, nome, uf, valor, endereco='', area=''):
        self._nome = nome
        self._uf = uf
        self._valor = valor
        self._endereco = endereco
        self._area = area

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def uf(self):
        return self._uf

    @uf.setter
    def uf(self, uf):
        self._uf = uf

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, area):
        self._area = area

    def detalhar(self):
       print(self.__dict__)

    def calcularImposto(self):
        return self._valor * 0.02

    @abstractmethod
    def aluguelSugerido(self):
        pass


class ImovelResidencial(Imovel):
    def __init__(self, nome, uf, valor, endereco='', area='', quartos=0, piscinas=False):
        super().__init__(nome, uf, valor, endereco, area)
        self._quartos = quartos
        self._piscinas = piscinas

    def aluguelSugerido(self):
        return self._valor * 0.01


class ImovelComercial(Imovel):
   
       def calcularImposto(self):
        match self._uf:
            case 'DF': taxa = 0.03
            case 'SP': taxa = 0.04
            case 'RJ': taxa = 0.025
            case _: taxa = 0.02

        return self._valor * taxa

       def aluguelSugerido(self):
            return self._valor * 0.015


class ImovelRural:
    def __init__(self, hectares='', curral='', produtiva=True):
        self._hectares = hectares
        self._curral = curral
        self._produtiva = produtiva

    def mesDePlantacao(self, mes):
        match int(mes):
            case 1:
                print('Milho')
            case 2:
                print('Feijão')
            case 3:
                print('Soja')
            case _:
                print('Algodão')


class Fazenda(Imovel, ImovelRural):
    def __init__(self, nome, uf, valor, hectares='', curral='', produtiva=True, endereco='', area=''):
        Imovel.__init__(self, nome, uf, valor, endereco, area)
        ImovelRural.__init__(self, hectares, curral, produtiva)

    def aluguelSugerido(self):
        return self._valor * 0.025


# Testes

casa = ImovelResidencial('Minha Casa', 'GO', 300000)
casa.nome = 'Casa Bonita'
print("Detalhes do imovel:")
casa.detalhar()
print("Imposto:", casa.calcularImposto())
print("Aluguel Sugerido:", casa.aluguelSugerido())

print("\nDetalhes do imovel:")
clinica = ImovelComercial('Clinica X', 'AL', 800000)
clinica.detalhar()
print("Imposto:", clinica.calcularImposto())
print("Aluguel Sugerido:", clinica.aluguelSugerido())

