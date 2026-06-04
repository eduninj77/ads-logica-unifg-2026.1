# ===============================================
#        CLASSE ESTUDANTE COM LISTA DE NOTAS    
# ===============================================

class Estudante:

    def __init__(self, nome, matricula):
        self.nome      = nome
        self.matricula = matricula
        self.notas     = []

estudante1 = Estudante("Daniel Rabelo",    "2026001")
estudante2 = Estudante("Pedro Luís", "2026002")

estudante1.notas.append(8.0)
estudante1.notas.append(7.5)
estudante1.notas.append(9.0)
estudante2.notas.append(6.0)
estudante2.notas.append(5.5)

print(f"Nome     : {estudante1.nome}")
print(f"Matrícula: {estudante1.matricula}")
print(f"Notas    : {estudante1.notas}")
print()
print(f"Nome     : {estudante2.nome}")
print(f"Matrícula: {estudante2.matricula}")
print(f"Notas    : {estudante2.notas}")