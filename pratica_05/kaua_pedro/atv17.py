notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

menor_media = float("inf")
menor_av = 0

for j in range(len(notas[0])):
    soma = sum(notas[i][j] for i in range(len(notas)))
    media = soma / len(notas)
    if media < menor_media:
        menor_media = media
        menor_av = j

print("Avaliação com menor média:", menor_av)
print(f"Média: {menor_media:.2f}")
