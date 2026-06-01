# ═══════════════════════════════════════════════
#   CLASSE ESTUDANTE — MÉTODO situacao
# ═══════════════════════════════════════════════

class Estudante:

    def __init__(self, nome, matricula):
        self.nome      = nome
        self.matricula = matricula
        self.notas     = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def situacao(self):
        media = self.calcular_media()   # ← reutiliza o método já criado

        if len(self.notas) == 0:
            return "Sem notas registradas"
        elif media >= 7.0:
            return "Aprovado"
        else:
            return "Recuperação"

estudante1 = Estudante("Ana Silva",      "2026001")
estudante2 = Estudante("Bruno Santos",   "2026002")
estudante3 = Estudante("Carla Souza",    "2026003")
estudante4 = Estudante("Diego Lima",     "2026004")
estudante5 = Estudante("Elena Ferreira", "2026005") 

estudante1.adicionar_nota(8.0)
estudante1.adicionar_nota(7.5)
estudante1.adicionar_nota(9.0)

estudante2.adicionar_nota(5.0)
estudante2.adicionar_nota(6.5)
estudante2.adicionar_nota(4.5)

estudante3.adicionar_nota(9.5)
estudante3.adicionar_nota(10.0)
estudante3.adicionar_nota(9.0)

estudante4.adicionar_nota(6.5)
estudante4.adicionar_nota(7.0)
estudante4.adicionar_nota(6.0)

turma = [estudante1, estudante2, estudante3, estudante4, estudante5]

print("╔═══════════════════════════════════════════════════════╗")
print("║            BOLETIM — SITUAÇÃO DOS ESTUDANTES          ║")
print("╠═══════════════════════════════════════════════════════╣")
print(f"║  {'Nome':<16} {'Notas':<22} {'Média':>6}  {'Situação':<22}║")
print("╠═══════════════════════════════════════════════════════╣")

for e in turma:
    media    = e.calcular_media()
    situacao = e.situacao()
    print(f"║  {e.nome:<16} {str(e.notas):<22} {media:>6.2f}  {situacao:<22}║")

print("╚═══════════════════════════════════════════════════════╝")