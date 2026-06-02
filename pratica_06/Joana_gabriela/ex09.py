class Produto:
    imposto_padrao = 0.10

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def preco_com_imposto(self):
        return self.preco * (1 + Produto.imposto_padrao)

p1 = Produto("Notebook", 3000.00)
p2 = Produto("Mouse",     150.00)
p3 = Produto("Teclado",   250.00)

for p in [p1, p2, p3]:
    print(f"{p.nome:<12} R$ {p.preco:>8.2f}  +  {Produto.imposto_padrao:.0%}  =  R$ {p.preco_com_imposto():>8.2f}")