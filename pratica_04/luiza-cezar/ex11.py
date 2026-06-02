def padronizar_nomes(nomes_bruto):
    """Retorna uma lista com nomes limpos e padronizados."""
    nomes = []
    for nome in nomes_bruto:
        nomes.append(nome.strip().title())
    return nomes


def verificar_presenca(presentes_bruto, consulta):
    """Padroniza os nomes e verifica se a consulta está presente."""
    presentes = padronizar_nomes(presentes_bruto)
    consulta_padronizada = consulta.strip().title()
    esta_presente = consulta_padronizada in presentes
    return presentes, consulta_padronizada, esta_presente


def main():
    presentes_bruto = ["  maria ", "JOÃO", "ana clara", "Bruno  ", "  carla"]
    consulta = input("Digite o nome a consultar: ").strip()
    if not consulta:
        consulta = "joão"

    presentes, consulta_padronizada, esta_presente = verificar_presenca(presentes_bruto, consulta)

    print("Lista final de presentes:", presentes)
    if esta_presente:
        print(f"O estudante {consulta_padronizada} está presente.")
    else:
        print(f"O estudante {consulta_padronizada} não está presente.")


if __name__ == "__main__":
    main()
