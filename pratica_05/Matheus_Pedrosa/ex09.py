valores = [
    [3, 5, 7],
    [2, 4, 6],
    [1, 8, 9]
]

soma_total = 0
for linha in valores:
    for valor in linha:
        soma_total += valor

print(f"Soma total: {soma_total}")
