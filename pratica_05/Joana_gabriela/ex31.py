vendas = [
    [20, 25, 18, 30],
    [15, 22, 20, 19],
    [30, 28, 35, 40]
]

produtos = ["Produto A", "Produto B", "Produto C"]

# 1. Total por produto
print("=" * 35)
print(f"{'VENDAS POR PRODUTO':^35}")
print("=" * 35)

maior_produto = None
nome_maior_produto = ""

for i in range(len(produtos)):
    total = 0
    for venda in vendas[i]:
        total += venda
    print(f"{produtos[i]}: {total} unidades")

    if maior_produto is None or total > maior_produto:
        maior_produto = total
        nome_maior_produto = produtos[i]

# 2. Total por semana
print()
print("=" * 35)
print(f"{'VENDAS POR SEMANA':^35}")
print("=" * 35)

maior_semana = None
num_maior_semana = 0

for j in range(len(vendas[0])):
    total = 0
    for i in range(len(vendas)):
        total += vendas[i][j]
    print(f"Semana {j + 1}: {total} unidades")

    if maior_semana is None or total > maior_semana:
        maior_semana = total
        num_maior_semana = j + 1

# 3 e 4. Destaques
print()
print("=" * 35)
print(f"{'DESTAQUES':^35}")
print("=" * 35)
print(f"🏆 Maior vendedor : {nome_maior_produto} ({maior_produto} unidades)")
print(f"📅 Melhor semana  : Semana {num_maior_semana} ({maior_semana} unidades)")
print("=" * 35)