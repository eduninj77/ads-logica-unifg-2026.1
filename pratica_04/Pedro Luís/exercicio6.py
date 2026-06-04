import os
os.system("clear" if os.name != "nt" else "cls")

alunos = ["Ana", "Bruno", "Carla", "Daniel"]

for i in range(len(alunos)):
    print(f"Índice {i} -> {alunos[i]}")