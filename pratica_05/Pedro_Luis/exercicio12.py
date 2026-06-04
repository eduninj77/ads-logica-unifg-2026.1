import os
os.system("clear" if os.name != "nt" else "cls")


numeros = [
    [12, 5, 8],
    [9, 21, 3],
    [14, 6, 18]
]

maior = 0
menor = 0
lista_maior = [0, 0]
lista_menor = [0, 0]
for i in range(len(numeros)):
    for c in range(len(numeros[i])):
        v = numeros[i][c]
        if maior and menor == 0:
            maior = v
            menor = v
        if maior < v:
            maior = v
            lista_maior[0] = i
            lista_maior[1] = c 
        if menor > v:
            menor = v
            lista_menor[0] = i
            lista_menor[1] = c
print(f"Maior valor: {maior}\nLinha: {lista_maior[0]}\nColuna: {lista_maior[1]}")
print(f"Menor valor: {menor}\nLinha: {lista_menor[0]}\nColuna: {lista_menor[1]}")