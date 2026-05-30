presencas = [
    ["P", "P", "F", "P", "P"],   # estudante 0
    ["P", "F", "F", "P", "P"],   # estudante 1
    ["P", "P", "P", "P", "F"],   # estudante 2
    ["F", "P", "P", "F", "P"]    # estudante 3
]

num_aulas   = len(presencas[0])
num_alunos  = len(presencas)      

maior_faltas  = None
aula_problema = 0

for j in range(num_aulas):
    faltas = 0
    for i in range(num_alunos):
        if presencas[i][j] == "F":
            faltas += 1

    print(f"Aula {j} - Faltas: {faltas}")

    if maior_faltas is None or faltas > maior_faltas:
        maior_faltas  = faltas
        aula_problema = j

print()
print(f"Aula com mais faltas: {aula_problema}")
print(f"Total de faltas: {maior_faltas}")