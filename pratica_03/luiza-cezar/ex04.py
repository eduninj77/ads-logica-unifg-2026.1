# ==========================================
# Exercício 04: Situação do aluno
# ==========================================
# Crie uma função verificar_situacao(media) que:
# - Retorne "Aprovado" se media >= 7
# - Retorne "Reprovado" caso contrário
# Depois, integre essa função com a função do exercício anterior.

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


# Programa principal
if __name__ == "__main__":
    print("=" * 40)
    print("VERIFICAÇÃO DE SITUAÇÃO DO ALUNO")
    print("=" * 40)
    
    # Receber as notas do usuário
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    
    # Calcular a média
    media = calcular_media(nota1, nota2)
    
    # Verificar a situação
    situacao = verificar_situacao(media)
    
    # Exibir resultados
    print(f"\nNota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Média: {media:.1f}")
    print(f"Situação: {situacao}")
