class Produto:
    imposto_padrao = 0.10

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


    def preco_com_imposto(self):
        return self.preco * (1 + Produto.imposto_padrao)


p = Produto("Cadeira Gamer", 1200.0)
print(f"Produto: {p.nome}")
print(f"Preço original: R${p.preco:.2f}")
print(f"Preço final com imposto: R${p.preco_com_imposto():.2f}")