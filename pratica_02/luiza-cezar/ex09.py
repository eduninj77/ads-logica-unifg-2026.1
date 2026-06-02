salario = float(input("Digite o salário do funcionário: R$ "))

if salario <= 1500.00:
    percentual = 15
elif salario <= 3000.00:
    percentual = 10
else:
    percentual = 5

novo_salario = salario * (1 + percentual / 100)

print(f"Salário original: R$ {salario:.2f}")
print(f"Percentual aplicado: {percentual}%")
print(f"Novo salário: R$ {novo_salario:.2f}")
