tabuleiro = [
    ["X", "O", " "],
    [" ", "X", "O"],
    ["O", " ", "X"]
]


linha = 1
coluna = 0
simbolo = "X"


if tabuleiro[linha][coluna] == " ":
    tabuleiro[linha][coluna] = simbolo
    print("Jogada realizada com sucesso!")
else:
    print("Jogada inválida! A posição já está ocupada.")

print("-" * 30)  

print("Tabuleiro Atualizado:")
for i in range(len(tabuleiro)):
    linha_formatada = " | ".join(tabuleiro[i])
    print(f" {linha_formatada} ")
    if i < 2:
        print("-----------")