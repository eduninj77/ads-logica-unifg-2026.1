presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

maior_faltas = -1
aula_maior = 0

for j in range(len(presencas[0])):
    faltas = sum(1 for i in range(len(presencas)) if presencas[i][j] == "F")
    if faltas > maior_faltas:
        maior_faltas = faltas
        aula_maior = j

print("Aula com mais faltas:", aula_maior)
print("Faltas:", maior_faltas)
