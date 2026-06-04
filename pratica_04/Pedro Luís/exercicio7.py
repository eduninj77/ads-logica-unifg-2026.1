import os
os.system("clear" if os.name != "nt" else "cls")

estudantes = ["Ana", "Bruno", "Carla", "Daniel"]
procurado = input("Digite o nome de um estudante: ").strip().title()
achou = False
for i in estudantes:
    if i == procurado:
        achou = True
        break
print(achou)