# ═══════════════════════════════════════════════
#   CLASSE ESTUDANTE — VALIDAÇÃO DE NOTAS
# ═══════════════════════════════════════════════

class Estudante:

    def __init__(self, nome, matricula):
        self.nome      = nome
        self.matricula = matricula
        self.notas     = []

    def adicionar_nota(self, nota):
        # ── Validação ────────────────────────────
        if not isinstance(nota, (int, float)):
            raise TypeError(f"Nota deve ser um número, não '{type(nota).__name__}'.")
        if nota < 0 or nota > 10:
            raise ValueError(f"Nota {nota} inválida — deve estar entre 0 e 10.")

        # ── Nota válida → adiciona ────────────────
        self.notas.append(nota)
        print(f"  ✓ Nota {nota} adicionada para {self.nome}.")

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def situacao(self):
        if len(self.notas) == 0:
            return "Sem notas registradas"
        return "Aprovado ✓" if self.calcular_media() >= 7.0 else "Recuperação ⚠"


# ══════════════════════════════════════════════
#   TESTE 1 — Notas válidas
# ══════════════════════════════════════════════
print("─── Teste 1: Notas válidas ───")
estudante1 = Estudante("Ana Silva", "2026001")
estudante1.adicionar_nota(8.0)
estudante1.adicionar_nota(0)      # limite mínimo
estudante1.adicionar_nota(10)     # limite máximo
estudante1.adicionar_nota(7.5)

# ══════════════════════════════════════════════
#   TESTE 2 — Nota acima de 10
# ══════════════════════════════════════════════
print()
print("─── Teste 2: Nota acima de 10 ───")
estudante2 = Estudante("Bruno Santos", "2026002")
try:
    estudante2.adicionar_nota(11)
except ValueError as e:
    print(f"  ✗ ValueError: {e}")

# ══════════════════════════════════════════════
#   TESTE 3 — Nota negativa
# ══════════════════════════════════════════════
print()
print("─── Teste 3: Nota negativa ───")
try:
    estudante2.adicionar_nota(-1)
except ValueError as e:
    print(f"  ✗ ValueError: {e}")

# ══════════════════════════════════════════════
#   TESTE 4 — Tipo inválido
# ══════════════════════════════════════════════
print()
print("─── Teste 4: Tipo inválido ───")
try:
    estudante2.adicionar_nota("oito")
except TypeError as e:
    print(f"  ✗ TypeError: {e}")

# ══════════════════════════════════════════════
#   TESTE 5 — Múltiplas notas com try/except
# ══════════════════════════════════════════════
print()
print("─── Teste 5: Lote de notas com validação ───")
estudante3  = Estudante("Carla Souza", "2026003")
notas_lote  = [9.0, 15.0, 8.5, -3, 7.0, "dez", 6.5]

for nota in notas_lote:
    try:
        estudante3.adicionar_nota(nota)
    except (ValueError, TypeError) as e:
        print(f"  ✗ Erro: {e}")

# ══════════════════════════════════════════════
#   RELATÓRIO FINAL
# ══════════════════════════════════════════════
print()
print("╔══════════════════════════════════════════════════╗")
print("║           RELATÓRIO FINAL                       ║")
print("╠══════════════════════════════════════════════════╣")

for e in [estudante1, estudante2, estudante3]:
    media = e.calcular_media()
    print(f"║  {e.nome:<16} | Notas: {str(e.notas):<18} ║")
    print(f"║  {'':16}   Média: {media:.2f} | {e.situacao():<16}  ║")
    print("╠══════════════════════════════════════════════════╣")

print("╚══════════════════════════════════════════════════╝")