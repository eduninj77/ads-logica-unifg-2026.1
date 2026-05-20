for i in range(1, 6):
    nota = float(input(f'Digite a nota {i}: '))
    if i == 1 or nota > maior_nota:
        maior_nota = nota
print(f'A maior nota informada foi: {maior_nota}')

