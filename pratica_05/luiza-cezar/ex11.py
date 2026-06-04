# Exercício 11 - Maior e menor valor

numeros = [
    [12, 5, 8],
    [9, 21, 3],
    [14, 6, 18]
]

print("=" * 60)
print("EXERCÍCIO 11 - MAIOR E MENOR VALOR")
print("=" * 60)

print("\nMatriz de números:")
for i, linha in enumerate(numeros):
    print(f"Linha {i}: {linha}")

# Inicializando com o primeiro valor
primeiro_valor = numeros[0][0]
maior = primeiro_valor
menor = primeiro_valor

# Encontrando maior e menor
for linha in numeros:
    for valor in linha:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

print("\n" + "-" * 60)
print(f"\nMaior valor: {maior}")
print(f"Menor valor: {menor}")

print("\n" + "=" * 60)
print("✓ Valores na matriz:")
print("  12, 5, 8, 9, 21, 3, 14, 6, 18")
print("  Maior: 21")
print("  Menor: 3")
print("=" * 60)
