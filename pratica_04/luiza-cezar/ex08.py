def contar_ocorrencias(itens, termo):
    """Conta quantas vezes um termo aparece na lista."""
    contador = 0
    for item in itens:
        if item == termo:
            contador += 1
    return contador


def main():
    itens = ["mouse", "teclado", "mouse", "monitor", "mouse", "teclado"]
    quantidade_mouse = contar_ocorrencias(itens, "mouse")
    quantidade_teclado = contar_ocorrencias(itens, "teclado")
    quantidade_monitor = contar_ocorrencias(itens, "monitor")

    print(f"O item 'mouse' aparece {quantidade_mouse} vezes.")
    print(f"O item 'teclado' aparece {quantidade_teclado} vezes.")
    print(f"O item 'monitor' aparece {quantidade_monitor} vez(es).")


if __name__ == "__main__":
    main()
