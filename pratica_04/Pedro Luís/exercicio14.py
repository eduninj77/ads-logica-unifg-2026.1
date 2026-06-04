import os
os.system("clear" if os.name != "nt" else "cls")

def centralizar(msg=""):
    tamanho = len(msg) * 9
    print("=" * tamanho)
    print(msg.center(tamanho))
    print("=" * tamanho)

presentes_bruto = ["  maria ", "JOÃO", "ana clara", "Bruno  ", "  carla"]
presentes_brutof = []
for i in presentes_bruto:
    i_f = i.strip().title().replace("ã", "a")
    presentes_brutof.append(i_f)
presentes_brutof.sort()

notas = [4.5, 7.0, 8.0, 5.5, 9.0, 6.8, 7.2]
notas.sort()
reprovados = []
aprovados = []
for i in notas:
    if i >= 7.0:
        aprovados.append(i)
    else:
        reprovados.append(i)

aluno = input("Digite o nome do aluno: ").strip().title()
presente = False
for i in presentes_brutof:
    if aluno in presentes_brutof:
        presente = True
    else:
        presente = False

centralizar("RESUMO")
print(f"NOTAS TOTAIS: ", end="")
for i in notas:
    if i in aprovados:
        print(f"\033[32m{i}\033[m", end="; " if i != aprovados[-1] else "")
    elif i in reprovados:
        print(f"\033[31m{i}\033[m", end="; ")
print("\nALUNOS:", end=" ")
for i in presentes_brutof:
    print(f"{i}", end="; " if i != presentes_brutof[-1] else "")
if presente:
    print(f"\nO aluno \033[32m{aluno}\033[m está presente!")
else:
    print(f"\nO aluno \033[31m{aluno}\033[m não está presente!")
print("=" * 54)