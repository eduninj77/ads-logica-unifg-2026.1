nomes = ["Ana", "Bruno", "Carla", "Diego"]

notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

maior_media = -1.0  
melhor_estudante = ""

for i in range(len(nomes)):
    

    sublista_notas = notas[i]
    media_atual = sum(sublista_notas) / len(sublista_notas)
    

    if media_atual > maior_media:
        maior_media = media_atual   
        melhor_estudante = nomes[i] 

print(f"Maior média: {melhor_estudante} - {maior_media:.2f}")