import os 
os.system("clear" if os.name != "nt" else "cls")

class Estudante():
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []
    
    def adicionar_notas(self, nota):
        if isinstance(nota, list):
            self.notas.extend(nota)
        else:
            self.notas.append(nota)
    
    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        else:
            return sum(self.notas) / len(self.notas)
    
class Turma():
    def __init__(self):
        self.estudantes = []
    
    def nuvo_estudante(self, novo_estudante):
        self.estudantes.append(novo_estudante)
        print(f"O estudante {novo_estudante.nome} foi adicionado com sucesso na turma!")
    
    def media_g(self):
        if len(self.estudantes) == 0 or len(self.estudantes) == 1:
            return "A turma não possui estudantes o suficiente para calcular a média da turma."
        else:
            soma_medias = 0

            for aluno in self.estudantes:
                soma_medias += aluno.calcular_media()
            
            media_geral = soma_medias / len(self.estudantes)
            return f"\nA média geral da turma é: {media_geral:.1f}"
    
    def dados(self):
        if len(self.estudantes) == 0 or len(self.estudantes) == 1:
            print("A turma não possui estudantes os suficientes para mostrar os dados da turma.")
        else:
            for aluno in self.estudantes:
                if aluno.calcular_media() >= 7.0:
                    situacao = "Aprovado"
                elif 5.0 <= aluno.calcular_media() < 7.0:
                    situacao = "Recuperação"
                else:
                    situacao = "Reprovado" 
                print(f"Nome - {aluno.nome} | Média - {aluno.calcular_media():.1f} | Situação - {situacao}")

turma = Turma()

al1 = Estudante("Luis", "001")
al1.adicionar_notas([8.0, 9.0, 7.0])

al2 = Estudante("Pedro", "002")
al2.adicionar_notas([6.0, 5.0, 7.0])

al3 = Estudante("Mariana", "003")
al3.adicionar_notas([4.0, 5.0, 4.0])

turma.nuvo_estudante(al1)
turma.nuvo_estudante(al2)
turma.nuvo_estudante(al3)

turma.dados()