# ✗ CÓDIGO COM ERRO
class Estudante:
    def __init__(self, nome):
        nome = nome          # ← variável local, não atributo!

    def exibir(self):
        print(self.nome)     # ← AttributeError: sem self.nome

# ✓ CÓDIGO CORRIGIDO
class Estudante:
    def __init__(self, nome):
        self.nome = nome     # ← agora é atributo do objeto

    def exibir(self):
        print(self.nome)     # ← funciona ✓

        # ✗ CÓDIGO COM ERRO
class Estudante:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def exibir(self):
        nota = 0             # ← variável local — ignora self.nota
        print(f"{self.nome}: {nota}")   # sempre imprime 0

# ✓ CÓDIGO CORRIGIDO
class Estudante:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def exibir(self):
        print(f"{self.nome}: {self.nota}")   # ← usa atributo ✓

# ✗ CÓDIGO COM ERRO
class Estudante:
    def __init__(self, nome, notas):
        self.nome  = nome
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def situacao(self):
        media = calcular_media()    # type: ignore # ← NameError: falta self.
        return "Aprovado" if media >= 7.0 else "Recuperação"
    
# ✓ CÓDIGO CORRIGIDO
class Estudante:
    def __init__(self, nome, notas):
        self.nome  = nome
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def situacao(self):
        media = self.calcular_media()   # ← chama via self ✓
        return "Aprovado" if media >= 7.0 else "Recuperação"

# ✗ CÓDIGO COM ERRO
class Turma:
    def __init__(self):
        estudantes = []              # ← variável local, some após __init__

    def matricular(self, estudante):
        self.estudantes.append(estudante)   # ← AttributeError!

# ✓ CÓDIGO CORRIGIDO
class Turma:
    def __init__(self):
        self.estudantes = []         # ← atributo do objeto ✓

    def matricular(self, estudante):
        self.estudantes.append(estudante)   # ← funciona ✓

# ═══════════════════════════════════════════════
#   VERSÃO CORRIGIDA — uso correto do self
# ═══════════════════════════════════════════════

class Estudante:

    def __init__(self, nome, matricula):
        self.nome      = nome        # ✓ atributo
        self.matricula = matricula   # ✓ atributo
        self.notas     = []          # ✓ atributo lista

    def adicionar_nota(self, nota):
        self.notas.append(nota)      # ✓ acessa atributo

    def calcular_media(self):
        if len(self.notas) == 0:     # ✓ acessa atributo
            return 0
        return sum(self.notas) / len(self.notas)   # ✓

    def situacao(self):
        media = self.calcular_media()   # ✓ chama método via self
        if media >= 7.0:
            return "Aprovado ✓"
        return "Recuperação ⚠"

    def exibir(self):
        print(f"  Nome      : {self.nome}")        # ✓
        print(f"  Matrícula : {self.matricula}")   # ✓
        print(f"  Notas     : {self.notas}")       # ✓
        print(f"  Média     : {self.calcular_media():.2f}")  # ✓
        print(f"  Situação  : {self.situacao()}")  # ✓


class Turma:

    def __init__(self, nome):
        self.nome       = nome           # ✓ atributo
        self.estudantes = []             # ✓ atributo lista

    def matricular(self, estudante):
        self.estudantes.append(estudante)   # ✓

    def media_geral(self):
        if len(self.estudantes) == 0:       # ✓
            return 0
        soma = 0
        for e in self.estudantes:           # ✓
            soma += e.calcular_media()      # ✓ chama método do objeto
        return soma / len(self.estudantes)  # ✓

    def relatorio(self):
        print(f"\n─── {self.nome} ───")    # ✓
        for e in self.estudantes:           # ✓ percorre atributo
            e.exibir()                      # ✓ chama método do objeto
            print()
        print(f"Média geral: {self.media_geral():.2f}")  # ✓


# ── Testando ────────────────────────────────────
e1 = Estudante("Ana Silva",    "2026001")
e2 = Estudante("Bruno Santos", "2026002")
e3 = Estudante("Carla Souza",  "2026003")

for nota in [8.0, 7.5, 9.0]: e1.adicionar_nota(nota)
for nota in [5.0, 6.5, 4.5]: e2.adicionar_nota(nota)
for nota in [9.5, 10.0, 9.0]: e3.adicionar_nota(nota)

turma = Turma("Turma A — ADS 2026.1")
for e in [e1, e2, e3]:
    turma.matricular(e)

turma.relatorio()