# Exercício 10 - Contagem de pares

valores = [
    [3, 5, 7],
    [2, 4, 6],
    [1, 8, 9]
]

print("=" * 60)
print("EXERCÍCIO 10 - CONTAGEM DE PARES")
print("=" * 60)

print("\nMatriz de valores:")
for i, linha in enumerate(valores):
    print(f"Linha {i}: {linha}")

# Contando pares
quantidade_pares = 0
pares_encontrados = []

for linha in valores:
    for valor in linha:
        if valor % 2 == 0:  # Se o resto da divisão por 2 é 0
            quantidade_pares += 1
            pares_encontrados.append(valor)

print("\n" + "-" * 60)
print(f"\nQuantidade de pares: {quantidade_pares}")
print(f"Pares encontrados: {pares_encontrados}")

print("\n" + "=" * 60)
print("✓ Análise detalhada:")
print("  Linha 0: 3(ímpar), 5(ímpar), 7(ímpar) → 0 pares")
print("  Linha 1: 2(par)*, 4(par)*, 6(par)* → 3 pares")
print("  Linha 2: 1(ímpar), 8(par)*, 9(ímpar) → 1 par")
print("  Total: 4 pares")
print("=" * 60)
