notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

total_avaliacoes = len(notas[0])
total_alunos = len(notas)

menor_media = float('inf')
avaliacao_menor_media = -1

for j in range(total_avaliacoes):
    soma_avaliacao = 0
    
    for i in range(total_alunos):
        soma_avaliacao += notas[i][j]
        
    media_avaliacao = soma_avaliacao / total_alunos
    
    if media_avaliacao < menor_media:
        menor_media = media_avaliacao
        avaliacao_menor_media = j

print(f"Avaliação com menor média: {avaliacao_menor_media}")
print(f"Média: {menor_media:.2f}")