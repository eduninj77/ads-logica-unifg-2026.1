# Faixas de desconto definidas no código:
# - sem desconto: compras até R$ 100,00
# - desconto básico: compras entre R$ 100,01 e R$ 500,00
# - desconto especial: compras acima de R$ 500,00

continuar = True

while continuar:
    valor = float(input("Digite o valor da compra: R$ "))

    if valor <= 100.00:
        classificacao = "sem desconto"
    elif valor <= 500.00:
        classificacao = "desconto básico"
    else:
        classificacao = "desconto especial"

    print(f"Classificação da compra: {classificacao}")

    resposta = input("Deseja informar outra compra? (s/n): ").strip().lower()
    if resposta != "s":
        continuar = False

print("Encerrando o programa.")
