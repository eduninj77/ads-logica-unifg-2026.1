matriz = [[0] * 3] * 3
matriz[0][0] = 1
print(matriz)  # Saída: [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

# Confunde iniciantes pq o operador *3 não cria 3 listas independentes, mas sim 3 referências à mesma lista. Assim, ao modificar uma linha, todas as linhas são modificadas, pois apontam para a mesma lista.

# ✓ CORRETO — cada linha é um objeto independente
matriz = [[0] * 3 for _ in range(3)]
matriz[0][0] = 1
print(matriz)  # Saída: [[1, 0, 0], [0, 0, 0], [0, 0, 0]]

matriz = [[0] * 3 for _ in range(3)]
print(id(matriz[0]), id(matriz[1]), id(matriz[2]))  # IDs diferentes, linhas independentes
