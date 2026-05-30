dados = [
    [1, 2],
    [3, 4]
]

print(dados[2][0])

# O código acima resultará em um erro de índice, pois a lista 'dados' possui apenas 2 elementos (índices 0 e 1). O acesso a dados[2] é inválido, pois não existe um terceiro elemento na lista.

dados = [
    [1, 2],     # linha 0
    [3, 4]      # linha 1 
]               # linha 2 (não existe)

dados = [
    [1, 2],     # linha 0 [1, 2]
    [3, 4]      # linha 1 [3, 4]
]               

# 3 está na linha 1, coluna 0
print(dados[1][0]) #3