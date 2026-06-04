import os
os.system("clear" if os.name != "nt" else "cls")

numeros = [
    [12, 5, 8],
    [9, 21, 3],
    [14, 6, 18]
]

maior = 0
menor = 0

for i in numeros:
    for v in i:
        if maior and menor == 0:
            maior = v
            menor = v
        if maior < v:
            maior = v
        if menor > v:
            menor = v

print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")