# O primeiro índice de uma lista é 1.

# Falso ✗
lista = [10, 20, 30]
print(lista[0])
print(lista[1])

# Em matriz[i][j], i indica a linha j indica a coluna.

# Verdadeiro ✓
matriz = [
    [10, 20, 30],  # i = 0
    [40, 50, 60],  # i = '
    [70, 80, 90]   # i = 2
]

print(matriz[1][2])

# Uma lista de listas sempre possui o mesmo número de elementos em todas as linhas.

#Falso ✗
irregular = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9]
]
print(len(irregular[0]))
print(len(irregular[1]))
print(len(irregular[2]))

# Uma matriz pode representar um boletim escolar.

# Verdadeiro ✓
boletim = [
    ["Ana", 7.0, 8.5, 9.0],
    ["Bruno", 5.5, 6.0, 7.0],
    ["Carla", 9.0, 9.5, 8.0]
]

for aluno in boletim:
    print(f"{aluno[0]}: notas {aluno[1]}, {aluno[2]}, {aluno[3]}")