numeros = [
    [12, 5, 8],
    [9, 21, 3],
    [14, 6, 18]
]

maior = numeros[0][0]
linha_maior = 0
coluna_maior = 0

for i, linha in enumerate(numeros):
    for j, numero in enumerate(linha):
        if numero > maior:
            maior = numero
            linha_maior = i
            coluna_maior = j
       
print(f"O maior número é: {maior}")
print(f"Linha: {linha_maior}")
print(f"Coluna: {coluna_maior}")