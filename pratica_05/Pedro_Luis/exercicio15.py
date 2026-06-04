import os
os.system("clear" if os.name != "nt" else "cls")

nomes = ["Ana", "Bruno", "Carla", "Diego"]

notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]
media = []
for i in notas:
    media.append(sum(i) / 3)

maior = 0 
for i in media:
    if maior == 0:
        maior = i
    if maior < i:
        maior = i

for i in range(len(nomes)):
    if maior == media[i]:
        print(f"\nMaior média: {nomes[i]} - Média: {media[i]:.2f}")