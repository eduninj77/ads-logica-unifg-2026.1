# Exercício 25 - Jogo da velha: jogada simples

tabuleiro = [
    ["X", "O", " "],
    [" ", "X", "O"],
    ["O", " ", "X"]
]

def exibir_tabuleiro(matriz_tabuleiro):
    """Exibe o tabuleiro de jogo da velha de forma visual"""
    print()
    for i in range(len(matriz_tabuleiro)):
        for j in range(len(matriz_tabuleiro[i])):
            print(matriz_tabuleiro[i][j], end="")
            if j < 2:
                print(" | ", end="")
        print()
        if i < 2:
            print("-" * 9)

def fazer_jogada(matriz_tabuleiro, linha, coluna, simbolo):
    """Tenta fazer uma jogada no tabuleiro"""
    if linha < 0 or linha >= len(matriz_tabuleiro) or coluna < 0 or coluna >= len(matriz_tabuleiro[0]):
        return False, "Posição fora dos limites"
    
    if matriz_tabuleiro[linha][coluna] == " ":
        matriz_tabuleiro[linha][coluna] = simbolo
        return True, "Jogada válida"
    else:
        return True, "Posição ocupada - Jogada inválida"

print("=" * 60)
print("EXERCÍCIO 25 - JOGO DA VELHA: JOGADA SIMPLES")
print("=" * 60)

print("\nTabuleiro antes da jogada:")
exibir_tabuleiro(tabuleiro)

print("\n" + "-" * 60)

# Fazendo uma jogada
linha_jogada = 1
coluna_jogada = 0
simbolo_jogada = "X"

print(f"\nFazendo jogada em posição [{linha_jogada}][{coluna_jogada}] com símbolo '{simbolo_jogada}'...")

sucesso, mensagem = fazer_jogada(tabuleiro, linha_jogada, coluna_jogada, simbolo_jogada)
print(f"{mensagem}")

print("\n" + "-" * 60)
print("\nTabuleiro após a jogada:")
exibir_tabuleiro(tabuleiro)

print("\n" + "=" * 60)
print("✓ A posição [1][0] estava vazia (' ') e foi preenchida com 'X'")
print("=" * 60)
