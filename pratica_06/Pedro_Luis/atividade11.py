import os 
os.system("clear" if os.name != "nt" else "cls")

class Estudante():
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

class Turma():
    def __init__(self):
        self.estudantes = []
    
    def novo_estudante(self, novo_estudante):
        self.estudantes.append(novo_estudante)
        print(f"O estudante {novo_estudante.nome} foi adicionado com sucesso na turma!")
    
    