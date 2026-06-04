grade = [
    [0, 1, 0, 0, 1],
    [0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0]
]

def exibir_grade(matriz):
    print("  " + " ".join(str(j) for j in range(len(matriz[0]))))
    print("  " + "--" * len(matriz[0]))
    for i in range(len(matriz)):
        linha = f"{i}|"
        for celula in matriz[i]:
            linha += " █" if celula == 1 else " ·"
        print(linha)
    print()

def contar_ocupadas(matriz):
    ocupadas = 0
    for linha in matriz:
        for celula in linha:
            if celula == 1:
                ocupadas += 1
    return ocupadas

# 1. Grade inicial
print("=" * 25)
print(f"{'GRADE INICIAL':^25}")
print("=" * 25)
exibir_grade(grade)
print(f"Células ocupadas : {contar_ocupadas(grade)}")
print(f"Células vazias   : {5 * 5 - contar_ocupadas(grade)}")

# 2. Alterações
novas_celulas = [(0, 2), (1, 4), (3, 3)]

print("\n--- Crescimento ---")
for linha, coluna in novas_celulas:
    grade[linha][coluna] = 1
    print(f"✅ Célula [{linha}][{coluna}] ocupada")

# 3 e 4. Grade atualizada
print()
print("=" * 25)
print(f"{'GRADE ATUALIZADA':^25}")
print("=" * 25)
exibir_grade(grade)
print(f"Células ocupadas : {contar_ocupadas(grade)}")
print(f"Células vazias   : {5 * 5 - contar_ocupadas(grade)}")
print(f"Crescimento      : +{len(novas_celulas)} células")