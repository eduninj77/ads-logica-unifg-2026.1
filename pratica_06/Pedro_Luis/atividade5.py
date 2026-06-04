import os 
os.system("clear" if os.name != "nt" else "cls")

class Estudante():
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)
        return f"Nota(s) {nota} adicionada(s)."
    
    def media(self):
        if len(self.notas) == 0:
            return 0
        else:
            try:
                escolha = int(input("Digite a númeração das notas que você quer calcular a média: "))
                media = sum(self.notas[escolha]) / len(self.notas[escolha])
                return print(f"A média dessas notas é {media:.1f}")
            except IndexError:
                return "Erro"

e1 = Estudante("Pedro", "Massa")
print(e1.adicionar_nota([10,10,2]))
print(e1.adicionar_nota([1,4,6]))
print(e1.media())

e2 = Estudante("Pedro", "Massa")
print(e2.adicionar_nota([8,5,6]))
print(e2.adicionar_nota([9,5,6]))
print(e2.media())

e3 = Estudante("Pedro", "Massa")
print(e3.adicionar_nota([7,6,8]))
print(e3.adicionar_nota([9,7,8]))
print(e3.media())