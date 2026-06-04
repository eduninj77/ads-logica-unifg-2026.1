class Produto:

    imposto_padrao = 0.10

    def __init__(self, nome, preco):
        self.nome = nome      
        self.preco = preco   


p1 = Produto("Notebook", 3000.0)
p2 = Produto("Mouse", 100.0)

print(f"Imposto padrão da classe Produto: {Produto.imposto_padrao}")
print(f"Produto 1: {p1.nome} | Preço: R${p1.preco:.2f}")
print(f"Produto 2: {p2.nome} | Preço: R${p2.preco:.2f}")