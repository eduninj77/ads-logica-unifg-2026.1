# ==========================================
# Exercício 07: Refatorando código monolítico
# ==========================================
# Transforme o código abaixo em uma solução modular:
# 
# n1 = 8
# n2 = 6
# media = (n1 + n2) / 2
# 
# if media >= 7:
#     print("Aprovado")
# else:
#     print("Reprovado")
#
# Requisitos:
# - Criar pelo menos 2 funções
# - Uma função deve calcular a média
# - Outra função deve verificar a situação

def calcular_media(n1, n2):
    """
    Calcula a média aritmética de dois números.
    
    Args:
        n1 (float): Primeiro número
        n2 (float): Segundo número
        
    Returns:
        float: A média dos dois números
    """
    media = (n1 + n2) / 2
    return media


def verificar_situacao(media):
    """
    Verifica a situação baseado na média.
    
    Args:
        media (float): Valor da média
        
    Returns:
        str: "Aprovado" se media >= 7, "Reprovado" caso contrário
    """
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"


# Programa principal - versão MODULAR
if __name__ == "__main__":
    # Dados de teste
    n1 = 8
    n2 = 6
    
    # Chamar função para calcular a média
    media = calcular_media(n1, n2)
    
    # Chamar função para verificar a situação
    situacao = verificar_situacao(media)
    
    # Exibir resultado
    print(f"Notas: {n1}, {n2}")
    print(f"Média: {media}")
    print(f"Situação: {situacao}")
