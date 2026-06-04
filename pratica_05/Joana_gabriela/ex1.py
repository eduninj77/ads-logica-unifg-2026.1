matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

#a) Quantas linhas?
print(len(matriz))

#b) Quantas colunas por linha?
print(len(matriz[0]))

#c) matriz[0][2]
print(matriz[0][2])

#d) matriz[2][1]
print(matriz[2][1])

#e) matriz[1][1] retorna 50 porque i=1 seleciona a segunda linha [40,50,60] e j=1 seleciona o segundo elemento: 50.