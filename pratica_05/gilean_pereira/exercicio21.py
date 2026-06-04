presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

total_presencas = 0
total_faltas = 0

for linha in presencas:
    total_presencas += linha.count("P")
    total_faltas += linha.count("F")

print(f"Total de presenças: {total_presencas}")
print(f"Total de faltas: {total_faltas}")