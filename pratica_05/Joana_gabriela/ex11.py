numeros = [
    [12, 5, 8],
    [9, 21, 3],
    [14, 6, 18]
]

maior = numeros[0][0]
menor = numeros[0][0]

for linha in numeros:
    for numero in linha:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")