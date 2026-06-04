import os
os.system("clear" if os.name != "nt" else "cls")

presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

aula_faltas = [0, 0, 0, 0, 0]

for i in range(len(presencas)):
    for c in range(len(presencas[i])):
        v = presencas[i][c]
        if v == "F":
            aula_faltas[c] +=1

print(f"A aula que possui mais faltas, é a aula {max(aula_faltas)}")