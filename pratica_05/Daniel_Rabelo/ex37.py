# Resposta é a letra C)

matriz = [
    [1, 2, 3], #linha 0
    [4, 5,], #linha 1
    [6, 7, 8]  #linha 2
]

print(matriz[1][2])   

# IndexError! matriz[1] retorna [4, 5] — uma lista com apenas 2 elementos. Tentar acessar o índice 2 ultrapassa o limite.

# Como corrigir 
linha  = 1
coluna = 2

if coluna < len(matriz[linha]):
    print(matriz[linha][coluna])
else:
    print(f"Índice {coluna} inválido — linha {linha} tem só {len(matriz[linha])} elementos.")