import os
os.system("clear" if os.name != "nt" else "cls")

nomes_brutos = ["  ana", "BRUNO  ", "cArLa silva", "  joão pedro  "]
nomes_brutosf = []

for i in nomes_brutos:
    i_f = i.strip().title()
    nomes_brutosf.append(i_f)

print(nomes_brutosf)
print(f"{len(nomes_brutosf)} foram exibidos.")