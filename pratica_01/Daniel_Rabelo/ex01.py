ANO_ATUAL = 2025

nome = input("Digite seu nome: ")
ano_nascimento = int(input("Digite seu ano de nascimento: "))
altura = float(input("Digite sua altura em metros (ex: 1.75): "))

idade = ANO_ATUAL - ano_nascimento

print(f"Olá, {nome}! Você tem {idade} anos e sua altura é de {altura}m. Registro concluído.")