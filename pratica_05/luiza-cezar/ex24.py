# Exercício 24 - Jogo da velha: exibição do tabuleiro

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

print("=" * 60)
print("EXERCÍCIO 24 - JOGO DA VELHA: EXIBIÇÃO DO TABULEIRO")
print("=" * 60)

print("\nTabuleiro em formato visual:")
exibir_tabuleiro(tabuleiro)

print("\n" + "=" * 60)
print("✓ Estado do tabuleiro:")
print("  X está em posições: [0][0], [1][1], [2][2] (diagonal)")
print("  O está em posições: [0][1], [1][2], [2][0]")
print("  Espaços vazios em: [0][2], [1][0], [2][1]")
print("=" * 60)
