valor_hora = float(input("Digite o valor por hora: \n"))
hora_estimativa = int(input("Digite a estimativa de conclusão em horas: \n"))

valor_bruto = hora_estimativa * valor_hora
impostos = valor_bruto * 0.15
valor_liq = valor_bruto - impostos

print(f"Valor Bruto: R${valor_bruto:.2f}")
print(f"Valor dos impostos: R${impostos:.2f}")
print(f"Valor liquido: R${valor_liq:.2f}")