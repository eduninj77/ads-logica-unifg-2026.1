laboratorio = [
    ["L", "O", "L", "M", "L"],
    ["O", "O", "L", "L", "L"],
    ["L", "M", "O", "L", "M"],
    ["L", "L", "L", "O", "L"]
]

print("--- MAPA DO LABORATÓRIO ---")
for fileira in laboratorio:
    print(" ".join(fileira))
print("-" * 27)

livres = sum(linha.count("L") for linha in laboratorio)
ocupados = sum(linha.count("O") for linha in laboratorio)
manutencao = sum(linha.count("M") for linha in laboratorio)

print(f"Livres: {livres} | Ocupados: {ocupados} | Manutenção: {manutencao}\n")

print("Deseja ocupar qual computador?")
f = int(input("Digite a fileira (1 a 4): ")) - 1
c = int(input("Digite o computador (1 a 5): ")) - 1

if not (0 <= f < 4 and 0 <= c < 5):
    print("Erro: Posição inválida! Fora dos limites do laboratório.")
else:
    if laboratorio[f][c] == "L":
        laboratorio[f][c] = "O"
        print("Sucesso: Computador ocupado com sucesso!")
    elif laboratorio[f][c] == "M":
        print("Erro: Não é possível ocupar. Computador em manutenção.")
    else:
        print("Aviso: Este computador já está ocupado.")