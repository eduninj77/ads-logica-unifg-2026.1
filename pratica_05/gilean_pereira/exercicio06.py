#dados = [
#    [1, 2],
#   [3, 4]
#]

# print(dados[2][0])


# Não. O programa vai travar e exibir o erro IndexError: list index out of range. 
# Isso acontece porque o código tenta acessar a linha de índice 2 (dados[2]), mas a matriz só possui duas linhas (índices 0 e 1).
#  O índice 2 está fora do limite.

# Os únicos índices válidos para as linhas são 0 (primeira linha [1, 2]) e 1 (segunda linha [3, 4]).


dados = [
    [1, 2],
    [3, 4]
]

print(dados[1][0])