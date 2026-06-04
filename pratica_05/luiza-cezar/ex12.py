# Exercício 12 - Localizando posição do maior valor

numeros = [
    [12, 5, 8],
    [9, 21, 3],
    [14, 6, 18]
]

print("=" * 60)
print("EXERCÍCIO 12 - LOCALIZANDO POSIÇÃO DO MAIOR VALOR")
print("=" * 60)

print("\nMatriz de números:")
for i, linha in enumerate(numeros):
    print(f"Linha {i}: {linha}")

# Inicializando com o primeiro valor
primeiro_valor = numeros[0][0]
maior = primeiro_valor
linha_maior = 0
coluna_maior = 0

# Encontrando maior valor e sua posição
for i in range(len(numeros)):
    for j in range(len(numeros[i])):
        if numeros[i][j] > maior:
            maior = numeros[i][j]
            linha_maior = i
            coluna_maior = j

print("\n" + "-" * 60)
print(f"\nMaior valor: {maior}")
print(f"Linha: {linha_maior}")
print(f"Coluna: {coluna_maior}")

# Verificação
print("\n" + "=" * 60)
print(f"✓ Verificação: numeros[{linha_maior}][{coluna_maior}] = {numeros[linha_maior][coluna_maior]}")
print("=" * 60)
