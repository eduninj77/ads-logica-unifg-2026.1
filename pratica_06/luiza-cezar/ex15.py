"""Reflexão final: diferença entre atributo de classe e de instância.

Exemplo demonstra comportamento diferente e imprime explicação sucinta.
"""

class Exemplo:
    atributo_de_classe = 0  # compartilhado entre instâncias

    def __init__(self, valor_instancia):
        self.atributo_de_instancia = valor_instancia  # exclusivo da instância


def demonstrar():
    a = Exemplo(1)
    b = Exemplo(2)
    # modificar atributo de instância não afeta o outro
    a.atributo_de_instancia = 10
    # modificar atributo de classe afeta a visibilidade via classe
    Exemplo.atributo_de_classe = 99
    print("a.atributo_de_instancia=", a.atributo_de_instancia)
    print("b.atributo_de_instancia=", b.atributo_de_instancia)
    print("Exemplo.atributo_de_classe=", Exemplo.atributo_de_classe)
    print("a.atributo_de_classe (acesso via instância)=", a.atributo_de_classe)


if __name__ == "__main__":
    print("Explicação: atributo de classe é compartilhado; atributo de instância é por objeto.")
    demonstrar()
