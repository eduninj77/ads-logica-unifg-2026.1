import os
os.system("clear" if os.name != "nt" else "cls")

presentes_bruto = ["  maria ", "JOÃO", "ana clara", "Bruno  ", "  carla"]
presentes_brutof = []
esta = False
for i in presentes_bruto:
    i_f = i.strip().title()
    presentes_brutof.append(i_f)
consulta = input("Digite o nome do aluno: ").strip().title().replace("ã", "a")

for i in presentes_brutof:
    if consulta in presentes_brutof:
        esta = True
    else:
        esta = False

print(f"LISTA DE ALUNOS: {presentes_brutof}")
if esta:
    print(f"O aluno {consulta} está presente.")
else:
    print(f"O aluno {consulta} não está presente")
