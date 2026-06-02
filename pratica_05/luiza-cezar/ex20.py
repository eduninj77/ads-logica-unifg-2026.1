# Exercício 20 - Reservando assento

sala = [
    ["L", "O", "L"],
    ["O", "O", "L"],
    ["L", "L", "O"]
]

def exibir_sala(matriz_sala):
    """Exibe a sala de forma visual"""
    print("Mapa da sala:")
    for i, linha in enumerate(matriz_sala):
        print(f"Fileira {i}: ", end="")
        for j, assento in enumerate(linha):
            print(f"[{assento}] ", end="")
        print()

def reservar_assento(matriz_sala, linha, coluna):
    """Tenta reservar um assento"""
    if linha < 0 or linha >= len(matriz_sala) or coluna < 0 or coluna >= len(matriz_sala[linha]):
        return False, "Posição fora dos limites"
    
    if matriz_sala[linha][coluna] == "L":
        matriz_sala[linha][coluna] = "O"
        return True, "Reserva realizada"
    else:
        return True, "Assento indisponível"

print("=" * 60)
print("EXERCÍCIO 20 - RESERVANDO ASSENTO")
print("=" * 60)

print("\nSala antes da reserva:\n")
exibir_sala(sala)

print("\n" + "-" * 60)

# Tentando reservar assento
linha_desejada = 2
coluna_desejada = 1

print(f"\nTentando reservar assento na linha {linha_desejada}, coluna {coluna_desejada}...\n")

sucesso, mensagem = reservar_assento(sala, linha_desejada, coluna_desejada)
print(mensagem)

print("\n" + "-" * 60)
print("\nSala após a reserva:\n")
exibir_sala(sala)

print("\n" + "=" * 60)
print("✓ Assento reservado com sucesso!")
print(f"  Posição [{linha_desejada}][{coluna_desejada}] foi alterada de 'L' para 'O'")
print("=" * 60)
