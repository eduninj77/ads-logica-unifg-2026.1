valores = [
    [3, 5, 7],
    [2, 4, 6],
    [1, 8, 9]
]

contagem_pares = 0
for linha in valores:
    for valor in linha:
        if valor % 2 == 0:
            contagem_pares += 1

print(f"Quantidade de pares: {contagem_pares}")
