def acessar_posicoes(palavra, notas):
    """Retorna valores específicos usando indexação em string e lista."""
    primeira_letra = palavra[0]
    quarta_letra = palavra[3]
    primeira_nota = notas[0]
    ultima_nota = notas[-1]
    return primeira_letra, quarta_letra, primeira_nota, ultima_nota


def main():
    palavra = "algoritmo"
    notas = [7.0, 8.5, 6.0, 9.0, 7.5]

    primeira_letra, quarta_letra, primeira_nota, ultima_nota = acessar_posicoes(palavra, notas)

    print(f"Primeira letra da palavra '{palavra}': {primeira_letra}")
    print(f"Quarta letra da palavra '{palavra}': {quarta_letra}")
    print(f"Primeira nota da lista: {primeira_nota}")
    print(f"Última nota da lista: {ultima_nota}")
    # Observação: o primeiro índice é 0 porque Python utiliza indexação baseada em zero.


if __name__ == "__main__":
    main()
