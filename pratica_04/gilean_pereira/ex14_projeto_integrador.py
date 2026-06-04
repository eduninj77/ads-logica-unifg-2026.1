nomes_brutos = ["  ana", "BRUNO  ", "cArLa silva", "  joão pedro  "]
nomes_padronizados = []
consulta = "bruno".strip().title()
encontrado = False
notas = [4.5, 7.0, 8.0, 5.5,]
aprovados = []

for i in nomes_brutos:
    nomes_limpos = i.strip().title()

    nomes_padronizados.append(nomes_limpos)

for i in notas:
    if (i >=7):
        aprovados.append(i)

for i in nomes_padronizados:
    if (i == consulta):
        encontrado = True
        break

for i in range(len(nomes_padronizados)):
    print("====relatorio====")
    print(f"Aluno :{nomes_padronizados[i]}")
    print(f"{notas[i]}")
    if notas[i] >= 7.0:
        print("Situação: APROVADO")
    else:
        print("Situação: REPROVADO")


if (encontrado == True):
    print("="*18)
    print(f"{consulta} está presente")
else:
    print(f"{consulta} está ausência")

