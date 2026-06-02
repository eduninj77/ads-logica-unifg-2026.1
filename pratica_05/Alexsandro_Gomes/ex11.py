numeros = [
    [12, 5, 8],
    [9, 21, 3],
    [14, 6, 18]
]

maior = numeros[0][0]
menor = numeros[0][1]

for linha in numeros:
    for n in linha:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")