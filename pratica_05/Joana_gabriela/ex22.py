presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

for i in range(len(presencas)):
    faltas = 0
    for registro in presencas[i]:
        if registro == "F":
            faltas += 1
    print(f"Estudante {i} - Faltas: {faltas}")