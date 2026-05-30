itens = ["mouse", "teclado", "monitor", "mouse", "teclado"]

contador_mouse = 0
for item in itens:
    if item == "mouse":
        contador_mouse += 1

print(f'"mouse" aparece {contador_mouse} vez(es) na lista.')

contador_teclado = 0
for item in itens:
    if item == "teclado":
        contador_teclado += 1

print(f'"teclado" aparece {contador_teclado} vez(es) na lista.')

# ---- Desafio: contando "monitor" -----
contador_monitor = 0
for item in itens:
    if item == "monitor":
        contador_monitor += 1

print(f'"monitor" aparece {contador_monitor} vez(es) na lista.')