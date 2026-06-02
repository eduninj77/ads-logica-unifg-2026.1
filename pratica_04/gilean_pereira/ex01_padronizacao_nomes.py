nomes_brutos = ["  ana", "BRUNO  ", "cArLa silva", "  joão pedro  "]
nomes_padronizados = []

for nome in nomes_brutos:
    nomes_limpos = nome.strip().title()

    nomes_padronizados.append(nomes_limpos)

print(nomes_padronizados)
