import os 
os.system("clear" if os.name != "nt" else "cls")

class Estudante():
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []
    
    def adicionar_notas(self, nota):
        self.notas.append(nota)
    
    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        else:
            return sum(self.notas) / len(self.notas)
    
class Turma():
    def __init__(self):
        self.estudantes = []
    
    def novo_estudante(self, novo_estudante):
        self.estudantes.append(novo_estudante)
        print(f"O estudante {novo_estudante.nome} foi adicionado com sucesso na turma!")
    
    def media_geral(self):
        if len(self.estudantes) == 0 or len(self.estudantes) == 1:
            return "A turma não possui estudantes o suficiente para calcular a média da turma."
        else:
            soma_medias = 0

            for aluno in self.estudantes:
                soma_medias += aluno.calcular_media()
            
            media_geral = soma_medias / len(self.estudantes)
            return f"\nA média geral da turma é: {media_geral:.1f}"
