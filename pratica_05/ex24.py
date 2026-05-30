tabuleiro = [
    ["X", "O", " "],
    [" ", "X", "O"],
    ["O", " ", "X"]
]

for i, linha in enumerate(tabuleiro):
    print(f" {linha[0]} | {linha[1]} | {linha[2]} ")
    if i < len(tabuleiro) - 1:
        print("------------")