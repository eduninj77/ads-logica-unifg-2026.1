def listar_alunos_com_indice(alunos):
    """Retorna uma lista de strings com índice e nome do aluno."""
    saida = []
    for indice in range(len(alunos)):
        saida.append(f"Índice {indice} -> {alunos[indice]}")
    return saida


def main():
    alunos = ["Ana", "Bruno", "Carla", "Daniel"]
    linhas = listar_alunos_com_indice(alunos)

    print("Posição e aluno:")
    for linha in linhas:
        print(linha)


if __name__ == "__main__":
    main()
