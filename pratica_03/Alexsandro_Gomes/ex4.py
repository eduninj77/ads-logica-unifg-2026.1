def calcular_media(n1, n2):
    return (n1 + n2) / 2

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))    
media_do_aluno = calcular_media(nota1, nota2)
resultado_final = verificar_situacao(media_do_aluno)

print(f"Média: {media_do_aluno:.1f} - O aluno está: {resultado_final}")