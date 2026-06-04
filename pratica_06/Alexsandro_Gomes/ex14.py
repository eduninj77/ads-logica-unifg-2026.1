#Um erro muito comum nesse código é tentar usar nome e matricula diretamente dentro do método, sem colocar self. antes deles. Quando isso acontece, o Python não entende que essas informações pertencem a um estudante específico e gera um erro de "variável não definida" porque procura por variáveis locais com esses nomes e não as encontra.

class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def exibir_dados(self):
        
        print(f"Estudante: {self.nome} | Matrícula: {self.matricula}")

aluno = Estudante("Ana", "202601")
aluno.exibir_dados()