class Produto:
    imposto_padrao = 0.10  # atributo de classe — compartilhado por todos

    def __init__(self, nome, preco):
        self.nome = nome    # atributo de instância — único por objeto
        self.preco = preco

    def preco_com_imposto(self):
        return self.preco * (1 + Produto.imposto_padrao)

p1 = Produto("Notebook", 3000.00)
p2 = Produto("Mouse",      150.00)
p3 = Produto("Teclado",    250.00)

print("=== Preços com imposto padrão (10%) ===\n")
for p in [p1, p2, p3]:
    print(f"{p.nome:<12} R$ {p.preco:>8.2f}  →  R$ {p.preco_com_imposto():>8.2f}")

# Alterando o imposto para toda a classe
print("\n--- Imposto alterado para 15% ---\n")
Produto.imposto_padrao = 0.15

for p in [p1, p2, p3]:
    print(f"{p.nome:<12} R$ {p.preco:>8.2f}  →  R$ {p.preco_com_imposto():>8.2f}")

# Imposto individual em uma instância
print("\n--- Imposto exclusivo para Notebook (5%) ---\n")
p1.imposto_padrao = 0.05  # cria atributo de instância, não altera a classe

for p in [p1, p2, p3]:
    print(f"{p.nome:<12} imposto: {p.imposto_padrao:.0%}  →  R$ {p.preco_com_imposto():>8.2f}")