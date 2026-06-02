# Exercício 34 - Questão objetiva ENADE

print("=" * 70)
print("EXERCÍCIO 34 - QUESTÃO OBJETIVA ENADE")
print("=" * 70)

print("\nQuestão:")
print("-" * 70)
print("""
Uma matriz 'notas' possui 5 linhas e 3 colunas. Considerando a 
indexação em Python, a última posição válida dessa matriz é:
""")

print("Opções:")
print("A) notas[5][3]")
print("B) notas[4][2]")
print("C) notas[3][4]")
print("D) notas[2][4]")
print("E) notas[1][1]")

print("\n" + "-" * 70)
print("RESPOSTA CORRETA: B\n")

print("Explicação:")
print("-" * 70)
print("""
• Matriz com 5 linhas → índices de linha: 0, 1, 2, 3, 4
• Matriz com 3 colunas → índices de coluna: 0, 1, 2

• Última posição válida:
  - Última linha: índice 4
  - Última coluna: índice 2
  - Logo: notas[4][2]

• Análise das opções:
  A) notas[5][3] - fora dos limites (não existe linha 5)
  B) notas[4][2] - VÁLIDA (última linha, última coluna)
  C) notas[3][4] - fora dos limites (não existe coluna 4)
  D) notas[2][4] - fora dos limites (não existe coluna 4)
  E) notas[1][1] - válida, mas não é a última posição
""")

# Verificação prática
print("Verificação prática:")
notas = [[0]*3 for _ in range(5)]  # 5 linhas, 3 colunas
print(f"Dimensões: {len(notas)} linhas × {len(notas[0])} colunas")
print(f"Última posição válida: notas[{len(notas)-1}][{len(notas[0])-1}]")
print(f"                    = notas[4][2]")

print("\n" + "=" * 70)
