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


estudante1 = Estudante("Matheus Pedrosa", "2024001")
estudante1.adicionar_nota(8.5)
estudante1.adicionar_nota(9.0)
estudante1.adicionar_nota(7.5)

estudante2 = Estudante("João Silva", "2024002")
estudante2.adicionar_nota(6.0)
estudante2.adicionar_nota(7.5)
estudante2.adicionar_nota(5.5)

print(f"{estudante1.nome} - Média: {estudante1.calcular_media():.2f}")
print(f"{estudante2.nome} - Média: {estudante2.calcular_media():.2f}")
