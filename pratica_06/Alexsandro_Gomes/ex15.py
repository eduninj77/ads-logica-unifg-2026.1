#Atributo de Instância (self.preco): é uma informação que pertence a cada produto individualmente. Ou seja, se você alterar o preço de um celular, o preço da TV não muda. Cada produto possui o seu próprio valor.
#Atributo de Classe (imposto_padrao): é uma informação compartilhada por todos os objetos da classe. Então, se a loja decidir aumentar o imposto de 0.10 para 0.15, essa mudança será aplicada automaticamente a todos os produtos que utilizam esse atributo.

class Produto:
    imposto_padrao = 0.10  

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco  

p1 = Produto("Celular", 1000)
p2 = Produto("Fone", 200)

print(f"Preço do {p1.nome}: R${p1.preco}")
print(f"Preço do {p2.nome}: R${p2.preco}")

print(f"Imposto padrão da loja: {Produto.imposto_padrao * 100}%")