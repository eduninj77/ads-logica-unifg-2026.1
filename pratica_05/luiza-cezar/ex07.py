# Exercício 7 - Percurso por valor

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("=" * 60)
print("EXERCÍCIO 7 - PERCURSO POR VALOR")
print("=" * 60)

print("\nMatriz:")
for linha in matriz:
    print(linha)

print("\n" + "-" * 60)
print("\nPercorrendo a matriz por valor (sem usar range(len(...))):\n")

# Percurso por valor
for linha in matriz:
    for valor in linha:
        print(f"Valor: {valor}")

print("\n" + "=" * 60)
print("✓ Neste exercício:")
print("  • Usamos for...in para iterar diretamente sobre os valores")
print("  • Não utilizamos índices ou range(len())")
print("  • Cada linha é uma sublista")
print("  • Cada valor é um elemento da sublista")
print("=" * 60)
