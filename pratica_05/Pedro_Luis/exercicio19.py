import os
os.system("clear" if os.name != "nt" else "cls")

sala = [
    ["L", "O", "L"],
    ["O", "O", "L"],
    ["L", "L", "O"]
]

livres = 0
ocupados = 0

for i in sala:
    for c in i:
        if c == "L":
            livres += 1
        else:
            ocupados += 1

print(f"{livres} assentos estão livres.")
print(f"{ocupados} assentos estão ocupados.")