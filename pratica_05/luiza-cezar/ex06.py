# Exercício 6 - Erro de índice

print("=" * 60)
print("EXERCÍCIO 6 - ERRO DE ÍNDICE")
print("=" * 60)

dados = [
    [1, 2],
    [3, 4]
]

print("\nMatriz dados:")
for i, linha in enumerate(dados):
    print(f"Linha {i}: {linha}")

print("\n" + "-" * 60)

# Questão 1
print("\n1. Esse código executa corretamente?")
print("   codigo_original = print(dados[2][0])")
print("\n   Resposta: NÃO, este código gera um ERRO (IndexError)")
print("   Motivo: A matriz dados possui apenas 2 linhas (índices 0 e 1).")
print("   Tentar acessar dados[2] ultrapassa os limites da matriz.")

# Questão 2
print("\n2. Quais são os índices válidos para as linhas dessa matriz?")
print("   Resposta: 0 e 1")
print("   • dados[0] = [1, 2]")
print("   • dados[1] = [3, 4]")

# Questão 3
print("\n3. Corrija o código para exibir o valor 3:")
print("\n   Código correto:")

# Demonstrando
print("\n   dados[1][0] = ", end="")
print(dados[1][0])

print("\n" + "-" * 60)
print("\nExplicação:")
print("• O valor 3 está na linha de índice 1, coluna de índice 0")
print("• Portanto, usamos dados[1][0]")
print("• O primeiro índice seleciona a linha: dados[1] = [3, 4]")
print("• O segundo índice seleciona a coluna dentro dessa linha: [3, 4][0] = 3")

print("\n" + "=" * 60)
print("✓ Lição importante: Sempre verifique se o índice está dentro")
print("  dos limites da matriz!")
print("=" * 60)
