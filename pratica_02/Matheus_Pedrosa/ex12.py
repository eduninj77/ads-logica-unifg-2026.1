while True:
    valor = float(input('Digite o valor da compra: R$ '))

    if valor < 100:
        classificacao = 'sem desconto'
    elif valor < 200:
        classificacao = 'desconto básico'
    else:
        classificacao = 'desconto especial'
    print(f'Classificação: {classificacao}')

    continuar = input('Deseja cadastrar outra compra? (S/N): ').strip().upper()
    if continuar != 'S':
        break

print('Encerrando o cadastro de compras.')