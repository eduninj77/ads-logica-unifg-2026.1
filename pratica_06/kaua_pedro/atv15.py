class Exemplo:
    atributo_de_classe = "compartilhado"

    def __init__(self, valor):
        self.atributo_de_instancia = valor

a = Exemplo("objeto A")
b = Exemplo("objeto B")

print(a.atributo_de_classe)
print(b.atributo_de_classe)

Exemplo.atributo_de_classe = "alterado"

print(a.atributo_de_classe)
print(b.atributo_de_classe)

print(a.atributo_de_instancia)
print(b.atributo_de_instancia)
