idade = int(input('Idade: '))
experiencia = int(input('Anos de experiência: '))
acesso = (idade >= 18) and (experiencia > 2)
print(f'Acesso Liberado: {acesso}')
