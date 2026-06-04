import os
os.system("clear" if os.name != "nt" else "cls")

presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]
falta = 0
faltas = []

for i in presencas:
    falta = 0
    for v in i:
        if v == "F":
            falta += 1
    faltas.append(falta)

for i in range(len(presencas)):
    print(f"Estudante {i} - Faltas {faltas[i]}")