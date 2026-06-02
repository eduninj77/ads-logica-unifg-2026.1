nomes_brutos = ["  ana", "BRUNO  ", "cArLa silva", "  joão pedro  "]
notas_brutas = [4.5, 8.0, 6.8, 9.5]
consulta     = "carla silva"

#Etapa 1  padronizar nomes
nomes = [n.strip().title() for n in nomes_brutos]

#Etapa 2 — filtrar aprovados (nota >= 7)
aprovados = []
for nota in notas_brutas:
    if nota >= 7.0:
        aprovados.append(nota)

#Etapa 3  verificar presença
consulta = consulta.strip().title()
presente = consulta in nomes

#Etapa 4 — relatório final
print("=== RELATÓRIO ===")
print(f"Alunos:    {nomes}")
print(f"Aprovados: {aprovados} ({len(aprovados)} notas)")
print(f"Presença de {consulta}: {'sim' if presente else 'não'}")