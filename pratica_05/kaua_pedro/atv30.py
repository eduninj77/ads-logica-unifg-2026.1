lab = [
    ["L", "O", "L", "M", "L"],
    ["O", "L", "L", "O", "L"],
    ["M", "L", "O", "L", "L"],
    ["L", "L", "M", "O", "L"]
]

for linha in lab:
    print(linha)

livres = sum(linha.count("L") for linha in lab)
ocupados = sum(linha.count("O") for linha in lab)
manutencao = sum(linha.count("M") for linha in lab)

print(f"\nLivres: {livres} | Ocupados: {ocupados} | Manutenção: {manutencao}")

linha = int(input("\nLinha para ocupar: "))
coluna = int(input("Coluna para ocupar: "))

if linha < 0 or linha >= len(lab) or coluna < 0 or coluna >= len(lab[0]):
    print("Posição fora dos limites.")
elif lab[linha][coluna] == "L":
    lab[linha][coluna] = "O"
    print("Computador ocupado com sucesso.")
elif lab[linha][coluna] == "M":
    print("Computador em manutenção. Não é possível ocupar.")
else:
    print("Computador já está ocupado.")

print()
for l in lab:
    print(l)
