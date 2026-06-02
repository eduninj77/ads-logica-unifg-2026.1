def montar_lista_tarefas(itens_iniciais):
    """Cria e retorna uma lista de tarefas a partir de itens iniciais."""
    tarefas = []
    for item in itens_iniciais:
        tarefas.append(item)
    return tarefas


def main():
    itens = ["estudar Python", "resolver exercícios", "revisar código", "enviar atividade"]
    tarefas = montar_lista_tarefas(itens)
    tarefas.append("participar de grupo de estudos")

    print("Lista de tarefas:")
    print(tarefas)
    print(f"Total de tarefas cadastradas: {len(tarefas)}")


if __name__ == "__main__":
    main()
