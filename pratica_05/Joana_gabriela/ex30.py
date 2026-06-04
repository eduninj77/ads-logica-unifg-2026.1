lab = [
    ["L", "O", "L", "M", "L"],
    ["O", "L", "L", "O", "M"],
    ["L", "M", "O", "L", "L"],
    ["O", "L", "M", "L", "O"]
]

def exibir_mapa(matriz):
    print("\n    ", end="")
    for c in range(len(matriz[0])):
        print(f" C{c} ", end="")
    print()
    print("    " + "----" * len(matriz[0]))
    for i in range(len(matriz)):
        print(f" F{i} |", end="")
        for j in range(len(matriz[i])):
            print(f" {matriz[i][j]}  ", end="")
        print()
    print()

def contar_status(matriz):
    livres = ocupados = manutencao = 0
    for linha in matriz:
        for pc in linha:
            if pc == "L":
                livres += 1
            elif pc == "O":
                ocupados += 1
            elif pc == "M":
                manutencao += 1
    print(f"💻 Livres: {livres}  |  👤 Ocupados: {ocupados}  |  🔧 Manutenção: {manutencao}")

def ocupar_posicao(matriz, fileira, computador):
    if fileira < 0 or fileira >= len(matriz) or computador < 0 or computador >= len(matriz[0]):
        print("❌ Posição fora dos limites do laboratório.")
        return
    status = matriz[fileira][computador]
    if status == "L":
        matriz[fileira][computador] = "O"
        print(f"✅ Computador F{fileira}/C{computador} ocupado com sucesso.")
    elif status == "M":
        print(f"🔧 Computador F{fileira}/C{computador} está em manutenção.")
    else:
        print(f"⚠️  Computador F{fileira}/C{computador} já está ocupado.")

# 1. Exibir mapa inicial
print("=" * 28)
print(f"{'MAPA DO LABORATÓRIO':^28}")
print("=" * 28)
exibir_mapa(lab)

# 2. Contagem de status
contar_status(lab)

# 3/4/5. Realizar ocupações
print("\n--- Tentativas de ocupação ---")

ocupar_posicao(lab, 0, 0)   # livre     → sucesso
ocupar_posicao(lab, 0, 3)   # manutenção → bloqueado
ocupar_posicao(lab, 1, 0)   # ocupado   → bloqueado
ocupar_posicao(lab, 9, 2)   # fora dos limites

# Mapa e contagem atualizados
print("\n--- Estado final ---")
exibir_mapa(lab)
contar_status(lab)