import os
os.system("clear" if os.name != "nt" else "cls")

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(matriz)):
    for coluna in range(len(matriz[i])):
        valor = matriz[i][coluna]
        print(f"Linha {i} Coluna {coluna} Valor {valor}")