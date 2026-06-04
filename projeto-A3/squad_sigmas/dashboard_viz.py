def exibir_dashboard(banco_de_dados, funcao_total):
    if not banco_de_dados:
        return

    estados = {}
    produtos = {}
    receita_total = 0

    for venda in banco_de_dados:
        total = funcao_total(venda)
        receita_total += total

        estados[venda.estado] = estados.get(venda.estado, 0) + total
        produtos[venda.produto] = produtos.get(venda.produto, 0) + total

    mais_vendido = max(produtos, key=produtos.get)

    print(f"Receita total : R$ {receita_total:.2f}")
    print(f"Ticket Médio  : R$ {receita_total / len(banco_de_dados):.2f}")
    print(f"Mais vendido  : {mais_vendido}\n")

    print("FATURAMENTO POR ESTADO:")
    for estado, valor in estados.items():
        barras = "#" * max(int(valor // 200), 1 if valor > 0 else 0)
        print(f"{estado} [R$ {valor:>7.2f}] : {barras}\n")