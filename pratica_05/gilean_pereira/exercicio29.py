estudantes = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]
notas = [
    [8.0, 7.5, 9.0, 8.5],
    [5.0, 6.0, 5.5, 6.5],
    [4.0, 3.5, 5.0, 4.5],
    [9.0, 10.0, 9.5, 9.0],
    [7.0, 5.0, 6.5, 7.5]
]

medias = []

for i in range(len(estudantes)):
    media = sum(notas[i]) / len(notas[i])
    medias.append(media)
    
    if media >= 7.0:
        situacao = "Aprovado"
    elif media >= 5.0:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
        
    print(f"Estudante: {estudantes[i]} | Média: {media:.1f} | Situação: {situacao}")

print("-" * 40)

print(f"Maior média da turma: {max(medias):.1f}")
print(f"Menor média da turma: {min(medias):.1f}")