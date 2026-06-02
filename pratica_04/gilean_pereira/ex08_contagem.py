
itens = ["mouse", "teclado", "mouse", "monitor", "mouse", "teclado"]
contador_mouse = 0
contador_teclado = 0

for i in itens:
    if (i == "mouse"):
        contador_mouse += 1
        
    if (i == "teclado"):
        contador_teclado += 1

print(f"'mouse' aparece {contador_mouse} vezes ")
print(f"'teclado' aparece {contador_teclado} vezes")