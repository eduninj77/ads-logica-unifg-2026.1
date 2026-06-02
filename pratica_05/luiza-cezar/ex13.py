# Exercício 13 - Média por estudante

nomes = ["Ana", "Bruno", "Carla", "Diego"]

notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

def calcular_media(lista_notas):
    """Calcula a média de uma lista de notas"""
    if len(lista_notas) == 0:
        return 0
    return sum(lista_notas) / len(lista_notas)

print("=" * 60)
print("EXERCÍCIO 13 - MÉDIA POR ESTUDANTE")
print("=" * 60)

print("\nBoletim de notas:")
for i, nome in enumerate(nomes):
    print(f"{nome}: {notas[i]}")

print("\n" + "-" * 60)
print("\nMédias calculadas:\n")

for i, nome in enumerate(nomes):
    media = calcular_media(notas[i])
    print(f"{nome} - Média: {media:.2f}")

print("\n" + "=" * 60)
print("✓ Cálculo:")
print(f"  Ana: (8.0 + 7.5 + 9.0) / 3 = 24.5 / 3 = 8.17")
print(f"  Bruno: (5.0 + 6.0 + 5.5) / 3 = 16.5 / 3 = 5.50")
print(f"  Carla: (9.0 + 8.5 + 10.0) / 3 = 27.5 / 3 = 9.17")
print(f"  Diego: (6.5 + 7.0 + 6.0) / 3 = 19.5 / 3 = 6.50")
print("=" * 60)
