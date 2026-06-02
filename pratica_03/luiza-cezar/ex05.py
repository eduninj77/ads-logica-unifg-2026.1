# ==========================================
# Exercício 05: Boletim simples com modularização
# ==========================================
# Crie um programa para um boletim simples, obrigatoriamente dividido em funções.
# O programa deve ter, no mínimo, estas funções:
# - ler_notas()
# - calcular_media(n1, n2)
# - verificar_situacao(media)
# - exibir_resultado(nome, media, situacao)

def ler_notas():
    """
    Lê duas notas do usuário.
    
    Returns:
        tuple: (nota1, nota2) como floats
    """
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    return nota1, nota2


def calcular_media(n1, n2):
    """
    Calcula a média aritmética de duas notas.
    
    Args:
        n1 (float): Primeira nota
        n2 (float): Segunda nota
        
    Returns:
        float: A média das duas notas
    """
    media = (n1 + n2) / 2
    return media


def verificar_situacao(media):
    """
    Verifica a situação do aluno baseado na média.
    
    Args:
        media (float): A média do aluno
        
    Returns:
        str: "Aprovado" se media >= 7, "Reprovado" caso contrário
    """
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"


def exibir_resultado(nome, media, situacao):
    """
    Exibe o resultado final do boletim.
    
    Args:
        nome (str): Nome do aluno
        media (float): Média do aluno
        situacao (str): Situação do aluno (Aprovado/Reprovado)
    """
    print("\n" + "=" * 50)
    print(f"BOLETIM DO ALUNO")
    print("=" * 50)
    print(f"Nome: {nome}")
    print(f"Média: {media:.1f}")
    print(f"Situação: {situacao}")
    print("=" * 50)


# Programa principal
if __name__ == "__main__":
    # Receber o nome do aluno
    nome = input("Digite o nome do aluno: ")
    
    # Ler as notas
    nota1, nota2 = ler_notas()
    
    # Calcular a média
    media = calcular_media(nota1, nota2)
    
    # Verificar a situação
    situacao = verificar_situacao(media)
    
    # Exibir o resultado
    exibir_resultado(nome, media, situacao)
