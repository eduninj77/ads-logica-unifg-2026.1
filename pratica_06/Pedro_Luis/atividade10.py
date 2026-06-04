import os 
os.system("clear" if os.name != "nt" else "cls")

class Turma():
    def __init__(self, estudantes):
        self.estudantes = []
    
    