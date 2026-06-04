# Exercício 4 - Acesso direto

notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

print("=" * 60)
print("EXERCÍCIO 4 - ACESSO DIRETO")
print("=" * 60)

print("\nMatriz de notas:")
for i, estudante in enumerate(notas):
    print(f"Estudante {i}: {estudante}")

print("\n" + "-" * 60)

# Acesso 1
print("\n1. A primeira nota do primeiro estudante:")
nota_1 = notas[0][0]
print(f"   notas[0][0] = {nota_1}")

# Acesso 2
print("\n2. A terceira nota do segundo estudante:")
nota_2 = notas[1][2]
print(f"   notas[1][2] = {nota_2}")

# Acesso 3
print("\n3. A segunda nota do terceiro estudante:")
nota_3 = notas[2][1]
print(f"   notas[2][1] = {nota_3}")

# Acesso 4
print("\n4. A terceira nota do quarto estudante:")
nota_4 = notas[3][2]
print(f"   notas[3][2] = {nota_4}")

# Acesso 5
print("\n5. A linha completa de notas do terceiro estudante:")
linha_3 = notas[2]
print(f"   notas[2] = {linha_3}")

print("\n" + "=" * 60)
print("✓ Nota: Em matriz[i][j], i é a linha e j é a coluna.")
print("  O primeiro índice vai de 0 a 3 (4 estudantes)")
print("  O segundo índice vai de 0 a 2 (3 notas por estudante)")
print("=" * 60)
