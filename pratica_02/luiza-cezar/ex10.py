opcao = None

while opcao != 0:
    print("\nMenu:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("0 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print(f"Resultado da soma: {a + b}")
    elif opcao == 2:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print(f"Resultado da subtração: {a - b}")
    elif opcao == 0:
        print("Encerrando o programa...")
    else:
        print("Opção inválida. Tente novamente.")
