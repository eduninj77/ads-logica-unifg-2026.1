dados = [
    [1, 2],
    [3, 4]
]

try:
    print(dados[2][0])
except IndexError:
    print("Erro: índice fora dos limites")

print("Índices válidos para linhas: 0, 1")
print("Corrigido:")
print(dados[1][0])
