#1- O resultado vai ser [[1, 0, 0], [1, 0, 0], [1, 0, 0]].
#2- confunde porque a intenção era mudar só um número, mas altera o primeiro elemento de todas as linhas de uma vez, já que elas compartilham a mesma referência na memória.

matriz = [[0 * 3] for _ in range(3)]
matriz[0][0] = 1
print(matriz)