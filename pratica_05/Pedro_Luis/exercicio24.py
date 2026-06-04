import os
os.system("clear" if os.name != "nt" else "cls")

tabuleiro = [
    ["X", "O", " "],
    [" ", "X", "O"],
    ["O", " ", "X"]
]

print(" | ".join(tabuleiro[0]))
print("---------")
print(" | ".join(tabuleiro[1]))
print("---------")
print(" | ".join(tabuleiro[-1]))
