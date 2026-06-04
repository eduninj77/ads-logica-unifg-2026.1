import os
os.system("clear" if os.name != "nt" else "cls")
def jogada(desisao):
    while True:
        try:
            coluna = int(input("Digite a coluna que você quer jogar: "))
            jogo = input("Digite o que você quer jogar? [X/O] ").strip().upper()
            if jogo not in ["X", "O"]:
                print("Digite apenas entre X ou O")
                continue
            if coluna not in [0, 1, 2]:
                print("Coluna não encontrada.")
                continue
            break
        except KeyboardInterrupt:
            print("Não pare o programa no meio da execução")
            continue
        except ValueError:
            print("Digite apenas números inteiros!")
            continue
    if tabuleiro[desisao][coluna] == " ":
        tabuleiro[desisao][coluna] = jogo        
        print("Jogada feita!")
    else:
        print("A casa está ocupada, jogada inválida!")

tabuleiro = [
    ["X", "O", " "],
    [" ", "X", "O"],
    ["O", " ", "X"]
]
while True:
    print(" | ".join(tabuleiro[0]))
    print("---------")
    print(" | ".join(tabuleiro[1]))
    print("---------")
    print(" | ".join(tabuleiro[-1]))
    jogar = input("Fazer uma jogada? [S/N] ").strip().upper()
    if jogar not in ["S", "N"] or not jogar:
        print("Digite apenas entre S(sim) ou N(não).")
        continue
    if jogar == "N":
        break
    else:
        while True:
            try:
                linha = int(input("Digite a linha que você quer jogar: "))
                if linha not in [0, 1, 2]:
                    print("Digite apenas entre 0, 1, 2")
                    continue
            except (ValueError, KeyboardInterrupt):
                print("Digite apenas números inteiros.")
                continue
            break
        jogada(linha)
print("Obrigado por jogar jogo da velha!")