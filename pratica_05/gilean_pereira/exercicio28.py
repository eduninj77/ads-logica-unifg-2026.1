
# A variável soma = 0 está fora dos loops. Como ela nunca é zerada, acumula os valores das linhas anteriores, gerando médias erradas.

notas = [
    [8, 7, 9],
    [5, 6, 5],
    [9, 10, 8]
]

for i in range(len(notas)):
    soma = 0 
    for j in range(len(notas[i])):
        soma += notas[i][j]
    media = soma / len(notas[i])
    print(media)


#Garante que a soma comece do zero a cada nova linha processada.