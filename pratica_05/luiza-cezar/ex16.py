# Exercício 16 - Média por avaliação

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
print("EXERCÍCIO 16 - MÉDIA POR AVALIAÇÃO")
print("=" * 60)

print("\nBoletim de notas (estudantes × avaliações):")
print("\nEstudantes\\Aval", end="")
for j in range(len(notas[0])):
    print(f"\t{j}", end="")
print()

for i, nome in enumerate(nomes):
    print(f"{nome}\t", end="")
    for j in range(len(notas[i])):
        print(f"\t{notas[i][j]}", end="")
    print()

print("\n" + "-" * 60)
print("\nMédia por avaliação:\n")

# Calculando média por avaliação (coluna)
num_avaliacoes = len(notas[0])
for j in range(num_avaliacoes):
    soma = 0
    for i in range(len(nomes)):
        soma += notas[i][j]
    media_aval = soma / len(nomes)
    print(f"Avaliação {j} - Média: {media_aval:.2f}")

print("\n" + "=" * 60)
print("✓ Cálculo:")
print("  Avaliação 0: (8.0+5.0+9.0+6.5)/4 = 28.5/4 = 7.13")
print("  Avaliação 1: (7.5+6.0+8.5+7.0)/4 = 29.0/4 = 7.25")
print("  Avaliação 2: (9.0+5.5+10.0+6.0)/4 = 30.5/4 = 7.63")
print("=" * 60)
