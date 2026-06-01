# ═══════════════════════════════════════════════
#   CLASSE ESTUDANTE — MÉTODO calcular_media
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
            return 0.0
        return sum(self.notas) / len(self.notas)
    
estudante1 = Estudante("Ana Silva",    "2026001")
estudante2 = Estudante("Bruno Santos", "2026002")
estudante3 = Estudante("Carla Souza",  "2026003")
estudante4 = Estudante("Diego Lima",   "2026004")

estudante1.adicionar_nota(8.0)
estudante1.adicionar_nota(7.5)
estudante1.adicionar_nota(9.0)
estudante1.adicionar_nota(8.5)


estudante2.adicionar_nota(5.0)
estudante2.adicionar_nota(6.5)
estudante2.adicionar_nota(5.5)
estudante2.adicionar_nota(4.0)

estudante3.adicionar_nota(9.5)
estudante3.adicionar_nota(10.0)
estudante3.adicionar_nota(9.0)
estudante3.adicionar_nota(9.5)

print("─── Médias dos Estudantes ───")
for estudante in [estudante1, estudante2, estudante3, estudante4]:
    media = estudante.calcular_media()
    print(f"  {estudante.nome:<15} | Notas: {str(estudante.notas):<30} | Média: {media:.2f}")