matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Laço externo percorre as linhas
# Laço interno percorre as colunas
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"Linha {i}, Coluna {j}: Valor {matriz[i][j]}")