import os 
os.system("clear" if os.name != "nt" else "cls")

class Estudante():
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        