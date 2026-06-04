"""Exemplo de correção de uso do self.

Mostra um caso onde uma variável deveria ser um atributo de instância.
"""

class ExemploCorreto:
    def __init__(self, valor):
        # CORRETO: usar self.valor para persistir o valor no objeto
        self.valor = valor

    def incrementar(self):
        # modifica o atributo de instância
        self.valor += 1

    def mostrar(self):
        print("Valor atual:", self.valor)


def demo():
    obj = ExemploCorreto(5)
    obj.incrementar()
    obj.mostrar()  # espera 6


if __name__ == "__main__":
    demo()
