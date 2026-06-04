itens = ["mouse", "teclado", "mouse", "monitor", "mouse", "teclado"]

contagem_mouse = 0
contagem_teclado = 0

for item in itens:
    if item == "mouse":
        contagem_mouse += 1
    elif item == "teclado":
        contagem_teclado += 1

print(f"Mouse aparece {contagem_mouse} vezes.")
print(f"Teclado aparece {contagem_teclado} vezes.")

contagem_monitor = itens.count("monitor")
print(f"Monitor aparece {contagem_monitor} vez.")
