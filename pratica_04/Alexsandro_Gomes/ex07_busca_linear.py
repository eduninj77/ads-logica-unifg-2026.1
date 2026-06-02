estudantes = ["Ana", "Bruno", "Carla", "Daniel"]
procurado = "Carla"
encontrado = False

for estudante in estudantes:
    if estudante == procurado:
        encontrado = True
        break

if encontrado == True:
    print(f"O estudante {procurado} foi encontrado")
else:
    print(f"O estudante {procurado} não foi encontrado")