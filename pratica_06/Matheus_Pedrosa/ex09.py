class Produto:
    imposto_padrao = 0.10

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def preco_com_imposto(self):
        return self.preco + (self.preco * Produto.imposto_padrao)


produto1 = Produto("Notebook", 3000)
print(f"Produto: {produto1.nome}")
print(f"Preço sem imposto: R$ {produto1.preco}")
print(f"Preço com imposto: R$ {produto1.preco_com_imposto():.2f}")
