nomes = ["Ana", "Bruno", "Carla", "Diego", "Eva"]

notas = [
    [8.0, 7.5, 9.0, 6.5],
    [5.0, 6.0, 5.5, 4.0],
    [9.0, 8.5, 10.0, 9.5],
    [6.5, 7.0, 6.0, 5.5],
    [3.0, 4.0, 3.5, 2.5]
]

medias = []

for i in range(len(nomes)):
    media = sum(notas[i]) / len(notas[i])
    medias.append(media)
    if media >= 7.0:
        situacao = "Aprovado"
    elif media >= 5.0:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    print(f"{nomes[i]} - Média: {media:.2f} - {situacao}")

print(f"\nMaior média: {nomes[medias.index(max(medias))]} - {max(medias):.2f}")
print(f"Menor média: {nomes[medias.index(min(medias))]} - {min(medias):.2f}")
