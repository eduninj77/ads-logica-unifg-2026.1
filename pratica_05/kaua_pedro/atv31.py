vendas = [
    [20, 25, 18, 30],
    [15, 22, 20, 19],
    [30, 28, 35, 40]
]

for i in range(len(vendas)):
    print(f"Produto {i} - Total: {sum(vendas[i])}")

print()
totais_semana = []
for j in range(len(vendas[0])):
    total = sum(vendas[i][j] for i in range(len(vendas)))
    totais_semana.append(total)
    print(f"Semana {j} - Total: {total}")

maior_prod = max(range(len(vendas)), key=lambda i: sum(vendas[i]))
maior_sem = totais_semana.index(max(totais_semana))

print(f"\nProduto com maior total: {maior_prod}")
print(f"Semana com maior total: {maior_sem}")
