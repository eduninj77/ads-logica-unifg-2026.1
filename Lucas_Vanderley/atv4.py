while True:
    def verificar_situacao(media):
        if media > 10:
            print("Digite um valor menor!")
        elif media >= 7:
            print("Aprovado")
        elif media < 0:
            print("Digite um valor maior que 0!")
        else:
            print("Reprovado")

    digite = float(input("Digite sua media: "))

    resultado = verificar_situacao(digite)
    
    break
