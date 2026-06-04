def padronizar_nomes(nomes_brutos):
    """Retorna uma lista com nomes limpos e com inicial maiúscula."""
    nomes_padronizados = []

    for nome in nomes_brutos:
        nome_limpo = nome.strip().title()
        nomes_padronizados.append(nome_limpo)

    return nomes_padronizados


def main():
    nomes_brutos = ["  ana", "BRUNO  ", "cArLa silva", "  joão pedro  "]
    nomes_padronizados = padronizar_nomes(nomes_brutos)

    print("Nomes padronizados:")
    print(nomes_padronizados)
    print(f"Quantidade de nomes: {len(nomes_padronizados)}")


if __name__ == "__main__":
    main()
