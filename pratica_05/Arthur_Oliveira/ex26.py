#1. Qual erro pode ocorrer? IndexError: list index out of range
#2. Por que esse erro acontece?O loop interno usa range(3) fixo para todas as linhas, mas a linha [4, 5] tem apenas 2 elementos (índices 0 e 1). Quando j chega em 2, tenta acessar dados[1][2] — que não existe. dados[1] = [4, 5] j=0 j=1  ← j=2 não existe!
#3. Código corrigido:
dados = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8]
]

for i in range(len(dados)):
    for j in range(len(dados[i])):  # ← se adapta ao tamanho de cada linha
        print(dados[i][j])