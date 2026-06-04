#1- O erro que vai dar é o "IndexError: list index out of range".
#2- Isso acontece porque a segunda linha da lista tem só 2 números, mas o código tenta buscar um terceiro elemento que não existe lá dentro.
#3- codigo corrigido.

dados = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8]
]

for i in range(len(dados)):
    for j in range(len(dados[i])):
        print(dados[i][j])