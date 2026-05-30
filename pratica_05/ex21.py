presencas = [
    ["P", "P", "F", "P", "P"],  #estudante 0
    ["P", "F", "F", "P", "P"],  #estudante 1
    ["P", "P", "P", "P", "F"],  #estudante 2
    ["F", "P", "P", "F", "P"]   #estudante 3
]

nomes = ["Ana", "Bruno", "Carla", "Diego"]

total_presencas = 0
total_faltas = 0

print("Presenças e faltas dos estudantes:")
for i in range(len(nomes)):
    presencas_estudante = presencas[i].count("P")
    faltas_estudante = presencas[i].count("F")
    
    total_presencas += presencas_estudante
    total_faltas += faltas_estudante
    
    print(f"{nomes[i]}: Presenças = {presencas_estudante}, Faltas = {faltas_estudante}")

    percentual = (presencas_estudante / len(presencas[i])) * 100
    situacao = "Regular ✓" if percentual >= 75 else "Irregular ✗"
    print(f"Percentual de presença: {percentual:.2f}% - {situacao}")