presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

total_aulas = len(presencas[0])
total_estudantes = len(presencas)

mais_faltas = -1
aula_com_mais_faltas = -1

for j in range(total_aulas):
    faltas_da_aula = 0
    for i in range(total_estudantes):
        if presencas[i][j] == "F":
            faltas_da_aula += 1
            
    if faltas_da_aula > mais_faltas:
        mais_faltas = faltas_da_aula
        aula_com_mais_faltas = j

print(f"Aula com mais faltas: {aula_com_mais_faltas}")
print(f"Total de faltas nessa aula: {mais_faltas}")