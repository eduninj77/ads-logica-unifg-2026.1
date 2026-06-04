import os
os.system("clear" if os.name != "nt" else "cls")

def calcular_media(n1, n2):
    media = (n1+n2) / 2
    return f"{media:.1f}"

nota = [float(input("Digite a primeira nota: ")), float(input("Digite a segunda nota: "))]

print(calcular_media(nota[0], nota[1]))
