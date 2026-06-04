class Produto:
    imposto_padrao = 0.10

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

p = Produto("Celular", 1500)
print(Produto.imposto_padrao)
print(p.nome)
print(p.preco)