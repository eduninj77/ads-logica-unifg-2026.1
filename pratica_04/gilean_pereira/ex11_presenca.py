presentes_bruto = ["  maria ", "JOÃO", "ana clara", "Bruno  ", "  carla"]
consulta = "joão".strip().title()
presentes_padronizados =[]
encontrado = False

for i in presentes_bruto:
    nomes_limpos = i.strip().title()

    presentes_padronizados.append(nomes_limpos)

for i in presentes_padronizados:
    if (i == consulta):
        encontrado = True
        break

print(presentes_padronizados)

if (encontrado == True):
    print(f"{consulta} está presente")
else:
    print(f"{consulta} está ausência")

