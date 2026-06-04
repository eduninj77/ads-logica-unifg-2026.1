# ═══════════════════════════════════════════════
#   CLASSES ESTUDANTE E TURMA — RELATÓRIO
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
        media = self.calcular_media()
        if media >= 7.0:
            return "Aprovado"
        elif media >= 5.0:
            return "Recuperação"
        else:
            return "Reprovado"


# ═══════════════════════════════════════════════
#   CLASSE TURMA
# ═══════════════════════════════════════════════

class Turma:

    def __init__(self, nome):
        self.nome       = nome
        self.estudantes = []

    def matricular(self, estudante):
        self.estudantes.append(estudante)

    def media_geral(self):
        if len(self.estudantes) == 0:
            return 0
        return sum(e.calcular_media() for e in self.estudantes) / len(self.estudantes)

    # ════════════════════════════════════════════
    #   RELATÓRIO SIMPLES
    # ════════════════════════════════════════════
    def relatorio_simples(self):
        print()
        print(f"─── Relatório — {self.nome} ───")
        print()
        for estudante in self.estudantes:
            print(f"  Nome    : {estudante.nome}")
            print(f"  Média   : {estudante.calcular_media():.2f}")
            print(f"  Situação: {estudante.situacao()}")
            print()

    # ════════════════════════════════════════════
    #   RELATÓRIO COMPLETO
    # ════════════════════════════════════════════
    def relatorio_completo(self):
        aprovados   = [e for e in self.estudantes if e.situacao() == "Aprovado"]
        recuperacao = [e for e in self.estudantes if e.situacao() == "Recuperação"]
        reprovados  = [e for e in self.estudantes if e.situacao() == "Reprovado"]

        print()
        print("╔══════════════════════════════════════════════════════════════╗")
        print(f"║  TURMA   : {self.nome:<50}║")
        print(f"║  ALUNOS  : {len(self.estudantes):<50}║")
        print("╠══════════════════════════════════════════════════════════════╣")
        print(f"║  {'#':<4} {'Nome':<18} {'Matrícula':<10} {'Notas':<16} {'Média':>6}  {'Situação':<12}║")
        print("╠══════════════════════════════════════════════════════════════╣")

        for i, e in enumerate(self.estudantes, start=1):
            media    = e.calcular_media()
            situacao = e.situacao()

            if situacao == "Aprovado":
                icone = "✓"
            elif situacao == "Recuperação":
                icone = "⚠"
            else:
                icone = "✗"

            notas_str = str(e.notas) if e.notas else "[]"
            print(f"║  {i:<4} {e.nome:<18} {e.matricula:<10} {notas_str:<16} {media:>6.2f}  {icone} {situacao:<10}║")

        print("╠══════════════════════════════════════════════════════════════╣")
        print(f"║  📊 Média geral    : {self.media_geral():.2f}{' '*41}║")
        print("╠══════════════════════════════════════════════════════════════╣")
        print(f"║  ✓  Aprovados      : {len(aprovados):<41}║")
        print(f"║  ⚠  Recuperação    : {len(recuperacao):<41}║")
        print(f"║  ✗  Reprovados     : {len(reprovados):<41}║")
        print("╚══════════════════════════════════════════════════════════════╝")

    # ════════════════════════════════════════════
    #   RELATÓRIO POR SITUAÇÃO
    # ════════════════════════════════════════════
    def relatorio_por_situacao(self):
        grupos = {
            "✓ Aprovados"   : [e for e in self.estudantes if e.situacao() == "Aprovado"],
            "⚠ Recuperação" : [e for e in self.estudantes if e.situacao() == "Recuperação"],
            "✗ Reprovados"  : [e for e in self.estudantes if e.situacao() == "Reprovado"],
        }

        print()
        print(f"─── Relatório por Situação — {self.nome} ───")

        for titulo, grupo in grupos.items():
            print()
            print(f"  {titulo} ({len(grupo)})")
            print(f"  {'─'*40}")
            if len(grupo) == 0:
                print("  Nenhum estudante nesta situação.")
            else:
                for e in grupo:
                    print(f"  • {e.nome:<18} Média: {e.calcular_media():.2f}")


# ══════════════════════════════════════════════
#   CRIANDO TURMA E ESTUDANTES
# ══════════════════════════════════════════════
turma_a = Turma("Turma A — ADS 2026.1")

e1 = Estudante("Ana Silva",      "2026001")
e2 = Estudante("Bruno Santos",   "2026002")
e3 = Estudante("Carla Souza",    "2026003")
e4 = Estudante("Diego Lima",     "2026004")
e5 = Estudante("Elena Ferreira", "2026005")
e6 = Estudante("Felipe Ramos",   "2026006")

for nota in [8.0, 7.5, 9.0, 8.5]:  e1.adicionar_nota(nota)
for nota in [5.0, 6.5, 4.5, 5.5]:  e2.adicionar_nota(nota)
for nota in [9.5, 10.0, 9.0, 9.5]: e3.adicionar_nota(nota)
for nota in [6.5, 7.0, 6.0, 6.8]:  e4.adicionar_nota(nota)
for nota in [3.0, 4.5, 3.5, 4.0]:  e5.adicionar_nota(nota)
for nota in [2.0, 3.0, 1.5, 2.5]:  e6.adicionar_nota(nota)

for e in [e1, e2, e3, e4, e5, e6]:
    turma_a.matricular(e)

# ══════════════════════════════════════════════
#   EXIBINDO OS RELATÓRIOS
# ══════════════════════════════════════════════
turma_a.relatorio_simples()
turma_a.relatorio_completo()
turma_a.relatorio_por_situacao()