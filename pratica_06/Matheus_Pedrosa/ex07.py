class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
        else:
            raise ValueError("Nota deve estar entre 0 e 10")

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)


estudante1 = Estudante("Matheus Pedrosa", "2024001")
try:
    estudante1.adicionar_nota(8.5)
    estudante1.adicionar_nota(11)
except ValueError as e:
    print(f"Erro: {e}")

print(f"Notas válidas: {estudante1.notas}")
