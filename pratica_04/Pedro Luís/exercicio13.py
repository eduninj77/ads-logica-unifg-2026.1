import os
os.system("clear" if os.name != "nt" else "cls")

#Errado
lista = [3, 1, 2]
resultado = lista.sort()#O comando .sort, apenas modifica a própria lista, mas não retorna ela, o certo seria usar lista.sort() e não tentar encaixar esse comando em outra variável.
print(resultado)
#Correto
lista = [3, 1, 2]
resultado = sorted(lista)#No sorted(variável), ele copia e reescreve a cópia em ordem, retornando uma lista ordenada.
print(resultado)

#Errado
nomes = ["Ana", "Bruno"]
print(nomes[5])#A lista nomes apenas possui 2 índice, rodando o código pedindo para o python mostrar o quinto índice daria uma excessão de IndexError.
#Correto
nomes = ["Ana", "Bruno"]
print(nomes[1])#Corrigindo apenas usando os índices que a lista possuis(0["Ana"] ou 1["Bruno"]).

#Errado
numeros = [1, 2, "3", 4, "5"]#O erro está na listagem de tipos dos índices, pois não sem como usar o sum(variável) tendo strings dentro da lista
print(sum(numeros))
#Correto
numeros = [1, 2.3, 3, 4.5, 5]#Já aqui o código funcionará normalmente, pois todas os índices são inteiras(podem possuir também alguns índices float dentro da lista também)
print(sum(numeros))