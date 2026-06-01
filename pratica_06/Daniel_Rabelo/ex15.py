# ═══════════════════════════════════════════════
#   ATRIBUTO DE CLASSE vs ATRIBUTO DE INSTÂNCIA
# ═══════════════════════════════════════════════

class Estudante:

    # ── Atributo de CLASSE ───────────────────────
    # Compartilhado por todos os objetos
    escola       = "EREM Augusto Severo"
    ano_letivo   = 2026
    total_criados = 0               # conta quantos estudantes foram criados

    def __init__(self, nome, matricula):
        # ── Atributos de INSTÂNCIA ───────────────
        # Exclusivos de cada objeto
        self.nome      = nome
        self.matricula = matricula
        self.notas     = []

        # Incrementa o contador de classe a cada novo objeto
        Estudante.total_criados += 1

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def exibir(self):
        print(f"  Nome        : {self.nome}")
        print(f"  Matrícula   : {self.matricula}")
        print(f"  Escola      : {self.escola}")        # atributo de classe
        print(f"  Ano letivo  : {self.ano_letivo}")    # atributo de classe
        print(f"  Notas       : {self.notas}")
        print(f"  Média       : {self.calcular_media():.2f}")


# ══════════════════════════════════════════════
#   TESTE 1 — Atributo de classe é compartilhado
# ══════════════════════════════════════════════
print("─── Teste 1: Compartilhamento ───")

e1 = Estudante("Ana Silva",    "2026001")
e2 = Estudante("Bruno Santos", "2026002")
e3 = Estudante("Carla Souza",  "2026003")

print(f"  Estudante.escola → {Estudante.escola}")
print(f"  e1.escola        → {e1.escola}")
print(f"  e2.escola        → {e2.escola}")
print(f"  e3.escola        → {e3.escola}")
print("  (todos o mesmo valor ✓)")

# ══════════════════════════════════════════════
#   TESTE 2 — Alterar classe afeta TODOS
# ══════════════════════════════════════════════
print()
print("─── Teste 2: Alterar classe → afeta todos ───")

Estudante.ano_letivo = 2027        # alterado na CLASSE

print(f"  e1.ano_letivo → {e1.ano_letivo}")   # 2027 ✓
print(f"  e2.ano_letivo → {e2.ano_letivo}")   # 2027 ✓
print(f"  e3.ano_letivo → {e3.ano_letivo}")   # 2027 ✓
print("  (todos atualizados automaticamente ✓)")

# ══════════════════════════════════════════════
#   TESTE 3 — Atributo de instância é individual
# ══════════════════════════════════════════════
print()
print("─── Teste 3: Instância → individual ───")

for nota in [8.0, 9.0, 7.5]: e1.adicionar_nota(nota)
for nota in [5.0, 6.0, 4.5]: e2.adicionar_nota(nota)
for nota in [9.5, 10.0, 9.0]: e3.adicionar_nota(nota)

print(f"  e1.notas → {e1.notas}")
print(f"  e2.notas → {e2.notas}")
print(f"  e3.notas → {e3.notas}")
print("  (cada objeto com sua própria lista ✓)")

# ══════════════════════════════════════════════
#   TESTE 4 — Alterar instância NÃO afeta outros
# ══════════════════════════════════════════════
print()
print("─── Teste 4: Alterar instância → só ela muda ───")

e1.escola = "Escola Técnica"       # cria atributo de instância em e1

print(f"  e1.escola → {e1.escola}")   # "Escola Técnica"
print(f"  e2.escola → {e2.escola}")   # "EREM Augusto Severo" — intacto ✓
print(f"  e3.escola → {e3.escola}")   # "EREM Augusto Severo" — intacto ✓
print("  (somente e1 foi afetado ✓)")

# ══════════════════════════════════════════════
#   TESTE 5 — Contador de classe
# ══════════════════════════════════════════════
print()
print("─── Teste 5: Contador de objetos criados ───")
print(f"  Estudante.total_criados → {Estudante.total_criados}")

e4 = Estudante("Diego Lima", "2026004")
print(f"  Após criar e4           → {Estudante.total_criados}")

# ══════════════════════════════════════════════
#   RELATÓRIO FINAL
# ══════════════════════════════════════════════
print()
print("╔══════════════════════════════════════════════╗")
print(f"║  ESCOLA    : {Estudante.escola:<30}║")
print(f"║  ANO       : {Estudante.ano_letivo:<30}║")
print(f"║  ALUNOS    : {Estudante.total_criados:<30}║")
print("╠══════════════════════════════════════════════╣")

for e in [e1, e2, e3]:
    print()
    e.exibir()

print()
print("╚══════════════════════════════════════════════╝")