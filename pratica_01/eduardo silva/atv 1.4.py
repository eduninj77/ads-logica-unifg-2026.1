# Solicita os dados do usuário
idade = int(input("Digite sua idade: "))
experiencia = int(input("Digite seus anos de experiência: "))

# Regra lógica de acesso (sem if/else)
acesso = (idade >= 18) and (experiencia > 2)

# Exibe o resultado
print(f"Acesso Liberado: {acesso}")