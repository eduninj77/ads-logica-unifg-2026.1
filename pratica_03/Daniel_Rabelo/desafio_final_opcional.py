#─────────────────────────────────────────
# CADASTRO DO ALUNO
# ────────────────────────────────────────

def ler_dados():
    nome = input("Digite o nome do aluno: ")
    n1 = float("Digite a nota 1:  ")
    n2 = float("Digite a nota 2:  ")
    return nome, n1, n2

def calcular_media(n1, n2):
    return (n1 + n2) / 2

def determinar_situacao(media):
    if media > 7:
        return "Aprovado!"
    elif media >= 5:
     return "Recuperação"
    else: 
       return "Reprovado"