laboratorio = [
    ["L", "O", "M", "L", "O"],
    ["O", "O", "L", "L", "L"],
    ["M", "L", "O", "O", "L"],
    ["L", "L", "L", "M", "O"]
]

print("---Mapa Inicial do Laboratório---")
for linha in laboratorio:
    print(" ".join(linha))

livres = 0
ocupados = 0
manutencao = 0

for i in range(len(laboratorio)):
    for j in range(len(laboratorio[i])):
        if laboratorio[i][j] == "L":
            livres += 1
        elif laboratorio[i][j] == "O":
            ocupados += 1
        elif laboratorio[i][j] == "M":
            manutencao += 1

print("\n---Contagem Atual---")
print(f"Computadores livres: {livres}")
print(f"Computadores ocupados: {ocupados}")
print(f"Computadores em manutenção: {manutencao}")

print("\n---Reservar Computador---")
linha_alvo = int(input("Digite a fileira (0 a 3): "))
coluna_alvo = int(input("Digite o computador (0 a 4): "))

if linha_alvo < 0 or linha_alvo >= 4 or coluna_alvo < 0 or coluna_alvo >= 5:
    print("Erro: Posição fora dos limites do laboratório!")
else:
    status = laboratorio[linha_alvo][coluna_alvo]
    
    if status == "L":
        laboratorio[linha_alvo][coluna_alvo] = "O"
        print("Sucesso: Computador ocupado com sucesso!")
    elif status == "M":
        print("Erro: Não é possível ocupar um computador em manutenção!")
    elif status == "O":
        print("Erro: Este computador já está ocupado!")

print("\n--- Mapa Atualizado ---")
for linha in laboratorio:
    print(" ".join(linha))