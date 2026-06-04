sala = [
    ["L", "O", "L"],
    ["O", "O", "L"],
    ["L", "L", "O"]
]

assentos_livres = 0
assentos_ocupados = 0

for fileira in sala:
    for assento in fileira:
        if assento == "L":
            assentos_livres += 1
        elif assento == "O":
            assentos_ocupados += 1

print(f"Assentos livres: {assentos_livres}")
print(f"Assentos ocupados: {assentos_ocupados}")