nomes = ["Ana", "Bruno", "Carla", "Diego", "Elena"]

notas = [
    [8.0, 7.5, 9.0, 8.5],
    [5.0, 6.0, 5.5, 4.0],
    [9.0, 8.5, 10.0, 9.5],
    [4.0, 3.5, 5.0, 4.5],
    [6.0, 6.5, 7.0, 5.5]
]

maior_media = None
menor_media = None
nome_maior = ""
nome_menor = ""

print("=" * 45)
print(f"{'BOLETIM ESCOLAR':^45}")
print("=" * 45)

for i in range(len(nomes)):
    soma = 0
    for nota in notas[i]:
        soma += nota
    media = soma / len(notas[i])

    if media >= 7.0:
        situacao = "Aprovado"
    elif media >= 5.0:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    print(f"{nomes[i]:<8} Média: {media:.2f}  Situação: {situacao}")

    if maior_media is None or media > maior_media:
        maior_media = media
        nome_maior = nomes[i]

    if menor_media is None or media < menor_media:
        menor_media = media
        nome_menor = nomes[i]

print("=" * 45)
print(f"Maior média: {nome_maior} - {maior_media:.2f}")
print(f"Menor média: {nome_menor} - {menor_media:.2f}")
print("=" * 45)