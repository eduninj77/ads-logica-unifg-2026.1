class RegistroVenda:
    def __init__(self, data, produto, quantidade, valor_unitario, estado):
        self.data = data
        self.produto = produto
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario
        self.estado = estado

    def get_valor_total(self):
        return self.quantidade * self.valor_unitario


class BancoDeDados:
    def __init__(self):
        self.registros = []

    def adicionar(self, linha_limpa):
        venda = RegistroVenda(
            data=linha_limpa[0],
            produto=linha_limpa[1],
            quantidade=linha_limpa[2],
            valor_unitario=linha_limpa[3],
            estado=linha_limpa[4]
        )
        self.registros.append(venda)

    def mostrar_tudo(self):
        if self.registros:
            for venda in self.registros:
                print(f"data: {venda.data}")
                print(f"produto: {venda.produto}")
                print(f"quantidade: {venda.quantidade}")
                print(f"valor: R${venda.valor_unitario:.2f}")
                print(f"estado: {venda.estado}")
                print(f"VALOR TOTAL: R${venda.get_valor_total():.2f}")
                print("-" * 25)
        else:
            print("Nenhum dado válido foi processado.")