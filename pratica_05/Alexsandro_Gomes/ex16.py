notas = [
    [8.0, 7.5, 9.0],  # Aluno 0
    [5.0, 6.0, 5.5],  # Aluno 1
    [9.0, 8.5, 10.0], # Aluno 2
    [6.5, 7.0, 6.0]   # Aluno 3
]

total_avaliacoes = len(notas[0]) 
total_alunos = len(notas)

for j in range(total_avaliacoes):
    soma_avaliacao = 0
    
    for i in range(total_alunos):
        soma_avaliacao += notas[i][j]

 
    media_avaliacao = soma_avaliacao / total_alunos
    print(f"Avaliação {j} - Média: {media_avaliacao:.2f}")