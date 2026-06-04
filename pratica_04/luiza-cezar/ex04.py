def fatiar_sequencias(palavra, valores):
    """Retorna recortes de string e lista usando slicing."""
    quatro_primeiros = palavra[:4]
    trecho_quatro_a_oito = palavra[4:9]
    tres_primeiros = valores[:3]
    a_partir_do_dois = valores[2:]
    return quatro_primeiros, trecho_quatro_a_oito, tres_primeiros, a_partir_do_dois


def main():
    palavra = "programacao"
    valores = [10, 20, 30, 40, 50, 60]

    quatro_primeiros, trecho_quatro_a_oito, tres_primeiros, a_partir_do_dois = fatiar_sequencias(palavra, valores)

    print("4 primeiros caracteres:", quatro_primeiros)
    print("Caracteres da posição 4 até 8:", trecho_quatro_a_oito)
    print("3 primeiros elementos da lista:", tres_primeiros)
    print("Elementos da posição 2 até o final:", a_partir_do_dois)
    # Testes adicionais: palavra[1:5] pega do segundo ao quinto caractere.


if __name__ == "__main__":
    main()
