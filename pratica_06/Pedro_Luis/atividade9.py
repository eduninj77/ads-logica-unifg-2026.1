import os 
os.system("clear" if os.name != "nt" else "cls")

class Produto():
    imposto_padrao = 0.10
    def __init__(self, preco):
        self.preco = preco

    def calcular_preco(self):
        total = self.preco + (self.preco * Produto.imposto_padrao)
        return f"Você irá pagar R${total:.2f} nesse produto."

p1 = Produto(100)
print(p1.calcular_preco())
