# Exercício 9 - Soma geral

valores = [
    [3, 5, 7],
    [2, 4, 6],
    [1, 8, 9]
]

print("=" * 60)
print("EXERCÍCIO 9 - SOMA GERAL")
print("=" * 60)

print("\nMatriz de valores:")
for i, linha in enumerate(valores):
    print(f"Linha {i}: {linha}")

# Calculando a soma
soma_total = 0
for linha in valores:
    for valor in linha:
        soma_total += valor

print("\n" + "-" * 60)
print(f"\nSoma total: {soma_total}")

print("\n" + "=" * 60)
print("✓ Cálculo detalhado:")
print("  Linha 0: 3 + 5 + 7 = 15")
print("  Linha 1: 2 + 4 + 6 = 12")
print("  Linha 2: 1 + 8 + 9 = 18")
print("  Total: 15 + 12 + 18 = 45")
print("=" * 60)
