#Parte A
#E que o sort mexe direto na lista e não devolve nada e quando tenta printar a variavel resultado ela fica vazia (none)

lista = [3, 1, 2]
resultado = lista.sort()
print(resultado) 

#Codigo arrumado

lista = [3, 1, 2]
lista.sort() #primeiro pede
print(lista) #depois mostra a lista

#Parte B
#Da erro porque a lista so tem apenas 2 nomes e tentar puxar a posicao 5 que não existe vai dar erro

nomes = ["Ana", "Bruno"]
print(nomes[5])

#Codigo arrumado

nomes = ["Ana", "Bruno"]
indice = 5

if indice < len(nomes):
    print(nomes[indice])
else:
    print("indice invalido, porque a lista e menor que o pedido")