def modelagem_inicial():
    """Cria exemplos de variáveis e classifica se são string ou lista."""
    # a) nome completo de um aluno -> string, porque é um texto contínuo.
    nome_completo = "Pedro Santos"

    # b) notas de quatro avaliações -> lista, pois são vários valores numéricos.
    notas_avaliacoes = [8.5, 7.0, 9.2, 6.8]

    # c) comentário escrito pelo professor -> string, porque é um texto livre.
    comentario_professor = "Bom desempenho, precisa revisar as últimas atividades."

    # d) tarefas de um projeto -> lista, pois há vários itens distintos.
    tarefas_projeto = ["planejar apresentação", "estudar teoria", "praticar exercícios"]

    # e) código de matrícula -> string, porque é um identificador único composto por caracteres.
    codigo_matricula = "2026.12345"

    # Situações adicionais:
    # f) disciplinas cursadas -> lista, pois são várias disciplinas.
    disciplinas_cursadas = ["Matemática", "Programação", "Banco de Dados"]

    # g) descrição do projeto -> string, porque é um texto explicativo.
    descricao_projeto = "Sistema simples de cadastro de alunos."

    return {
        "nome_completo": nome_completo,
        "notas_avaliacoes": notas_avaliacoes,
        "comentario_professor": comentario_professor,
        "tarefas_projeto": tarefas_projeto,
        "codigo_matricula": codigo_matricula,
        "disciplinas_cursadas": disciplinas_cursadas,
        "descricao_projeto": descricao_projeto,
    }


def main():
    dados = modelagem_inicial()
    print("Exemplos de modelagem de dados:")
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")


if __name__ == "__main__":
    main()
