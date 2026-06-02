vendas = [
    [20, 25, 18, 30],  
    [15, 22, 20, 19],  
    [30, 28, 35, 40]  
]

total_produtos = [sum(produto) for produto in vendas]
for i, total in enumerate(total_produtos):
    print(f"Total Produto {i+1}: {total}")

print("-" * 30)

total_semanas = [0, 0, 0, 0]
for produto in vendas:
    for semana in range(4):
        total_semanas[semana] += produto[semana]

for i, total in enumerate(total_semanas):
    print(f"Total Semana {i+1}: {total}")

print("-" * 30)

maior_produto = total_produtos.index(max(total_produtos)) + 1
print(f"Produto com maior total vendido: Produto {maior_produto}")

maior_semana = total_semanas.index(max(total_semanas)) + 1
print(f"Semana com maior total vendido: Semana {maior_semana}")