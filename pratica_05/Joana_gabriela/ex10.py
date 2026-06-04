valores = [
    [3, 5, 7],
    [2, 4, 6],
    [1, 8, 9]
]

contagem = 0

for linha in valores:
    for numero in linha:
        if numero % 2 == 0:
            contagem += 1

print(f"Quantidade de pares: {contagem}")