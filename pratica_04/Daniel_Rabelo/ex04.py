palavra = "programacao"
valores = [10, 20, 30, 40, 50, 60]

# 1. Primeiros 4 caracteres (posições 0, 1, 2, 3)
print("4 primeiros caracteres:", palavra[:4])

# 2. Caracteres da posição 4 até 8 (não inclui o 8)
print("Posição 4 até 8:", palavra[4:8])

# 3. Três primeiros elementos da lista
print("3 primeiros valores:", valores[:3])

# 4. Da posição 2 até o final
print("Do índice 2 ao final:", valores[:2])

# ------- Desafio: outros recortes observados -------

# Invertendo a palavra completa com passo -1
print(palavra[::-1])
# Observação: passo -1 percorre a sequência de trás pra frente

# Pulando de 2 em 2 na lista
print(valores[::2])
# Observação: o terceiro parâmetro define o "salto" entre índices

# Últimos 3 caracteres com índice negativo
print(palavra[-3:])
# Observação: índices negativos contam a partir do final

# Fatia vazia - início maior que fim
print(palavra[8:4])
# Observação: retorna string vazia quando os limites são invertidos

