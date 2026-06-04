# ═══════════════════════════════════════════════
#   CLASSES ESTUDANTE E TURMA
# ═══════════════════════════════════════════════

class Estudante:

    def __init__(self, nome, matricula):
        self.nome      = nome
        self.matricula = matricula
        self.notas     = []

    def adicionar_nota(self, nota):
        if not isinstance(nota, (int, float)):
            raise TypeError(f"Nota deve ser número, não '{type(nota).__name__}'.")
        if nota < 0 or nota > 10:
            raise ValueError(f"Nota {nota} inválida — deve estar entre 0 e 10.")
        self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def situacao(self):
        if len(self.notas) == 0:
            return "Sem notas"
        return "Aprovado ✓" if self.calcular_media() >= 7.0 else "Recuperação ⚠"


# ═══════════════════════════════════════════════
#   CLASSE TURMA
# ═══════════════════════════════════════════════

class Turma:

    def __init__(self, nome):
        self.nome        = nome
        self.estudantes  = []        # ← lista de objetos Estudante

    # ── Adicionar estudante ─────────────────────
    def adicionar_estudante(self, estudante):
        self.estudantes.append(estudante)
        print(f"  ✓ {estudante.nome} adicionado(a) à turma {self.nome}.")

    # ── Buscar estudante por nome ───────────────
    def buscar_estudante(self, nome):
        for estudante in self.estudantes:
            if estudante.nome.lower() == nome.lower():
                return estudante
        return None

    # ── Total de estudantes ─────────────────────
    def total_estudantes(self):
        return len(self.estudantes)

    # ── Média geral da turma ────────────────────
    def media_geral(self):
        if len(self.estudantes) == 0:
            return 0
        total = sum(e.calcular_media() for e in self.estudantes)
        return total / len(self.estudantes)

    # ── Melhor estudante ────────────────────────
    def melhor_estudante(self):
        if len(self.estudantes) == 0:
            return None
        return max(self.estudantes, key=lambda e: e.calcular_media())

    # ── Relatório completo ──────────────────────
    def exibir_relatorio(self):
        print()
        print("╔══════════════════════════════════════════════════════════╗")
        print(f"║   TURMA: {self.nome:<48}║")
        print(f"║   Total de estudantes: {self.total_estudantes():<34}║")
        print("╠══════════════════════════════════════════════════════════╣")
        print(f"║  {'Nome':<16} {'Matrícula':<10} {'Média':>7}  {'Situação':<18}║")
        print("╠══════════════════════════════════════════════════════════╣")

        for e in self.estudantes:
            media    = e.calcular_media()
            situacao = e.situacao()
            print(f"║  {e.nome:<16} {e.matricula:<10} {media:>7.2f}  {situacao:<18}║")

        print("╠══════════════════════════════════════════════════════════╣")
        print(f"║  Média geral da turma : {self.media_geral():.2f}{' '*33}║")

        melhor = self.melhor_estudante()
        if melhor:
            print(f"║  🏆 Melhor estudante  : {melhor.nome:<34}║")

        print("╚══════════════════════════════════════════════════════════╝")


# ══════════════════════════════════════════════
#   CRIANDO A TURMA E OS ESTUDANTES
# ══════════════════════════════════════════════
turma_a = Turma("Turma A — ADS 2026.1")

# ── Criando estudantes ──────────────────────────
e1 = Estudante("Ana Silva",      "2026001")
e2 = Estudante("Bruno Santos",   "2026002")
e3 = Estudante("Carla Souza",    "2026003")
e4 = Estudante("Diego Lima",     "2026004")
e5 = Estudante("Elena Ferreira", "2026005")

# ── Adicionando notas ───────────────────────────
for nota in [8.0, 7.5, 9.0, 8.5]: e1.adicionar_nota(nota)
for nota in [5.0, 6.5, 4.5, 5.5]: e2.adicionar_nota(nota)
for nota in [9.5, 10.0, 9.0, 9.5]: e3.adicionar_nota(nota)
for nota in [6.5, 7.0, 6.0, 6.8]: e4.adicionar_nota(nota)
for nota in [3.0, 4.5, 3.5, 4.0]: e5.adicionar_nota(nota)

# ── Adicionando à turma ─────────────────────────
print("─── Adicionando estudantes ───")
for e in [e1, e2, e3, e4, e5]:
    turma_a.adicionar_estudante(e)

# ══════════════════════════════════════════════
#   TESTE — Buscar estudante
# ══════════════════════════════════════════════
print()
print("─── Buscando estudante ───")
encontrado = turma_a.buscar_estudante("carla souza")
if encontrado:
    print(f"  ✓ Encontrado: {encontrado.nome} | Média: {encontrado.calcular_media():.2f}")
else:
    print("  ✗ Estudante não encontrado.")

# ══════════════════════════════════════════════
#   RELATÓRIO FINAL
# ══════════════════════════════════════════════
turma_a.exibir_relatorio()