grade = [
    [1, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

print("---Grade Antes---")
for linha in grade:
    print(linha)

ocupadas_antes = 0
for i in range(5):
    for j in range(5):
        if grade[i][j] == 1:
            ocupadas_antes += 1
print(f"Células ocupadas inicialmente: {ocupadas_antes}")

grade[0][1] = 1
grade[1][2] = 1
grade[4][4] = 1

print("\n---Grade Depois---")
for linha in grade:
    print(linha)

ocupadas_depois = 0
for i in range(5):
    for j in range(5):
        if grade[i][j] == 1:
            ocupadas_depois += 1
print(f"Células ocupadas após alteração: {ocupadas_depois}")