# a)
#lista = [3, 1, 2]
#resultado = lista.sort()
#print(resultado)

# O problema: O .sort() organiza a lista, mas não manda nada de volta. Por isso, salvar o resultado dele deixa a variável vazia (None).
lista = [3, 1, 2]
lista.sort()
print(lista) 



# b) 
#nomes = ["Ana", "Bruno"]
#print(nomes[5])

# O problema: A lista só tem as posições 0 e 1. Procurar a posição 5 dá erro porque ela não existe
nomes = ["Ana", "Bruno"]
indice = 5

if indice < len(nomes):
    print(nomes[indice])
else:
    print("Esse índice não existe nessa lista!")