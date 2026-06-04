estudantes = ["Ana", "Bruno", "Carla", "Daniel"]
procurado = "Carla"

encontrado = False
for aluno in estudantes:
    if aluno == procurado:
        encontrado = True
        break

if encontrado:
    print(f"{procurado} foi encontrado na lista.")
else:
    print(f"{procurado} não foi encontrado na lista.")
