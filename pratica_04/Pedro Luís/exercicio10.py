import os
os.system("clear" if os.name != "nt" else "cls")

notas = [4.5, 7.0, 8.0, 5.5, 9.0, 6.8, 7.2]
aprovados = []

for i in notas:
    if i >= 7.0:
        aprovados.append(i)

print(aprovados)