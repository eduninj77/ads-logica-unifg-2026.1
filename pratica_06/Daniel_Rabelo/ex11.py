# ═══════════════════════════════════════════════
#   CLASSES ESTUDANTE E TURMA — MÉTODO matricular
# ═══════════════════════════════════════════════

class Estudante:

    def __init__(self, nome, matricula):
        self.nome       = nome
        self.matricula  = matricula
        self.notas      = []
        self.turma      = None     

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
            return "Sem notas    "
        return "Aprovado" if self.calcular_media() >= 7.0 else "Recuperação"

    def exibir(self):
        turma_nome = self.turma if self.turma else "Não matriculado"
        print(f"  Nome      : {self.nome}")
        print(f"  Matrícula : {self.matricula}")
        print(f"  Turma     : {turma_nome}")
        print(f"  Notas     : {self.notas}")
        print(f"  Média     : {self.calcular_media():.2f}")
        print(f"  Situação  : {self.situacao()}")


# ═══════════════════════════════════════════════
#   CLASSE TURMA
# ═══════════════════════════════════════════════

class Turma:

    def __init__(self, nome, capacidade=30):
        self.nome        = nome
        self.capacidade  = capacidade
        self.estudantes  = []

    def matricular(self, estudante):

        if not isinstance(estudante, Estudante):
            raise TypeError("Apenas objetos do tipo Estudante podem ser matriculados.")

        if len(self.estudantes) >= self.capacidade:
            print(f"  ✗ Turma {self.nome} está cheia! Capacidade: {self.capacidade}")
            return

        for e in self.estudantes:
            if e.matricula == estudante.matricula:
                print(f"  ✗ {estudante.nome} já está matriculado(a) nesta turma!")
                return

        self.estudantes.append(estudante)
        estudante.turma = self.nome     
        print(f"  ✓ {estudante.nome} matriculado(a) na {self.nome}.")

    def remover(self, nome):
        for e in self.estudantes:
            if e.nome.lower() == nome.lower():
                self.estudantes.remove(e)
                e.turma = None
                print(f"  ✓ {e.nome} removido(a) da turma.")
                return
        print(f"  ✗ '{nome}' não encontrado(a) na turma.")

    def total(self):
        return len(self.estudantes)

    def vagas(self):
        return self.capacidade - len(self.estudantes)

    def exibir_relatorio(self):
        print()
        print("╔══════════════════════════════════════════════════════════╗")
        print(f"║  TURMA : {self.nome:<48}║")
        print(f"║  Alunos: {self.total():<5} | Capacidade: {self.capacidade:<5} | Vagas: {self.vagas():<14}║")
        print("╠══════════════════════════════════════════════════════════╣")
        print(f"║  {'Nome':<16} {'Matrícula':<10} {'Média':>7}  {'Situação':<16}║")
        print("╠══════════════════════════════════════════════════════════╣")

        for e in self.estudantes:
            print(f"║  {e.nome:<16} {e.matricula:<10} {e.calcular_media():>7.2f}  {e.situacao():<16}║")

        print("╚══════════════════════════════════════════════════════════╝")


# ══════════════════════════════════════════════
#   CRIANDO ESTUDANTES
# ══════════════════════════════════════════════
e1 = Estudante("Ana Silva",      "2026001")
e2 = Estudante("Bruno Santos",   "2026002")
e3 = Estudante("Carla Souza",    "2026003")
e4 = Estudante("Diego Lima",     "2026004")
e5 = Estudante("Elena Ferreira", "2026005")

for nota in [8.0, 7.5, 9.0]: e1.adicionar_nota(nota)
for nota in [5.0, 6.5, 4.5]: e2.adicionar_nota(nota)
for nota in [9.5, 10.0, 9.0]: e3.adicionar_nota(nota)
for nota in [6.5, 7.0, 6.0]: e4.adicionar_nota(nota)

# ══════════════════════════════════════════════
#   TESTE 1 — Matrículas normais
# ══════════════════════════════════════════════
turma_a = Turma("Turma A — ADS 2026.1", capacidade=4)

print("─── Teste 1: Matrículas normais ───")
turma_a.matricular(e1)
turma_a.matricular(e2)
turma_a.matricular(e3)
turma_a.matricular(e4)

# ══════════════════════════════════════════════
#   TESTE 2 — Turma cheia
# ══════════════════════════════════════════════
print()
print("─── Teste 2: Turma cheia ───")
turma_a.matricular(e5)

# ══════════════════════════════════════════════
#   TESTE 3 — Matrícula duplicada
# ══════════════════════════════════════════════
print()
print("─── Teste 3: Matrícula duplicada ───")
turma_a.matricular(e1)

# ══════════════════════════════════════════════
#   TESTE 4 — Tipo inválido
# ══════════════════════════════════════════════
print()
print("─── Teste 4: Tipo inválido ───")
try:
    turma_a.matricular("João")
except TypeError as e:
    print(f"  ✗ TypeError: {e}")

# ══════════════════════════════════════════════
#   TESTE 5 — Verificando turma no estudante
# ══════════════════════════════════════════════
print()
print("─── Teste 5: Turma registrada no estudante ───")
e1.exibir()

# ══════════════════════════════════════════════
#   TESTE 6 — Remover e rematricular
# ══════════════════════════════════════════════
print()
print("─── Teste 6: Remover e rematricular ───")
turma_a.remover("Bruno Santos")
turma_a.matricular(e5)

# ══════════════════════════════════════════════
#   RELATÓRIO FINAL
# ══════════════════════════════════════════════
turma_a.exibir_relatorio()