nomes = ["Ana", "Bruno", "Carla", "Diego"]

notas = [
    [8.0, 7.5,  9.0],
    [5.0, 6.0,  5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0,  6.0]
]

num_avaliacoes = len(notas[0])
num_alunos = len(nomes)

for j in range(num_avaliacoes):
    soma = 0
    for i in range(num_alunos):
        soma += notas[i][j]
    media = soma / num_alunos
    print(f"A média da avaliação {j} é: {media:.2f}")