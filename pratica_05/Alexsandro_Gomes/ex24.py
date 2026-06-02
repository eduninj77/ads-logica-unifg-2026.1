tabuleiro = [
    ["X", "O", " "],
    [" ", "X", "O"],
    ["O", " ", "X"]
]

for i in range(len(tabuleiro)):
    linha_formatada = ""
    for j in range(len(tabuleiro[i])):
        linha_formatada += tabuleiro[i][j]
        if j < len(tabuleiro[i]) - 1:
            linha_formatada += " | "
            
    print(linha_formatada)
    
    if i < len(tabuleiro) - 1:
        print("---------")