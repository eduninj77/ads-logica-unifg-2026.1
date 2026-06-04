class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)


x = Estudante("Teste", "2024000")
x.adicionar_nota(7.5)
x.adicionar_nota(8.0)
media = x.calcular_media()
print(f"Média calculada: {media:.2f}")
