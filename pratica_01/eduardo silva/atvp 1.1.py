from datetime import datetime

# Solicita os dados do usuário
nome = input("Digite seu nome: ")
ano_nascimento = int(input("Digite seu ano de nascimento: "))
altura = float(input("Digite sua altura em metros: "))

# Obtém o ano atual
ano_atual = datetime.now().year

# Calcula a idade
idade = ano_atual - ano_nascimento

# Exibe a mensagem final
print(f"Olá, {nome}! Você tem {idade} anos e sua altura é de {altura}m. Registro concluído.")