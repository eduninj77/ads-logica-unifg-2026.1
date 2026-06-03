idade = int(input("Idade do usuário: \n"))
anos_exp = int(input("Tempo de experiência: \n"))

acesso = (idade >= 18) and (anos_exp >= 2)

print(acesso)