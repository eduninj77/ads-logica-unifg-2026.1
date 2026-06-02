# Exercício 37 - Questão objetiva ENADE

print("=" * 70)
print("EXERCÍCIO 37 - QUESTÃO OBJETIVA ENADE")
print("=" * 70)

print("\nQuestão:")
print("-" * 70)
print("""
O código abaixo apresenta um problema:

matriz = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8]
]

print(matriz[1][2])

A análise correta é:
""")

print("Opções:")
print("A) O código imprime 5.")
print("B) O código imprime 6.")
print("C) O código apresenta erro, pois a linha de índice 1 não possui")
print("   coluna de índice 2.")
print("D) O código imprime [4, 5].")
print("E) O código imprime 3.")

print("\n" + "-" * 70)
print("RESPOSTA CORRETA: C\n")

print("Explicação:")
print("-" * 70)
print("""
Análise da matriz:

matriz = [
    [1, 2, 3],      ← linha 0: 3 elementos (índices 0, 1, 2)
    [4, 5],         ← linha 1: 2 elementos (índices 0, 1)
    [6, 7, 8]       ← linha 2: 3 elementos (índices 0, 1, 2)
]

• O código tenta acessar matriz[1][2]
  - Índice 1: seleciona a segunda linha [4, 5]
  - Índice 2: tenta acessar a terceira coluna [4, 5][2]
  
• MAS: a linha de índice 1 só tem 2 elementos (índices 0 e 1)
  Não existe [4, 5][2]!

• RESULTADO: IndexError - list index out of range

Análise das opções:
A) Não, pois causaria erro
B) Não, pois causaria erro
C) SIM! A linha 1 ([4, 5]) não possui índice 2
D) Não, matriz[1] retornaria [4, 5], mas matriz[1][2] causa erro
E) Não, pois causaria erro
""")

# Verificação prática
print("Verificação prática:\n")

matriz = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8]
]

print("Tentando executar: print(matriz[1][2])")
print("Linha 1: ", matriz[1])
print(f"Tamanho da linha 1: {len(matriz[1])} elementos")
print("Índices válidos: 0, 1")
print("\nTentativa de acessar índice 2:")

try:
    resultado = matriz[1][2]
    print(resultado)
except IndexError as e:
    print(f"ERRO: {e}")
    print("IndexError: list index out of range")

print("\n" + "=" * 70)
print("✓ Esta é uma matriz IRREGULAR!")
print("  Nem todas as linhas têm o mesmo número de elementos")
print("=" * 70)
