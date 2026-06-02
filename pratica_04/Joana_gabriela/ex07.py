estudantes = ["Ana", "Bruno", "Carla", "Daniel"]
procurado = "Carla"

encontrado = False

for aluno in estudantes:
    if aluno == procurado:
        encontrado = True
        break

if encontrado:
    print(f"{procurado} está na lista.")
else:
    print(f"{procurado} não está na lista.")

#Desafio: trocando por "Lucas" → não está na lista.