def filtrar_aprovados(notas, limite=7.0):
    """Retorna apenas notas maiores ou iguais ao limite de aprovação."""
    aprovados = []
    for nota in notas:
        if nota >= limite:
            aprovados.append(nota)
    return aprovados


def main():
    notas = [4.5, 7.0, 8.0, 5.5, 9.0, 6.8, 7.2]
    aprovados = filtrar_aprovados(notas)

    print("Notas aprovadas:", aprovados)
    print(f"Quantidade de aprovados: {len(aprovados)}")


if __name__ == "__main__":
    main()
