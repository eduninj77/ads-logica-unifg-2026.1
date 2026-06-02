# ==========================================
# DESAFIO FINAL: Cadastro de Aluno
# ==========================================
# Crie um programa completo de cadastro de aluno que:
# - Leia o nome do aluno
# - Leia duas notas
# - Calcule a média usando função
# - Determine a situação usando função
# - Exiba um pequeno relatório final
# Requisito: usar pelo menos 4 funções

def ler_nome():
    """
    Lê o nome do aluno do usuário.
    
    Returns:
        str: O nome do aluno
    """
    while True:
        nome = input("Digite o nome do aluno: ").strip()
        if nome:
            return nome
        else:
            print("Erro: O nome não pode estar vazio. Tente novamente.")


def ler_notas():
    """
    Lê duas notas do aluno com validação.
    
    Returns:
        tuple: (nota1, nota2) como floats entre 0 e 10
    """
    notas = []
    for i in range(1, 3):
        while True:
            try:
                nota = float(input(f"Digite a {i}ª nota (0-10): "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Erro: A nota deve estar entre 0 e 10. Tente novamente.")
            except ValueError:
                print("Erro: Digite um número válido. Tente novamente.")
    
    return notas[0], notas[1]


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


def determinar_situacao(media):
    """
    Determina a situação do aluno baseado na média.
    
    Args:
        media (float): A média do aluno
        
    Returns:
        str: "Aprovado" se media >= 7, "Reprovado" caso contrário
    """
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"


def exibir_relatorio(nome, nota1, nota2, media, situacao):
    """
    Exibe um relatório completo do cadastro do aluno.
    
    Args:
        nome (str): Nome do aluno
        nota1 (float): Primeira nota
        nota2 (float): Segunda nota
        media (float): Média do aluno
        situacao (str): Situação (Aprovado/Reprovado)
    """
    print("\n" + "=" * 60)
    print(" " * 15 + "RELATÓRIO DO ALUNO")
    print("=" * 60)
    print(f"Nome do aluno: {nome}")
    print(f"Primeira nota: {nota1:.1f}")
    print(f"Segunda nota:  {nota2:.1f}")
    print("-" * 60)
    print(f"Média: {media:.1f}")
    print(f"Situação: {situacao}")
    print("=" * 60 + "\n")


# Programa principal
def main():
    """
    Função principal que controla o fluxo do programa.
    """
    print("\n" + "=" * 60)
    print(" " * 10 + "BEM-VINDO AO SISTEMA DE CADASTRO DE ALUNO")
    print("=" * 60 + "\n")
    
    # Ler dados do aluno
    nome = ler_nome()
    print()
    nota1, nota2 = ler_notas()
    
    # Calcular média
    media = calcular_media(nota1, nota2)
    
    # Determinar situação
    situacao = determinar_situacao(media)
    
    # Exibir relatório
    exibir_relatorio(nome, nota1, nota2, media, situacao)
    
    # Perguntar se deseja cadastrar outro aluno
    while True:
        opcao = input("Deseja cadastrar outro aluno? (s/n): ").strip().lower()
        if opcao == 's':
            print("\n")
            main()  # Chamar recursivamente para cadastro de novo aluno
            break
        elif opcao == 'n':
            print("\nObrigado por usar o sistema! Até logo!")
            break
        else:
            print("Opção inválida. Digite 's' ou 'n'.")


if __name__ == "__main__":
    main()
