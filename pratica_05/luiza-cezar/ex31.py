# Exercício 31 - Matriz de vendas

vendas = [
    [20, 25, 18, 30],
    [15, 22, 20, 19],
    [30, 28, 35, 40]
]

def calcular_total_por_produto(matriz_vendas):
    """Calcula o total vendido de cada produto"""
    totais = []
    for linha in matriz_vendas:
        totais.append(sum(linha))
    return totais

def calcular_total_por_semana(matriz_vendas):
    """Calcula o total vendido em cada semana"""
    num_semanas = len(matriz_vendas[0])
    totais = []
    
    for j in range(num_semanas):
        soma = 0
        for i in range(len(matriz_vendas)):
            soma += matriz_vendas[i][j]
        totais.append(soma)
    
    return totais

def encontrar_maior(lista):
    """Encontra o índice e o valor máximo de uma lista"""
    valor_max = max(lista)
    indice_max = lista.index(valor_max)
    return indice_max, valor_max

print("=" * 70)
print("EXERCÍCIO 31 - MATRIZ DE VENDAS")
print("=" * 70)

print("\nTabela de vendas (produtos × semanas):\n")
print("Produto\\Semana", end="")
for j in range(len(vendas[0])):
    print(f"\tSem{j}", end="")
print()

for i in range(len(vendas)):
    print(f"Produto {i}\t", end="")
    for j in range(len(vendas[i])):
        print(f"\t{vendas[i][j]}", end="")
    print()

print("\n" + "-" * 70)

# 1. Total por produto
print("\n1. TOTAL VENDIDO POR PRODUTO\n")

totais_produtos = calcular_total_por_produto(vendas)
for i, total in enumerate(totais_produtos):
    print(f"Produto {i}: {total} unidades")

# 2. Total por semana
print("\n" + "-" * 70)
print("\n2. TOTAL VENDIDO POR SEMANA\n")

totais_semanas = calcular_total_por_semana(vendas)
for j, total in enumerate(totais_semanas):
    print(f"Semana {j}: {total} unidades")

# 3. Produto com maior total
print("\n" + "-" * 70)
print("\n3. PRODUTO COM MAIOR TOTAL VENDIDO\n")

prod_max, total_max = encontrar_maior(totais_produtos)
print(f"Produto {prod_max}: {total_max} unidades")

# 4. Semana com maior total
print("\n" + "-" * 70)
print("\n4. SEMANA COM MAIOR TOTAL VENDIDO\n")

sem_max, total_max = encontrar_maior(totais_semanas)
print(f"Semana {sem_max}: {total_max} unidades")

print("\n" + "=" * 70)
print("✓ Análise de vendas concluída!")
print("=" * 70)
