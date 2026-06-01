# ═══════════════════════════════════════════════
#                CLASSE ESTUDANTE
# ═══════════════════════════════════════════════

class Estudante:

    def __init__(self, nome, matricula):
        self.nome      = nome
        self.matricula = matricula


estudante1 = Estudante("Ana Silva",    "2026001")
estudante2 = Estudante("Bruno Santos", "2026002")

print(f"Nome     : {estudante1.nome}")
print(f"Matrícula: {estudante1.matricula}")
print()
print(f"Nome     : {estudante2.nome}")
print(f"Matrícula: {estudante2.matricula}")