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
      
for i in range(len(nomes)):
    print(f"{nomes[i]} - Média {media[i]:.2f} - {"Aprovado" if media[i] >= 7.0 else "Recuperação"}")