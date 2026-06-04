import os
os.system("clear" if os.name != "nt" else "cls")

estudante = ["Pedro", "Anderson", "Daniel", "Williyan", "Luckyan"]
notas = [    
    [5.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 4.5, 10.0],
    [3.5, 2.0, 6.0],
    [8.4, 4.8, 7.9]]



media = []
for i in notas:
    media.append(sum(i) / 3)

menor_media = min(media)
maior_media = max(media)

menor_mediai = media.index(menor_media)
maior_mediai = media.index(maior_media)

print("-" * 50)
print("Situação".center(50))
print("-" * 50)
for i in range(len(estudante)):
    if media[i] >= 7.0:
        situacao = "Aprovado"
    elif 5.0 <= media[i] < 7.0:
        situacao = "Recuperação"
    elif media[i] < 5.0:
        situacao = "Reprovado"
    print(f"{estudante[i]} - Média: {media[i]:.1f} - Situação: {situacao}")
print("-" * 50)

print(f"Menor média: {estudante[menor_mediai]} - Média: {media[menor_mediai]:.1f}")
print(f"Maior média: {estudante[maior_mediai]} - Média: {media[maior_mediai]:.1f}")