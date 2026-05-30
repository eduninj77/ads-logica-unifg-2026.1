presencas = [
    ["P", "P", "F", "P", "P"],   # estudante 0
    ["P", "F", "F", "P", "P"],   # estudante 1
    ["P", "P", "P", "P", "F"],   # estudante 2
    ["F", "P", "P", "F", "P"]    # estudante 3
]

for i in range(len(presencas)):
    faltas = 0
    for registro in presencas[i]:
        if registro == "F":
            faltas += 1
    print(f"Estudante {i}: Faltas = {faltas}")