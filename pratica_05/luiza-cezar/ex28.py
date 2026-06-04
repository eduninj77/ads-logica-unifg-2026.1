# Exercício 28 - Acumulador no lugar errado

print("=" * 60)
print("EXERCÍCIO 28 - ACUMULADOR NO LUGAR ERRADO")
print("=" * 60)

notas = [
    [8, 7, 9],
    [5, 6, 5],
    [9, 10, 8]
]

print("\nMatriz de notas:")
for i, linha in enumerate(notas):
    print(f"Linha {i}: {linha}")

print("\n" + "-" * 60)
print("\n--- CÓDIGO COM ERRO ---\n")

print("soma = 0")
print("for i in range(len(notas)):")
print("    for j in range(len(notas[i])):")
print("        soma += notas[i][j]")
print("    media = soma / len(notas[i])")
print("    print(media)")

print("\nExecutando código com erro:\n")

# Código com erro
soma_errada = 0
for i in range(len(notas)):
    for j in range(len(notas[i])):
        soma_errada += notas[i][j]
    media_errada = soma_errada / len(notas[i])
    print(f"Linha {i}: {media_errada:.2f}")

print("\n" + "-" * 60)
print("\nPergunta 1: Qual é o problema com a variável soma?")
print("Resposta: A soma nunca é zerada! Ela ACUMULA valores de todas as linhas.")
print("         Você vê: [8+7+9]/3, depois [8+7+9+5+6+5]/3, depois [8+7+9+5+6+5+9+10+8]/3")

print("\nPergunta 2: Código corrigido\n")

print("Código correto:")
print("for i in range(len(notas)):")
print("    soma = 0  # ← Zera a soma para CADA linha")
print("    for j in range(len(notas[i])):")
print("        soma += notas[i][j]")
print("    media = soma / len(notas[i])")
print("    print(media)")

print("\nExecutando código corrigido:\n")

# Código correto
for i in range(len(notas)):
    soma = 0  # Zera a soma para cada linha
    for j in range(len(notas[i])):
        soma += notas[i][j]
    media = soma / len(notas[i])
    print(f"Linha {i}: {media:.2f}")

print("\n" + "-" * 60)
print("\nPergunta 3: Explique por que a correção funciona")
print("Resposta: Ao zerar a soma dentro do loop externo, cada linha")
print("         calcula sua própria média independentemente das linhas anteriores.")

print("\n" + "=" * 60)
print("✓ Lição: Verifique o escopo dos acumuladores/variáveis!")
print("=" * 60)
