presentes_bruto = ["  maria ", "JOÃO", "ana clara", "Bruno  ", "  carla"]
consulta = "joão"

presentes = []
for nome in presentes_bruto:
    presentes.append(nome.strip().title())

consulta = consulta.strip().title()

if consulta in presentes:
    print(f"{consulta} está presente.")
else:
    print(f"{consulta} não está presente.")

print(presentes)