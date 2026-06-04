nomes = ["Ana", "Bruno", "Carla", "Diego"]
notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

maior_media = 0.0
aluno_maior_media = ""

for i in range (len(nomes)):
    soma_nota = sum(notas[i])
    quantidade_notas = len(notas[i])
    media = soma_nota / quantidade_notas
    if media > maior_media:
        maior_media = media 
        aluno_maior_media = nomes[i]

print(f"Maior média: {aluno_maior_media} - {maior_media:.2f}")