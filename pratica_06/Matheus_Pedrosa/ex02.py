class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []


estudante1 = Estudante("Matheus Pedrosa", "2024001")
print(f"Notas iniciais: {estudante1.notas}")
