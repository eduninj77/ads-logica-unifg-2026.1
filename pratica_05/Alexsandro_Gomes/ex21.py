presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

total_presencas = 0
total_faltas = 0

for i in range(len(presencas)):
    for j in range(len(presencas[i])):
        if presencas[i][j] == "P":
            total_presencas += 1
        elif presencas[i][j] == "F":
            total_faltas += 1


print(f"Total de presenças: {total_presencas}")
print(f"Total de faltas: {total_faltas}")