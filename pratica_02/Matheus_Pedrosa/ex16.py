contador_sim = 0
while True:
    resposta = input('Digite S para sim, N para não ou FIM para encerrar: ').strip().upper()
    if resposta == 'FIM':
        break
    if resposta == 'S':
        contador_sim += 1
print(f'Quantidade de respostas S: {contador_sim}')