def separar_e_reunir(nome_completo):
    """Retorna a lista de partes do nome e a string unida por hífen."""
    partes = nome_completo.split()
    nome_com_hifen = "-".join(partes)
    return partes, nome_com_hifen


def main():
    nome_completo = input("Digite um nome completo: ").strip()
    if not nome_completo:
        nome_completo = "Maria Clara Souza"

    partes, nome_com_hifen = separar_e_reunir(nome_completo)

    print("Partes do nome:", partes)
    print("Nome com hífen:", nome_com_hifen)
    if partes:
        print("Primeiro nome:", partes[0])
        print("Último sobrenome:", partes[-1])


if __name__ == "__main__":
    main()
