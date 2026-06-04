presentes_bruto = ["  maria ", "JOÃO", "ana clara", "Bruno  ", "  carla"]
consulta = "joão"

presentes = []

for nome in presentes_bruto:
    nome_presente = nome.strip().lower()
    presentes.append(nome_presente)

consulta = consulta.strip().lower()
encontrado = False

for pessoa in presentes:
    if pessoa == consulta:
        encontrado = True
        break

if encontrado == True:
    print(f"O estudante {consulta} está presente")
else:
    print(f"O estudante {consulta} está ausente")