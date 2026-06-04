def exibir_frutas(frutas):
    """Percorre a lista de frutas e exibe mensagem para cada item."""
    for fruta in frutas:
        print(f"Eu gosto de {fruta}.")
    return len(frutas)


def main():
    frutas = ["maçã", "banana", "uva", "pera"]
    total_frutas = exibir_frutas(frutas)
    print(f"Quantidade de frutas percorridas: {total_frutas}")

    print("\nPercorrendo cada letra da palavra 'Python':")
    for letra in "Python":
        print(f"Letra: {letra}")


if __name__ == "__main__":
    main()
