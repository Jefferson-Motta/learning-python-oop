# Exceções em Python
''''
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

try:
    resultado = n1 / n2
    print(f"O resultado da divisão é: {resultado}")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
    
'''
# Exceções personalizadas


n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

try:
    resultado = n1 / n2
    print(f"O resultado da divisão é: {resultado}")

except ValueError:
    print("Valor inválido. Por favor, insira um número inteiro.")

except ZeroDivisionError:
    print("Não é possível dividir por zero.")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
    
finally:
    print("Fim do programa.")   