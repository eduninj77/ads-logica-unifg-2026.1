# Lista original
nomes_brutos = ["  ana", "BRUNO  ", "cArLa silva", "  joão pedro  "]

# Lista padronizada
nomes_padronizados = []

for nome in nomes_brutos:
    nome_limpo = nome.strip().title()
    nomes_padronizados.append(nome_limpo)

# Exibindo resultado
print(nomes_padronizados)

# Desafio: total de nomes
print(f"Total de nomes: {len(nomes_padronizados)}")
