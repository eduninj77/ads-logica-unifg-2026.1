sala = [
    ["L", "O", "L"],
    ["O", "O", "L"],
    ["L", "L", "O"]
]

linha = 2
coluna = 1

# Mapa ANTES
print("----------sala ANTES----------")
for i, fileira in enumerate(sala):
    print(f" L{i} ", end="")
    for cadeira in fileira:
        simbolo = "[]" if cadeira == "L" else "[X]"
        print(f"{simbolo}", end="")
    print()  

print()

if sala[linha][coluna] == "L":
    sala[linha][coluna] = "O"
    print(f"Cadeira na linha {linha} e coluna {coluna} ocupada com sucesso!")

# Mapa DEPOIS
print("----------sala DEPOIS----------")
for i, fileira in enumerate(sala):
    print(f" L{i} ", end="")
    for cadeira in fileira:
        simbolo = "[]" if cadeira == "L" else "[X]"
        print(f"{simbolo}", end="")
    print()  
