presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

maior_faltas = None
aula_maior = 0

for j in range(len(presencas[0])):
    faltas = 0
    for i in range(len(presencas)):
        if presencas[i][j] == "F":
            faltas += 1

    if maior_faltas is None or faltas > maior_faltas:
        maior_faltas = faltas
        aula_maior = j

print(f"Aula com mais faltas: {aula_maior}")
print(f"Total de faltas: {maior_faltas}")