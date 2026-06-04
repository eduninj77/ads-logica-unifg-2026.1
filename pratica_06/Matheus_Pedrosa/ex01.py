class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula


estudante1 = Estudante("Matheus Pedrosa", "2024001")
print(f"Estudante: {estudante1.nome}, Matrícula: {estudante1.matricula}")
