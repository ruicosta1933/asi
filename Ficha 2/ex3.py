#receber uma data DD/MM/AAAA

x = input("Insira uma data no formato DD/MM/AAAA: ")

# verificar se é válida

if len(x) != 10:
    print("Data inválida")
    exit()

if x[2] != "/" or x[5] != "/":
    print("Data inválida")
    exit()


#pegar no ano
ano = x[6:]

idade = 2021 - int(ano)

print("A idade é: ", idade)

if idade <= 12:
    print("Crianca")
elif idade >= 13 and idade <= 17:
    print("Juvenil")
elif idade >= 18 and idade <= 64:
    print("Adulto")
else:
    print("Senior")

    