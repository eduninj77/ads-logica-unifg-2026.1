presentes_bruto = ["  maria ", "JOÃO", "ana clara", "Bruno  ", "  carla"]
consulta = "joão"

nomes_padronizados = []
for nome in presentes_bruto:
    nomes_padronizados.append(nome.strip().lower())

consulta_padronizada = consulta.lower()

if consulta_padronizada in nomes_padronizados:
    print(f"Lista de presentes: {nomes_padronizados}")
    print(f"{consulta_padronizada.title()} está presente.")
else:
    print(f"Lista de presentes: {nomes_padronizados}")
    print(f"{consulta_padronizada.title()} não está presente.")
