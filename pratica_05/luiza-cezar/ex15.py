# Exercício 15 - Maior média da turma

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
print("EXERCÍCIO 15 - MAIOR MÉDIA DA TURMA")
print("=" * 60)

print("\nCálculo das médias:\n")

medias = []
for i, nome in enumerate(nomes):
    media = calcular_media(notas[i])
    medias.append((nome, media))
    print(f"{nome}: {media:.2f}")

# Encontrando a maior média
maior_media = max(medias, key=lambda x: x[1])

print("\n" + "-" * 60)
print(f"\nMaior média: {maior_media[0]} - {maior_media[1]:.2f}")

print("\n" + "=" * 60)
print("✓ Resultado: Carla tem a maior média da turma com 9.17")
print("=" * 60)
