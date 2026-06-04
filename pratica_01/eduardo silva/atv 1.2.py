# Solicita os dados do usuário
valor_hora = float(input("Digite o valor cobrado por hora: R$ "))
horas = float(input("Digite a quantidade de horas estimadas: "))

# Calcula os valores
valor_bruto = horas * valor_hora
impostos = valor_bruto * 0.15
valor_liquido = valor_bruto - impostos

# Exibe os resultados
print(f"\nValor Bruto: R$ {valor_bruto:.2f}")
print(f"Impostos (15%): R$ {impostos:.2f}")
print(f"Valor Líquido: R$ {valor_liquido:.2f}")