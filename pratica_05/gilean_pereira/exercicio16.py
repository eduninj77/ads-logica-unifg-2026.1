notas = [
    [8.0, 7.5, 9.0], 
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]   
]


total_alunos = len(notas)
total_avaliacoes = len(notas[0]) 


for j in range(total_avaliacoes):
    soma_prova = 0.0
    

    for i in range(total_alunos):
        soma_prova += notas[i][j] 
        
    media_prova = soma_prova / total_alunos
    
    print(f"Avaliação {j} - Média: {media_prova:.2f}")