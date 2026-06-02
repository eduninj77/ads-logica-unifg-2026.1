# Exercício 26 - Corrigindo matriz irregular

print("=" * 60)
print("EXERCÍCIO 26 - CORRIGINDO MATRIZ IRREGULAR")
print("=" * 60)

print("\n--- ANÁLISE DO CÓDIGO ORIGINAL ---\n")

dados = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8]
]

print("dados = [")
print("    [1, 2, 3],")
print("    [4, 5],       ← Esta linha tem apenas 2 elementos!")
print("    [6, 7, 8]")
print("]")

print("\nCódigo original:")
print("for i in range(len(dados)):")
print("    for j in range(3):          ← Problema: sempre tenta acessar 3 elementos")
print("        print(dados[i][j])")

print("\n" + "-" * 60)
print("\nPergunta 1: Qual erro pode ocorrer?")
print("Resposta: IndexError - tentativa de acessar um índice inexistente")

print("\nPergunta 2: Por que esse erro acontece?")
print("Resposta: A linha de índice 1 tem apenas 2 elementos (índices 0 e 1)")
print("         O código tenta acessar dados[1][2], que não existe!")

print("\nPergunta 3: Reescreva o código de forma segura\n")

# Código corrigido
print("Código corrigido:\n")
codigo_corrigido = """
for i in range(len(dados)):
    for j in range(len(dados[i])):  ← Usa len(dados[i]) para cada linha
        print(dados[i][j])
"""
print(codigo_corrigido)

print("Executando código corrigido:\n")

for i in range(len(dados)):
    for j in range(len(dados[i])):
        print(dados[i][j])

print("\n" + "=" * 60)
print("✓ Solução: Use len(dados[i]) para cada linha, não len(dados)")
print("=" * 60)
