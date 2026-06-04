# ═══════════════════════════════════════════════
#   CLASSE PRODUTO — MÉTODO preco_com_imposto
# ═══════════════════════════════════════════════

class Produto:

    imposto_padrao = 0.10   # atributo de classe

    def __init__(self, nome, preco):
        self.nome  = nome
        self.preco = preco

    def preco_com_imposto(self):
        imposto     = self.preco * Produto.imposto_padrao
        preco_final = self.preco + imposto
        return preco_final

    def exibir(self):
        imposto     = self.preco * Produto.imposto_padrao
        preco_final = self.preco_com_imposto()  # ← reutiliza o método
        print(f"  Produto       : {self.nome}")
        print(f"  Preço base    : R$ {self.preco:.2f}")
        print(f"  Imposto ({Produto.imposto_padrao*100:.0f}%)  : R$ {imposto:.2f}")
        print(f"  Preço final   : R$ {preco_final:.2f}")


# ══════════════════════════════════════════════
#   TESTE 1 — Chamada direta do método
# ══════════════════════════════════════════════
print("─── Teste 1: Chamada direta ───")
p1 = Produto("Notebook",  3500.00)
p2 = Produto("Mouse",       80.00)
p3 = Produto("Teclado",    150.00)
p4 = Produto("Monitor",   1200.00)
p5 = Produto("Headset",    250.00)

print(f"  Notebook → R$ {p1.preco_com_imposto():.2f}")
print(f"  Mouse    → R$ {p2.preco_com_imposto():.2f}")
print(f"  Teclado  → R$ {p3.preco_com_imposto():.2f}")
print(f"  Monitor  → R$ {p4.preco_com_imposto():.2f}")
print(f"  Headset  → R$ {p5.preco_com_imposto():.2f}")

# ══════════════════════════════════════════════
#   TESTE 2 — Exibição detalhada
# ══════════════════════════════════════════════
print()
print("─── Teste 2: Detalhes por produto ───")
for p in [p1, p2, p3, p4, p5]:
    p.exibir()
    print()

# ══════════════════════════════════════════════
#   TESTE 3 — Mudando imposto e recalculando
# ══════════════════════════════════════════════
print("─── Teste 3: Imposto de 20% ───")
Produto.imposto_padrao = 0.20

for p in [p1, p2, p3]:
    print(f"  {p.nome:<12} → R$ {p.preco_com_imposto():.2f}")

# ══════════════════════════════════════════════
#   RELATÓRIO FINAL — imposto restaurado
# ══════════════════════════════════════════════
Produto.imposto_padrao = 0.10

print()
print("╔═════════════════════════════════════════════════╗")
print("║          TABELA DE PREÇOS COM IMPOSTO           ║")
print(f"║          Imposto aplicado: {Produto.imposto_padrao*100:.0f}%               ║")
print("╠═════════════════════════════════════════════════╣")
print(f"║  {'Produto':<12} {'Preço base':>12} {'Imposto':>10} {'Total':>12} ║")
print("╠═════════════════════════════════════════════════╣")

produtos = [p1, p2, p3, p4, p5]
for p in produtos:
    imposto = p.preco * Produto.imposto_padrao
    total   = p.preco_com_imposto()
    print(f"║  {p.nome:<12} R${p.preco:>10.2f} R${imposto:>8.2f} R${total:>10.2f} ║")

print("╠═════════════════════════════════════════════════╣")
total_geral = sum(p.preco_com_imposto() for p in produtos)
print(f"║  {'TOTAL GERAL':<12} {'':>12} {'':>10} R${total_geral:>10.2f} ║")
print("╚═════════════════════════════════════════════════╝")
