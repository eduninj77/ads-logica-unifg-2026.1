import os
os.system("clear" if os.name != "nt" else "cls")

#1. Será exibido  [[0,0,0],[0,0,0],[0,0,0]]
#2. Pois em vez de ser escrito de maneira convencional, ele apenas multiplica a quantidade de elementos por três e multiplica a própria lista vezes três.
#3. Resposta
matriz = [[0,0,0], [0,0,0], [0,0,0]]
matriz[0][0] = 1
print(matriz)