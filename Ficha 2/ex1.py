idades = [16, 18, 10, 28, 24, 26, 30, 46, 72, 65, 91]
count = 0
soma = 0
# Indique qual é a idade da pessoa mais nova

idades.sort()
print(idades[0])

# Indique qual é a idade da pessoa mais velha

print(idades[-1])

# c) qual a média de idades

print(sum(idades)/len(idades))

# d) media de idades maiores ou iguais a 18 anos e menores ou iguais a 65 


for i in idades:
    if i >= 18 and i <= 65:
        soma += i
        count += 1

print(soma  / count)