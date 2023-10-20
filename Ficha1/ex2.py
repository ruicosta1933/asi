string = "8200123;Ana Maria;931221012;12/05/2000"

sol = "SOL"
# Crie uma lista (array) a partir da string usando o “;” como separador

lista = string.split(";")

# Imprima a lista

print(lista)

# Imprima o tamanho da lista

print(len(lista))

# Acrescentar sol a lista
print ("#"*60)
lista.append(sol)
print(lista)

# Converta a lista final para string, usando como separador “,”
print ("#"*60)
string2 = ",".join(lista)
print(string2)





