vendas = [
    [20, 25, 18, 30],
    [15, 22, 20, 19],
    [30, 28, 35, 40]
]

totais_produtos = []
maior_venda_prod = -1
prod_campeao = -1

for i in range(len(vendas)):
    soma_prod = 0
    for j in range(len(vendas[i])):
        soma_prod += vendas[i][j]
    totais_produtos.append(soma_prod)
    print(f"Total Produto {i}: {soma_prod}")
    
    if soma_prod > maior_venda_prod:
        maior_venda_prod = soma_prod
        prod_campeao = i

maior_venda_sem = -1
semana_campea = -1

for j in range(4):
    soma_sem = 0
    for i in range(3):
        soma_sem += vendas[i][j]
    print(f"Total Semana {j}: {soma_sem}")
    
    if soma_sem > maior_venda_sem:
        maior_venda_sem = soma_sem
        semana_campea = j

print(f"Produto com maior total vendido: Produto {prod_campeao}")
print(f"Semana com maior total vendido: Semana {semana_campea}")