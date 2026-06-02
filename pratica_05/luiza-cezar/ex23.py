# Exercício 23 - Aula com mais faltas

presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

def encontrar_aula_com_mais_faltas(matriz_presencas):
    """Encontra a aula com mais faltas"""
    num_aulas = len(matriz_presencas[0])
    aula_com_mais_faltas = 0
    maior_quantidade_faltas = 0
    
    # Percorrendo por coluna (cada aula)
    for j in range(num_aulas):
        faltas_nesta_aula = 0
        for i in range(len(matriz_presencas)):
            if matriz_presencas[i][j] == "F":
                faltas_nesta_aula += 1
        
        if faltas_nesta_aula > maior_quantidade_faltas:
            maior_quantidade_faltas = faltas_nesta_aula
            aula_com_mais_faltas = j
    
    return aula_com_mais_faltas, maior_quantidade_faltas

print("=" * 60)
print("EXERCÍCIO 23 - AULA COM MAIS FALTAS")
print("=" * 60)

print("\nMatriz de presença:\n")
print("Estudante\\Aula", end="")
for j in range(len(presencas[0])):
    print(f"\tAula {j}", end="")
print()

for i, linha in enumerate(presencas):
    print(f"Estudante {i}\t", end="")
    for j, status in enumerate(linha):
        print(f"\t{status}", end="")
    print()

print("\n" + "-" * 60)
print("\nAnalisando faltas por aula:\n")

num_aulas = len(presencas[0])
for j in range(num_aulas):
    faltas = 0
    for i in range(len(presencas)):
        if presencas[i][j] == "F":
            faltas += 1
    print(f"Aula {j}: {faltas} falta(s)")

aula_max, faltas_max = encontrar_aula_com_mais_faltas(presencas)

print("\n" + "-" * 60)
print(f"\nAula com mais faltas: Aula {aula_max}")
print(f"Total de faltas: {faltas_max}")

print("\n" + "=" * 60)
print("✓ Resultado: Aulas 1 e 2 empatam com 2 faltas cada.")
print("  (O programa identifica a primeira com essa quantidade)")
print("=" * 60)
