contagem_positivos = 0
for i in range(1, 11):
    valor = float(input(f'Digite o {i}º número: '))
    if valor > 0:
        contagem_positivos += 1
print(f'Quantidade de números positivos: {contagem_positivos}')