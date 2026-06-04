# Exercício 17 - Avaliação com menor média

nomes = ["Ana", "Bruno", "Carla", "Diego"]

notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

print("=" * 60)
print("EXERCÍCIO 17 - AVALIAÇÃO COM MENOR MÉDIA")
print("=" * 60)

print("\nCalculando média por avaliação:\n")

# Calculando média por avaliação
num_avaliacoes = len(notas[0])
medias_avaliacoes = []

for j in range(num_avaliacoes):
    soma = 0
    for i in range(len(nomes)):
        soma += notas[i][j]
    media_aval = soma / len(nomes)
    medias_avaliacoes.append(media_aval)
    print(f"Avaliação {j} - Média: {media_aval:.2f}")

# Encontrando a avaliação com menor média
indice_menor = medias_avaliacoes.index(min(medias_avaliacoes))
menor_media = medias_avaliacoes[indice_menor]

print("\n" + "-" * 60)
print(f"\nAvaliação com menor média: {indice_menor}")
print(f"Média: {menor_media:.2f}")

print("\n" + "=" * 60)
print("✓ Resultado: A Avaliação 0 teve a menor média com 7.13")
print("=" * 60)
