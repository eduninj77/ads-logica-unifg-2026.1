# Exercício 33 - Questão objetiva ENADE

print("=" * 70)
print("EXERCÍCIO 33 - QUESTÃO OBJETIVA ENADE")
print("=" * 70)

print("\nQuestão:")
print("-" * 70)
print("""
Considere o código:

matriz = [
    [2, 4, 6],
    [8, 10, 12]
]

print(matriz[1][0])

O resultado impresso será:
""")

print("Opções:")
print("A) 2")
print("B) 4")
print("C) 6")
print("D) 8")
print("E) [8, 10, 12]")

print("\n" + "-" * 70)
print("RESPOSTA CORRETA: D\n")

print("Explicação:")
print("-" * 70)
print("""
• matriz[1][0] significa:
  - Índice 1: seleciona a segunda linha [8, 10, 12]
  - Índice 0: seleciona o primeiro elemento dessa linha
  
• Resultado: 8
""")

# Verificação prática
print("Verificação prática:")
matriz = [
    [2, 4, 6],
    [8, 10, 12]
]
resultado = matriz[1][0]
print(f"matriz[1][0] = {resultado}")

print("\n" + "=" * 70)
