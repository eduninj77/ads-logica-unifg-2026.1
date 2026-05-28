import os 
os.system("clear" if os.name != "nt" else "cls")

class Estudante():
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)
    
    def media(self):
        if len(self.notas) == 0:
            return 0
        else:
            try:
                escolha = int(input("Digite a númeração das notas que você quer calcular a média: "))
                media = sum(self.notas[escolha]) / len(self.notas[escolha])
                self.media = media
                return f"A média dessas notas é {media:.1f}"
            except IndexError:
                return "Erro"
        
    def situacao(self):
        if self.media > 7:
            return "Aprovado"
        if self.media < 7:
            return "Recuperação"

e1 = Estudante("Pedro", "Massa")
e1.adicionar_nota([10,18,2])
e1.adicionar_nota([1,4,6])
print(e1.media(), end=" - ")
print(e1.situacao())

e2 = Estudante("Pedro", "Massa")
e2.adicionar_nota([8,5,6])
e2.adicionar_nota([9,5,6])
print(e2.media(), end=" - ")
print(e2.situacao())

e3 = Estudante("Pedro", "Massa")
e3.adicionar_nota([7,6,8])
e3.adicionar_nota([9,7,8])
print(e3.media(), end=" - ")
print(e3.situacao())