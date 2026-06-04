class Pessoa:
    atributo_classe = "Pessoa"

    def __init__(self, nome):
        self.nome = nome
        self.atributo_instancia = "Instância"


pessoa1 = Pessoa("Matheus")
pessoa2 = Pessoa("João")

print(f"pessoa1.atributo_classe: {pessoa1.atributo_classe}")
print(f"pessoa2.atributo_classe: {pessoa2.atributo_classe}")

print(f"pessoa1.atributo_instancia: {pessoa1.atributo_instancia}")
print(f"pessoa2.atributo_instancia: {pessoa2.atributo_instancia}")

Pessoa.atributo_classe = "Pessoa (modificado)"
print(f"Após modificação: {pessoa1.atributo_classe}")
print(f"Após modificação: {pessoa2.atributo_classe}")
