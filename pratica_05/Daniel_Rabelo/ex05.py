notas = [
    [8.0, 7.5, 9.0],  # estudante 0
    [5.0, 6.0, 5.5],  # estudante 1
    [9.0, 8.5, 10.0], # estudante 2
    [6.5, 7.0, 6.0]   # estudante 3
]

# Matriz ANTES das alterações
print("---- ANTES ----")
for i, linha in enumerate(notas):
    print(f"Estudante {i}: {linha}")

print()

# 1. Alterar a primeira nota do segundo estudante para 6.5
notas[1][0] = 6.5

# 2. Alterar a terceira nota do quarto estudante para 7.0
notas[3][2] = 7.0

# Matriz DEPOIS das alterações
print("---- DEPOIS ----")
for i, linha in enumerate(notas):
    print(f"Estudante {i}: {linha}")