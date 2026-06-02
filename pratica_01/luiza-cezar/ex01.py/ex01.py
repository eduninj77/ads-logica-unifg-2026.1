
##################################################
#                                                #
#               by: Luiza Cezar                  #
#                                                #
##################################################


from datetime import datetime

nome = input("Digite seu nome: ")
data_nascimento = input("Digite sua data de nascimento: ")

altura_input = input("Digite sua altura em metros: ")
altura = float(altura_input.replace(",", "."))

ano_nascimento = int(data_nascimento[-4:])


ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento

print(f"Olá, {nome}! Você tem {idade} anos e sua altura é de {altura}m. Registro concluído.")