from ex08 import Produto

class ProdutoComImposto(Produto):
    def preco_com_imposto(self) -> float:
        """Calcula o preço final utilizando o imposto padrão da classe Produto."""
        return self.preco * (1 + Produto.imposto_padrao)


if __name__ == "__main__":
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    p = ProdutoComImposto(nome, preco)
    print(f"Preço sem imposto: {p.preco:.2f}")
    print(f"Preço com imposto: {p.preco_com_imposto():.2f}")
