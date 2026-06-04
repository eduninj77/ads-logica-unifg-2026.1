nomes = ["Ana", "Bruno", "Carla", "Diego"]
notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

print("Estudantes em recuperação: ")

for i in range(len(nomes)):
    soma_notas = sum(notas[i])
    quantidade_notas = len(notas[i])
    media = soma_notas / quantidade_notas
    
    if media < 7.0:
        print(f"{nomes[i]} - Média: {media:.2f}")