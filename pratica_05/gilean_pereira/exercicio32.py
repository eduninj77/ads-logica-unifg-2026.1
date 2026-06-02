grade_inicial = [
    [1, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1]
]

grade_final = [linha[:] for linha in grade_inicial]


ocupadas_antes = sum(linha.count(1) for linha in grade_inicial)

grade_final[0][1] = 1
grade_final[1][2] = 1
grade_final[2][4] = 1

ocupadas_depois = sum(linha.count(1) for linha in grade_final)

print("--- GRADE ANTES ---")
for linha in grade_inicial:
    print(" ".join(map(str, linha)))
print(f"Células ocupadas: {ocupadas_antes}\n")

print("--- GRADE DEPOIS ---")
for linha in grade_final:
    print(" ".join(map(str, linha)))
print(f"Células ocupadas: {ocupadas_depois}")