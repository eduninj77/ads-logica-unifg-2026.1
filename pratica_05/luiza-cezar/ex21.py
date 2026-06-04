# Exercício 21 - Controle de presença

presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

def contar_presencas_e_faltas(matriz_presencas):
    """Conta o total de presenças e faltas"""
    total_presencas = 0
    total_faltas = 0
    
    for linha in matriz_presencas:
        for status in linha:
            if status == "P":
                total_presencas += 1
            elif status == "F":
                total_faltas += 1
    
    return total_presencas, total_faltas

print("=" * 60)
print("EXERCÍCIO 21 - CONTROLE DE PRESENÇA")
print("=" * 60)

print("\nMatriz de presença (P=Presente, F=Falta):\n")
print("Estudante\\Aula", end="")
for j in range(len(presencas[0])):
    print(f"\t{j}", end="")
print()

for i, linha in enumerate(presencas):
    print(f"Estudante {i}\t", end="")
    for j, status in enumerate(linha):
        print(f"\t{status}", end="")
    print()

print("\n" + "-" * 60)

total_p, total_f = contar_presencas_e_faltas(presencas)
total = total_p + total_f

print(f"\nTotal de presenças: {total_p}")
print(f"Total de faltas: {total_f}")
print(f"Total de registros: {total}")

print("\n" + "=" * 60)
print("✓ Análise:")
print("  • 4 estudantes")
print("  • 5 aulas monitoradas")
print("  • Total de registros: 20")
print(f"  • Presenças: {total_p}")
print(f"  • Faltas: {total_f}")
print("=" * 60)
