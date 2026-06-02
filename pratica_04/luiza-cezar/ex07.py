def busca_linear(estudantes, procurado):
    """Busca linear por nome e retorna True se encontrado."""
    encontrado = False
    for estudante in estudantes:
        if estudante == procurado:
            encontrado = True
            break
    return encontrado


def main():
    estudantes = ["Ana", "Bruno", "Carla", "Daniel"]
    procurado = "Carla"

    presente = busca_linear(estudantes, procurado)
    print(f"O nome '{procurado}' está presente? {presente}")

    procurado_inexistente = "Pedro"
    ausente = busca_linear(estudantes, procurado_inexistente)
    print(f"O nome '{procurado_inexistente}' está presente? {ausente}")


if __name__ == "__main__":
    main()
