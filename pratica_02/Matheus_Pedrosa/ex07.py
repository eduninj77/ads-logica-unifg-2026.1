soma_pares = 0
for i in range(1, 9):
    valor = int(input(f'Digite o {i}º valor inteiro: '))
    if valor % 2 == 0:
        soma_pares += valor
print(f'Soma dos números pares: {soma_pares}')
