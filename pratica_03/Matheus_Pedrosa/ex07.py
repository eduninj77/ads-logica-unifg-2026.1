from ex05 import ler_notas, calcular_media, verificar_situacao, exibir_resultado

nome = input("Digite o nome do aluno: ")
n1, n2 = ler_notas()
media = calcular_media(n1, n2)
situacao = verificar_situacao(media)
print(exibir_resultado(nome, media, situacao))