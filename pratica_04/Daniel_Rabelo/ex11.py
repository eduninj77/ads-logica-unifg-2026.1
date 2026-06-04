presentes_bruto = ["  maria ", "JOÃO", "ana clara", "Bruno  ", "  carla"]
consulta = "joão"

presentes = []
for nome in presentes_bruto:
    presentes.append(nome.strip().title())

consulta_padronizada = consulta.strip().title()

encontrado = False
for nome in presentes:
    if nome == consulta_padronizada:
        encontrado = True
        break

print("─── Lista de presentes ───")
for i, nome in enumerate(presentes, start=1):
    print(f"  {i}. {nome}")

print()
if encontrado:
    print(f'✓ "{consulta_padronizada}" está presente.')
else:
    print(f'✗ "{consulta_padronizada}" não está presente.')

# ---- Desafio: testando com nome ausente ----
print()
consulta2 = "  FERNANDA  "
consulta2_padronizada = consulta2.strip().title()

encontrado2 = False
for nome in presentes:
    if nome == consulta2_padronizada:
        encontrado2 = True
        break

if encontrado2:
    print(f'✓ "{consulta2_padronizada}" está presente.')
else:
    print(f'✗ "{consulta2_padronizada}" não está presente.')