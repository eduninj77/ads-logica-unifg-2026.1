# ==========================================
# Exercício 03: Média de aluno
# ==========================================
# Crie uma função calcular_media(n1, n2) que receba duas notas 
# e retorne a média aritmética.

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


# Programa principal
if __name__ == "__main__":
    # Pedir ao usuário duas notas
    print("=" * 40)
    print("CÁLCULO DE MÉDIA DO ALUNO")
    print("=" * 40)
    
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    
    # Chamar a função
    media = calcular_media(nota1, nota2)
    
    # Exibir a média com uma casa decimal
    print(f"\nNota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Média: {media:.1f}")
