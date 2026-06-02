#matriz = [[0] * 3] * 3
#matriz[0][0] = 1
#print(matriz)


# Será exibido: [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

#Porque o iniciante espera modificar apenas a posição [0][0]. 
# No entanto, o operador * 3 externo não cria cópias independentes das linhas; 
# ele copia a referência na memória.



matriz = [[0] * 3 for _ in range(3)]

matriz[0][0] = 1
print(matriz)
