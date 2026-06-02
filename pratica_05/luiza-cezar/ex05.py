# Exercício 5 - Alterando valores

notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

print("=" * 60)
print("EXERCÍCIO 5 - ALTERANDO VALORES")
print("=" * 60)

print("\nMatriz original:")
for i, linha in enumerate(notas):
    print(f"Linha {i}: {linha}")

print("\n" + "-" * 60)

# Alteração 1
print("\n1. Alterando a primeira nota do segundo estudante para 6.5:")
notas[1][0] = 6.5
print(f"   notas[1][0] = 6.5 ✓")
print(f"   Linha 1 agora: {notas[1]}")

# Alteração 2
print("\n2. Alterando a terceira nota do quarto estudante para 7.0:")
notas[3][2] = 7.0
print(f"   notas[3][2] = 7.0 ✓")
print(f"   Linha 3 agora: {notas[3]}")

print("\n" + "-" * 60)

# Exibição da matriz completa após alterações
print("\nMatriz completa após as alterações:")
for i, linha in enumerate(notas):
    print(f"Linha {i}: {linha}")

print("\n" + "=" * 60)
print("✓ Resumo das alterações realizadas:")
print("  • notas[1][0]: alterada de 5.0 para 6.5")
print("  • notas[3][2]: alterada de 6.0 para 7.0")
print("=" * 60)
