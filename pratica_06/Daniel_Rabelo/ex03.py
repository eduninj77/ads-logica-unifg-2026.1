# ═══════════════════════════════════════════════
#   CLASSE ESTUDANTE — MÉTODO adicionar_nota
# ═══════════════════════════════════════════════

class Estudante:
    def __init__(self, nome, matricula):
        self.nome      = nome
        self.matricula = matricula
        self.notas     = []
    
    def adicionar_nota(self, nota):
        self.notas.append(nota)
        print(f"Nota {nota} adicionada para o estudante {self.nome}.")

estudante1 = Estudante("Daniel Rabelo",    "2026001")
estudante2 = Estudante("Pedro Luís", "2026002")
estudante3 = Estudante("Luckiã Oliveira", "2026003")

print("---- Adicionando notas ----")
estudante1.adicionar_nota(8.0)
estudante1.adicionar_nota(7.5)
estudante1.adicionar_nota(9.0)
estudante1.adicionar_nota(7.0)
print()
estudante2.adicionar_nota(5.0)
estudante2.adicionar_nota(6.5)
estudante2.adicionar_nota(5.0)
estudante2.adicionar_nota(4.0)
print()
estudante3.adicionar_nota(9.5)
estudante3.adicionar_nota(8.5)
estudante3.adicionar_nota(9.0)
estudante3.adicionar_nota(10.0)
print()

print("---- Resultado final ----")
print(f"Nome     : {estudante1.nome}")  
print(f"Matrícula: {estudante1.matricula}")
print(f"Notas    : {estudante1.notas}")
print()
print(f"Nome     : {estudante2.nome}")
print(f"Matrícula: {estudante2.matricula}")
print(f"Notas    : {estudante2.notas}")
print()
print(f"Nome     : {estudante3.nome}")
print(f"Matrícula: {estudante3.matricula}")
print(f"Notas    : {estudante3.notas}")