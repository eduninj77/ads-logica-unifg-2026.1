matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Laço externo percorre as linhas
# Laço interno percorre as colunas
for linha in matriz:
    for valor in linha:
        print(f"Valor: {valor}")