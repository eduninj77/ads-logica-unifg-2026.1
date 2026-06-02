nomes = ["Ana", "Bruno", "Carla", "Diego"]

notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]


for i in range(len(nomes)):
    

    notas_do_aluno = notas[i]
    media = sum(notas_do_aluno) / len(notas_do_aluno)
    
    if media >= 7.0:
        situacao = "Aprovado"
    else:
        situacao = "Recuperação"
        
    print(f"{nomes[i]} - Média: {media:.2f} - {situacao}")