class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)


estudante1 = Estudante("Matheus Pedrosa", "2024001")
estudante1.adicionar_nota(8.5)
estudante1.adicionar_nota(9.0)
estudante1.adicionar_nota(7.5)
print(f"Notas: {estudante1.notas}")
