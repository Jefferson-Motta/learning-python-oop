
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))
n4 = float(input("Digite a nota 4: "))

soma = n1 + n2 + n3 + n4
media = soma/4

print (f"Sua média é: {media:.2f} !")

if media >= 7:
    print ("Aprovado!")
elif media < 5:
    print ("Reprovado!")
else:
    print ("Em recuperação!")