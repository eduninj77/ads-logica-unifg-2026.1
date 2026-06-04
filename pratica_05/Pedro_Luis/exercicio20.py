import os
os.system("clear" if os.name != "nt" else "cls")

def assento(decisao):
    while True:
        try:
            coluna = int(input(f"Digite a coluna que você quer reservar da linha {decisao}: "))
            if coluna not in [0, 1, 2]:
                print("Escolha apenas entre a fileira 0, 1, ou 2!")
                continue
            break
        except (ValueError, KeyboardInterrupt):
            print("Digite apenas números inteiros nessa opção!")
            continue  
    if sala[decisao][coluna] == "L":
        sala[decisao][coluna] = "O"
        print(f"Reserva realizada no assento {coluna} da linha {decisao}!")
    else:
        print(f"O assento {coluna} da linha {decisao} está indisponível.")
sala = [
    ["L", "O", "L"],
    ["O", "O", "L"],
    ["L", "L", "O"]
]

while True:
    try:
        escolha_assento = int(input("Digite qual linha você quer reservar um assento? "))
        if escolha_assento not in [0,1,2]:
            print("Escolha apenas entre a fileira 0, 1, ou 2!")
            continue
    except (ValueError, KeyboardInterrupt):
        print("Digite apenas números inteiros nessa opção!")
        continue
    assento(escolha_assento)
    while True:
        try:
            escolha = input("Você quer continuar reservando assentos? [S/N] ").strip().upper()
            if escolha not in ["S", "N"] or not escolha:
                print("Digite apenas entre S(sim) ou N(não)!")
                continue
        except KeyboardInterrupt:
            print("Não feche a aplicação no meio da execução!")
            continue
        break
    if escolha == "N":
        break
print("Obrigado por reservar seus assentos conosco!")   
for i in sala:
        print("[ " + " | ".join(i) + " ]")