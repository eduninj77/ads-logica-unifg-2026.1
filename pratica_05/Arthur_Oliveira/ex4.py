notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

numero_aluno = int(input("Qual aluno deseja ver as notas? (1 a 4): "))

print(f"Notas do aluno {numero_aluno}:")
for i in range(len(notas[numero_aluno - 1])):
    print(f"  Nota {i + 1}: {notas[numero_aluno - 1][i]}")