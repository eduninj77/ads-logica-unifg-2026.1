# O problema com a varável "soma" é que ela não está sendo atualizada dentro do loop, ou seja, o valor de "soma" permanece 0 durante toda a execução do código. Para corrigir isso, é necessário adicionar o valor de cada número à variável "soma" dentro do loop. Aqui está a correção:

# O que o codigo faz (ERRADO):
# soma = 0

# linha 0 soma = 0+8+7+9 = 24 média = 24/3 = 8.0
# linha 1 soma = 24+5+6+5 = 40 média = 40/3 = 13.3
# linha 2 soma = 40+9+8+10+8 = 67 média = 67/3 = 22.3

# Codigo corrigido:
notas = [
    [8.0, 7.0, 9.0],
    [5.0, 6.0,  5.0],
    [9.0, 8.0, 10.0]
]

for i in range(len(notas)):
    soma = 0
    for nota in notas[i]:
        soma += nota
    media = soma / len(notas[i])
    print(f"Linha {i}: Média = {media:.2f}")