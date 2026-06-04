sala = [
    ["L", "O", "L"],
    ["O", "O", "L"],
    ["L", "L", "O"]
]

assentos_livres = 0
assentos_ocupados = 0

for i in range(len(sala)):
    for j in range(len(sala[i])):
        if sala[i][j] == "L":
            assentos_livres += 1
        elif sala[i][j] == "O":
            assentos_ocupados += 1

print(f"Assentos livres: {assentos_livres}")
print(f"Assentos ocupados: {assentos_ocupados}")