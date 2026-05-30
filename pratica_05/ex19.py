sala = [
    ["L", "O", "L"],
    ["O", "O", "L"],
    ["L", "L", "O"]
]

livres = 0
ocupados = 0

for linha in sala:
    for cadeira in linha:
        if cadeira == "L":
            livres += 1
        elif cadeira == "O":
            ocupados += 1

print(f"Quantidade de cadeiras livres: {livres}")
print(f"Quantidade de cadeiras ocupadas: {ocupados}")
print(f"Total de cadeiras: {livres + ocupados}")
