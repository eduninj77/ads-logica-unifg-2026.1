import os
os.system("clear" if os.name != "nt" else "cls")

nomes = ["Ana", "Bruno", "Carla", "Diego"]

notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]
menor_media = 0
total_alunos = len(nomes)
total_notas = len(notas[0])
for i in range(total_notas):
    soma_notas = 0
    
    for c in range(total_alunos):
        soma_notas += notas[c][i]

    media = soma_notas / total_alunos
    if menor_media == 0:
        menor_media = media
    if menor_media > media:
        menor_media = media
    
    if menor_media == media:
        print(f"Avaliação com menor média: {i}")
        print(f"Avaliação {i} - Média: {media:.2f}")