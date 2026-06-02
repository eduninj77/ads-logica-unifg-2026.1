def corrigir_exemplos():
    """Apresenta correções de erros comuns com listas."""
    # Exemplo corrigido a): sort() modifica a lista no lugar, não retorna uma nova lista.
    lista = [3, 1, 2]
    lista.sort()
    resultado = lista

    # Exemplo corrigido b): verificar o índice antes de acessar para evitar erro.
    nomes = ["Ana", "Bruno"]
    indice_a_acessar = 1
    elemento_seguro = nomes[indice_a_acessar] if 0 <= indice_a_acessar < len(nomes) else None

    return resultado, elemento_seguro, nomes


def main():
    resultado, elemento_seguro, nomes = corrigir_exemplos()
    print("Resultado após ordenação:", resultado)
    print("Acessando índice seguro:", elemento_seguro)
    print("Nomes disponíveis:", nomes)
    print("\nObservações:")
    print("- O método sort() retorna None porque altera a lista original.")
    print("- Acessar nomes[5] causa IndexError se o índice estiver fora do intervalo disponível.")


if __name__ == "__main__":
    main()
