# Exercício 8 - Percurso por índice

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("=" * 60)
print("EXERCÍCIO 8 - PERCURSO POR ÍNDICE")
print("=" * 60)

print("\nMatriz:")
for linha in matriz:
    print(linha)

print("\n" + "-" * 60)
print("\nPercorrendo a matriz por índice (usando range(len(...))):\n")

# Percurso por índice
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        valor = matriz[i][j]
        print(f"Linha {i} Coluna {j} Valor {valor}")

print("\n" + "=" * 60)
print("✓ Neste exercício:")
print("  • Usamos range(len()) para obter os índices")
print("  • i percorre as linhas (0 a 2)")
print("  • j percorre as colunas (0 a 2)")
print("  • Temos acesso aos índices para usar em cálculos ou verificações")
print("=" * 60)
