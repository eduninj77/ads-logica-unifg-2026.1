# ═══════════════════════════════════════════════
#   CLASSES ESTUDANTE E TURMA — MÉDIA GERAL
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
            return "Sem notas    "
        return "Aprovado" if self.calcular_media() >= 7.0 else "Recuperação ⚠"


# ═══════════════════════════════════════════════
#   CLASSE TURMA
# ═══════════════════════════════════════════════

class Turma:

    def __init__(self, nome):
        self.nome = nome
        self.estudantes = []

    def matricular(self, estudante):
        self.estudantes.append(estudante)

    def media_geral(self):

        if len(self.estudantes) == 0:
            return 0

        soma = 0
        for estudante in self.estudantes:
            soma += estudante.calcular_media()   # ← chama método do objeto

        return soma / len(self.estudantes)

    def media_aprovados(self):
        aprovados = [e for e in self.estudantes if e.calcular_media() >= 7.0]
        if len(aprovados) == 0:
            return 0
        return sum(e.calcular_media() for e in aprovados) / len(aprovados)

    def media_recuperacao(self):
        recuperacao = [e for e in self.estudantes if e.calcular_media() < 7.0]
        if len(recuperacao) == 0:
            return 0
        return sum(e.calcular_media() for e in recuperacao) / len(recuperacao)

    def exibir_relatorio(self):
        aprovados   = sum(1 for e in self.estudantes if e.calcular_media() >= 7.0)
        recuperacao = len(self.estudantes) - aprovados

        print()
        print("╔══════════════════════════════════════════════════════════╗")
        print(f"║  TURMA : {self.nome:<48}║")
        print("╠══════════════════════════════════════════════════════════╣")
        print(f"║  {'Nome':<16} {'Matrícula':<10} {'Média':>7}  {'Situação':<16}║")
        print("╠══════════════════════════════════════════════════════════╣")

        for e in self.estudantes:
            print(f"║  {e.nome:<16} {e.matricula:<10} {e.calcular_media():>7.2f}  {e.situacao():<16}║")

        print("╠══════════════════════════════════════════════════════════╣")
        print(f"║  Média geral da turma    : {self.media_geral():.2f}{' '*28}║")
        print(f"║  Média dos aprovados     : {self.media_aprovados():.2f}{' '*28}║")
        print(f"║  Média em recuperação    : {self.media_recuperacao():.2f}{' '*28}║")
        print("╠══════════════════════════════════════════════════════════╣")
        print(f"║  Total de estudantes        : {len(self.estudantes):<28}║")
        print(f"║  Aprovados                  : {aprovados:<28}║")
        print(f"║  Em recuperação             : {recuperacao:<28}║")
        print("╚══════════════════════════════════════════════════════════╝")


# ══════════════════════════════════════════════
#   CRIANDO ESTUDANTES E TURMA
# ══════════════════════════════════════════════
turma_a = Turma("Turma A — ADS 2026.1")

e1 = Estudante("Ana Silva",      "2026001")
e2 = Estudante("Bruno Santos",   "2026002")
e3 = Estudante("Carla Souza",    "2026003")
e4 = Estudante("Diego Lima",     "2026004")
e5 = Estudante("Elena Ferreira", "2026005")

for nota in [8.0, 7.5, 9.0, 8.5]: e1.adicionar_nota(nota)
for nota in [5.0, 6.5, 4.5, 5.5]: e2.adicionar_nota(nota)
for nota in [9.5, 10.0, 9.0, 9.5]: e3.adicionar_nota(nota)
for nota in [6.5, 7.0, 6.0, 6.8]: e4.adicionar_nota(nota)
for nota in [3.0, 4.5, 3.5, 4.0]: e5.adicionar_nota(nota)

for e in [e1, e2, e3, e4, e5]:
    turma_a.matricular(e)

# ══════════════════════════════════════════════
#   TESTE 1 — Chamada direta
# ══════════════════════════════════════════════
print("─── Teste 1: Chamada direta ───")
print(f"  Média geral: {turma_a.media_geral():.2f}")

# ══════════════════════════════════════════════
#   TESTE 2 — Passo a passo do cálculo
# ══════════════════════════════════════════════
print()
print("─── Teste 2: Passo a passo ───")
soma = 0
for e in turma_a.estudantes:
    media = e.calcular_media()
    soma += media
    print(f"  {e.nome:<16} → média: {media:.2f}  | soma acumulada: {soma:.2f}")

print(f"\n  Soma total: {soma:.2f} ÷ {len(turma_a.estudantes)} = {soma/len(turma_a.estudantes):.2f}")

# ══════════════════════════════════════════════
#   TESTE 3 — Turma vazia
# ══════════════════════════════════════════════
print()
print("─── Teste 3: Turma vazia ───")
turma_vazia = Turma("Turma Vazia")
print(f"  Média geral: {turma_vazia.media_geral():.2f}  (retorna 0 ✓)")

# ══════════════════════════════════════════════
#   RELATÓRIO FINAL
# ══════════════════════════════════════════════
turma_a.exibir_relatorio()