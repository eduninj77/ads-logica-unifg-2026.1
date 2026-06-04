import os
os.system("clear" if os.name != "nt" else "cls")

valores = [
    [3, 5, 7],
    [2, 4, 6],
    [1, 8, 9]
]

pares = 0

for i in valores:
    for v in i:
        if v % 2 == 0:
            pares += 1

print(pares)