##################################################
#                                                #
#               by: Luiza Cezar                  #
#                                                #
##################################################

import menus_interface as menu
import motor_alocacao as motor


def iniciar_sistema():
    banco_de_aulas = []
    LIMITE_AULAS_PROFESSOR = 2

    print("Iniciando sistema...")
    while True:
        opcao = menu.exibir_menu_principal()

        if opcao == 1:
            print("\n--- CADASTRO DE ALOCAÇÃO ---")

            prof       = input("Nome do Professor: ").strip()
            turma      = input("Nome da Turma: ").strip()
            disciplina = input("Nome da Disciplina: ").strip()
            dia        = input("Dia da semana: ").strip().upper()
            turno      = input("Turno (MANHÃ/TARDE/NOITE): ").strip().upper()

            permitido, mensagem = motor.validar_alocacao(
                lista_de_alocacoes=banco_de_aulas,
                professor=prof,
                turma=turma,
                dia=dia,
                turno=turno,
                limite_carga_horaria=LIMITE_AULAS_PROFESSOR
            )

            if permitido:
                nova_aula = {
                    "professor": prof,
                    "turma": turma,
                    "disciplina": disciplina,
                    "dia": dia,
                    "turno": turno
                }
                banco_de_aulas.append(nova_aula)
                print(f"\n✔ {mensagem}")
            else:
                print(f"\n✘ {mensagem}")

        elif opcao == 2:
            print("\n--- ENTRADA DE NOTAS ---")
            nota_teste = menu.ler_numero_decimal("Digite a nota do aluno (0 a 10): ", 0.0, 10.0)
            print(f"Sistema aceitou a nota: {nota_teste:.1f}")

        elif opcao == 3:
            print("\nEncerrando o sistema logístico...")
            break


if __name__ == "__main__":
    iniciar_sistema()