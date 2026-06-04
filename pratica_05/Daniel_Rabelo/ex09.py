valores = [
    [3, 5, 7],
    [2, 4, 6],
    [1, 8, 9]
]

soma = 0

for linha in valores:
    for numero in linha:
        soma += numero

print(f"A soma de todos os valores é: {soma}")