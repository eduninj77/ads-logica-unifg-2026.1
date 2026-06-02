# Exercício 3 - Complete as lacunas

print("=" * 60)
print("EXERCÍCIO 3 - COMPLETE AS LACUNAS")
print("=" * 60)

# Lacuna 1
print("\n1. Em uma matriz, cada sublista pode ser interpretada como uma")
print("   ___________.")
print("   Resposta: LINHA")

# Lacuna 2
print("\n2. A estrutura que agrupa todas as sublistas é chamada de")
print("   ___________.")
print("   Resposta: LISTA EXTERNA")

# Lacuna 3
print("\n3. O valor armazenado em uma posição específica é chamado de")
print("   ___________.")
print("   Resposta: ELEMENTO")

# Lacuna 4
print("\n4. Em matriz[2][0], o índice 2 seleciona a")
print("   ___________.")
print("   Resposta: LINHA")

# Lacuna 5
print("\n5. Em matriz[2][0], o índice 0 seleciona a")
print("   ___________ dentro da linha.")
print("   Resposta: COLUNA")

# Resumo com exemplo
print("\n" + "=" * 60)
print("Resumo com exemplo:")
print("=" * 60)

matriz_exemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\nmatriz = [")
for linha in matriz_exemplo:
    print(f"    {linha},")
print("]")

print("\n• A LISTA EXTERNA agrupa todas as sublistas")
print("• Cada sublista é uma LINHA")
print("• Cada valor em uma posição é um ELEMENTO")
print("• matriz[2][0] acessa a LINHA 2, COLUNA 0 → valor 7")
print("=" * 60)
