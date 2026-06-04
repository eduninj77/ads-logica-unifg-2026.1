presencas = [
    ["P", "P", "F", "P", "P"], 
    ["P", "F", "F", "P", "P"], 
    ["P", "P", "P", "P", "F"], 
    ["F", "P", "P", "F", "P"]  
]

for i in range(len(presencas)):
    faltas_estudante = 0
    
    
    for j in range(len(presencas[i])):
        if presencas[i][j] == "F":
            faltas_estudante += 1
            
    print(f"Estudante {i} - Faltas: {faltas_estudante}")