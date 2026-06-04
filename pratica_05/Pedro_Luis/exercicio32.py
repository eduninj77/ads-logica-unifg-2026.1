import os
os.system("clear" if os.name != "nt" else "cls")

def celula(desisao):
    while True:
        try:
            p_celula = int(input("Digite a célula que será ocupada: "))
            if p_celula not in [0, 1, 2, 3, 4]:
                print("Essa célula não existe.")
                continue
            break
        except (ValueError, KeyboardInterrupt):
            print("Digite apenas números inteiros.")
            continue
    if matriz[desisao][p_celula] == 0:
        matriz[desisao][p_celula] = 1
        print(f"Agora a célula {p_celula} está ocupada.")
    else:
        print(f"A célula {p_celula} já está ocupada.")

matriz = [
        [1,0,1,0,0],
        [0,1,0,0,1],
        [1,0,1,1,0],
        [0,1,0,1,0],
        [1,0,1,1,1]
    ]

while True:
    ocupadas = 0
    print("=" * 21)
    for i in matriz:
        txt_matriz = [str(elemento) for elemento in i]
        print("[ " + " | ".join(txt_matriz) + " ]")
        for v in i:
            if v == 1:
                ocupadas += 1
    print("=" * 21)
    print("-" * 30)
    print(f"{ocupadas} células estão ocupadas.")
    print("-" * 30)
    try:
        escolha = input("Você quer reservar uma célua? [S/N] ").strip().upper()
        if escolha not in ["S", "N"] or not escolha:
            print("Digite apenas entre S(sim) ou N(não).")
            continue 
        if escolha == "N":
            break
        else:       
            desisao = int(input("Digite o número da fileira da célula que você quer ocupar: "))
            if desisao not in [0, 1, 2, 3, 4]:
                print("Essa fileira não existe.")
                continue
            celula(desisao)
    except (ValueError):
        print("Digite apenas números inteiros.")
        continue
    except(KeyboardInterrupt):
        print("Não enterrompa o programa no meio da execução!")
        continue
print("Obrigado por executar o programa!")
    