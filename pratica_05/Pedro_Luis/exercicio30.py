import os
os.system("clear" if os.name != "nt" else "cls")

def computador(desisao):
    while True:
        try:
            p_computador = int(input("Digite a cadeira que você quer sentar: "))
            if p_computador not in [0, 1, 2, 3, 4]:
                print("Esse computador não existe.")
                continue
            
        except (ValueError, KeyboardInterrupt):
            print("Digite apenas números inteiros.")
            continue
        break
    if laboratorio[desisao][p_computador] == "L":
        laboratorio[desisao][p_computador] = "O"
        print(f"Agora o computador {p_computador} está ocupado.")
    elif laboratorio[desisao][p_computador] == "O":
        print(f"O computador {p_computador} já está ocupado.")
    else:
        print(f"O computador {p_computador} está em manutenção.")
    
laboratorio = [
    ["L", "L", "M", "O", "L"],
    ["L", "L", "L", "O", "M"],
    ["L", "O", "O", "L", "O"],
    ["L", "L", "O", "M", "O"],
]

manutencao = 0
livres = 0
ocupados = 0


while True:
    manutencao = 0
    livres = 0
    ocupados = 0
    print("=" * 21)
    for i in laboratorio:
        print("[ "+" | ".join(i) + " ]")
        for v in i:
            if v == "L":
                livres += 1
            if v == "M":
                manutencao += 1
            if v == "O":
                ocupados += 1
    print("=" * 21)
    print("-" * 30)
    print(f"Computadores livres {livres}")
    print(f"Computadores ocupados {ocupados}")
    print(f"Computadores em manutenção {manutencao}")
    print("-" * 30)
    try:
        escolha = input("Você quer reservar um computador? [S/N] ").strip().upper()
        if escolha not in ["S", "N"] or not escolha:
            print("Digite apenas entre S(sim) ou N(não).")
            continue 
        if escolha == "N":
            break
        else:       
            desisao = int(input("Digite o número da fileira que você quer sentar: "))
            if desisao not in [0, 1, 2, 3]:
                print("Essa fileira não existe.")
                continue
            computador(desisao)
    except (ValueError):
        print("Digite apenas números inteiros.")
        continue
    except(KeyboardInterrupt):
        print("Não enterrompa o programa no meio da execução!")
        continue
print("Obrigado por executar o programa!")
                  


