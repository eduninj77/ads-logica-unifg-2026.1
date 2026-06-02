# Exercício 1 - Identificando linhas e colunas

# Matriz de análise
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Respondendo as questões
print("=" * 50)
print("EXERCÍCIO 1 - IDENTIFICANDO LINHAS E COLUNAS")
print("=" * 50)

# Pergunta 1
print("\n1. Quantas linhas a matriz possui?")
num_linhas = len(matriz)
print(f"   Resposta: {num_linhas} linhas")

# Pergunta 2
print("\n2. Quantas colunas existem em cada linha?")
num_colunas = len(matriz[0])
print(f"   Resposta: {num_colunas} colunas")

# Pergunta 3
print("\n3. Qual valor está em matriz[0][2]?")
valor_0_2 = matriz[0][2]
print(f"   Resposta: {valor_0_2}")

# Pergunta 4
print("\n4. Qual valor está em matriz[2][1]?")
valor_2_1 = matriz[2][1]
print(f"   Resposta: {valor_2_1}")

# Pergunta 5
print("\n5. Explique, com suas palavras, por que matriz[1][1] retorna 50.")
print("   Resposta: matriz[1][1] retorna 50 porque o índice 1 da primeira")
print("   dimensão acessa a linha com índice 1 (segunda linha), que é")
print("   [40, 50, 60], e o índice 1 da segunda dimensão acessa a coluna")
print("   com índice 1 (segundo elemento), que é 50.")

# Exibição da matriz
print("\n" + "=" * 50)
print("Matriz analisada:")
for linha in matriz:
    print(linha)
print("=" * 50)

print("\n✓ Em uma matriz, as linhas são o primeiro índice e as colunas")
print("  são o segundo índice. Ou seja, em matriz[i][j], i é a linha e")
print("  j é a coluna.")
