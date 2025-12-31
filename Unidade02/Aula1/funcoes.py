# Funções

def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2): 
    if n2 == 0:
        print("Divisão por zero não é permitida.")
    else:
        return n1 / n2

def calcular(n1, operador, n2):
    
    match operador:
       case '+':
           return somar(n1, n2)
       case '-':
           return subtrair(n1, n2)
       case '*':
           return multiplicar(n1, n2)
       case '/':
           return dividir(n1, n2)
       case other:
           print('Operação inválida')
           return None
       
print(calcular(10, '+', 5))
print(calcular(10, '-', 5))
print(calcular(10, '*', 5))
print(calcular(10, '/', 5))
print(calcular(10, '/', 0))
print(calcular(10, 'x', 5))
# # Funções


