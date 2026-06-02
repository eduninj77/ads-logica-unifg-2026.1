class Produto:
    # atributo de classe: imposto padrão
    imposto_padrao = 0.10

    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = float(preco)

    def __repr__(self):
        return f"Produto({self.nome!r}, preco={self.preco:.2f})"


if __name__ == "__main__":
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    p = Produto(nome, preco)
    print(p)
    print(f"Imposto padrão (classe): {Produto.imposto_padrao}")
