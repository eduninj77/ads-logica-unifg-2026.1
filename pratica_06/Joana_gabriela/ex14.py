# ✅ Código corrigido
class Contador:
    def __init__(self):
        self.total = 0          # atributo do objeto

    def incrementar(self):
        self.total += 1         # acessa o atributo do objeto

    def exibir(self):
        print(f"Total: {self.total}")  # acessa o atributo do objeto


# Testando
c1 = Contador()
c2 = Contador()

c1.incrementar()
c1.incrementar()
c1.incrementar()

c2.incrementar()

c1.exibir()
c2.exibir()