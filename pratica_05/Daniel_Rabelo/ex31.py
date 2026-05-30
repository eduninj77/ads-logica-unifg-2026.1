# =======================================================
#             SISTEMA DE VENDAS -- ANÁLISE SEMANAL
# =======================================================

vendas = [
    [20, 25, 18, 30],  # Produto 0
    [15, 22, 20, 19], # Produto 1
    [30, 28, 35, 40]  # Produto 2
]

produto = ["Produto A", "Produto B", "Produto C"]
semanas = ["Semana 1", "Semana 2", "Semana 3", "Semana 4"]

totais_produtos = []
for i in range(len(produto)):
    total = 0
    for venda in vendas[i]:
        total += venda
    totais_produtos.append(total)

    totais_semanas = []
for j in range(len(semanas)):
    total = 0
    for i in range(len(produto)):
        total += vendas[i][j]
    totais_semanas.append(total)

totais_semana = []
for j in range(len(semanas)):
    total = 0
    for i in range(len(produto)):
        total += vendas[i][j]
    totais_semana.append(total)

maior_produto = totais_produtos[0]
nome_maior_produto = produto[0]
for i in range(len(totais_produtos)):
    if totais_produtos[i] > maior_produto:
        maior_produto = totais_produtos[i]
        nome_maior_produto = produto[i]

maior_semana = totais_semanas[0]
nome_maior_semana = semanas[0]
for j in range(len(totais_semanas)):
    if totais_semanas[j] > maior_semana:
        maior_semana = totais_semanas[j]
        nome_maior_semana = semanas[j]


# ========================================================
#                    RELATÓRIO DE VENDAS -- LOJA
# ========================================================

print(f"|| {'Produto':<12}", end="")
for semana in semanas:
    print(f" {semana:>8}", end="")
print(f" {'Total':>8} ||")
print("===============================================")

for i in range(len(produto)):
    print(f"|| {produto[i]:<12}", end="")
    for venda in vendas[i]:
        print(f" {venda:>8}", end="")
    print(f" {totais_produtos[i]:>8} ||")

print("===============================================")
print(f"|| {'Total':<12}", end="")
for total in totais_semanas:
    print(f" {total:>8}", end="")
print(f" {sum(totais_produtos):>8} ||")

print("===============================================")
print(f"Produto mais vendido: {nome_maior_produto} com {maior_produto} unidades.")
print(f"Semana com mais vendas: {nome_maior_semana} com {maior_semana} unidades.")
print("===============================================")
