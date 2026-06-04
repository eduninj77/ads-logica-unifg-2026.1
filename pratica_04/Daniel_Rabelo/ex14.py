# ═══════════════════════════════════════════
#   SISTEMA DE GERENCIAMENTO DE TURMA
# ═══════════════════════════════════════════

# ─── DADOS BRUTOS ───────────────────────────
nomes_brutos = ["  maria ", "JOÃO", "ana clara", "Bruno  ", "  carla"]
notas_brutas = [4.5, 7.0, 8.0, 5.5, 9.0, 6.8, 7.2]
consulta     = "ana clara"


# ════════════════════════════════════════════
# ETAPA 1 — Padronização dos nomes
# Remove espaços e aplica inicial maiúscula
# ════════════════════════════════════════════
nomes_padronizados = []
for nome in nomes_brutos:
    nomes_padronizados.append(nome.strip().title())


# ════════════════════════════════════════════
# ETAPA 2 — Filtragem das notas aprovadas
# Apenas notas >= 7.0 entram na nova lista
# ════════════════════════════════════════════
notas_aprovadas = []
for nota in notas_brutas:
    if nota >= 7.0:
        notas_aprovadas.append(nota)


# ════════════════════════════════════════════
# ETAPA 3 — Verificação de presença
# Padroniza a consulta antes de comparar
# ════════════════════════════════════════════
consulta_padronizada = consulta.strip().title()
presente = False
for nome in nomes_padronizados:
    if nome == consulta_padronizada:
        presente = True
        break


# ════════════════════════════════════════════
# ETAPA 4 — Cálculo da média das aprovadas
# ════════════════════════════════════════════
soma = 0
for nota in notas_aprovadas:
    soma += nota

if len(notas_aprovadas) > 0:
    media_aprovados = soma / len(notas_aprovadas)
else:
    media_aprovados = 0


# ════════════════════════════════════════════
# ETAPA 5 — Relatório final
# ════════════════════════════════════════════
print("╔══════════════════════════════════════╗")
print("║     RELATÓRIO FINAL DA TURMA         ║")
print("╠══════════════════════════════════════╣")

print("║                                      ║")
print("║  ESTUDANTES PRESENTES                ║")
for i, nome in enumerate(nomes_padronizados, start=1):
    linha = f"║    {i}. {nome}"
    print(linha)

print("║                                      ║")
print("╠══════════════════════════════════════╣")
print("║                                      ║")
print("║  NOTAS REGISTRADAS                   ║")
print(f"║    Todas  : {notas_brutas}")
print(f"║    Aprovadas (>= 7.0): {notas_aprovadas}")
print(f"║    Média dos aprovados: {media_aprovados:.1f}")
print("║                                      ║")
print("╠══════════════════════════════════════╣")
print("║                                      ║")
print("║  CONSULTA DE PRESENÇA                ║")

if presente:
    print(f'║    ✓ "{consulta_padronizada}" está presente.')
else:
    print(f'║    ✗ "{consulta_padronizada}" não encontrado.')

print("║                                      ║")
print("╠══════════════════════════════════════╣")
print("║                                      ║")
print(f"║  Total de estudantes : {len(nomes_padronizados)}")
print(f"║  Total de notas      : {len(notas_brutas)}")
print(f"║  Aprovados           : {len(notas_aprovadas)}")
print(f"║  Reprovados          : {len(notas_brutas) - len(notas_aprovadas)}")
print("║                                      ║")
print("╚══════════════════════════════════════╝")