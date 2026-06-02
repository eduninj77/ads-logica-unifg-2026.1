class Produto:
    imposto_padrao = 0.10

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

p = Produto("Notebook", 3000.0)
print(p.nome)
print(p.preco)
print(Produto.imposto_padrao)
