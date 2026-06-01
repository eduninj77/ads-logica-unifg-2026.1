# ═══════════════════════════════════════════════
#   CLASSE ESTUDANTE — CRIANDO OBJETOS
# ═══════════════════════════════════════════════

class Estudante:

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)
    
# ══════════════════════════════════════════════
#   INSTANCIANDO MÚLTIPLOS ESTUDANTES
# ══════════════════════════════════════════════


estudante1 = Estudante("Ana Silva",    "2026001")
estudante2 = Estudante("Bruno Santos", "2026002")
estudante3 = Estudante("Carla Souza",  "2026003")
estudante4 = Estudante("Diego Lima",   "2026004")
estudante5 = Estudante("Elisa Costa",  "2026005")

estudante1.adicionar_nota(8.0)
estudante1.adicionar_nota(7.5)
estudante1.adicionar_nota(9.0)

estudante2.adicionar_nota(5.0)
estudante2.adicionar_nota(6.5)
estudante2.adicionar_nota(5.5)

estudante3.adicionar_nota(9.5)
estudante3.adicionar_nota(10.0)
estudante3.adicionar_nota(9.0)

estudante4.adicionar_nota(7.0)
estudante4.adicionar_nota(8.0)
estudante4.adicionar_nota(7.5)

estudante5.adicionar_nota(6.0)
estudante5.adicionar_nota(7.0)
estudante5.adicionar_nota(6.5)

# ══════════════════════════════════════════════
#   VERIFICANDO INDEPENDÊNCIA DOS DADOS
# ══════════════════════════════════════════════

print("─── Verificando independência ───")
print(f"  estudante1.notas → {estudante1.notas}")
print(f"  estudante2.notas → {estudante2.notas}")
print(f"  estudante3.notas → {estudante3.notas}")
print(f"  estudante4.notas → {estudante4.notas}")
print(f"  estudante5.notas → {estudante5.notas}")
print()

print("  Alterar nota de estudante1 afeta estudante2?")
estudante1.adicionar_nota(99.0)
print(f"  estudante1.notas → {estudante1.notas}  ← alterado")
print(f"  estudante2.notas → {estudante2.notas}  ← intacto")

# ══════════════════════════════════════════════
#   RELATÓRIO GERAL
# ══════════════════════════════════════════════
turma = [estudante1, estudante2, estudante3, estudante4, estudante5]

print()
print("╔══════════════════════════════════════════════════╗")
print("║           RELATÓRIO GERAL DA TURMA              ║")
print("╠══════════════════════════════════════════════════╣")
print(f"║  {'Nome':<16} {'Matrícula':<12} {'Notas':<18} {'Média':>6} ║")
print("╠══════════════════════════════════════════════════╣")

for e in turma:
    media = e.calcular_media()
    print(f"║  {e.nome:<16} {e.matricula:<12} {str(e.notas):<18} {media:>6.2f} ║")

print("╚══════════════════════════════════════════════════╝")

# ══════════════════════════════════════════════
#   PROVA DE INDEPENDÊNCIA COM id()
# ══════════════════════════════════════════════
print()
print("─── Endereços na memória (id) ───")
for e in turma:
    print(f"  {e.nome:<16} → id: {id(e.notas)}")
print("  (ids diferentes = listas independentes)")