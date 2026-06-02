class Produto:
    imposto_padrao = 0.10

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


produto1 = Produto("Notebook", 3000)
print(f"Produto: {produto1.nome}, Preço: R$ {produto1.preco}")
print(f"Imposto padrão: {Produto.imposto_padrao * 100}%")
