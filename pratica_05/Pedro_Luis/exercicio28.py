import os
os.system("clear" if os.name != "nt" else "cls")

#1. Porque ela não "reinicia" a cada linha da matriz notas.
#2. Correção:
notas = [
    [8, 7, 9],
    [5, 6, 5],
    [9, 10, 8]
]

soma = 0
for i in range(len(notas)):
    soma = 0
    for j in range(len(notas[i])):
        soma += notas[i][j]
    media = soma / len(notas[i])
    print(f"{media:.2f}")

#3. Definindo a variável soma como 0 no primeiro for, a cada linha ele não irá continuar somando todas as notas juntas.

