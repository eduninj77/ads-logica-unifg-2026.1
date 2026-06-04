valores = [
    [3, 5, 7],
    [2, 4, 6],
    [1, 8, 9]
]

soma = 0

for linha in valores:
    for numeros in linha:
        soma += numeros

print(f"Soma completa é : {soma}")