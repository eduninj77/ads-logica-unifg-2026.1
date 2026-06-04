presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

for i in range(len(presencas)):

    linha_estudante = presencas[i]
    
    total_faltas = linha_estudante.count("F")
    
    print(f"Estudante {i} - Faltas: {total_faltas}")