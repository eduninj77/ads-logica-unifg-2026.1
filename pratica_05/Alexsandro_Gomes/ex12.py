numeros = [
    [12, 5, 8],
    [9, 21, 3],
    [14, 6, 18]
]

maior = numeros[0][0]
menor = numeros[0][0]
linha_maior = 0
coluna_maior = 0

for i in range(len(numeros)):
    for j in range(len(numeros[i])):
        atual = numeros[i][j]
        
        
        if atual < menor:
            menor = atual
            
        
        if atual > maior:
            maior = atual
            linha_maior = i
            coluna_maior = j

print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
print(f"Linha: {linha_maior}")
print(f"Coluna: {coluna_maior}")