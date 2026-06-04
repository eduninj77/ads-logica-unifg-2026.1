#1- O problema é que a variável "soma" foi criada fora dos loops. Com isso, ela nunca é zerada e vai acumulando as notas das linhas anteriores na hora de calcular a próxima média.

#2- Codigo corrigido.

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


#3. Funciona porque colocando "soma = 0" dentro do primeiro loop, a conta reseta toda vez que o código muda de aluno. Assim, a nota de um não atrapalha a média do outro.