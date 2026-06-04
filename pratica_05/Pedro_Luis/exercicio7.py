import os
os.system("clear" if os.name != "nt" else "cls")

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in matriz:
    for c in i:
        print(f"Valor: {c}")