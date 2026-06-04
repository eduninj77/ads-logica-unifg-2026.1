#1 O primeiro índice de uma lista em Python é 1. F
#2 Em matriz[i][j], i indica a linha e j a coluna. V
#3 Uma lista de listas sempre tem o mesmo número de elementos em todas as linhas. F
#4 Uma matriz pode representar um boletim escolar. V
#5 Para percorrer uma matriz inteira, geralmente usamos laços aninhados. V

#correção 01
frutas = ["maçã", "banana", "uva"]
print(frutas[0])  # "maçã"  ← primeiro elemento
print(frutas[1])  # "banana"
#O primeiro índice de uma lista em Python é 0, não 1. Python utiliza indexação baseada em zero (zero-based indexing).

#correção 03
# Lista irregular — completamente válida em Python
irregular = [
    [1, 2, 3],
    [4, 5],        # só 2 elementos
    [6, 7, 8, 9]   # 4 elementos
]

# Matriz retangular — linhas com mesmo tamanho (por escolha do programador)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
