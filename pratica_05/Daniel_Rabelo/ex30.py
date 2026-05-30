# ===============================================
#          SISTEMA DE OCUPAÇÂO DE LABORATÒRIO
# ===============================================

laboratorio = [
    ["L", "O", "L", "M", "L"], # fileira 0  
    ["O", "O", "L", "L", "O"], # fileira 1  
    ["M", "L", "O", "L", "L"], # fileira 2  
    ["L", "L", "M", "O", "L"], # fileira 3
]

def exibir_mapa(lab):
    print("\n        C0    C1    C2    C3    C4")
    print("   __________________________________")
    print("  |       |        |        |        |  ")
    for i, fileira in enumerate(lab):
        print(f"F {i}", end="")
        for computador in fileira:
            if computador == "L":
                simbolo = "🟩"
            elif computador == "O":
                simbolo = "[XXX]"
            else:
                simbolo = "🟥"
            print(f" {simbolo} ", end="")

        print()
        if i < len(lab) - 1:
            print("  |_______|________|________|________|  ")
    print("  |       |        |        |        |  ")
print()
print("  [ 🟩 ] Livre ")
print("  [ 🟥 ] Ocupado ")
print("  [ XXX ] Manutenção ")

# Contar computadores
def contar_computadores(lab):
    livres = 0
    ocupados = 0
    manutencao = 0
    for fileira in lab:
        for pc in fileira:
            if pc == "L":
                livres += 1
            elif pc == "O":
                ocupados += 1
            elif pc == "M":
                manutencao += 1
    print(f"\n------- Situação do Laboratório -------")
    print(f"Computadores livres: {livres}")
    print(f"Computadores ocupados: {ocupados}")
    print(f"Computadores em manutenção: {manutencao}")
    print(f"Total de computadores: {livres + ocupados + manutencao}")

#----- Ocupar posição --------------------------------
def ocupar_posicao(lab):
    print("\n---------- Reservar Computador ----------")
    try:
        fileira = int(input("Fileira (0-3): "))
        coluna = int(input(" Coluna  (0-4): "))
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números.")
        return
    if fileira < 0 or fileira >= len(lab) or coluna < 0 or coluna >= len(lab[0]):
        print("Posição inválida. Por favor, escolha uma posição dentro do mapa.")
        return

    status = lab[fileira][coluna]
    if status == "L":
        lab[fileira][coluna] = "O"
        print(f"Computador na fileira {fileira} e coluna {coluna} reservado com sucesso!")
    elif status == "O":
        print(f"Computador na fileira {fileira} e coluna {coluna} já está ocupado. Escolha outro.")
    else:
        print(f"Computador na fileira {fileira} e coluna {coluna} está em manutenção. Escolha outro.")
        
#=======================================================================
#         EXECUÇÃO PRINCIPAL
#=======================================================================
print("==============================================================")
print("              LABORATÓRIO DE INFORMÁTICA")
print("==============================================================")

exibir_mapa(laboratorio)
contar_computadores(laboratorio)
ocupar_posicao(laboratorio)

print("\nMapa atualizado após a reserva:")
exibir_mapa(laboratorio)
contar_computadores(laboratorio)