# ═══════════════════════════════════════════════
#   CLASSE PRODUTO — ATRIBUTO DE CLASSE
# ═══════════════════════════════════════════════

class Produto:
    imposto_padrao = 0.10

    def __init__(self, nome, preco):
        self.nome  = nome
        self.preco = preco

    def calcular_preco_final(self):
        imposto = self.preco * Produto.imposto_padrao
        return self.preco + imposto
    
    def exibir(self):
        print(f"Produto: {self.nome}")
        print(f"Preço base: R$ {self.preco:.2f}")
        print(f" Imposto ({Produto.imposto_padrao*100:.0f}%): R$ {self.preco * Produto.imposto_padrao:.2f}")
        print(f"Preço final: R$ {self.calcular_preco_final():.2f}")

    def calcular_preco_final(self):
        imposto = self.preco * Produto.imposto_padrao
        return self.preco + imposto
    
    def exibir(self):
        print(f"Produto: {self.nome}")
        print(f"Preço base: R$ {self.preco:.2f}")
        print(f" Imposto ({Produto.imposto_padrao*100:.0f}%): R$ {self.preco * Produto.imposto_padrao:.2f}")
        print(f"Preço final: R$ {self.calcular_preco_final():.2f}")

 # ══════════════════════════════════════════════
 #   TESTE 1 — Imposto padrão
 # ══════════════════════════════════════════════    
print()
print("------ Criando Produtos------q")
p1 = Produto("Notebook", 3000.00)
p2 = Produto("Mouse", 100.00)
p3 = Produto("Teclado", 200.00)

print("\n--- Produto 1 ---")
p1.exibir()

print("\n--- Produto 2 ---")
p2.exibir()

print("\n--- Produto 3 ---")
p3.exibir()

# ══════════════════════════════════════════════
#   TESTE 2 — Atributo de classe é compartilhado
# ══════════════════════════════════════════════
print()
print("─── Atributo de classe ───")
print(f"  Produto.imposto_padrao → {Produto.imposto_padrao}")
print(f"  p1.imposto_padrao      → {p1.imposto_padrao}")
print(f"  p2.imposto_padrao      → {p2.imposto_padrao}")
print(f"  p3.imposto_padrao      → {p3.imposto_padrao}")
print("  (todos apontam para o mesmo valor)")

# ══════════════════════════════════════════════
#   TESTE 3 — Alterando atributo de classe
#   afeta TODOS os objetos
# ══════════════════════════════════════════════
print()
print("─── Alterando imposto_padrao para 15% ───")
Produto.imposto_padrao = 0.15

print(f" p1 -> Notebook: R$ {p1.calcular_preco_final():.2f}")
print(f" p2 -> Mouse: R$ {p2.calcular_preco_final():.2f}")
print(f" p3 -> Teclado: R$ {p3.calcular_preco_final():.2f}")
print("   (todos atualizados automaticamente)")

# ══════════════════════════════════════════════
#   TESTE 4 — Atributo de instância NÃO afeta
#   os demais objetos
# ══════════════════════════════════════════════
print()
print("---- Alterando imposto_padrao apenas para p1 ----")
p1.imposto_padrao = 0.05

print(f" p1 -> Notebook: {p1.imposto_padrao*100:.0f}% )")
print(f" p2 -> Mouse: {p2.imposto_padrao*100:.0f}% )")
print(f" p3 -> Teclado: {p3.imposto_padrao*100:.0f}% )")
print( "   (somente p1 foi alterado))")

# ══════════════════════════════════════════════
#   RELATÓRIO FINAL
# ══════════════════════════════════════════════
Produto.imposto_padrao = 0.10
p1.imposto_padrao = 0.10

print()
print("╔══════════════════════════════════════════════════╗")
print("║           RELATÓRIO FINAL                       ║")
print("╠══════════════════════════════════════════════════╣")
for p in [p1, p2, p3]:
    print(f"║  {p.nome:<16} | Preço final: R$ {p.calcular_preco_final():<10.2f} | Imposto: {Produto.imposto_padrao*100:.0f}%  ║")
    print("╠══════════════════════════════════════════════════╣")
