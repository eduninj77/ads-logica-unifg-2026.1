contador_s = 0

while True:
    resposta = input("Digite S, N ou FIM para encerrar: ").strip().upper()
    if resposta == "FIM":
        break
    if resposta == "S":
        contador_s += 1
    elif resposta != "N":
        print("Resposta inválida. Use S, N ou FIM.")

print(f"Quantidade de respostas S: {contador_s}")

# O while com sentinela é adequado porque a quantidade de respostas não é
# conhecida antes. Ele permite continuar lendo até o usuário digitar FIM.
