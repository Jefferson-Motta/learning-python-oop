dia = int(input("Digite o numero equivalente ao dia da semana: "))

'''if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda")
elif dia == 3:
    print("Terça")
elif dia == 4:
    print("Quarta")
elif dia == 5:
    print("Qinta")
elif dia == 6:
    print("Sexta")
elif dia == 7:
    print("Sabado")
else:
    print("O dia não existe.")

'''

match dia:
    case 1:
        print("Domingo!")
    case 2:
        print("Segunda!")
    case 3:
        print("Terça!")
    case 4:
        print("Quarta!")
    case 5:
        print("Quinta!")
    case 6:
        print("Sexta!")
    case 7:
        print("Sábado!")
    case other:
        print("O dia não existe.")
    
