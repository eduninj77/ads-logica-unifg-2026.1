estudantes = ["Ana", "Bruno", "Carla", "Diego", "Edu"]
notas = [
    [8.0, 7.5, 9.0, 8.5],
    [5.0, 6.0, 5.5, 5.0],
    [4.0, 3.5, 5.0, 4.5],
    [9.0, 8.5, 10.0, 9.5],
    [6.5, 7.0, 6.0, 6.5]
]

maior_media = -1
menor_media = 11

for i in range(len(estudantes)):
    soma = 0
    for j in range(len(notas[i])):
        soma += notas[i][j]
    
    media = soma / len(notas[i])
    
    if media >= 7.0:
        situacao = "aprovado"
    elif media >= 5.0:
        situacao = "recuperação"
    else:
        situacao = "reprovado"
        
    print(f"{estudantes[i]} - Média: {media:.2f} ({situacao})")
    
    if media > maior_media:
        maior_media = media
    if media < menor_media:
        menor_media = media

print(f"\nMaior média da turma: {maior_media:.2f}")
print(f"Menor média da turma: {menor_media:.2f}")