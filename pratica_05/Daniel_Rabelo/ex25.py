tabuleiro = [
    ["X", "O", " "],
    [" ", "X", "O"],
    ["O", " ", "X"]
]

linha = 1
coluna = 0  
simbolo = "X"

def exibir_tabuleiro(tabuleiro):
    for i, linha in enumerate(tabuleiro):
        print(f" {linha[0]} | {linha[1]} | {linha[2]} ")
        if i < len(tabuleiro) - 1:
            print("------------")

# Tabuleiro ANTES
print("----------Tabuleiro ANTES----------")
exibir_tabuleiro(tabuleiro)
print()

# Verificação e jogada
if tabuleiro[linha][coluna] == " ":
    tabuleiro[linha][coluna] = simbolo
    print(f"Jogada realizada na linha {linha} e coluna {coluna} com o símbolo '{simbolo}'!")
else:
    print(f"Posição na linha {linha} e coluna {coluna} já está ocupada por '{tabuleiro[linha][coluna]}'. Escolha outra posição.")
print()

# Tabuleiro DEPOIS
print("----------Tabuleiro DEPOIS----------")
exibir_tabuleiro(tabuleiro)