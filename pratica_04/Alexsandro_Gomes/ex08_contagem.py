itens = ["mouse", "teclado", "mouse", "monitor", "mouse", "teclado"]

quantidade_teclado = 0
quantidade_mouse = 0

for item in itens:
    if item == "teclado":
        quantidade_teclado = quantidade_teclado + 1
    if item == "mouse":
        quantidade_mouse = quantidade_mouse + 1

print(f"Voce possui {quantidade_mouse} mouses")
print(f"Voce possui {quantidade_teclado} teclados")
