# Exercício 22 - Faltas por estudante

presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

def contar_faltas_por_estudante(matriz_presencas):
    """Conta as faltas de cada estudante"""
    faltas = []
    for i, linha in enumerate(matriz_presencas):
        total_faltas = linha.count("F")
        faltas.append(total_faltas)
    return faltas

print("=" * 60)
print("EXERCÍCIO 22 - FALTAS POR ESTUDANTE")
print("=" * 60)

print("\nMatriz de presença:\n")
print("Estudante\\Aula", end="")
for j in range(len(presencas[0])):
    print(f"\t{j}", end="")
print()

for i, linha in enumerate(presencas):
    print(f"Estudante {i}\t", end="")
    for j, status in enumerate(linha):
        print(f"\t{status}", end="")
    print()

print("\n" + "-" * 60)
print("\nFaltas por estudante:\n")

faltas_por_estudante = contar_faltas_por_estudante(presencas)

for i, total_faltas in enumerate(faltas_por_estudante):
    print(f"Estudante {i} - Faltas: {total_faltas}")

print("\n" + "=" * 60)
print("✓ Contagem de faltas:")
print("  Estudante 0: 1 falta (aula 2)")
print("  Estudante 1: 2 faltas (aulas 1 e 2)")
print("  Estudante 2: 1 falta (aula 4)")
print("  Estudante 3: 2 faltas (aulas 0 e 3)")
print("=" * 60)
