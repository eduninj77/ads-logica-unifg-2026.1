#1. Qual resultado será exibido? python[[1, 0, 0], [1, 0, 0], [1, 0, 0]]
#Ao invés de alterar só [0][0], as 3 linhas foram modificadas.

#2. Por que isso confunde iniciantes?[[0] * 3] * 3 não cria 3 listas independentes — cria 3 referências apontando para a mesma lista na memória:
#matriz[0] ──┐
#matriz[1] ──┼──→ [0, 0, 0]  (uma única lista)
#matriz[2] ──┘
#Então ao modificar matriz[0][0], as 3 linhas refletem a mudança, pois são o mesmo objeto: pythonprint(matriz[0] is matriz[1])  # True ← mesma lista!

#3. Código corrigido:
matriz = [[0] * 3 for _ in range(3)]
matriz[0][0] = 1
print(matriz)