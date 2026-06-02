
##################################################
#                                                #
#                                                #
#               by: Luiza Cezar                  #
#                                                #
#                                                #
##################################################



def validar_alocacao(lista_de_alocacoes, professor, turma, dia, turno, limite_carga_horaria):  # ← ddia → dia, limite_carga,horaria → limite_carga_horaria
    aulas_do_professor = 0  

    for aula in lista_de_alocacoes:

        if aula["professor"] == professor:  
            aulas_do_professor += 1

        if aula["dia"] == dia and aula["turno"] == turno and aula["professor"] == professor:
            return False, "Erro! Esse(a) Professor(a) já dá aula nesse horário!"

        if aula["dia"] == dia and aula["turno"] == turno and aula["turma"] == turma:
            return False, f"Erro! A turma {turma} já tem aula nesse horário."

    if aulas_do_professor >= limite_carga_horaria:  
        return False, f"Erro! O(a) Professor(a) estourou o limite de {limite_carga_horaria} aulas."

    return True, "Alocação permitida!"  