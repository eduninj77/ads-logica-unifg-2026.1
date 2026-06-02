notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

total_alunos = len(notas)
total_avaliacoes = len(notas[0])

menor_media = 11.0  
avaliacao_menor = -1

for j in range(total_avaliacoes):
    soma_prova = 0.0

    for i in range(total_alunos):
        soma_prova += notas[i][j]
        
    media_prova = soma_prova / total_alunos
    
    if media_prova < menor_media:
        menor_media = media_prova     
        avaliacao_menor = j       

print(f"Avaliação com menor média: {avaliacao_menor}")
print(f"Média: {menor_media:.2f}")