import os
os.system("clear" if os.name != "nt" else "cls")

notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

print(notas[0][0])
print(notas[1][2])
print(notas[2][1])
print(notas[-1][-1])
print(notas[3])