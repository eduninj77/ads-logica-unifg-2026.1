
# FUNÇÃO

def calcular_total(preco, quantidade):
    subtotal = preco * quantidade
    desconto = subtotal * 0.1
    total = subtotal - desconto
    return {"subtotal": subtotal, "desconto": desconto, "total": total}



# PARTE A — TESTE DE MESA

r = calcular_total(50, 2)

print("=== PARTE A — Teste de Mesa ===")
print(f"preco      : 50")
print(f"quantidade : 2")
print(f"subtotal   : {r['subtotal']:.1f}")
print(f"desconto   : {r['desconto']:.1f}")
print(f"total      : {r['total']:.1f}")



# PARTE B — CASOS DE TESTE


casos = [
    {"tipo": "Normal",    "preco": 50,     "quantidade": 2},
    {"tipo": "Normal",    "preco": 30,     "quantidade": 5},
    {"tipo": "Limítrofe", "preco": 0,      "quantidade": 5},
    {"tipo": "Extremo",   "preco": 999999, "quantidade": 100},
]

print("\n=== PARTE B — Casos de Teste ===")
print(f"{'Tipo':<12} {'Preço':>10} {'Qtd':>5} {'Subtotal':>14} {'Desconto':>12} {'Total':>14}")
print("-" * 70)

for c in casos:
    r = calcular_total(c["preco"], c["quantidade"])
    print(f"{c['tipo']:<12} {c['preco']:>10.2f} {c['quantidade']:>5} {r['subtotal']:>14.2f} {r['desconto']:>12.2f} {r['total']:>14.2f}")