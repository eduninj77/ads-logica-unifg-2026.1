tabuleiro = [
    ["X", "O", " "],
    [" ", "X", "O"],
    ["O", " ", "X"]
]


for i in range(len(tabuleiro)):
    

    linha_formatada = " | ".join(tabuleiro[i])
    print(f" {linha_formatada} ")
    
    if i < 2:
        print("-----------")