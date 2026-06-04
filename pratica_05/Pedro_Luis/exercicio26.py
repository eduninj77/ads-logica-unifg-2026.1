import os
os.system("clear" if os.name != "nt" else "cls")

#1. Erro de índice/lista com um range maior do que a quantidade de elementos dentro dela.
#2. Pois ele está tentando procurar um índice 3 dentro das listas internas da matriz dados, sendo que nenhuma das três listas possuem índice 3.
#3. Resposta:
dados = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8]
]

for i in range(len(dados)):
    for j in range(len(dados[i])):
        print(dados[i][j])