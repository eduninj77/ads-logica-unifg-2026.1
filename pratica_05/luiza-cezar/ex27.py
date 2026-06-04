# Exercício 27 - Inicialização incorreta

print("=" * 60)
print("EXERCÍCIO 27 - INICIALIZAÇÃO INCORRETA")
print("=" * 60)

print("\n--- PROBLEMA ---\n")

print("Código problemático:")
print("matriz = [[0] * 3] * 3")
print("matriz[0][0] = 1")
print("print(matriz)")

matriz_problema = [[0] * 3] * 3
print("\nExplicação do problema:")
print("O operador * cria referências ao MESMO objeto (não cópias!)")

print("\nAntes da alteração:")
for linha in matriz_problema:
    print(linha)

matriz_problema[0][0] = 1
print("\nDepois de matriz[0][0] = 1:")
for linha in matriz_problema:
    print(linha)

print("\n" + "-" * 60)
print("\nPergunta 1: Qual resultado será exibido?")
print("Resposta: [[1, 0, 0], [1, 0, 0], [1, 0, 0]]")
print("Todas as linhas foram alteradas, não apenas a primeira!")

print("\nPergunta 2: Por que esse comportamento pode confundir iniciantes?")
print("Resposta: O iniciante espera alterar apenas matriz[0][0], mas como")
print("         todas as linhas referem-se ao MESMO objeto, todas mudam.")

print("\nPergunta 3: Reescreva usando compreensão de listas\n")

# Solução correta usando compreensão de lista
print("Código correto com compreensão de listas:")
print("matriz = [[0 for j in range(3)] for i in range(3)]")
print("ou")
print("matriz = [[0]*3 for i in range(3)]  # Mais simples")

matriz_correta = [[0]*3 for i in range(3)]

print("\nAntes da alteração:")
for linha in matriz_correta:
    print(linha)

matriz_correta[0][0] = 1
print("\nDepois de matriz[0][0] = 1:")
for linha in matriz_correta:
    print(linha)

print("\n" + "=" * 60)
print("✓ Solução: Use compreensão de listas para criar matrizes independentes")
print("=" * 60)
