# Exercício 32 - Simulação de crescimento em grade

def exibir_grade(matriz_grade, titulo=""):
    """Exibe a grade de forma visual"""
    if titulo:
        print(f"\n{titulo}")
    print()
    for i, linha in enumerate(matriz_grade):
        for j, celula in enumerate(linha):
            if celula == 0:
                print("[ ]", end=" ")
            else:
                print("[X]", end=" ")
        print()

def contar_ocupadas(matriz_grade):
    """Conta quantas células estão ocupadas"""
    count = 0
    for linha in matriz_grade:
        for celula in linha:
            if celula == 1:
                count += 1
    return count

# Criando grade inicial 5x5
grade = [
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 1, 0, 1, 0]
]

print("=" * 70)
print("EXERCÍCIO 32 - SIMULAÇÃO DE CRESCIMENTO EM GRADE")
print("=" * 70)

print("\n--- ESTADO INICIAL ---")

exibir_grade(grade, "Grade inicial (5x5):")
ocupadas_inicial = contar_ocupadas(grade)
print(f"\nCélulas ocupadas: {ocupadas_inicial}")

print("\n" + "-" * 70)

print("\n--- ALTERAÇÕES REALIZADAS ---\n")

# Alteração 1
print("1. Alterando célula [0][0] de 0 para 1")
grade[0][0] = 1
print(f"   Antes: 0 | Depois: {grade[0][0]}")

# Alteração 2
print("\n2. Alterando célula [2][2] de 0 para 1")
grade[2][2] = 1
print(f"   Antes: 0 | Depois: {grade[2][2]}")

# Alteração 3
print("\n3. Alterando célula [4][4] de 0 para 1")
grade[4][4] = 1
print(f"   Antes: 0 | Depois: {grade[4][4]}")

print("\n" + "-" * 70)

print("\n--- ESTADO FINAL ---")

exibir_grade(grade, "Grade final (após alterações):")
ocupadas_final = contar_ocupadas(grade)
print(f"\nCélulas ocupadas: {ocupadas_final}")

print("\n" + "-" * 70)

print("\n--- RESUMO DA SIMULAÇÃO ---\n")

print(f"Células ocupadas inicialmente: {ocupadas_inicial}")
print(f"Células alteradas: 3")
print(f"Células ocupadas finalmente: {ocupadas_final}")
print(f"Crescimento: {ocupadas_final - ocupadas_inicial} células")

print("\n" + "=" * 70)
print("✓ Simulação de crescimento concluída!")
print("=" * 70)
