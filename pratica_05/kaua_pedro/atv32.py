grade = [
    [0, 1, 0, 0, 1],
    [0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0]
]

print("Grade antes:")
for linha in grade:
    print(linha)

ocupadas = sum(v for linha in grade for v in linha)
print(f"\nCélulas ocupadas antes: {ocupadas}")

grade[0][0] = 1
grade[1][1] = 1
grade[3][3] = 1

ocupadas = sum(v for linha in grade for v in linha)
print(f"Células ocupadas depois: {ocupadas}")

print("\nGrade depois:")
for linha in grade:
    print(linha)
