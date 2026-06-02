estudantes = ["Ana", "Bruno", "Carla", "Daniel"]
procurado = "Carla"
encontrado = False

for i in estudantes:
    print(i)
    if (i == procurado):
        encontrado = True
        break

if (encontrado == True):
    print(f"{procurado} foi encontrado")
