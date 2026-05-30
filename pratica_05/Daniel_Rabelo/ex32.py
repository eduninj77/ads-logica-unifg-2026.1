# ═══════════════════════════════════════════════
#   SIMULAÇÃO DE CRESCIMENTO EM GRADE 5x5
# ═══════════════════════════════════════════════

grade = [
    [0, 1, 0, 0, 1],
    [0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0]
]

# ── Exibir grade ────────────────────────────────
def exibir_grade(g, titulo):
    print(f"\n─── {titulo} ───")
    print("    C0  C1  C2  C3  C4")
    print("  ┌───┬───┬───┬───┬───┐")
    for i, linha in enumerate(g):
        print(f"L{i} ", end="")
        for celula in linha:
            simbolo = "[■]" if celula == 1 else "[ ]"
            print(f" {simbolo}", end="")
        print()
        if i < len(g) - 1:
            print("  ├───┼───┼───┼───┼───┤")
    print("  └───┴───┴───┴───┴───┘")
    print("  [ ] vazia   [■] ocupada")

# ── Contar células ──────────────────────────────
def contar_celulas(g):
    ocupadas = 0
    vazias   = 0
    for linha in g:
        for celula in linha:
            if celula == 1:
                ocupadas += 1
            else:
                vazias += 1
    total = ocupadas + vazias
    print(f"\n  🟩 Células vazias  : {vazias}")
    print(f"  🟦 Células ocupadas: {ocupadas}")
    print(f"  📐 Total de células: {total}")
    print(f"  📊 Taxa de ocupação: {(ocupadas/total*100):.1f}%")
    return ocupadas

# ══════════════════════════════════════════════
#   1. ESTADO INICIAL
# ══════════════════════════════════════════════
exibir_grade(grade, "GRADE INICIAL")
print("\n─── Contagem Inicial ───")
ocupadas_antes = contar_celulas(grade)

# ══════════════════════════════════════════════
#   2. ALTERANDO TRÊS CÉLULAS VAZIAS
# ══════════════════════════════════════════════
print("\n─── Aplicando Crescimento ───")

novas_celulas = [
    (0, 2),   # linha 0, coluna 2
    (1, 0),   # linha 1, coluna 0
    (3, 1)    # linha 3, coluna 1
]

for linha, coluna in novas_celulas:
    if grade[linha][coluna] == 0:
        grade[linha][coluna] = 1
        print(f"  ✓ Célula L{linha}C{coluna}: vazia → ocupada")
    else:
        print(f"  ✗ Célula L{linha}C{coluna}: já estava ocupada")

# ══════════════════════════════════════════════
#   3 e 4. ESTADO FINAL
# ══════════════════════════════════════════════
exibir_grade(grade, "GRADE APÓS CRESCIMENTO")
print("\n─── Contagem Final ───")
ocupadas_depois = contar_celulas(grade)

# ── Resumo das alterações ───────────────────────
print("\n─── Resumo ───")
print(f"  Células ocupadas antes : {ocupadas_antes}")
print(f"  Células ocupadas depois: {ocupadas_depois}")
print(f"  Novas células ocupadas : +{ocupadas_depois - ocupadas_antes}")