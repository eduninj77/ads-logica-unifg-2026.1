nome = input('Nome do usuário: ')
ano_nascimento = int(input('Ano de nascimento: '))
altura = float(input('Altura em metros: '))

ano_atual = 2026
idade = ano_atual - ano_nascimento
print(f'Olá, {nome}! Você tem {idade} anos e sua altura é de {altura}m. Registro concluído.')
